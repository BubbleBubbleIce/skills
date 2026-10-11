<!--
Create: always (minimum workbook). This file is what lets agents without the
project-workbook skill maintain the docs, so it must be complete on its own.
Adjust paths and drop sections for files the repo doesn't have yet.
-->

# Documentation Rules

## 1. Where content goes

| Content | Location |
|---|---|
| Session entry, reading routes, doc navigation | `INDEX.md` |
| Agent discipline for starting, checking, and delivering | root `AGENTS.md` |
| Execution order from task to delivery | `WORKFLOW.md` |
| Long-term requirements, prohibitions, invariants | `REQUIREMENTS.md` |
| Accepted unfinished work, blockers, resume points | `NOW.md` |
| Significant choices, rationale, alternatives, corrections | `decisions/` |
| Architecture, call paths, migration, and acceptance for one problem | `design/` |
| Current implementation details | Code, types, tests, nearby comments |

One fact, one authoritative place. Other docs cite the clause ID or link to it.

INDEX holds only paths, order, and reading conditions. When a doc is added, moved, renamed, or retired, update INDEX in the same change.

## 2. Requirements

- Every clause has a stable ID. Rewording keeps it; a change in meaning needs a decision record.
- State the observable outcome first, then forbidden paths. Leave out class names, line numbers, test counts, and temporary progress.
- When the implementation disagrees, the requirement keeps the intended behavior. The gap goes to `NOW.md`; evidence and migration go to a design doc.

## 3. Decision records

- File name `NNNN-short-title.md`; numbers only increase.
- Status is `proposed`, `accepted`, `superseded`, or `rejected`.
- Each record has context, decision, rationale, alternatives considered, consequences, acceptance, and related clauses.
- A wrong decision isn't deleted. A new record corrects it, and the two note `supersedes` / `superseded by`.
- Pending implementation steps go to `NOW.md`, not into the record.
- Write a record only when a choice has lasting impact, a real trade-off, and a rationale nobody could recover from the code.

## 4. NOW

- Only accepted work that is unfinished, in progress, or blocked.
- Each item states its expected outcome and acceptance boundary.
- Delete an item once it's done and verified. No "Done" section, no weekly logs, no long-term wishes.
- A session's step-by-step plan stays in the session or its handoff note. Only work that outlives the session and that the maintainer accepted goes here.
- An interrupted item records the remaining goal, blockers, and resume point.

## 5. Design docs

Each design doc starts with a status: `proposed`, `accepted`, `implemented`, or `superseded`. It covers at least:

1. The problem and the user's intent.
2. The current real call path and the owner of each piece of state.
3. Confirmed facts, inferences, and unknowns, kept apart.
4. The target structure and its boundaries.
5. Failure, concurrency, migration, and rollback.
6. A phased plan.
7. Acceptance criteria that can be judged independently.

## 6. Evidence

- Cite code by symbol and relative path. Line numbers are for one-off reviews only.
- Conclusions taken from old sessions, memory, or historical docs name their source and are re-checked against current code.
- Unverified information is written as unknown, never filled with a plausible guess.
- Keep status levels distinct: proposed, accepted, implemented, verified, deployed.

## 7. Change linkage

| Change | Check |
|---|---|
| Doc added, moved, renamed, or retired | `INDEX.md` and every inbound link |
| Start, verify, or deliver order changed | `WORKFLOW.md`, `AGENTS.md`, `INDEX.md` |
| User-visible behavior or data rules changed | `REQUIREMENTS.md`, related decisions and tests |
| Architecture boundary or ownership changed | New or updated decision record, related design doc |
| New accepted unfinished work | `NOW.md` |
| Work finished and verified | Remove it from `NOW.md` |
| Agent discipline changed | `AGENTS.md` |
| Internal change, behavior unchanged | Usually code and tests only |

When docs and implementation conflict, surface the conflict. Never use vague wording to make both look right.

## 8. Style

- Write in <language>.
- Plain and precise: say who does what to which object, with what result.
- One main judgment per sentence. Use lists for stable mappings and acceptance items.
- Abstract terms land on concrete objects: say which state, which caller, which write.
- Rules may use MUST / MUST NOT. In explanations, prefer stating the target action over stacking prohibitions.
