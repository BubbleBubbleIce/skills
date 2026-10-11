<!--
Create: always (minimum workbook).
Keep it short: paths, reading conditions, and precedence only. No requirement text, no progress.
For a file not created yet, write its row as "(not created yet — create when …)".
-->

# <Project> Reading Index

The first file every new session reads. It answers three questions: what to read first, what to read next for a given task, and where to verify against the real implementation.

It is not a spec and holds no progress. Requirements live in [REQUIREMENTS.md](REQUIREMENTS.md), current work in [NOW.md](NOW.md), decision rationale in [decisions/](decisions/README.md), and doc maintenance rules in [WRITING-RULES.md](WRITING-RULES.md).

## 1. Start here

1. Read this index.
2. Read [NOW.md](NOW.md) and carry only the items relevant to your task.
3. Read the §3 rows that match your task, and nothing else.
4. Check the real code, config, and tests on the current branch. Docs state intent and rationale; code shows what currently happens.

## 2. Where things live

| File | Answers | When to read |
|---|---|---|
| [`AGENTS.md`](../AGENTS.md) | How agents start, check, and deliver | Every session |
| [`NOW.md`](NOW.md) | What is accepted but unfinished | Every non-trivial task |
| [`REQUIREMENTS.md`](REQUIREMENTS.md) | What the system must keep true | Common sections first, then by area |
| [`WORKFLOW.md`](WORKFLOW.md) | Execution order from task to delivery | Tasks that modify the repo |
| [`WRITING-RULES.md`](WRITING-RULES.md) | Where content goes and how docs are maintained | Adding or editing docs |
| [`decisions/`](decisions/README.md) | Significant choices already made | Scan the index; open only relevant records |
| [`design/`](design/) | Call paths, plans, and acceptance for one problem | When the task hits that problem; check the status line first |

## 3. Reading routes by task

| Task | Read, in order | Then check in code |
|---|---|---|
| Any task that modifies the repo | This index → [WORKFLOW.md](WORKFLOW.md) → the matching row below | Branch, full diff, verification results |
| Adding or editing docs | This index → [WRITING-RULES.md](WRITING-RULES.md) → the target doc's upstream | Relative links, duplicated rules |
| <Area> | REQUIREMENTS §<n> → [decision NNNN](decisions/NNNN-short-title.md) → [design](design/<doc>.md) | `<path>/` |

<!-- Add rows only for areas that exist today. -->

When a task matches two or more rows, changes persistent data, or has irreversible external effects, read REQUIREMENTS in full.

## 4. Conflict precedence

1. The user's current explicit instruction governs this task, read narrowly rather than stretched.
2. [REQUIREMENTS.md](REQUIREMENTS.md) defines long-term goals and invariants.
3. Accepted decision records explain current choices; a later correction outranks a superseded record.
4. [NOW.md](NOW.md) describes current work and cannot redefine requirements.
5. Code, config, and tests show what *is*, not what *should be*.
6. Old notes, past sessions, and memory are leads only; verify them against current sources.

When items 2–5 conflict, state the objects in conflict, the current and intended behavior, and the impact, then ask the maintainer. Don't continue with whichever version is easiest to implement.
