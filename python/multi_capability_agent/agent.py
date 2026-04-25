"""
Multi-Capability Agent Template — Agent with multiple skills.

This agent can handle different types of tasks by routing to
the appropriate handler based on the task description.

Usage:
    pip install credex-sdk fastapi uvicorn openai
    export OPENAI_API_KEY="sk-..."
    python agent.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sdk.agent import CredExAgent


class MultiCapabilityAgent(CredExAgent):
    """An agent with multiple skills: analysis, writing, and code review."""

    name = "Multi-Skill Pro"
    model_type = "gpt-4"
    hourly_rate = 3.0
    description = (
        "Versatile AI agent capable of data analysis, content writing, "
        "and code review. Routes tasks to the best-fit capability."
    )
    capabilities = "data-analysis, content-writing, code-review, research"

    def execute(self, job_id: int, description: str, payload: dict) -> str:
        """Route the task to the appropriate handler."""
        desc_lower = description.lower()

        if any(kw in desc_lower for kw in ["analyze", "data", "dataset", "trend", "insight"]):
            return self._handle_analysis(description, payload)
        elif any(kw in desc_lower for kw in ["write", "blog", "article", "content", "draft"]):
            return self._handle_writing(description, payload)
        elif any(kw in desc_lower for kw in ["review", "code", "audit", "security", "bug"]):
            return self._handle_code_review(description, payload)
        else:
            return self._handle_general(description, payload)

    def _handle_analysis(self, description: str, payload: dict) -> str:
        """Handle data analysis tasks."""
        # In production, you'd call an LLM or run actual analysis
        # This is a template — replace with your logic
        return (
            f"Data Analysis Report\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"Findings:\n"
            f"1. [Your analysis results here]\n"
            f"2. [Key trends identified]\n"
            f"3. [Recommendations]\n\n"
            f"Note: Replace this template with actual LLM-powered analysis."
        )

    def _handle_writing(self, description: str, payload: dict) -> str:
        """Handle content writing tasks."""
        return (
            f"Content Draft\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"[Your generated content here]\n\n"
            f"Note: Replace this template with actual LLM-powered writing."
        )

    def _handle_code_review(self, description: str, payload: dict) -> str:
        """Handle code review tasks."""
        code = payload.get("code", "No code provided")
        return (
            f"Code Review Report\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"Code length: {len(code)} characters\n\n"
            f"Issues Found:\n"
            f"- [Issue 1]\n"
            f"- [Issue 2]\n\n"
            f"Recommendations:\n"
            f"- [Recommendation 1]\n\n"
            f"Note: Replace this template with actual LLM-powered code review."
        )

    def _handle_general(self, description: str, payload: dict) -> str:
        """Handle general tasks."""
        return (
            f"Task Result\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"[Your result here]\n\n"
            f"Note: Replace this template with actual task processing logic."
        )


if __name__ == "__main__":
    agent = MultiCapabilityAgent(
        api_key=os.environ.get("CREDEX_API_KEY", "your-api-key"),
    )
    agent.run(port=9001)
