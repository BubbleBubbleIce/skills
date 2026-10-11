# Sync Examples

Four common outcomes. Each shows the facts, the doc actions, and the delivery note. Paths follow the default workbook layout.

## 1. Feature finished, with a decision

**Facts**

- `NOW.md` had: `## P1 · Export` — "Users can download any report as CSV with headers matching the on-screen columns. Done when export works for every report type."
- The diff adds `src/export/csv.ts`, a route, and tests.
- The project's agreed checks (targeted tests and lint, per `WORKFLOW.md`) passed locally. Nothing was deployed.
- During the work the user chose to stream rows instead of building the file in memory, because reports can reach a million rows. Buffering was simpler but ran out of memory.
- `REQUIREMENTS.md` already had `EXP-001`, and its meaning didn't change.

**Doc actions**

| Doc | Action | Why |
|---|---|---|
| `NOW.md` | Delete the P1 · Export section | The acceptance boundary is met and the agreed checks passed |
| `decisions/0004-csv-export-streams-rows.md` | Create, status `accepted` | A lasting trade-off whose reason isn't visible in the code |
| `decisions/README.md` | Add the 0004 row | The index must list every record |
| `REQUIREMENTS.md` | No change | `EXP-001` still describes the behavior |
| `INDEX.md` | No change | The existing route already covers `src/export/` |

**Delivery note**

> Docs synced:
> - `NOW.md`: removed P1 · Export (implemented; targeted tests and lint passed locally; not deployed).
> - `decisions/0004-csv-export-streams-rows.md` + index: recorded streaming vs. in-memory buffering.
>
> Unchanged: `REQUIREMENTS.md` (EXP-001 still accurate), `INDEX.md`.
> Gap: not verified against production-size data.

## 2. Interrupted, blocked on a decision

**Facts**

- The task was moving auth from JWT to server sessions. The backend is done on branch `feat/session-auth`, and its unit tests pass. The frontend hasn't started.
- Work stopped because the cookie domain is undecided: `app.example.com` or `.example.com`. `design/session-auth.md` lists it as an open question.

**Doc actions**

| Doc | Action | Why |
|---|---|---|
| `NOW.md` | Rewrite the item: frontend migration remaining; blocked on the cookie-domain choice; resume from `feat/session-auth` | Accepted work outlives the session |
| `design/session-auth.md` | No change | Status is still `accepted`; the open question is already listed there; progress belongs in NOW |
| Handoff note | Delivered in the reply ([template](../templates/handoff.md)) | Session-level detail: verified facts, pending checks, next action |

The rewritten NOW item:

```markdown
## P0 · Session auth

- Move the frontend to server sessions. Done when login, logout, and refresh work with
  the JWT path removed. Blocked on the cookie-domain choice
  ([design §5](design/session-auth.md#5-failure-migration-rollback)).
  Resume from `feat/session-auth` (backend done, unit tests pass; not run end-to-end).
```

## 3. No doc change

**Facts:** an internal helper `formatDate` was renamed to `formatIsoDate`, and the tests pass. A search of `docs/` finds no reference to either name, and the INDEX routes point to directories, not files.

**Delivery note**

> No doc changes: internal rename, and no doc references the symbol (searched `docs/`).

## 4. Implementation contradicts a requirement

**Facts:** the user asked to fix deleted items still appearing in search. While investigating, it turned out that `cleanup.ts` purges soft-deleted items after 30 days, while `REQUIREMENTS.md` `DAT-002` says they are kept for 90. The user's task covers only the search bug.

**Doc actions**

- `REQUIREMENTS.md`: no change. No confirmed basis exists to move the requirement to 30 days, and the code doesn't define intent.
- `NOW.md`: no change yet. The gap isn't accepted work until the user says so.
- Report the conflict in the delivery note.

**Delivery note**

> Docs: no changes for the search fix (internal query change).
>
> Conflict found, not resolved: `DAT-002` requires keeping soft-deleted items for 90 days, but `src/jobs/cleanup.ts` (`purgeDeleted`) removes them after 30. Either the code or the requirement needs to change. Should I add a NOW item to fix the purge window, or is 30 days the intended rule (which would need a decision record)?
