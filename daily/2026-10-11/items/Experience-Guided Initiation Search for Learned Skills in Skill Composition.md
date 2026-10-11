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
url: "https://arxiv.org/abs/2610.11418v1"
published: "2026-10-08T07:46:08Z"
age_days: 2
score: 31
created: 2026-10-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Experience-Guided Initiation Search for Learned Skills in Skill Composition

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> EVIS 给冻结的机器人技能寻找合适的起始站位：先用旧执行记录挑值得试的位置，再在新环境重复执行确认。它检查整段任务能否完成，避免“抽屉打开了，下一步却够不着”。

## 问题

任务是在新厨房调用不再训练的 VLA，完成开抽屉及后续操作。瓶颈是起始底座位置既影响当前技能，也决定交给下一技能的物理状态；几何可行或单步成功都不足够。大量试跑昂贵，直接照搬历史站位又会受布局、外观和接触条件变化影响。[S2](https://arxiv.org/html/2610.11418v1#S1.p1.1) [S3](https://arxiv.org/html/2610.11418v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入新抽屉位置和“打开后取杯子”；历史记录先推荐几个底座姿态，机器人逐个执行整段任务，对暂定成功姿态重新试跑，输出通过检查的站位，或预算耗尽后不返回。

## 创新点或方法

旧做法要么从头试，要么信任旧候选；EVIS 把历史记录用于排序，把目标环境执行用于决定接受。离线分别估计当前技能可行性、到达交接状态后的继续成功率、全程成功率，用 RBF 平滑保留多个评分假设。部署时首次成功只产生暂定候选，另做新试跑资格检查，且不计入触发检查的那次成功；达到规定成功次数便接受，已不可能达标便提前拒绝。拒绝后继续扩展搜索，策略参数始终冻结。[S15](https://arxiv.org/html/2610.11418v1#S4.SS1.p4.1) [S16](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.1) [S17](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.2) [S18](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.1) [S19](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.2) [S20](https://arxiv.org/html/2610.11418v1#S4.SS3.p2.3) [S21](https://arxiv.org/html/2610.11418v1#S4.SS3.p5.2) [S22](https://arxiv.org/html/2610.11418v1#S4.SS3.p6.4) [S23](https://arxiv.org/html/2610.11418v1#S4.SS3.p7.1) [S24](https://arxiv.org/html/2610.11418v1#S4.SS3.p8.1)

### 方法如何工作

1. 把历史轨迹拆成局部成功、交接后成功和全程成功，得到互补排序线索，避免只偏爱容易开抽屉的位置。
2. 按历史线索挑候选，在目标环境执行完整目标，得到实际成功或失败证据。
3. 对首次成功候选另做资格试跑，决定接受或拒绝，降低偶然成功造成的误判。
4. 拒绝后根据目标反馈扩展覆盖或探索成功位置附近，直到找到合格候选或耗尽预算。

### 必要术语

- 起始配置：技能启动前的可调物理状态；实验中是底座相对目标的平移和朝向。
- 条件继续成功：已经到达交接状态时，下游技能成功的程度；用于区别开抽屉容易与后续操作容易。
- 资格检查：对暂定候选重新执行并累计成功次数；用于决定是否返回候选。

## 证据

实验在 RoboCasa365 仿真中使用冻结的 RLDX-1-FT-RC365，搜索底座平移及朝向，测试 OpenDrawer 和两种两阶段任务。[S26](https://arxiv.org/html/2610.11418v1#S5.SS1.p1.1) [S27](https://arxiv.org/html/2610.11418v1#S5.SS1.p2.1) 单技能对比固定预算、历史复用、Scratch-Sobol；一个示例首次成功需要 5 次查询，对方需 12 次，不能当作平均收益。[S31](https://arxiv.org/html/2610.11418v1#S5.SS2.p2.1) [S32](https://arxiv.org/html/2610.11418v1#S5.F4) [S33](https://arxiv.org/html/2610.11418v1#S5.SS2.p4.1) 两阶段资格检查使两个任务的可靠返回精度从 41.7%、8.3% 到 100%，但减少返回覆盖。[S36](https://arxiv.org/html/2610.11418v1#S5.T3.2.1) [S37](https://arxiv.org/html/2610.11418v1#S5.SS3.p6.1) 恢复实验中 EVIS Fallback 的最终可靠率为 41.7%，Sobol 为 33.3%，平均查询为 13.00、13.83。[S39](https://arxiv.org/html/2610.11418v1#S5.T4.2.1) 节选未给主实验完整均值和不确定性。

## 局限

资格检查中的零误接受是有限实验结果，不是可靠性保证。Mean Queries 排除了独立确认试验，[S30](https://arxiv.org/html/2610.11418v1#S5.SS1.p4.1) 所以不能直接视为部署全部成本；我还会核查复位成本、可靠阈值和样本数。这里提供的是仿真证据。

- **判断**：值得读到资格检查和恢复搜索的实现，因为真正可复用的是有限预算下的接受、拒绝与继续搜索规则。

## 研究关联

值得借鉴的是把“哪里可能成功”和“是否有足够证据相信它”分开。旧经验可能失准、每次执行又昂贵时，先排序再验证，比要求历史模型精确预测新环境成功率更务实。

### 下一步读哪里

先看 [S15](https://arxiv.org/html/2610.11418v1#S4.SS1.p4.1) 如何构造条件继续评分，再核查 [S16](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.1) [S17](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.2) [S18](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.1) [S19](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.2) 的资格参数与可靠阈值关系；检查 [S30](https://arxiv.org/html/2610.11418v1#S5.SS1.p4.1) 独立确认成本，以及 [S23](https://arxiv.org/html/2610.11418v1#S4.SS3.p7.1) 实际启用哪些恢复算子。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：31
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.11418v1
- 获取时间：2026-10-11T00:33:19.189728+00:00
- [S1] [Experience-Guided Initiation Search for Learned Skills in Skill Composition · 正文段落 1](https://arxiv.org/html/2610.11418v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2610.11418v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2610.11418v1#S1.p2.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2610.11418v1#S1.F1)
- [S5] [I Introduction · 正文段落 6](https://arxiv.org/html/2610.11418v1#S1.p4.1)
- [S6] [I Introduction · 正文段落 10](https://arxiv.org/html/2610.11418v1#S1.I1.i3)
- [S7] [II-A Skill Applicability and Composition · 正文段落 11](https://arxiv.org/html/2610.11418v1#S2.SS1.p1.1)
- [S8] [II-B Policy Orchestration and Execution Memory · 正文段落 12](https://arxiv.org/html/2610.11418v1#S2.SS2.p1.1)
- [S9] [II-C Experience-Guided Search and Candidate Discovery · 正文段落 13](https://arxiv.org/html/2610.11418v1#S2.SS3.p1.1)
- [S10] [II-C Experience-Guided Search and Candidate Discovery · 正文段落 14](https://arxiv.org/html/2610.11418v1#S2.F2)
- [S11] [III Problem Formulation · 正文段落 16](https://arxiv.org/html/2610.11418v1#S3.p2.1)
- [S12] [III Problem Formulation · 正文段落 27](https://arxiv.org/html/2610.11418v1#S3.p4.3)
- [S13] [III Problem Formulation · 正文段落 30](https://arxiv.org/html/2610.11418v1#S3.p5.2)
- [S14] [IV Methods · 正文段落 32](https://arxiv.org/html/2610.11418v1#S4.p1.1)
- [S15] [IV-A Experience-Guided Proposal · 正文段落 40](https://arxiv.org/html/2610.11418v1#S4.SS1.p4.1)
- [S16] [IV-B Behavioral Validation and Budgeted Return · 正文段落 46](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.1)
- [S17] [IV-B Behavioral Validation and Budgeted Return · 正文段落 48](https://arxiv.org/html/2610.11418v1#S4.SS2.p1.2)
- [S18] [IV-B Behavioral Validation and Budgeted Return · 正文段落 49](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.1)
- [S19] [IV-B Behavioral Validation and Budgeted Return · 正文段落 51](https://arxiv.org/html/2610.11418v1#S4.SS2.p2.2)
- [S20] [IV-C Behavior-Guided Recovery Search · 正文段落 61](https://arxiv.org/html/2610.11418v1#S4.SS3.p2.3)
- [S21] [IV-C Behavior-Guided Recovery Search · 正文段落 68](https://arxiv.org/html/2610.11418v1#S4.SS3.p5.2)
- [S22] [IV-C Behavior-Guided Recovery Search · 正文段落 75](https://arxiv.org/html/2610.11418v1#S4.SS3.p6.4)
- [S23] [IV-C Behavior-Guided Recovery Search · 正文段落 77](https://arxiv.org/html/2610.11418v1#S4.SS3.p7.1)
- [S24] [IV-C Behavior-Guided Recovery Search · 正文段落 78](https://arxiv.org/html/2610.11418v1#S4.SS3.p8.1)
- [S25] [V Experiments · 正文段落 79](https://arxiv.org/html/2610.11418v1#S5.p1.1)
- [S26] [V-A Experimental Setup · 正文段落 80](https://arxiv.org/html/2610.11418v1#S5.SS1.p1.1)
- [S27] [V-A Experimental Setup · 正文段落 81](https://arxiv.org/html/2610.11418v1#S5.SS1.p2.1)
- [S28] [V-A Experimental Setup · 正文段落 82](https://arxiv.org/html/2610.11418v1#S5.F3)
- [S29] [V-A Experimental Setup · 正文段落 83](https://arxiv.org/html/2610.11418v1#S5.SS1.p3.1)
- [S30] [V-A Experimental Setup · 正文段落 84](https://arxiv.org/html/2610.11418v1#S5.SS1.p4.1)
- [S31] [V-B Initiation Search on Unseen Target Contexts · 正文段落 86](https://arxiv.org/html/2610.11418v1#S5.SS2.p2.1)
- [S32] [V-B Initiation Search on Unseen Target Contexts · 正文段落 87](https://arxiv.org/html/2610.11418v1#S5.F4)
- [S33] [V-B Initiation Search on Unseen Target Contexts · 正文段落 91](https://arxiv.org/html/2610.11418v1#S5.SS2.p4.1)
- [S34] [V-B Initiation Search on Unseen Target Contexts · 正文段落 92](https://arxiv.org/html/2610.11418v1#S5.SS2.p5.1)
- [S35] [V-B Initiation Search on Unseen Target Contexts · 正文段落 96](https://arxiv.org/html/2610.11418v1#S5.SS2.p7.1)
- [S36] [V-C Mechanism Analysis: Propose, Validate, and Recover · 正文段落 104](https://arxiv.org/html/2610.11418v1#S5.T3.2.1)
- [S37] [V-C Mechanism Analysis: Propose, Validate, and Recover · 正文段落 105](https://arxiv.org/html/2610.11418v1#S5.SS3.p6.1)
- [S38] [V-C Mechanism Analysis: Propose, Validate, and Recover · 正文段落 106](https://arxiv.org/html/2610.11418v1#S5.SS3.p7.1)
- [S39] [V-C Mechanism Analysis: Propose, Validate, and Recover · 正文段落 108](https://arxiv.org/html/2610.11418v1#S5.T4.2.1)
- [S40] [VI Conclusion · 正文段落 110](https://arxiv.org/html/2610.11418v1#S6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/Experience-Guided Initiation Search for Learned Skills in Skill Composition.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution. In skill composition, an initiation configuration affects not only the current skill but also the physical state passed to subsequent skills, so successful execution of an individual skill does not necessarily imply successful completion of the composed task. Estimating target-specific capability through extensive rollouts is costly in real-world deployment, while directly reusing historical experience can be unreliable under environment changes. We propose EVIS, an Experience-Guided and Behavior-Validated Initiation Search framework for discovering reliable initiation configurations under limited target interaction. EVIS uses historical execution experience to prioritize promising candidates and target-environment behavior to validate whether they remain effective. We evaluate EVIS on single-skill and two-stage manipulation tasks with frozen VLA policies. EVIS reduces mean target-environment queries and improves reliable candidate discovery under small interaction budgets. These results show that combining historical guidance with target-side behavioral validation can reduce the interaction cost of deploying frozen learned skills in new environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11418v1
- Authors: Qixuan Li, Yanhong Zhao, Jincheng Yu
- Published: 2026-10-08T07:46:08Z
- Age days: 2

</details>
