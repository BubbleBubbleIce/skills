# Skills

随着模型能力不断提升，一些复杂的 tdd 流程 skill 逐步被淘汰，这个仓库存放的是本人开发中真正会使用到的 skill。


# Skill Name

（具体步骤、约束、输出格式……）
```

编写时注意：

- **description 要可触发**：写清场景与关键词，方便 Agent 自动匹配
- **指令要可执行**：步骤明确，避免空泛原则
- **范围要克制**：一个 skill 专注一类任务，不要塞进无关流程

## 安装与使用

本仓库是 skill 的源。Codex 等 agent 从 `~/.agents/skills` 读取，**不要整目录替换或整目录软链**（仓库里有 `.git` / README，且 `~/.agents/skills` 里还有本仓库没有的第三方 skill）。

做法：把每个 skill **单独软链**到 `~/.agents/skills/<name>`。改仓库即改 agent 侧，无需再复制。

```bash
# 首次，以及以后每加一个新 skill 后跑一次
./scripts/link-skills.sh
```

- 缺的会建链接；内容相同的拷贝会换成链接。
- 若某 skill 在仓库和 `~/.agents/skills` 已经分叉：默认跳过。`--force` 以仓库为准（先备份），`--adopt-agents` 先把 agent 侧拷回仓库再链接。
- 备份目录：`~/.agents/skills-backup/`（不放在 `skills/` 里，避免被扫描成 skill）。

Claude Code 这边若已把 `~/.claude/skills/<name>` 链到 `~/.agents/skills/<name>`，跟着 `~/.agents/skills` 一起更新即可。

### Cursor

- **个人全局**：`~/.cursor/skills/<skill-name>/`（需要的话也可对该目录跑同样的软链）
- **项目内共享**：仓库的 `.cursor/skills/<skill-name>/`

安装后，在对话里描述对应任务即可；Agent 会根据 skill 的 `description` 决定是否启用。

## 添加新 Skill

1. 新建目录：`mkdir <skill-name>`
2. 编写 `SKILL.md`（含 frontmatter）
3. 按需补充 `reference.md` / `examples.md` / `scripts/`
4. 在本 README 的「已有 Skills」中登记一条说明

## 已有 Skills

仓库刚初始化，skills 会陆续迁入。当前列表：

| Skill | 说明 |
|-------|------|
| — | 暂无 |

## License

MIT
