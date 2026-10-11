<!--
Create: once at least one goal or constraint is confirmed by the user.
Only confirmed content. Anything unconfirmed goes under "Open questions".
-->

# <Project> Requirements

The long-term spec: what the system must keep true. Current work is in [NOW.md](NOW.md); rationale is in [decisions/](decisions/README.md).

## 1. Conventions

- **MUST / MUST NOT** — merge gate. A violation is a bug unless the requirement is changed first.
- **SHOULD** — the default. Deviating needs a recorded reason.
- **MAY** — free choice within the other clauses.

Clause IDs (`<AREA>-NNN`) are stable addresses for PRs, tests, and conversations. Rewording keeps the ID. A change in meaning needs a decision record covering compatibility and migration. Retired IDs are never reused.

### Reading routes

| Task area | Read |
|---|---|
| Every non-trivial task | §1–2 |
| <Area> | §<n> |

## 2. Goals

### OBJ-001 <Short title>

<The observable outcome: what a user or the system can see when this holds.>

## 3. <Area>

### <AREA>-001 <Short title>

<Observable behavior first, then forbidden paths. Name the protected state, the allowed changes, and what happens on failure. "Must be safe" or "must be stable" alone is not a complete clause.>

## Open questions

- <Unconfirmed point. It stays here until the maintainer decides; it is not a requirement.>
