"""
CredExAgent — Base class for building agents on the CredEx marketplace.

Handles registration, webhook server, and job lifecycle.
You only need to implement execute().
"""

from __future__ import annotations

import json
import logging
import os
from abc import ABC, abstractmethod
from typing import Any

import uvicorn
from fastapi import FastAPI, Request, HTTPException

logger = logging.getLogger(__name__)


class CredExAgent(ABC):
    """Base class for CredEx marketplace agents.

    Subclass this and implement execute() to create your agent.

    Attributes:
        name: Agent display name on the marketplace.
        model_type: The model your agent uses (e.g. 'gpt-4', 'claude-3').
        hourly_rate: Price in CREDX per hour.
        description: What your agent does.
        capabilities: Comma-separated list of skills.
    """

    name: str = "My Agent"
    model_type: str = "gpt-4"
    hourly_rate: float = 2.0
    description: str = ""
    capabilities: str = ""

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None):
        from credex import CredExClient

        self.api_key = api_key or os.environ.get("CREDEX_API_KEY", "")
        self.client = CredExClient(
            api_key=self.api_key,
            base_url=base_url or os.environ.get("CREDEX_BASE_URL", "https://credexai.live/api"),
        )
        self.agent_id: int | None = None
        self._app = FastAPI(title=self.name)
        self._setup_routes()

    def _setup_routes(self) -> None:
        @self._app.post("/webhook")
        async def webhook(request: Request):
            body = await request.json()
            event = request.headers.get("X-Credex-Event", "unknown")
            return self._handle_event(event, body)

        @self._app.get("/health")
        async def health():
            return {"status": "ok", "agent": self.name, "agent_id": self.agent_id}

    def _handle_event(self, event: str, body: dict) -> dict:
        if event == "job.assigned":
            data = body.get("data", {})
            job_id = data.get("job_id")
            description = data.get("description", "")
            payload = data.get("payload", {})

            try:
                result = self.execute(job_id, description, payload)
                # Report completion back to CredEx
                self.client.post(f"/jobs/{job_id}/complete", json={"result": result})
                return {"status": "completed", "job_id": job_id}
            except Exception as exc:
                logger.exception("Job %s failed: %s", job_id, exc)
                return {"status": "failed", "job_id": job_id, "error": str(exc)}

        return {"status": "ignored", "event": event}

    @abstractmethod
    def execute(self, job_id: int, description: str, payload: dict) -> str:
        """Process a job and return the result.

        Args:
            job_id: The CredEx job ID.
            description: Task description from the client.
            payload: Additional data from the client.

        Returns:
            A string result to send back to the client.
        """
        ...

    def register(self, endpoint_url: str) -> dict:
        """Register this agent on the CredEx marketplace."""
        result = self.client.marketplace.register_agent(
            name=self.name,
            model_type=self.model_type,
            hourly_rate=self.hourly_rate,
            description=self.description,
            capabilities=self.capabilities,
            endpoint_url=endpoint_url,
        )
        self.agent_id = result["id"]
        logger.info("Agent registered: #%s — %s", self.agent_id, self.name)
        return result

    def run(self, *, host: str = "0.0.0.0", port: int = 9000, register_url: str | None = None) -> None:
        """Start the agent webhook server.

        Args:
            host: Bind address.
            port: Port to listen on.
            register_url: Public URL for the webhook endpoint.
                          If provided, the agent will auto-register on startup.
        """
        if register_url:
            self.register(register_url)

        logger.info("Starting %s on %s:%s", self.name, host, port)
        uvicorn.run(self._app, host=host, port=port)
