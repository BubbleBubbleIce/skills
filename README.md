# Skills

个人 Agent Skills 合集：为 Cursor、Claude Code、Codex 等 AI 编程助手提供可复用的工作流与领域知识。

每个 skill 是一份结构化说明（通常是 `SKILL.md`），告诉 Agent **何时启用**、**怎么做**、以及需要遵守的约束。把重复性流程写成 skill 后，Agent 就能稳定按同一套规范执行。

## 目录结构

```text
skills/
├── README.md
└── <skill-name>/
    ├── SKILL.md          # 必需：触发条件与核心指令
    ├── reference.md      # 可选：补充文档
    ├── examples.md       # 可选：示例
    └── scripts/          # 可选：辅助脚本
```

## Skill 约定

每个 skill 目录下的 `SKILL.md` 使用 YAML frontmatter + Markdown 正文：

```markdown
---
name: skill-name
description: 一句话说明做什么、何时使用
---

# Skill Name

（具体步骤、约束、输出格式……）
```

编写时注意：

- **description 要可触发**：写清场景与关键词，方便 Agent 自动匹配
- **指令要可执行**：步骤明确，避免空泛原则
- **范围要克制**：一个 skill 专注一类任务，不要塞进无关流程

## 安装与使用

### Cursor

- **个人全局**：复制到 `~/.cursor/skills/<skill-name>/`
- **项目内共享**：复制到仓库的 `.cursor/skills/<skill-name>/`

### Claude Code

复制到 `~/.claude/skills/<skill-name>/`，或按 Claude Code 文档中的 skills 路径配置。

### Codex

复制到 `~/.codex/skills/<skill-name>/`，或按 Codex 文档中的 skills 路径配置。

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
