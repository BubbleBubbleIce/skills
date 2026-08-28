# Commit message template (gitmoji + Conventional Commits)

```text
<emoji> <type>(<scope>): <summary>

<What changed.>
<Why it changed.>
```

## Examples

```text
✨ feat(auth): add JWT refresh tokens

Issue short-lived access tokens and rotate refresh tokens on use
so stolen tokens have a narrow window of abuse.
```

```text
🐛 fix(api): handle null profile on first login

New users have no profile row yet; return an empty profile instead
of 500 so onboarding can continue.
```

```text
♻️ refactor(ui): extract menu state into useMenu hook

Keep Header presentational and make menu behavior unit-testable.
```

```text
💥 feat(api)!: require Idempotency-Key on POST /orders

BREAKING CHANGE: clients must send Idempotency-Key; duplicate
requests without it are rejected with 400.
```

## Notes
- Put the Unicode emoji first, then a space, then the Conventional Commits header.
- Keep the summary imperative and specific ("Add", "Fix", "Remove", "Refactor").
- Avoid implementation minutiae; focus on behavior and intent.
- If breaking: use `!` after type/scope and/or add `BREAKING CHANGE:` footer; prefer 💥 when the commit introduces a breaking change.
- One emoji only — pick the best match from [gitmoji.md](gitmoji.md).
