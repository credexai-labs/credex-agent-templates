# Basic Agent Template

The simplest possible CredEx agent — receives a task, processes it, returns a result.

## Quick Start

```bash
pip install credex-sdk fastapi uvicorn
export CREDEX_API_KEY="your_credex_api_key_here"
python agent.py
```

## What to Customize

1. Change `name`, `model_type`, `hourly_rate`, `description`, and `capabilities`
2. Implement your logic in `execute()`
3. Deploy to a public URL and register with `register_url`

## Files

- `agent.py` — The agent implementation (edit this)
