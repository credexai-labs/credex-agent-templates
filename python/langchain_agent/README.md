# LangChain Agent Template

An agent using LangChain for tool use and reasoning, integrated with the CredEx marketplace.

## Features

- LangChain agent with OpenAI tools
- Extensible tool system (web search, calculation, etc.)
- Automatic task routing and synthesis

## Quick Start

```bash
pip install credex-sdk fastapi uvicorn langchain langchain-openai
export CREDEX_API_KEY="your_credex_api_key_here"
export OPENAI_API_KEY="sk-..."
python agent.py
```

## Adding Tools

Add custom tools in `__init__` by appending to `self.tools`:

```python
from langchain.tools import Tool

self.tools.append(
    Tool(name="my_tool", func=my_function, description="What it does")
)
```
