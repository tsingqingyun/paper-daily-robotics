---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.07652v1"
published: "2026-11-05T08:38:51Z"
age_days: 1
score: 36
created: 2026-11-07
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Skillware 把反复需要的执行逻辑做成带类型契约、版本和测试的软件包，让模型主要负责选能力、填参数。它把临场写代码改成调用已准备好的程序，并在执行前检查参数和约束。

## 问题

目标是完成金融筛查等多步工具工作流。若模型每次都重写脚本、猜接口并靠提示记住限制，会反复消耗上下文、修复语法和遗漏步骤。本文试图减少这些执行层错误，而不是训练模型获得新的推理能力。

### 用一个例子理解

理解用例（非论文实验）：用户要求检查一批地址，模型选择筛查能力并填写地址列表；契约先查格式，固定程序查询随包数据并计算结果，返回结构化报告。数据版本决定报告依据，模型无需现场编写筛查逻辑。

## 创新点或方法

旧做法把说明、编程和约束都交给模型；本文把代码、输入输出契约、指引、数据及测试封装起来。运行时先给短签名供选工具，再展开参数 schema，执行前验证，通过后加载代码。[S11](https://arxiv.org/html/2611.07652v1#S3.I1.i1) [S12](https://arxiv.org/html/2611.07652v1#S3.SS1.p1.1) [S13](https://arxiv.org/html/2611.07652v1#S4.p1.1) [S14](https://arxiv.org/html/2611.07652v1#S4.SS1.p4.2) 这是软件运行架构，节选没有模型训练方案；推理时仍由模型选择能力，确定性主要属于受控代码执行部分。

### 方法如何工作

1. 把稳定任务写成版本化程序，附输入输出契约与测试，使执行行为可单独检查。[S2](https://arxiv.org/html/2611.07652v1#abstract1.2) [S11](https://arxiv.org/html/2611.07652v1#S3.I1.i1)
2. 先暴露短能力签名，再按需提供完整参数说明，减少常驻上下文。[S14](https://arxiv.org/html/2611.07652v1#S4.SS1.p4.2)
3. 模型选能力并填参数后，运行时检查类型和执行条件，阻止不合约调用进入程序。[S27](https://arxiv.org/html/2611.07652v1#S6.I1.i3)
4. 执行已验证调用并返回结果；配合审计记录追溯版本和事件，但记录本身不证明结果正确。[S58](https://arxiv.org/html/2611.07652v1#S7.I5.i3)

### 必要术语

- 类型契约：机器可检查的参数与输出规则；本文用它拦截部分格式和约束错误。
- 渐进披露：需要时才加载更详细说明；本文用于降低工具文档的上下文成本。
- 确定性执行：给定相同输入与受控环境，固定代码重复运行可复现；不等于模型每次都选对工具。

## 证据

Skillware-Bench 的模拟工作流比较现场写代码、普通工具调用、完整 Skillware 三组。通过率依次为 58.2%、71.4%、91.8%；普通工具组参数错误率为 14.2%，完整组为 0.0%，安全拦截率从 82.6% 到 92.4%。[S42](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p1.1) 另有每次成功调用 token 中位数从 5,520 到 1,620 的结果。[S19](https://arxiv.org/html/2611.07652v1#S5.SS3.p4.1) 这些支持封装与执行检查在该基准有效，尚不能证明跨领域普遍可靠或机器人能力。

## 局限

我的首要核查问题是统计口径：摘要称 368 种条件，[S20](https://arxiv.org/html/2611.07652v1#S5.SS3.p6.1) 用 736，[S44](https://arxiv.org/html/2611.07652v1#S6.T1) [S50](https://arxiv.org/html/2611.07652v1#S6.T2) 又分别涉及不同模型数量，需查清配对、子集和重复次数。零参数错误也不代表零语义错误；[S17](https://arxiv.org/html/2611.07652v1#S4.SS5.p3.1) 执行分数仍有波动。机器人和脑机接口属于作者展望，[S4](https://arxiv.org/html/2611.07652v1#abstract1.4) 不能当成实验证据。

- **判断**：值得按工程设计文档读契约和运行时，实验结论则应先复核基准口径及普通工具组的配置，暂不接受普遍确定性的强结论。

## 研究关联

可以借鉴的是先划清稳定算法与开放判断：校验、计算、格式转换等已有明确规则的工作，应尽量交给可测试程序。模型继续处理意图与工具选择，既节省生成，也让错误更容易定位到参数、选择或程序本身。

### 下一步读哪里

先看 [S14](https://arxiv.org/html/2611.07652v1#S4.SS1.p4.2) 的分阶段加载和 [S32](https://arxiv.org/html/2611.07652v1#S6.I10.i1) [S33](https://arxiv.org/html/2611.07652v1#S6.I10.i2) [S34](https://arxiv.org/html/2611.07652v1#S6.I10.i3) 三组区别，再核查 [S36](https://arxiv.org/html/2611.07652v1#S6.I11.i1) [S37](https://arxiv.org/html/2611.07652v1#S6.I11.i2) [S38](https://arxiv.org/html/2611.07652v1#S6.I11.i3) [S39](https://arxiv.org/html/2611.07652v1#S6.I11.i4) [S40](https://arxiv.org/html/2611.07652v1#S6.I11.i5) [S41](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.p1.2) [S42](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p1.1) 是否真正逐项控制变量。还应检查错误计数是否包含被拒绝调用、静态数据更新机制，以及费用统计是否计入重试和本地运行成本。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.07652v1
- 获取时间：2026-11-07T03:39:45.166702+00:00
- [S1] [Don’t Prompt Your Agents. Equip Them. Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems · 正文段落 1](https://arxiv.org/html/2611.07652v1#abstract1.1)
- [S2] [Don’t Prompt Your Agents. Equip Them. Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems · 正文段落 2](https://arxiv.org/html/2611.07652v1#abstract1.2)
- [S3] [Don’t Prompt Your Agents. Equip Them. Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems · 正文段落 3](https://arxiv.org/html/2611.07652v1#abstract1.3)
- [S4] [Don’t Prompt Your Agents. Equip Them. Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems · 正文段落 4](https://arxiv.org/html/2611.07652v1#abstract1.4)
- [S5] [1 Introduction: The Stochastic Impedance Mismatch · 正文段落 7](https://arxiv.org/html/2611.07652v1#S1.p2.1)
- [S6] [2.1.1 The Enterprise and Regulatory Layer: The Illusion of Compliance · 正文段落 28](https://arxiv.org/html/2611.07652v1#S2.I1.i2)
- [S7] [2.2 The Chronic Crises of Rented Intelligence: Infrastructure Cascades and Hidden Penalties · 正文段落 43](https://arxiv.org/html/2611.07652v1#S2.I3.i4)
- [S8] [2.3.2 Autonomous Logical Systems: Bounded State and Safe Asynchronous Execution · 正文段落 50](https://arxiv.org/html/2611.07652v1#S2.I5.i3)
- [S9] [2.3.3 Enterprise Operators: Deterministic Logic, Confirmation Gates, and Secret Isolation · 正文段落 51](https://arxiv.org/html/2611.07652v1#S2.I6.i1)
- [S10] [2.3.4 Sovereign Infrastructure: Air-Gapped Autonomy, Supply-Chain Provenance, and Forensic Auditability · 正文段落 56](https://arxiv.org/html/2611.07652v1#S2.I7.i3)
- [S11] [3.1 Formal Mathematical Definition of an Agent Skill · 正文段落 62](https://arxiv.org/html/2611.07652v1#S3.I1.i1)
- [S12] [3.1 Formal Mathematical Definition of an Agent Skill · 正文段落 67](https://arxiv.org/html/2611.07652v1#S3.SS1.p1.1)
- [S13] [4 Runtime Operations, Deterministic Chaining, and Operator Control · 正文段落 92](https://arxiv.org/html/2611.07652v1#S4.p1.1)
- [S14] [4.1 SkillContext: Hierarchical Discovery and Shadow Guards · 正文段落 102](https://arxiv.org/html/2611.07652v1#S4.SS1.p4.2)
- [S15] [4.3 Operator Infrastructure: Segregated Identity and State · 正文段落 116](https://arxiv.org/html/2611.07652v1#S4.I2.i1)
- [S16] [4.5 Execution Telemetry: Call Survival Flow and Run-to-Run Determinism · 正文段落 129](https://arxiv.org/html/2611.07652v1#S4.SS5.p2.1)
- [S17] [4.5 Execution Telemetry: Call Survival Flow and Run-to-Run Determinism · 正文段落 131](https://arxiv.org/html/2611.07652v1#S4.SS5.p3.1)
- [S18] [5.2 Soft Skills vs. Hard Skills: The Moat of Executable Software · 正文段落 145](https://arxiv.org/html/2611.07652v1#S5.SS2.p3.1)
- [S19] [5.3 Empirical Cost Economics: Multi-Turn Scaling · 正文段落 156](https://arxiv.org/html/2611.07652v1#S5.SS3.p4.1)
- [S20] [5.3 Empirical Cost Economics: Multi-Turn Scaling · 正文段落 160](https://arxiv.org/html/2611.07652v1#S5.SS3.p6.1)
- [S21] [5.3 Empirical Cost Economics: Multi-Turn Scaling · 正文段落 161](https://arxiv.org/html/2611.07652v1#S5.F12)
- [S22] [5.4 The Empirical Parameter Paradox: Asymmetric Lift Across Model Scales · 正文段落 162](https://arxiv.org/html/2611.07652v1#S5.SS4.p1.1)
- [S23] [5.4 The Empirical Parameter Paradox: Asymmetric Lift Across Model Scales · 正文段落 163](https://arxiv.org/html/2611.07652v1#S5.SS4.p2.1)
- [S24] [5.4 The Empirical Parameter Paradox: Asymmetric Lift Across Model Scales · 正文段落 164](https://arxiv.org/html/2611.07652v1#S5.SS4.p3.1)
- [S25] [5.4 The Empirical Parameter Paradox: Asymmetric Lift Across Model Scales · 正文段落 168](https://arxiv.org/html/2611.07652v1#S5.I4.i3)
- [S26] [5.4 The Empirical Parameter Paradox: Asymmetric Lift Across Model Scales · 正文段落 169](https://arxiv.org/html/2611.07652v1#S5.F13)
- [S27] [6.1 Taxonomic Framework: Seven Architectural Dimensions · 正文段落 177](https://arxiv.org/html/2611.07652v1#S6.I1.i3)
- [S28] [6.4 Skillware vs. Antigravity Skills (Agentic Coding Skills) · 正文段落 194](https://arxiv.org/html/2611.07652v1#S6.I4.i2)
- [S29] [6.10 Comprehensive Cross-Model Evaluation: The Skillware-Bench Crucible · 正文段落 208](https://arxiv.org/html/2611.07652v1#S6.SS10.p2.1)
- [S30] [6.10 Comprehensive Cross-Model Evaluation: The Skillware-Bench Crucible · 正文段落 211](https://arxiv.org/html/2611.07652v1#S6.I9.i3)
- [S31] [6.10.1 Experimental Triangulation: The Three Operational Evaluation Arms · 正文段落 217](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS1.p1.1)
- [S32] [6.10.1 Experimental Triangulation: The Three Operational Evaluation Arms · 正文段落 218](https://arxiv.org/html/2611.07652v1#S6.I10.i1)
- [S33] [6.10.1 Experimental Triangulation: The Three Operational Evaluation Arms · 正文段落 219](https://arxiv.org/html/2611.07652v1#S6.I10.i2)
- [S34] [6.10.1 Experimental Triangulation: The Three Operational Evaluation Arms · 正文段落 220](https://arxiv.org/html/2611.07652v1#S6.I10.i3)
- [S35] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 221](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.p1.1)
- [S36] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 222](https://arxiv.org/html/2611.07652v1#S6.I11.i1)
- [S37] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 223](https://arxiv.org/html/2611.07652v1#S6.I11.i2)
- [S38] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 224](https://arxiv.org/html/2611.07652v1#S6.I11.i3)
- [S39] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 225](https://arxiv.org/html/2611.07652v1#S6.I11.i4)
- [S40] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 226](https://arxiv.org/html/2611.07652v1#S6.I11.i5)
- [S41] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 227](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.p1.2)
- [S42] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 228](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p1.1)
- [S43] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 229](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p2.1)
- [S44] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 230](https://arxiv.org/html/2611.07652v1#S6.T1)
- [S45] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 231](https://arxiv.org/html/2611.07652v1#S6.SS10.SSS2.Px1.p3.1)
- [S46] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 232](https://arxiv.org/html/2611.07652v1#S6.I12.i1)
- [S47] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 233](https://arxiv.org/html/2611.07652v1#S6.I12.i2)
- [S48] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 234](https://arxiv.org/html/2611.07652v1#S6.I12.i3)
- [S49] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 235](https://arxiv.org/html/2611.07652v1#S6.I12.i4)
- [S50] [6.10.2 Component-by-Component Load-Bearing Ablation Analysis · 正文段落 236](https://arxiv.org/html/2611.07652v1#S6.T2)
- [S51] [6.11 Empirical Frontiers: Latency Anatomy, Pareto Dominance, and Small Model Parity · 正文段落 239](https://arxiv.org/html/2611.07652v1#S6.F14)
- [S52] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 272](https://arxiv.org/html/2611.07652v1#S7.SS4.p1.1)
- [S53] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 273](https://arxiv.org/html/2611.07652v1#S7.SS4.p2.1)
- [S54] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 274](https://arxiv.org/html/2611.07652v1#S7.E13)
- [S55] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 275](https://arxiv.org/html/2611.07652v1#S7.SS4.p3.1)
- [S56] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 276](https://arxiv.org/html/2611.07652v1#S7.I5.i1)
- [S57] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 277](https://arxiv.org/html/2611.07652v1#S7.I5.i2)
- [S58] [7.4 Egress Governance: Pre-Execution Policy Interception · 正文段落 278](https://arxiv.org/html/2611.07652v1#S7.I5.i3)
- [S59] [8.4 Adversarial Evaluation: Empirical Injection and Boundary Stress Tests · 正文段落 310](https://arxiv.org/html/2611.07652v1#S8.SS4.p2.1)
- [S60] [8.4 Adversarial Evaluation: Empirical Injection and Boundary Stress Tests · 正文段落 315](https://arxiv.org/html/2611.07652v1#S8.T4)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/Don't Prompt Your Agents. Equip Them Skillware as a Modular Standard for Soverei.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current autonomous logical systems rely on a fragile assumption: that language models should dynamically write code, guess API payloads, and memorize operational constraints through prompt engineering. In practice, this burns massive context windows, inflates API bills, and produces brittle agents that fail unpredictably in production. In this work, we present Skillware, an open architectural framework and capability registry that formally separates what an agent wants to do from how that task is executed. Instead of prompting models with loose text instructions or markdown files baptized as 'skills', Skillware equips them with modular, versioned software capability bundles. Much like skill hotkeys in video games that execute deterministically under fixed world rules, each bundle combines a typed JSON input contract, deterministic Python code, task directives, bundled datasets, and automated unit tests. In-process adapters translate these capabilities into native tool declarations for any model, from frontier cloud APIs to local open-weight runtimes with zero network latency. Evaluating 23 frontier and open-weight models across 368 benchmark conditions, we show that small local models (3B to 8B parameters) equipped with Skillware consistently outperform unequipped frontier models on complex multi-step workflows. They cut token usage by up to 84.8%, slash inference costs by up to 97.3%, and eliminate parameter errors entirely. True agent reliability does not come from larger models or longer prompts, but from equipping logical systems with verified, deterministic software. Finally, we articulate the trajectory of capability bundles across an invariant continuum of information processing systems: from digital logical systems today, to IoT, drones, and embodied robotics tomorrow, establishing a foundation for auditable, real-time capability execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.07652v1
- Authors: Vladimiros Peilivanidis
- Published: 2026-11-05T08:38:51Z
- Age days: 1

</details>
