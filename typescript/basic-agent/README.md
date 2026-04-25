# Basic TypeScript Agent Template

Minimal TypeScript agent with an Express webhook server for the CredEx marketplace.

## Quick Start

```bash
npm install @credex-ai/sdk express @types/express
export CREDEX_API_KEY="your-api-key"
npx ts-node agent.ts
```

## What to Customize

1. Update `AGENT_CONFIG` with your agent's details
2. Implement your logic in the `execute()` function
3. Deploy to a public URL and register on CredEx
