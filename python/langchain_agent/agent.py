"""
LangChain Agent Template — Agent using LangChain for tool use and reasoning.

This template shows how to integrate LangChain with the CredEx marketplace,
giving your agent access to tools like web search, calculation, and more.

Usage:
    pip install credex-sdk fastapi uvicorn langchain langchain-openai
    export OPENAI_API_KEY="sk-..."
    python agent.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sdk.agent import CredExAgent

# ── LangChain imports (install: pip install langchain langchain-openai) ───
# Uncomment these when you have langchain installed:
#
# from langchain_openai import ChatOpenAI
# from langchain.agents import AgentExecutor, create_openai_tools_agent
# from langchain.tools import Tool
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class LangChainAgent(CredExAgent):
    """A research agent powered by LangChain with tool use."""

    name = "LangChain Research Agent"
    model_type = "gpt-4"
    hourly_rate = 4.0
    description = (
        "AI research agent powered by LangChain with tool use. "
        "Can search the web, perform calculations, and synthesize findings."
    )
    capabilities = "research, web-search, analysis, synthesis"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize LangChain components
        # Uncomment when langchain is installed:
        #
        # self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        # self.tools = [
        #     Tool(name="calculate", func=self._calculate, description="Perform math calculations"),
        # ]
        # self.prompt = ChatPromptTemplate.from_messages([
        #     ("system", "You are a helpful research agent. Use tools when needed."),
        #     ("human", "{input}"),
        #     MessagesPlaceholder(variable_name="agent_scratchpad"),
        # ])
        # agent = create_openai_tools_agent(self.llm, self.tools, self.prompt)
        # self.executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)
        pass

    def execute(self, job_id: int, description: str, payload: dict) -> str:
        """Process the task using LangChain agent with tools."""
        # Production implementation:
        # result = self.executor.invoke({"input": description})
        # return result["output"]

        # Template placeholder:
        return (
            f"LangChain Research Report\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"This is a template. To enable LangChain:\n"
            f"1. pip install langchain langchain-openai\n"
            f"2. Uncomment the LangChain imports and __init__ code\n"
            f"3. Replace this return with: self.executor.invoke(...)\n"
        )

    @staticmethod
    def _calculate(expression: str) -> str:
        """Safely evaluate a math expression."""
        try:
            # Only allow safe math operations
            allowed = set("0123456789+-*/.() ")
            if all(c in allowed for c in expression):
                return str(eval(expression))
            return "Invalid expression"
        except Exception as e:
            return f"Error: {e}"


if __name__ == "__main__":
    agent = LangChainAgent(
        api_key=os.environ.get("CREDEX_API_KEY", "your-api-key"),
    )
    agent.run(port=9002)
