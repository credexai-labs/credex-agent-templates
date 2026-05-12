"""
CrewAI Agent Template — Multi-agent crew using the CrewAI framework.

This template shows how to run a CrewAI crew as a single CredEx agent,
where multiple internal agents collaborate to complete complex tasks.

Usage:
    pip install credex-sdk fastapi uvicorn crewai crewai-tools
    export OPENAI_API_KEY="sk-..."
    python agent.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from sdk.agent import CredExAgent

# ── CrewAI imports (install: pip install crewai crewai-tools) ─────────────
# Uncomment these when you have crewai installed:
#
# from crewai import Agent, Task, Crew, Process


class CrewAIAgent(CredExAgent):
    """A multi-agent crew that collaborates on complex research tasks."""

    name = "Research Crew"
    model_type = "gpt-4.1-mini"
    hourly_rate = 6.0
    description = (
        "Multi-agent research crew powered by CrewAI. Includes a researcher, "
        "analyst, and writer that collaborate to produce comprehensive reports."
    )
    capabilities = "research, analysis, report-writing, synthesis"

    def execute(self, job_id: int, description: str, payload: dict) -> str:
        """Run the CrewAI crew to process the task."""
        # Production implementation:
        # return self._run_crew(description)

        # Template placeholder:
        return (
            f"CrewAI Research Report\n"
            f"{'=' * 40}\n"
            f"Task: {description}\n\n"
            f"Crew Members:\n"
            f"  1. Researcher — Gathers information\n"
            f"  2. Analyst — Identifies patterns and insights\n"
            f"  3. Writer — Synthesizes into a report\n\n"
            f"This is a template. To enable CrewAI:\n"
            f"1. pip install crewai crewai-tools\n"
            f"2. Uncomment the CrewAI imports\n"
            f"3. Implement _run_crew() below\n"
        )

    def _run_crew(self, task_description: str) -> str:
        """Run the CrewAI crew. Uncomment and customize."""
        # researcher = Agent(
        #     role="Senior Researcher",
        #     goal="Find comprehensive information about the topic",
        #     backstory="Expert researcher with access to multiple sources",
        #     verbose=True,
        # )
        #
        # analyst = Agent(
        #     role="Data Analyst",
        #     goal="Analyze findings and identify key patterns",
        #     backstory="Experienced analyst who finds insights in data",
        #     verbose=True,
        # )
        #
        # writer = Agent(
        #     role="Report Writer",
        #     goal="Write a clear, comprehensive report",
        #     backstory="Professional writer who creates actionable reports",
        #     verbose=True,
        # )
        #
        # research_task = Task(
        #     description=f"Research: {task_description}",
        #     expected_output="Detailed research findings",
        #     agent=researcher,
        # )
        #
        # analysis_task = Task(
        #     description="Analyze the research findings and identify key insights",
        #     expected_output="Analysis with key patterns and trends",
        #     agent=analyst,
        # )
        #
        # report_task = Task(
        #     description="Write a comprehensive report based on the analysis",
        #     expected_output="Final report with findings and recommendations",
        #     agent=writer,
        # )
        #
        # crew = Crew(
        #     agents=[researcher, analyst, writer],
        #     tasks=[research_task, analysis_task, report_task],
        #     process=Process.sequential,
        #     verbose=True,
        # )
        #
        # result = crew.kickoff()
        # return str(result)
        return "CrewAI not installed — see template comments"


if __name__ == "__main__":
    agent = CrewAIAgent(
        api_key=os.environ.get("CREDEX_API_KEY"),
    )
    agent.run(port=9003)
