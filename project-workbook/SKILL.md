---
name: project-workbook
description: Set up and maintain a project workbook — the versioned docs that tell coding agents where goals, requirements, current work, decisions, and conventions live — and sync those docs to what a task actually changed and verified. Use when establishing AGENTS.md, a docs index, NOW.md, or decision records for a new or existing repo; when finishing, interrupting, or handing off a task and the docs must match reality; or when the user says "setup workbook", "sync docs", "update NOW", "handoff", "建立工作手册", "同步文档", "整理文档", "交接".
---

# Project Workbook

A project workbook is the small set of versioned documents that lets every coding-agent session start from the same reality: what the project must do, what is unfinished, why past choices were made, and how work is delivered. This skill builds that workbook and keeps it accurate as work lands.

Two modes:

- **setup** — create a workbook in an empty repo, or connect an existing repo's docs into one. Rare. Follow [references/setup.md](references/setup.md).
- **sync** — after a task, update the docs that the task's confirmed results affect. Frequent. Follow [Sync](#sync) below.

Pick the mode the user names. Otherwise:

- The user asks to establish or reorganize doc governance → setup.
- A task finished or stopped, or the user asks to update docs → sync.
- Sync is requested but the repo has no workbook (no agent entry pointing at a docs index) → sync against the docs that exist, then suggest setup in the delivery note. Setup changes the repo's structure, so the user opts into it.

Thin documentation alone never triggers setup during an ordinary coding task.

## Core principles

These hold in both modes. When a situation isn't covered below, reason from them.

1. **One fact, one home.** Each fact has exactly one authoritative location; other docs link to it or cite its stable ID. Copies drift, and once two versions disagree an agent follows whichever is convenient.
2. **Intent is not reality.** Requirements say what *should* be true; code, config, and verification results show what *is* true. When they disagree, surface the conflict. Rewriting a requirement to match the code silently turns a bug into a spec.
3. **Label certainty.** Only maintainer-confirmed choices become project conventions. Proposals, inferences, and unknowns stay labeled as such, so later agents don't build on guesses.
4. **Current work is not history.** NOW holds only accepted, unfinished work; finished items are deleted, and Git, PRs, and decision records keep the history. NOW is read every session, so each stale line costs every future session.
5. **Read progressively.** The index routes each task to the few docs it needs. Loading all history dilutes the current facts.
6. **Follow the repo.** Reuse existing paths, terms, task trackers, and workflows. One imperfect system beats two parallel ones.
7. **No change, no edit.** When a task doesn't affect what any doc says, leave the docs alone. Re-running sync on the same facts produces no diff.
8. **Match the docs' language.** Write in the language the repo's docs already use; in a new repo, the user's language. Templates here are structural guides, not text to paste verbatim.

This skill governs documentation only. Implementing, running full test suites, committing, publishing, closing tickets, and sending messages follow the user's authorization and the project's own rules.

## Workbook roles

Roles matter more than paths. An existing repo keeps its own paths; these are defaults for a new one.

| Role | Default path | Template |
|---|---|---|
| Agent entry: how to start and deliver | `AGENTS.md` | [agents-snippet.md](templates/agents-snippet.md) |
| Reading index: what to read per task, conflict precedence | `docs/INDEX.md` | [INDEX.md](templates/INDEX.md) |
| Where each kind of content goes, how docs are maintained | `docs/WRITING-RULES.md` | [WRITING-RULES.md](templates/WRITING-RULES.md) |
| Accepted unfinished work and resume points | `docs/NOW.md` | [NOW.md](templates/NOW.md) |
| Long-term goals, scope, invariants with stable IDs | `docs/REQUIREMENTS.md` | [REQUIREMENTS.md](templates/REQUIREMENTS.md) |
| Execution order from task to delivery | `docs/WORKFLOW.md` | [WORKFLOW.md](templates/WORKFLOW.md) |
| Significant decisions, rationale, supersession | `docs/decisions/` | [decisions-README.md](templates/decisions-README.md), [decision-record.md](templates/decision-record.md) |
| Per-problem design: call paths, migration, acceptance | `docs/design/` | [design-doc.md](templates/design-doc.md) |

The first four form the minimum workbook. The rest are created when real content exists for them; each template states its own trigger.

## Sync

### 1. Establish scope

Take scope from the task, spec, or commit range the user named; otherwise from the work clearly established in this session. Gather:

- The task goal, acceptance criteria, and confirmed behavior changes.
- The actual diff in scope, plus enough code and docs to understand it. A clean working tree doesn't mean nothing to sync: the work may already be committed.
- The verification that actually ran, what didn't run, and real blockers.

Only this task's changes count; other uncommitted edits belong to someone else. Ask only when the ambiguity would change what gets written.

Read the repo's INDEX and WRITING-RULES (or their equivalents) before editing. The project's own rules override this skill's defaults.

### 2. Decide doc impact

| What happened | Action |
|---|---|
| A confirmed long-term requirement changed | Update the clause and keep its ID. A change in meaning, not just wording, also gets a decision record. |
| A significant choice with a real trade-off was made | New decision record: context, decision, rationale, alternatives, consequences |
| An existing decision was overturned | Keep the old record; the new one says `supersedes`, the old one gains `superseded by` |
| Interface, usage, config, or migration steps changed | Update the matching design or usage doc |
| A doc was added, moved, renamed, or retired | Update INDEX and every inbound link |
| The start, verify, or deliver process changed | Update WORKFLOW and the agent entry |
| A NOW item meets its acceptance boundary | Delete it from NOW in the same delivery |
| Work is partial or interrupted and the rest is accepted | Rewrite the NOW item: remaining goal, blocker, resume point |
| Internal change; existing docs are still accurate | No doc change |

A decision record needs all three: lasting impact, a real trade-off, and rationale a future maintainer couldn't recover from the code. Most implementation choices don't qualify.

When a task tracker owns per-task status, NOW keeps only project-level resume points and links to tracker items.

Finishing a subtask doesn't finish the item. Remove a NOW item only when the whole item meets its acceptance boundary.

### 3. Record status by evidence

Keep these states distinct; each needs its own evidence:

```
proposed → accepted → implemented → verified (by the project's agreed checks) → deployed / released
```

Written code is not verified code, and local verification is not deployment. A tracker marked "done" is a lead to check, not proof. When evidence is missing, record the gap precisely; widening the task (extra test runs, deploys) to close it is the user's call.

When the implementation contradicts a confirmed requirement:

- State the current behavior, the intended behavior, and the evidence.
- With a confirmed basis for changing the requirement, update it on that basis.
- Without one, leave the requirement intact and record the gap — in NOW if it's accepted work, otherwise in the delivery note.
- Continue with the docs the conflict doesn't touch.

### 4. Interrupted work

Two layers, kept apart:

- **Project level** — accepted work that outlives the session goes to NOW: remaining goal, blocker, resume point.
- **Session level** — step-by-step plan, verified facts, pending checks, next action. Write a handoff note from [templates/handoff.md](templates/handoff.md) and deliver it in the reply, or wherever the project's convention keeps handoffs.

Session-level steps stay out of NOW; that's how NOW turns into a log.

### 5. Keep edits lean

- Requirements describe observable behavior, without class names, line numbers, or test counts that rot.
- INDEX holds paths and when-to-read conditions only.
- Decision records hold rationale and consequences; their pending implementation steps go to NOW.
- Design docs carry a status line, and a proposal is never described as implemented.
- Cite existing IDs and links instead of restating facts.

## Check and deliver

Check only what this change could have broken:

- New or edited relative links resolve.
- No rule or status now contradicts another.
- Finished items no longer appear in NOW or any other resume list.
- New commands and paths exist in the repo.
- Every doc change maps to a confirmed result of this task.

Use the project's existing doc checks if it has any; sync is not the moment to add a new checking framework.

Deliver a short note:

- Docs updated, and the change each one reflects.
- Related docs deliberately left unchanged, with the reason when it isn't obvious.
- Open conflicts, verification gaps, and remaining work.

When nothing needed changing, say so in one line. No separate report files.

Worked examples: [references/sync-examples.md](references/sync-examples.md).
