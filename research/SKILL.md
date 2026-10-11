---
name: research
description: Investigate a question against high-trust primary sources and present findings in conversation. Only persist findings to a Markdown file in the research/ folder when explicitly requested by the user. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. **Default to direct conversation response**: Present findings clearly and structured in the conversation, citing each claim's source. Do NOT create or write any files by default.
3. **User-controlled persistence**: Only save findings to a Markdown file if the user explicitly asks to save, persist, record, or export them to disk. When explicitly requested, save the file under the `research/` directory (e.g., `research/<topic>.md`), creating the directory if it does not already exist.
