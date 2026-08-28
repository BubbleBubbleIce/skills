# Research: Skill-to-LoRA (S2L) 与「skills → LoRA/参数」相关工作

> 整理日期：2026-08-06  
> 范围：以 [Skill-to-LoRA (S2L)](https://arxiv.org/abs/2606.16769) 为核心，并覆盖同期/相邻的 skills→权重 工作与 S2L 文中提及的谱系论文。  
> 原则：结论均锚定 arXiv 主页/摘要等一手来源；不外推未在论文中出现的数字或引用。

---

## Summary

**Skill-to-LoRA (S2L)**（Tianyi Zhang & Zhonghao Qi, CUHK；arXiv:2606.16769）提出一种 *behavior-centric* 的技能表示：离线用完整 `SKILL.md` 做 skill-based self-distillation，把技能诱导的行为蒸馏进 **per-skill LoRA**；在线只加载对应 adapter、省略全文技能正文，从而降低反复注入上下文的成本，并缓解长技能文本对推理的干扰。([arxiv abs](https://arxiv.org/abs/2606.16769))

在 **SWE-Skills-Bench 的 21-skill 子集**、基座 **Qwen3.6-27B** 上，相对 no-skill / Full Skill Text，S2L 的 pass rate 分别 **+2.9 / +5.2 个百分点**；相对 Full Skill Text，per-step token cost **−6.6%**；**18/21** 技能匹配或超过 Full Skill Text。Wrong-LoRA 与 Shared-LoRA 控制实验均更差，说明收益依赖 **技能对齐的专用 adapter**。代码声明 **“will be released upon acceptance”**（预印本阶段）。([arxiv abs](https://arxiv.org/abs/2606.16769))

同期相邻路线包括 **LatentSkill**（超网络即时生成 skill LoRA）与 **ParametricSkills**（测试时将文本技能参数化为 LoRA）；S2L 相关谱系还包括 Text-to-LoRA、Doc-to-LoRA、PromptIntern、SKILL0 等「把重复上下文/技能迁入参数」工作。整体仍是 **早期研究线**：技能从 **context → weights**。

---

## Core idea

| 维度 | 要点 | 来源 |
|------|------|------|
| 问题 | Agent skills 常以 `SKILL.md` 分发；部署时反复把同一可复用流程注入 runtime context，既费 token，也可能与仓库证据竞争、放大动作空间。SWE-Skills-Bench 报告：即便 curated skill prompting 也常 **neutral or harmful**。 | [S2L abs/HTML](https://arxiv.org/abs/2606.16769) |
| 目标 | 保留技能诱导的程序化行为，但 **推理时不再读完整技能正文**，并降低 context 长度与 token 开销。 | [S2L §3.1](https://arxiv.org/html/2606.16769) |
| 表示 | 不直接压缩技能文档文本；建模「注入技能后模型行为如何改变」，用轻量 LoRA 存该 *functional bias*。 | [S2L abs](https://arxiv.org/abs/2606.16769) |
| 运行时 | 仅保留轻量 skill metadata 做路由；动态加载匹配的 LoRA adapter。 | [S2L abs](https://arxiv.org/abs/2606.16769) |

一句话：从「每步读技能说明书」变为「加载已学到的技能行为模块」。

---

## Method

两阶段流水线（offline 转换 + online 激活）：

1. **Offline · skill-based self-distillation**  
   - 用完整 `SKILL.md` 自动合成任务输入与「技能条件下」的目标输出（无需大规模人工标注）。  
   - Teacher：带 Full Skill Text 的 LLM；Student：冻结基座 + 可训练 LoRA，只见任务输入（外加短 skill id 路由信息），拟合 teacher 行为演示。  
   - 对库中每个技能训练 **独立** LoRA，得到 adapter library \(\mathcal{A}=\{A_s\}\)。  
   来源：[S2L §3.2](https://arxiv.org/html/2606.16769)

2. **Online · skill-conditioned LoRA activation**  
   - 按任务对应 skill id 加载 \(A_s\)；**不注入完整 SKILL.md**。  
   - 多技能共享同一冻结基座，靠换 adapter 切换技能。  
   来源：[S2L §3.3](https://arxiv.org/html/2606.16769)

**训练配置（论文报告）**：QLoRA；每技能独立 adapter，\(r=16\)、\(\alpha=32\)、目标模块 `q_proj`/`v_proj`；约 **6.03M** 可训练参数（约基座 **0.022%**），约 **24MB** 存储；vLLM 动态 LoRA serving。([S2L §4](https://arxiv.org/html/2606.16769))

**评测设定**：SWE-Skills-Bench 固定 **21 skills / 210 tasks**（含全部 7 个 skill prompting 有正向 gain 的技能 + 14 个零增益但 token 成本极端的技能）；基座 **Qwen3.6-27B**；对比 Vanilla（无技能）、Full Skill Text、S2L，以及 Wrong-LoRA / Shared-LoRA。([S2L §4](https://arxiv.org/html/2606.16769))

---

## Results

数字均来自 S2L 摘要与正文 Table 1 / §5（聚合：Vanilla **59/210**，Full Skill Text **54/210**，S2L **65/210**）。

| 指标 | 报告结果 | 来源 |
|------|----------|------|
| Pass rate vs no-skill (Vanilla) | **+2.9** percentage points | [abs](https://arxiv.org/abs/2606.16769) |
| Pass rate vs Full Skill Text | **+5.2** percentage points | [abs](https://arxiv.org/abs/2606.16769) |
| Per-step token cost vs Full Skill Text | **−6.6%** | [abs](https://arxiv.org/abs/2606.16769) |
| 相对 Vanilla 的 token \(\rho\)（Table 1 聚合） | Full Skill Text **+13.39%**；S2L **−4.89%** | [Table 1](https://arxiv.org/html/2606.16769) |
| 技能级对照 Full Skill Text | **18/21** match or improve | [abs](https://arxiv.org/abs/2606.16769) |
| 技能级对照 no-skill | **15/21** match or improve | [abs](https://arxiv.org/abs/2606.16769) |
| CNG（相对 Vanilla） | S2L **0.58**；Full Skill Text **−0.18** | [Table 1 / §5.1](https://arxiv.org/html/2606.16769) |

**控制 / 消融（论文用语：control experiments）**

- **Shared-LoRA**（多技能演示池化训一个 adapter）：在 6 个代表技能上全面弱于 skill-specific S2L（例：`gitlab-ci-patterns` Shared **3/10** → S2L **7/10**）。([§5.2](https://arxiv.org/html/2606.16769))  
- **Wrong-LoRA**（加载最不相似技能的 adapter）：摘要写明与 Shared-LoRA 一样会降低性能；§5.2 的检索错配实验进一步显示：错误技能条件下 Full Skill Text 快速塌向 Vanilla，而 S2L 仍明显高于 Vanilla。([abs](https://arxiv.org/abs/2606.16769)；[§5.2 / Fig. 4](https://arxiv.org/html/2606.16769))  
- **Rank / 数据规模**（`gitlab-ci-patterns`）：选中配置为 **64 rows、rank 16**；更大数据量（128 rows）或更高 rank 未必更好。([Table 2](https://arxiv.org/html/2606.16769))

---

## Related work

### 同期 / 相邻：「skills → LoRA / 参数」

| 工作 | 核心机制（一手摘要） | 与 S2L 的粗对照 |
|------|----------------------|-----------------|
| **LatentSkill** ([arXiv:2606.06087](https://arxiv.org/abs/2606.06087)) | 用 **预训练超网络** 把文本技能编译为可插拔 LoRA；推理去掉逐步 skill tokens。ALFWorld seen/unseen 相对 in-context skill **+21.4 / +13.4** points，prefill tokens **−64.1%**；Search-QA EM **+3.0**，skill-token overhead **−72.2%**。强调权重空间结构、\(\alpha\) 可控、参数算术可组合。 | 同属「技能进权重、减上下文」；LatentSkill 偏 **hypernetwork 即时生成 + 组合**，评测在 ALFWorld / Search-QA；S2L 偏 **每技能离线 QLoRA 蒸馏 + SWE-Skills-Bench**。 |
| **ParametricSkills** ([arXiv:2606.30015](https://arxiv.org/abs/2606.30015)) | 大规模技能库 + OpenCode 轨迹，训练超网络在 **test time** 把自由文本技能转为 LoRA，实现 context-free skill exploitation。六类复杂 SWE 子任务上，相对 ICL 平均 **+6.44** points（DeepSeek-V4-Flash 评判），并报告更高 BERT Score / F1；讨论与持续学习、技能自演化结合。 | 同样把技能参数化；强调 **超网络 + 利用方法内化 + 多技能 merge**；S2L 用监督自蒸馏、单技能单 adapter、SWE-Skills-Bench verifier pass。 |

### S2L 文中点名的谱系（parameter-side internalization）

摘自 S2L Related Work「Parameter-side context and skill internalization」段落：([S2L §2](https://arxiv.org/html/2606.16769))

| 工作 | 一手要点 | URL |
|------|----------|-----|
| **PromptIntern** | 微调时把重复 prompt（指令模板、few-shot 等）内化进参数，推理少依赖长 prompt；NL2Code 上报告输入 token **>90%** 减少、推理 **4.2×**、费用 **−88.3%**。 | [arXiv:2407.02211](https://arxiv.org/abs/2407.02211) |
| **Text-to-LoRA** | 超网络根据自然语言任务描述 **单次前向** 生成 LoRA，支持适配器库压缩与未见任务 zero-shot。 | [arXiv:2506.06105](https://arxiv.org/abs/2506.06105) |
| **Doc-to-LoRA** | 超网络把文档/上下文近似「蒸馏」为 LoRA，后续查询可不重消费原上下文，降延迟与 KV 缓存。 | [arXiv:2602.15902](https://arxiv.org/abs/2602.15902) |
| **SKILL0**（文题 *Skill0*） | **Agentic RL 课程**：训练时逐渐撤掉 skill context，用环境反馈把技能内化进参数，推理零技能检索；报告相对标准 RL 基线 ALFWorld **+9.7%**、Search-QA **+6.6%**、WebShop **+10.1%**，逐步上下文 **<0.5k** tokens。S2L 明确对比：SKILL0 走 RL 撤上下文，S2L 走 **技能条件合成演示的监督 LoRA**。 | [arXiv:2604.02268](https://arxiv.org/abs/2604.02268) |

---

## Open questions / limits

直接来自 S2L Limitations / Discussion（及相邻工作隐含的开放问题）：

1. **适用技能类型**：对工作流稳定、产物 schema 清晰、验证步骤明确的 procedural skills 更有效；强依赖具体代码样例、灵活语法迁移或开放式推理的技能，仍可能需要 runtime 文本。([S2L Limitations](https://arxiv.org/html/2606.16769))  
2. **行为压缩损失**：adapter 学的是主导行为效应，未必保留技能文档全部细节；稀有边角或高度特定配置可能丢失。([同上](https://arxiv.org/html/2606.16769))  
3. **可解释性 / 可编辑性**：LoRA 中的行为比 `SKILL.md` 更难直接检查与手工修改。([同上](https://arxiv.org/html/2606.16769))  
4. **多技能组合**：当前设定 **每任务一技能、推理时激活单个 adapter**；多技能交互、adapter 路由与行为冲突仍开放（LatentSkill / ParametricSkills 在组合方向上有额外探索，但是否通用于 SWE 文件式技能库仍待验证）。([S2L Limitations](https://arxiv.org/html/2606.16769)；[LatentSkill abs](https://arxiv.org/abs/2606.06087)；[ParametricSkills abs](https://arxiv.org/abs/2606.30015))  
5. **工程与发布状态**：S2L 为 **preprint**；**代码将于录用后发布**——可复现性与生态工具链仍早期。([S2L abs](https://arxiv.org/abs/2606.16769))  
6. **研究线定位**：2026 年中前后多篇工作并行把「Agent Skills / 长上下文指令」从 prompt 迁到 LoRA/权重；方法分叉（离线 per-skill SFT vs 超网络 vs RL 内化），统一基准与生产标准尚未成熟。

---

## Sources

| # | 文献 | 类型 | URL |
|---|------|------|-----|
| 1 | Zhang & Qi. *Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents*. arXiv:2606.16769 | 核心预印本 | https://arxiv.org/abs/2606.16769 · https://arxiv.org/html/2606.16769 |
| 2 | Yu et al. *LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents*. arXiv:2606.06087 | 同期相关 | https://arxiv.org/abs/2606.06087 |
| 3 | Zhao et al. *Parametric Skills*. arXiv:2606.30015 | 同期相关 | https://arxiv.org/abs/2606.30015 |
| 4 | Charakorn et al. *Text-to-LoRA: Instant Transformer Adaption*. arXiv:2506.06105 | S2L 谱系 | https://arxiv.org/abs/2506.06105 |
| 5 | Charakorn et al. *Doc-to-LoRA: Learning to Instantly Internalize Contexts*. arXiv:2602.15902 | S2L 谱系 | https://arxiv.org/abs/2602.15902 |
| 6 | Zou et al. *PromptIntern: Saving Inference Costs by Internalizing Recurrent Prompt during Large Language Model Fine-tuning*. arXiv:2407.02211 | S2L 谱系 | https://arxiv.org/abs/2407.02211 |
| 7 | Lu et al. *Skill0: In-Context Agentic Reinforcement Learning for Skill Internalization*. arXiv:2604.02268 | S2L 谱系（文中写作 SKILL0） | https://arxiv.org/abs/2604.02268 |

**未纳入独立数字断言的引用**（仅在 S2L 问题背景中出现，如需 dig deeper 可再开笔记）：SWE-Skills-Bench ([arXiv:2603.15401](https://arxiv.org/abs/2603.15401))、SkillsBench ([arXiv:2602.12670](https://arxiv.org/abs/2602.12670))。
