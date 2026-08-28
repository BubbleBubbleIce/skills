# writing-internship-project-output

一个用于整理中文实习项目产出的 Codex Skill。它把项目代码、设计文档、任务记录、已有笔记或草稿整理成更适合简历和面试表达的材料。

## 功能

- 归纳项目定位、需求背景和技术栈。
- 提炼 4-5 个核心技术亮点，并按“问题背景 -> 技术方案 -> 收益”展开。
- 生成简历项目经历 bullet，控制表达长度和真实性边界。
- 生成面试深挖问题、30 秒介绍话术和避坑提醒。
- 总结开发复盘、真实问题、联调坑点、vibe coding 难点和项目踩坑。
- 检查业务规模、个人贡献、上线状态、性能收益等内容是否有证据支撑。
- 将无法证明的信息移入“待补充信息”，避免编造指标或夸大贡献。

## 目录结构

```text
writing-internship-project-output/
├── SKILL.md
├── README.md
├── scripts/
│   └── validate_output.py
└── references/
    ├── evidence-checklist.md
    ├── output-structure.md
    ├── resume-bullets.md
    └── style-guide.md
```

## 使用方式

在 Codex 中引用该 skill，并提供项目代码、项目说明、已有笔记或草稿:

```text
使用 $writing-internship-project-output，参考这个项目代码和已有文档，
帮我整理一份实习项目产出总结、简历描述和面试话术。
```

如果只需要简历内容，可以明确说明:

```text
使用 $writing-internship-project-output，只输出简历项目经历 bullet 和待补充信息。
```

如果需要真实开发复盘或联调坑点，可以明确说明:

```text
使用 $writing-internship-project-output，结合这个项目代码和已有文档，
总结开发/联调中可能遇到的真实问题、vibe coding 需要人工攻破的难点，
以及可以在面试里讲的复盘话术。
```

## 输出验收

生成完整项目产出、项目总结或评测样稿后，使用验收脚本检查是否覆盖工作流要求:

```bash
python scripts/validate_output.py <output.md> --strict
```

如果只生成简历 bullet 或局部面试话术，可以不加 `--strict`，但仍建议运行脚本检查风险表述。

## 写作原则

- 先看证据，再提炼故事。
- 先保证真实性，再追求表达效果。
- 写真实问题时优先关注需求口径、联调字段、配置验证、展示协议、测试样例和 AI 生成方案纠偏，不要只输出代码审查式 bug 清单。
- 不写没有证据的数字、上线状态或个人贡献。
- 对受限系统、非公开接口、账号、Cookie、Token 和不可公开地址保持脱敏。

## 输出内容

默认完整输出包括:

- 项目定位
- 核心亮点
- 技术深度储备
- 简历段落草稿
- 待补充信息
- 面试话术要点
- 项目意义总结
- 开发/联调真实问题复盘（按用户需要输出）
