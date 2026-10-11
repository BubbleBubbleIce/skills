<!--
Create: once the project has confirmed commands, stages, or gates beyond the default
loop in the agent entry. Fill in only commands that exist in the repo; mark anything
unconfirmed as such. Doc maintenance rules live in WRITING-RULES.md — link, don't copy.
-->

# <Project> Workflow

The execution order from picking up a task to delivering it. Long-term behavior is defined in [REQUIREMENTS.md](REQUIREMENTS.md); current work is in [NOW.md](NOW.md).

## 1. Stages

```text
Read → Plan → Implement → Verify → Sync docs → Deliver
```

Move to the next stage only when the current stage's exit evidence exists.

| Stage | Do | Exit evidence |
|---|---|---|
| Read | [INDEX.md](INDEX.md) → the routed requirements, NOW items, decisions → real code | Confirmed facts, unknowns, and doc conflicts are listed |
| Plan | State the goal, success criteria, allowed changes, protected state, and side effects | High-risk ambiguity is resolved by the maintainer, or work stops to ask |
| Implement | Change only what the plan allows | The diff adds no undeclared side effect |
| Verify | `<targeted test command>` → `<lint / type / build command>` | Results come from the current source; anything not run is stated |
| Sync docs | Follow [WRITING-RULES.md](WRITING-RULES.md) §7 | Docs, code, and NOW agree |
| Deliver | `<commit / PR convention>` | Another maintainer can review and continue the work |

## 2. Definition of done

- The user-visible goal and success criteria are met.
- The diff stays within the declared scope.
- The agreed checks passed; anything not run has an explicit status.
- Docs match the code, and finished items are gone from NOW.
