---
name: commit-work
description: "Create high-quality git commits: review/stage intended changes, split into logical commits, and write clear commit messages using Conventional Commits prefixed with gitmoji. Use when the user asks to commit, craft a commit message, stage changes, or split work into multiple commits."
---

# Commit work

## Goal
Make commits that are easy to review and safe to ship:
- only intended changes are included
- commits are logically scoped (split when needed)
- commit messages describe what changed and why
- subjects are scannable via [gitmoji](https://gitmoji.dev/) + Conventional Commits

## Inputs to ask for (if missing)
- Single commit or multiple commits? (If unsure: default to multiple small commits when there are unrelated changes.)
- Commit style: Conventional Commits + gitmoji are required.
- Any rules: max subject length, required scopes.

## Workflow (checklist)
1) Inspect the working tree before staging
   - `git status`
   - `git diff` (unstaged)
   - If many changes: `git diff --stat`
2) Decide commit boundaries (split if needed)
   - Split by: feature vs refactor, backend vs frontend, formatting vs logic, tests vs prod code, dependency bumps vs behavior changes.
   - If changes are mixed in one file, plan to use patch staging.
3) Stage only what belongs in the next commit
   - Prefer patch staging for mixed changes: `git add -p`
   - To unstage a hunk/file: `git restore --staged -p` or `git restore --staged <path>`
4) Review what will actually be committed
   - `git diff --cached`
   - Sanity checks:
     - no secrets or tokens
     - no accidental debug logging
     - no unrelated formatting churn
5) Describe the staged change in 1-2 sentences (before writing the message)
   - "What changed?" + "Why?"
   - If you cannot describe it cleanly, the commit is probably too big or mixed; go back to step 2.
6) Write the commit message
   - Required format (gitmoji + Conventional Commits):
     - `<emoji> <type>(<scope>): <summary>`
     - blank line
     - body (what/why, not implementation diary)
     - footer (`BREAKING CHANGE:`) if needed
   - Pick the emoji that best matches the change intent (not just the Conventional type). Prefer one emoji; never stack multiple.
   - Use the Unicode emoji character (e.g. `✨`), not the `:sparkles:` shortcode — better readability in `git log` and hosting UIs.
   - Common type → emoji defaults (override when a more specific gitmoji fits better):

     | type | emoji | when |
     |------|-------|------|
     | feat | ✨ | new feature |
     | fix | 🐛 | bug fix (🚑 critical hotfix; 🩹 simple non-critical) |
     | refactor | ♻️ | refactor without behavior change |
     | perf | ⚡️ | performance |
     | docs | 📝 | documentation |
     | test | ✅ | add/update/pass tests (🧪 failing test only) |
     | style | 💄 | UI / formatting / style files |
     | build | 📦️ | build system / compiled packages |
     | ci | 👷 | CI config |
     | chore | 🔧 | config / tooling / mundane tasks |
     | revert | ⏪️ | revert |

   - For specialized cases (deps, i18n, a11y, security, rename, etc.), see [references/gitmoji.md](references/gitmoji.md).
   - Prefer an editor for multi-line messages: `git commit -v`
   - Use [references/commit-message-template.md](references/commit-message-template.md) if helpful.
7) Run the smallest relevant verification
   - Run the repo's fastest meaningful check (unit tests, lint, or build) before moving on.
8) Repeat for the next commit until the working tree is clean

## Deliverable
Provide:
- the final commit message(s)
- a short summary per commit (what/why)
- the commands used to stage/review (at minimum: `git diff --cached`, plus any tests run)
