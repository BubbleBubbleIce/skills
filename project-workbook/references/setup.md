# Setup

The goal is a workbook that stands on its own. An agent without this skill installed must be able to read the repo and learn:

- where to start reading;
- where each kind of fact lives;
- which changes require doc updates;
- how to handle conflicts and unfinished work.

Any rule that lives only in this skill is lost the moment someone works without it, so the rules go into the repo (mainly `WRITING-RULES.md`).

## 1. Survey

Read the existing agent entries first (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.github/copilot-instructions.md`, …) and the doc entry points, then the material relevant to doc roles:

- README, contributing guide, development workflow.
- Requirements, architecture, decision, and operations docs.
- Current tasks, plans, handoff notes, and the issue tracker if one is in use.
- Build, test, and CI config — the commands and gates already in use.

Survey just enough to assign doc roles; setup is not a code audit.

Sort what you find into three buckets:

- **Confirmed** goals and rules — stated by the maintainer or in accepted docs.
- **Demonstrated** facts — what the current implementation shows.
- **Missing or conflicting** material.

Code behavior alone doesn't establish a long-term requirement, and an old plan doesn't establish current status.

Look for entry drift: an agent entry that points to paths that don't exist, or that doesn't point to the docs that do. It is the most common gap and the most damaging, because every session starts there.

## 2. Map roles to paths

Start from the role table in [SKILL.md](../SKILL.md#workbook-roles). In an existing repo:

- A file that already serves a role keeps it; no synonym file is created.
- One file that clearly serves several roles stays whole.
- Scattered but consistent information is linked from INDEX, not moved.
- An existing task tracker owns task status; NOW links to it instead of duplicating it.
- Historical docs keep their historical status. INDEX labels them "leads only — verify against current code" rather than promoting them to current rules.
- Before migrating or deleting important docs, or settling which of two conflicting files is authoritative, describe the concrete impact and get the user's go-ahead.

The final role → path mapping lives in INDEX. No separate config file.

## 3. Fill gaps

**Empty repo** — create the minimum workbook from the templates:

- the agent entry ([agents-snippet.md](../templates/agents-snippet.md) inside `AGENTS.md`);
- `docs/INDEX.md`;
- `docs/WRITING-RULES.md`;
- `docs/NOW.md` — just the header when no work is accepted yet.

Add the rest only when real content exists:

| File | Create when |
|---|---|
| `REQUIREMENTS.md` | At least one goal or constraint is confirmed by the user |
| `WORKFLOW.md` | The project has confirmed commands, stages, or gates beyond the default loop in the agent entry |
| `decisions/` | The first real decision is made |
| `design/` | The first real design exists |

Unconfirmed content is written as "not decided yet" or left out. Invented requirements, commands, progress, or decisions are worse than gaps, because later agents will treat them as fact. An INDEX row may read "(not created yet — create when …)".

**Existing repo** — fill only the gaps that matter; working material isn't rewritten.

## 4. Agent entry

Add a short section to `AGENTS.md`, or to whichever agent entry the repo actually uses, based on [agents-snippet.md](../templates/agents-snippet.md) with real paths. Keep existing content; when a similar rule already exists, edit it in place instead of appending a duplicate.

When several agent entries exist, one holds the rules and the others point to it.

Keep INDEX short. Build reading routes for task areas that exist today, not for modules that might exist later.

## 5. Version control

Workbook files are shared project state and follow the repo's version-control policy. If the new entry points at a file that is gitignored or untracked, report the gap; changing ignore rules is the user's call.

## 6. Verify and deliver

- Every path in INDEX and the agent entry exists, and relative links resolve.
- A fresh agent reading only the agent entry and INDEX can say where requirements, current work, decisions, and workflow live.
- No two files claim the same role.
- Nothing is invented: every requirement, command, and status has a source.

Report:

- files created or changed, and the role each one fills;
- existing files mapped to roles;
- conflicts and gaps that need the user's decision.
