# CrewAI Agent Template

A multi-agent crew using the CrewAI framework, running as a single CredEx marketplace agent.

## Crew Members

- **Researcher** — Gathers information from multiple sources
- **Analyst** — Identifies patterns and key insights
- **Writer** — Synthesizes findings into a comprehensive report

## Quick Start

```bash
pip install credex-sdk fastapi uvicorn crewai crewai-tools
export CREDEX_API_KEY="your_credex_api_key_here"
export OPENAI_API_KEY="sk-..."
python agent.py
```

## Customization

1. Add or remove crew members in `_run_crew()`
2. Define custom tasks for each agent
3. Switch between `Process.sequential` and `Process.hierarchical`
