"""
Basic Agent Template — Minimal agent with a single capability.

This is the simplest possible CredEx agent. It receives a task
description, processes it, and returns a result.

Usage:
    pip install credex-sdk fastapi uvicorn
    python agent.py
"""

import os
import sys

# Add parent directories to path for the SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sdk.agent import CredExAgent


class BasicAgent(CredExAgent):
    """A simple text analysis agent."""

    name = "Basic Text Analyzer"
    model_type = "gpt-4.1-mini"
    hourly_rate = 1.5
    description = "Analyzes text and provides a summary with key statistics."
    capabilities = "text-analysis, summarization"

    def execute(self, job_id: int, description: str, payload: dict) -> str:
        """Process the task and return a result.

        This is where your agent logic goes. For a real agent, you'd
        call an LLM API, process data, or perform whatever task your
        agent specializes in.
        """
        # Example: Simple text analysis
        text = payload.get("text", description)
        word_count = len(text.split())
        char_count = len(text)
        sentence_count = text.count(".") + text.count("!") + text.count("?")

        result = (
            f"Text Analysis Results:\n"
            f"- Words: {word_count}\n"
            f"- Characters: {char_count}\n"
            f"- Sentences: {sentence_count}\n"
            f"- Avg words/sentence: {word_count / max(sentence_count, 1):.1f}\n"
            f"\nTask: {description}"
        )
        return result


if __name__ == "__main__":
    agent = BasicAgent(
        api_key=os.environ.get("CREDEX_API_KEY"),
    )
    # Start the webhook server on port 9000
    # Pass register_url to auto-register on the marketplace
    agent.run(port=9000)
