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
url: "https://arxiv.org/abs/2610.07652v1"
published: "2026-10-06T02:47:22Z"
age_days: 0
score: 45
created: 2026-10-07
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> SMART 把开门、拉抽屉这类必须沿关节运动的操作，做成能批量生成的仿真示范。关键是先标明可操作部件和运动约束，再让任务生成智能体组合技能，避免生成看似合理却无法保持接触的动作。

## 问题

操作活动物体时，抓住把手只是开始，还得持续接触并沿滑轨或铰链移动。真人示范难规模化，人体动作转成机器人动作还可能不可执行；通用仿真生成流程又缺部件语义和关节约束，难以覆盖多种对象 [S5](https://arxiv.org/html/2610.07652v1#S1.p2.1) [S6](https://arxiv.org/html/2610.07652v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“拉开这个抽屉”；生成智能体找到抽屉资产和把手标注，组合抓取与拉动技能；规划器沿滑轨生成示范，训练后视觉策略依据画面输出抓取和拉动动作。

## 创新点或方法

旧流程主要扩大任务和轨迹数量；SMART-Sim 先让资产带有操作坐标与关节信息，再针对接触阶段生成受约束轨迹。自由空间使用 cuRobo 规划，接触阶段利用仿真中的精确关节类型、位置和范围优化动作，并过滤不稳定轨迹 [S15](https://arxiv.org/html/2610.07652v1#S3.SS2.p4.1)。智能体负责找资产、组合已有技能，不负责凭空发明低层控制 [S21](https://arxiv.org/html/2610.07652v1#S4.SS1.p3.1)。仿真基准训练先用 SMART-Data 学动作 token，再加入连续动作专家，在下游数据上训练 [S23](https://arxiv.org/html/2610.07652v1#S5.SS1.p1.1)；推理输出机器人动作。真机零样本实验的完整训练配方未提供。

### 方法如何工作

1. 标注物体部件及可运动方向，使任务语言能对应到具体操作位置。
2. 智能体检索资产并组合已有技能，得到含初始状态和成功条件的仿真配置。
3. 按自由运动与接触运动分别规划，并筛掉不可执行轨迹，得到有效示范。
4. 并行生成多对象、多配置数据，用于预训练；下游训练和真机零样本流程应分别检查，不能混为一次实验。

### 必要术语

- 活动物体：部件通过滑轨、铰链等连接的物体；动作必须遵守这些连接。
- 操作坐标系：标在可操作部件上的位置与方向参照；帮助规划抓取和运动。
- 仿真特权信息：模拟器知道的精确关节状态；用于生成示范，不等于部署输入。
- 行为克隆：从示范学习观察到动作的对应关系；SMART 用它利用合成数据。

## 证据

数据超过 100 万条示范，覆盖 44 种原子任务、5 种机器人配置和 2,507 个活动物体（摘要）。仿真测试使用 LIBERO、RoboCasa365，控制架构与下游训练配方，对比合成预训练、真实数据预训练和无第一阶段预训练 [S22](https://arxiv.org/html/2610.07652v1#S5.p1.1) [S23](https://arxiv.org/html/2610.07652v1#S5.SS1.p1.1) [S24](https://arxiv.org/html/2610.07652v1#S5.SS1.p2.1)。真机测试覆盖三个双臂平台、十二项任务，并对齐仿真与真实相机参数 [S25](https://arxiv.org/html/2610.07652v1#S6.p1.1) [S29](https://arxiv.org/html/2610.07652v1#S6.SS1.p1.1) [S31](https://arxiv.org/html/2610.07652v1#S6.SS1.p2.1)。材料报告正向迁移和规模趋势，但未给成功率、试验次数及曲线，无法量化收益或判断稳定性。

## 局限

作者明确指出长任务生成成功率下降、智能体可能幻觉、资产分离与关节标注需要大量后处理 [S33](https://arxiv.org/html/2610.07652v1#S7.p1.1)。我的待核查问题是：真机任务需要多少专门资产准备，以及零样本是否只指不使用真实任务示范。仿真规划器使用精确物理信息，不意味着部署策略能直接获得这些信息。

- **判断**：值得深入读轨迹约束与质量筛选；零样本真机迁移很值得关注，但需拿到逐任务结果和数据配方后判断可复用程度。

## 研究关联

可借鉴的是把任务生成建立在可执行的部件语义上：语言可以组合“抓、拉、转”，但每个动作必须有对应的物理约束。这样扩大数据时，增加的是有效交互，而不只是更多描述。

### 下一步读哪里

沿 [S15](https://arxiv.org/html/2610.07652v1#S3.SS2.p4.1) 检查接触轨迹优化的约束和筛选标准，沿 [S20](https://arxiv.org/html/2610.07652v1#S4.SS1.p2.1) [S21](https://arxiv.org/html/2610.07652v1#S4.SS1.p3.1) 检查生成配置如何验证。重点核查真机各任务的成功率、随机化范围，以及预训练收益与任务专用仿真数据收益是否分开测量。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：45
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.07652v1
- 获取时间：2026-10-07T02:13:50.783783+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.07652v1#p1.2)
- [S2] [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining · 正文段落 2](https://arxiv.org/html/2610.07652v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.07652v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.07652v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.07652v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.07652v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.07652v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.07652v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.07652v1#S1.I1.i2)
- [S10] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.07652v1#S1.I1.i3)
- [S11] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.07652v1#S2.p1.1)
- [S12] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.07652v1#S2.p2.1)
- [S13] [3 Simulation Platform · 正文段落 14](https://arxiv.org/html/2610.07652v1#S3.F2)
- [S14] [3.2 Manipulation Motion Generation · 正文段落 28](https://arxiv.org/html/2610.07652v1#S3.F3)
- [S15] [3.2 Manipulation Motion Generation · 正文段落 32](https://arxiv.org/html/2610.07652v1#S3.SS2.p4.1)
- [S16] [3.2 Manipulation Motion Generation · 正文段落 33](https://arxiv.org/html/2610.07652v1#S3.SS2.p5.1)
- [S17] [3.2 Manipulation Motion Generation · 正文段落 34](https://arxiv.org/html/2610.07652v1#S3.SS2.p6.1)
- [S18] [3.2 Manipulation Motion Generation · 正文段落 35](https://arxiv.org/html/2610.07652v1#S3.SS2.p7.1)
- [S19] [4.1 Agentic Task Generation · 正文段落 46](https://arxiv.org/html/2610.07652v1#S4.SS1.p1.1)
- [S20] [4.1 Agentic Task Generation · 正文段落 48](https://arxiv.org/html/2610.07652v1#S4.SS1.p2.1)
- [S21] [4.1 Agentic Task Generation · 正文段落 49](https://arxiv.org/html/2610.07652v1#S4.SS1.p3.1)
- [S22] [5 Simulation Experiments · 正文段落 68](https://arxiv.org/html/2610.07652v1#S5.p1.1)
- [S23] [5.1 Experiment Setup · 正文段落 69](https://arxiv.org/html/2610.07652v1#S5.SS1.p1.1)
- [S24] [5.1 Experiment Setup · 正文段落 70](https://arxiv.org/html/2610.07652v1#S5.SS1.p2.1)
- [S25] [6 Sim-to-Real Experiments · 正文段落 79](https://arxiv.org/html/2610.07652v1#S6.p1.1)
- [S26] [6 Sim-to-Real Experiments · 正文段落 80](https://arxiv.org/html/2610.07652v1#S6.I1.i1)
- [S27] [6 Sim-to-Real Experiments · 正文段落 81](https://arxiv.org/html/2610.07652v1#S6.I1.i2)
- [S28] [6 Sim-to-Real Experiments · 正文段落 82](https://arxiv.org/html/2610.07652v1#S6.I1.i3)
- [S29] [6.1 Experiment Setup · 正文段落 83](https://arxiv.org/html/2610.07652v1#S6.SS1.p1.1)
- [S30] [6.1 Experiment Setup · 正文段落 84](https://arxiv.org/html/2610.07652v1#S6.F8)
- [S31] [6.1 Experiment Setup · 正文段落 85](https://arxiv.org/html/2610.07652v1#S6.SS1.p2.1)
- [S32] [6.1 Experiment Setup · 正文段落 87](https://arxiv.org/html/2610.07652v1#S6.I2.i2)
- [S33] [7 Limitations · 正文段落 123](https://arxiv.org/html/2610.07652v1#S7.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/SMART Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synt.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation constraints, hindering agentic task generation and scalable synthesis of high-quality articulated-manipulation demonstrations. To bridge this gap, we introduce SMART, a scalable system leveraging large-scale Synthesized Manipulation demonstrations for ARTiculated-object manipulation. At its core, we develop SMART-Sim, a simulation platform with articulation-aware design that enables effective task generation and efficient demonstration collection. Building on SMART-Sim, we apply agentic task generation and design a scalable distributed synthesis system, using them to synthesize SMART-Data, comprising over 1M demonstrations across 44 atomic task types, 5 robot setups, and 2,507 articulated objects. The vision-language-action (VLA) model pretrained on SMART-Data shows competitive performance on simulation benchmarks and achieves zero-shot sim-to-real transfer and scalable performance in real-world articulated-object manipulation tasks. This highlights the potential of synthetic demonstrations in providing effective and scalable supervision for improving VLA model performance in contact-rich articulated-object manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07652v1
- Authors: Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao, Jiangyuan Zhao, Yang Zhang, Shiqiang Zhu, Chenjia Bai, Xuelong Li
- Published: 2026-10-06T02:47:22Z
- Age days: 0

</details>
