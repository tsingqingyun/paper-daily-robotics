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
url: "https://arxiv.org/abs/2610.23288v1"
published: "2026-10-16T10:56:10Z"
age_days: 3
score: 42
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CoEvolve 让两台机器人保留已有运动技能，由模型编写并修改“怎样一起搬”的协作代码。执行不合格时，它根据物理检查结果限定修改策略、角色关系或参数，再从仿真检查点重试。

## 问题

两个人形机器人托着同一物体穿过窄走廊，任何一方的位移都会改变另一方的支撑条件。分配好“谁走、谁转”仍可能掉落；作者针对的是已有任务分解和重规划对执行中协作关系变化支持不足，而不是机器人缺少走路技能。[S4](https://arxiv.org/html/2610.23288v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入“两台机器人把长板搬过直角弯”和当前状态；同时转弯导致支撑恶化，验证器拒绝后恢复检查点，改成一台支撑、另一台小步转向；输出新的配对程序，再检查是否推进。

## 创新点或方法

旧做法可以重写计划或程序；CoEvolve 把修改范围明确分为三层：换动作策略、换同步方式或临时支撑角色、只改幅度等参数。未选中的字段保持固定，避免失败后毫无约束地重写。模型和底层运动权重均不更新；运行中生成配对代码，逐段执行、验证，成功经验保存为策略记录和代码示例。失败后恢复最近接受的模拟器状态，不是现场学出物理恢复动作。[S6](https://arxiv.org/html/2610.23288v1#S1.p4.1) [S15](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px2.p2.1) [S16](https://arxiv.org/html/2610.23288v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2610.23288v1#S3.SS3.p3.2)

### 方法如何工作

1. 根据任务阶段、路线和当前状态选协作动作与临时角色，明确这一段要完成什么。
2. 生成每台机器人的受限动作代码并执行，得到实际运动结果，而非假定两台响应相同。
3. 物理验证接受或拒绝状态转移，区分局部有效动作和阶段进展。
4. 失败时只修改指定层级并回滚重试；接受的经验进入后续检索，避免把未执行修复当成成功。

### 必要术语

- 固定运动技能：已有且权重不变的走、转等能力；本文只改变其协作组合。
- 物理验证：依据执行状态检查动作结果；决定接受、修复和恢复。
- 检查点：最近被接受的模拟器状态；允许失败后重新尝试，但真机不能直接复制。
- 临时角色：某段动作中谁支撑、谁移动等职责；用于改变协作关系。

## 证据

MuJoCo 中两台 G1 搬运自由支撑的 0.5kg 刚体；基础任务要求放置、释放并直立撤离。[S20](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px1.p1.1) 三种模型各五次，共完成 8/15：GPT、Gemini 各 3/5，Claude 2/5。[S18](https://arxiv.org/html/2610.23288v1#S4.T1.2) [S19](https://arxiv.org/html/2610.23288v1#S4.T1) GPT 条件下四个外部基线和两个组件变体均为 0/5，完整方法 3/5。[S25](https://arxiv.org/html/2610.23288v1#S4.T2.2) 但作者说明部分比较的运行配置、预算或继续条件不同，因此结果支持系统能完成任务，不能直接证明每个组件的独立因果收益。[S7](https://arxiv.org/html/2610.23288v1#S1.p5.1)

## 局限

作者明确承认全部实验在仿真，使用特权物理状态和给定路线，失败靠状态回滚；运动精度、接触稳定性和运行耗时仍有限，且没有系统随机化接触条件。[S34](https://arxiv.org/html/2610.23288v1#S6.p1.1) 新布局的终点不要求撤离，因此不能与基础完整任务成功直接合并。[S31](https://arxiv.org/html/2610.23288v1#S4.SS5.p1.1)

- **判断**：值得细读结构化修复与验证逻辑，作为协作代码设计案例；真机可用性仍取决于感知、精确控制和实际恢复能力。

## 研究关联

值得借鉴的是失败诊断应对应可控修改范围：转弯失败可能要换支撑角色，而不是只缩小转角。另一个启示是把动作被接受与任务真正推进分开统计；安全可执行的小动作，也可能让系统一直停在同一阶段。[S27](https://arxiv.org/html/2610.23288v1#S4.SS3.SSS0.Px1.p1.1)

### 下一步读哪里

先读 [S14](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px2.p1.1) [S15](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px2.p2.1) [S16](https://arxiv.org/html/2610.23288v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2610.23288v1#S3.SS3.p3.2) 的角色、修改范围与经验晋升规则，再核查验证器阈值、预算和恢复计费；结合 [S27](https://arxiv.org/html/2610.23288v1#S4.SS3.SSS0.Px1.p1.1) [S34](https://arxiv.org/html/2610.23288v1#S6.p1.1) 理解为什么动作通过检查仍可能无法完成任务。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.23288v1
- 获取时间：2026-10-19T15:35:19.987300+00:00
- [S1] [CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots · 正文段落 1](https://arxiv.org/html/2610.23288v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.23288v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.23288v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.23288v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.23288v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.23288v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.23288v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.23288v1#S1.I1.i3)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.23288v1#S1.F2)
- [S10] [Robot Policy Refinement from Execution Feedback. · 正文段落 13](https://arxiv.org/html/2610.23288v1#S2.SS0.SSS0.Px2.p1.1)
- [S11] [3 Method · 正文段落 14](https://arxiv.org/html/2610.23288v1#alg1)
- [S12] [3 Method · 正文段落 15](https://arxiv.org/html/2610.23288v1#S3.p1.1)
- [S13] [Task formulation. · 正文段落 16](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px1.p1.1)
- [S14] [Executable coordination. · 正文段落 17](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px2.p1.1)
- [S15] [Executable coordination. · 正文段落 18](https://arxiv.org/html/2610.23288v1#S3.SS1.SSS0.Px2.p2.1)
- [S16] [3.2 Verifier Guided Coordination Evolution · 正文段落 20](https://arxiv.org/html/2610.23288v1#S3.SS2.p2.1)
- [S17] [3.3 Verified Cooperative Experience · 正文段落 25](https://arxiv.org/html/2610.23288v1#S3.SS3.p3.2)
- [S18] [4 Experiments · 正文段落 26](https://arxiv.org/html/2610.23288v1#S4.T1.2)
- [S19] [4 Experiments · 正文段落 27](https://arxiv.org/html/2610.23288v1#S4.T1)
- [S20] [Task and observations. · 正文段落 28](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px1.p1.1)
- [S21] [Task and observations. · 正文段落 29](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px1.p2.1)
- [S22] [Execution and models. · 正文段落 30](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px2.p1.1)
- [S23] [Execution and models. · 正文段落 31](https://arxiv.org/html/2610.23288v1#S4.SS1.SSS0.Px2.p2.1)
- [S24] [4.2 Evaluation Protocol and Metrics · 正文段落 33](https://arxiv.org/html/2610.23288v1#S4.SS2.p2.1)
- [S25] [4.2 Evaluation Protocol and Metrics · 正文段落 38](https://arxiv.org/html/2610.23288v1#S4.T2.2)
- [S26] [4.2 Evaluation Protocol and Metrics · 正文段落 39](https://arxiv.org/html/2610.23288v1#S4.T2)
- [S27] [Local acceptance does not guarantee sustained task advancement. · 正文段落 41](https://arxiv.org/html/2610.23288v1#S4.SS3.SSS0.Px1.p1.1)
- [S28] [4.4 Method Comparisons and Component Analysis · 正文段落 42](https://arxiv.org/html/2610.23288v1#S4.SS4.p1.1)
- [S29] [4.4 Method Comparisons and Component Analysis · 正文段落 43](https://arxiv.org/html/2610.23288v1#S4.F3)
- [S30] [Structured revision and verified experience target different repair failures. · 正文段落 45](https://arxiv.org/html/2610.23288v1#S4.SS4.SSS0.Px1.p2.1)
- [S31] [4.5 Evaluation Across Layouts · 正文段落 46](https://arxiv.org/html/2610.23288v1#S4.SS5.p1.1)
- [S32] [Local progress does not guarantee future physical feasibility. · 正文段落 50](https://arxiv.org/html/2610.23288v1#S4.F4)
- [S33] [5 Conclusion · 正文段落 56](https://arxiv.org/html/2610.23288v1#S5.p1.1)
- [S34] [6 Limitations · 正文段落 57](https://arxiv.org/html/2610.23288v1#S6.p1.1)
- [S35] [B.3 Controller and Contact Configuration · 正文段落 87](https://arxiv.org/html/2610.23288v1#A2.SS3.p1.1)
- [S36] [B.3 Controller and Contact Configuration · 正文段落 88](https://arxiv.org/html/2610.23288v1#A2.SS3.p2.1)
- [S37] [B.3 Controller and Contact Configuration · 正文段落 89](https://arxiv.org/html/2610.23288v1#A2.SS3.p3.1)
- [S38] [C.2 Reconstructing Progress AUC · 正文段落 113](https://arxiv.org/html/2610.23288v1#A3.SS2.p1.2)
- [S39] [C.2 Reconstructing Progress AUC · 正文段落 115](https://arxiv.org/html/2610.23288v1#A3.SS2.p3.1)
- [S40] [C.2 Reconstructing Progress AUC · 正文段落 117](https://arxiv.org/html/2610.23288v1#A3.T12)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/CoEvolve Self-Evolving Code Policies from Skills to Strategies for Humanoid Robo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize task decomposition, allocation, and replanning, while providing limited support for adapting executable coordination when physical execution deviates from the intended behavior. We present CoEvolve, a framework that represents team coordination as executable code over fixed robot motor skills. CoEvolve introduces Verifier Guided Coordination Evolution, where a multimodal foundation model instantiates coordination strategies through motion primitives, semantic objectives, temporary robot roles, and bounded execution parameters. Physical verification evaluates each executed transition, rejected behaviors trigger structured coordination revision from an accepted checkpoint, and verified experience is retained to guide subsequent decisions. We evaluate CoEvolve with two simulated Unitree G1 humanoids transporting a freely supported rigid payload through constrained corridors. Across 15 base task runs with three multimodal backbone families, CoEvolve completes 8 tasks, with every backbone achieving end to end success. Additional evaluations yield verified placement on two additional corridor layouts and after both same-backbone and cross-backbone experience initialization, while exposing persistent limitations in motion precision and contact stability. These results support executable coordination as a practical interface for adapting long horizon multi robot collaboration under shared physical constraints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23288v1
- Authors: Zicheng Liu, Haochen Wu, Jiawei He, Suyun Zhao, Huan Yang, Cheng Chi, Hao Tang
- Published: 2026-10-16T10:56:10Z
- Age days: 3

</details>
