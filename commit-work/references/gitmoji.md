# Gitmoji quick reference

Source of truth: [gitmoji.dev](https://gitmoji.dev/). Use **one** Unicode emoji per commit, chosen by **intent** of the staged change.

## Prefer these when they fit better than the type default

| emoji | intent | typical Conventional type |
|-------|--------|---------------------------|
| 🎨 | Improve structure / format of the code | style / refactor |
| ⚡️ | Improve performance | perf |
| 🔥 | Remove code or files | chore / refactor |
| 🐛 | Fix a bug | fix |
| 🚑️ | Critical hotfix | fix |
| ✨ | Introduce new features | feat |
| 📝 | Add or update documentation | docs |
| 🚀 | Deploy stuff | chore |
| 💄 | Add or update UI and style files | style / feat |
| ✅ | Add, update, or pass tests | test |
| 🔒 | Fix security or privacy issues | fix |
| 🔐 | Add or update secrets | chore |
| 🔖 | Release / version tags | chore |
| 🚨 | Fix compiler / linter warnings | fix |
| 🚧 | Work in progress | chore |
| 💚 | Fix CI build | fix / ci |
| ⬇️ | Downgrade dependencies | build |
| ⬆️ | Upgrade dependencies | build |
| 📌 | Pin dependencies to specific versions | build |
| 👷 | Add or update CI build system | ci |
| 📈 | Add or update analytics / tracking | feat |
| ♻️ | Refactor code | refactor |
| ➕ | Add a dependency | build |
| ➖ | Remove a dependency | build |
| 🔧 | Add or update configuration files | chore |
| 🔨 | Add or update development scripts | chore |
| 🌐 | Internationalization and localization | feat |
| ✏️ | Fix typos | fix / docs |
| ⏪️ | Revert changes | revert |
| 🔀 | Merge branches | chore |
| 📦️ | Add or update compiled files or packages | build |
| 👽️ | Update code due to external API changes | fix / refactor |
| 🚚 | Move or rename resources (files, paths, routes) | chore / refactor |
| 📄 | Add or update license | docs / chore |
| 💥 | Introduce breaking changes | feat / fix (`!`) |
| 🍱 | Add or update assets | chore / feat |
| ♿️ | Improve accessibility | feat / fix |
| 💡 | Add or update comments in source code | docs / chore |
| 💬 | Add or update text and literals | feat / fix |
| 🗃️ | Database-related changes | feat / fix |
| 🔊 | Add or update logs | feat / chore |
| 🔇 | Remove logs | refactor / chore |
| 👥 | Add or update contributor(s) | docs / chore |
| 🚸 | Improve UX / usability | feat / fix |
| 🏗️ | Architectural changes | refactor |
| 📱 | Responsive design | style / feat |
| 🤡 | Mock things | test |
| 🙈 | Add or update `.gitignore` | chore |
| 📸 | Add or update snapshots | test |
| ⚗️ | Perform experiments | chore / feat |
| 🔍️ | Improve SEO | feat |
| 🏷️ | Add or update types | feat / refactor |
| 🌱 | Add or update seed files | chore |
| 🚩 | Feature flags (add/update/remove) | feat / chore |
| 🥅 | Catch errors | fix / feat |
| 💫 | Animations and transitions | feat / style |
| 🗑️ | Deprecate code that needs cleanup | chore / refactor |
| 🛂 | Authorization, roles, permissions | feat / fix |
| 🩹 | Simple fix for a non-critical issue | fix |
| 🧐 | Data exploration / inspection | chore |
| ⚰️ | Remove dead code | refactor / chore |
| 🧪 | Add a failing test | test |
| 👔 | Business logic | feat / refactor |
| 🩺 | Healthcheck | feat / chore |
| 🧱 | Infrastructure | build / chore |
| 🧑‍💻 | Developer experience | chore / feat |
| 🧵 | Multithreading / concurrency | feat / fix |
| 🦺 | Validation | feat / fix |
| ✈️ | Offline support | feat |
| 🦖 | Backwards compatibility | feat / fix |

## Selection rules

1. Match **what the commit does**, not the file path alone.
2. If two emojis fit, prefer the more specific one (e.g. ⬆️ over 🔧 for a dependency bump; 🚑️ over 🐛 for a production hotfix).
3. Breaking changes: use 💥 (and `!` / `BREAKING CHANGE:` as usual).
4. Never invent emojis outside gitmoji; if unsure, fall back to the type default in `SKILL.md`.
