# MEMORY.md - Long-Term Memory

*Last updated: 2026-07-24*

## System Configuration

### Translation Pipeline (2026-06-16)
- **Unified model**: `qwen/qwen3.7-max` (阿里百炼 DashScope)
- **No more 3-tier fallback** — previously used Gemini → MiniMax → DeepSeek cascade
- All translation scripts now use Qwen3.7 Max directly via DashScope API
- Affected scripts: `send_daily_ai_news_real.py`, `translate_news_to_html.py`, `translate_and_send_news.py`, `send_daily_ai_news_fixed.py`

### Memory Search Embedding (2026-06-16)
- **Current**: Local Ollama `nomic-embed-text` (768 dim, free, unlimited)
- **Previous**: Gemini `gemini-embedding-2-preview` — key was flagged as leaked (403)
- DashScope `text-embedding-v3` didn't work (API key lacks embedding permissions)

### Cron Jobs (2026-06-16)
- All scheduled tasks use `qwen/qwen3.7-max` as primary model
- Fallback chain: `zai/glm-5.2 → deepseek-v4-flash → deepseek-v4-pro` (default)
- 11 cron tasks total including: AI news, daily diary, memory archival, Obsidian feedback, health research monitoring

### Peekaboo (2026-06-16)
- Upgraded to v3.4.0 via Homebrew
- AI analysis model: `qwen3-vl:4b` (3.3GB, 44-83s per analysis)
- `qwen3-vl:8b` too slow (6GB), `minicpm-v` incompatible (missing vision metadata)
- Old v3.0.0-beta3 residual at `/usr/local/bin/peekaboo` (needs sudo rm)

## Known Issues

### Cron API Bug (2026-06-27)
- **Issue**: `model: null` patch is silently ignored — cannot clear explicitly set model field
- **GitHub Issue**: [openclaw/openclaw#97222](https://github.com/openclaw/openclaw/issues/97222)
- **Workaround**: Setting `model` to the default primary (`qwen/qwen3.7-max`) + empty `fallbacks: []` achieves functional equivalence with default model chain
- 4 tasks have residual explicit model fields that can't be cleared via API

## User Preferences
- Communicates in Chinese (中文)
- Uses Feishu for messaging
- Prefers practical solutions over theoretical perfection
- Values transparency — wants honest status reports even when things aren't perfect
