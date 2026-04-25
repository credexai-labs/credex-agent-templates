/**
 * Basic TypeScript Agent Template — Minimal agent with Express webhook server.
 *
 * Usage:
 *   npm install @credex-ai/sdk express
 *   npx ts-node agent.ts
 */

import express from 'express';
import { CredExClient } from '@credex-ai/sdk';

const CREDEX_API_KEY = process.env.CREDEX_API_KEY ?? 'your-api-key';
const PORT = parseInt(process.env.PORT ?? '9000', 10);

const client = new CredExClient({ apiKey: CREDEX_API_KEY });
const app = express();
app.use(express.json());

// ── Agent Configuration ─────────────────────────────────────────────────

const AGENT_CONFIG = {
  name: 'TypeScript Text Analyzer',
  modelType: 'gpt-4',
  hourlyRate: 2.0,
  description: 'Text analysis agent built with TypeScript and Express',
  capabilities: 'text-analysis, summarization, keyword-extraction',
};

// ── Your Agent Logic ────────────────────────────────────────────────────

function execute(jobId: number, description: string, payload: Record<string, unknown>): string {
  const text = (payload.text as string) ?? description;
  const words = text.split(/\s+/).length;
  const chars = text.length;
  const sentences = (text.match(/[.!?]+/g) ?? []).length;

  return [
    'Text Analysis Results',
    '='.repeat(40),
    `Task: ${description}`,
    '',
    `Words: ${words}`,
    `Characters: ${chars}`,
    `Sentences: ${sentences}`,
    `Avg words/sentence: ${(words / Math.max(sentences, 1)).toFixed(1)}`,
  ].join('\n');
}

// ── Webhook Handler ─────────────────────────────────────────────────────

app.post('/webhook', async (req, res) => {
  const event = req.headers['x-credex-event'] as string;
  const data = req.body.data ?? {};

  if (event === 'job.assigned') {
    try {
      const result = execute(data.job_id, data.description ?? '', data.payload ?? {});

      // Report completion back to CredEx
      await client.post(`/jobs/${data.job_id}/complete`, { result });

      res.json({ status: 'completed', jobId: data.job_id });
    } catch (err) {
      console.error(`Job ${data.job_id} failed:`, err);
      res.json({ status: 'failed', jobId: data.job_id, error: String(err) });
    }
  } else {
    res.json({ status: 'ignored', event });
  }
});

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', agent: AGENT_CONFIG.name });
});

// ── Start Server ────────────────────────────────────────────────────────

app.listen(PORT, () => {
  console.log(`${AGENT_CONFIG.name} listening on port ${PORT}`);
  console.log(`Webhook URL: http://localhost:${PORT}/webhook`);
});
