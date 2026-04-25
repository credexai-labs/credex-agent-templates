# Multi-Capability Agent Template

An agent with multiple skills that routes tasks to the appropriate handler.

## Capabilities

- **Data Analysis** — Process datasets, identify trends
- **Content Writing** — Blog posts, reports, documentation
- **Code Review** — Security audits, best practices
- **General** — Fallback for other task types

## Quick Start

```bash
pip install credex-sdk fastapi uvicorn openai
export CREDEX_API_KEY="your-api-key"
python agent.py
```

## Customization

1. Add new handlers for additional capabilities
2. Replace template responses with actual LLM calls
3. Adjust the routing logic in `execute()`
