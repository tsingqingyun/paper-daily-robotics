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
url: "https://arxiv.org/abs/2609.37810v1"
published: "2026-09-29T15:25:43Z"
age_days: 0
score: 43
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboSkill 让机器人把一次试错留下的经验写成说明和可复用代码，下次遇到类似任务先查着用，省掉重复思考与摸索。它还用触觉确认有没有碰到、抓住物体，再根据执行结果修订技能库。

## 问题

通用智能体可以边看边想、尝试陌生任务，但如果每次开抽屉、抓东西都重新试探，推理和机器人执行都会耗时间。[S3](https://arxiv.org/html/2609.37810v1#S1.p1.1) 把上次动作原样重放也不行：物体位置会变，发出“抓住”的指令不代表真的抓住。本文要复用的是解决问题的经验，同时保留观察、确认和纠错。[S4](https://arxiv.org/html/2609.37810v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：机器人昨天花很久才学会开抽屉，留下抓哪里、往哪个方向拉、卡住时检查什么，以及相应代码。今天换了抽屉位置，它先读这份经验，再观察当前把手位置，执行并用反馈确认抽屉真的打开；新的卡顿情况会补进技能包。省掉的是重新发明整套办法，现场确认仍然要做。

## 创新点或方法

把一次执行留下来的经验，整理成一个技能包：文字讲策略、适用条件和失败教训，代码保存可复用操作，记录保存动作、观察和关键画面。[S12](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px2.p1.1) 遇到新任务时，智能体先看技能简介，最多选三个包放进工作区，读其中说明、调用代码，再针对当前场景补充探索。[S13](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px3.p1.1) 执行时结合视觉和触觉确认实际发生了什么，结束后再用新结果更新技能库，形成“探索—执行—更新—下次复用”的循环。[S10](https://arxiv.org/html/2609.37810v1#S3.p1.1)[S11](https://arxiv.org/html/2609.37810v1#S3.F2)[S50](https://arxiv.org/html/2609.37810v1#S9.p1.1) 变化主要发生在部署时可读取、可调用的经验资料中；这几段没有给出重新训练 VLA 权重的流程。真机主实验还要注意：用的是一个同任务技能，并非同时检索三个跨任务技能。[S16](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)

### 方法如何工作

1. 把上次成功与失败整理成技能包，既保留“为什么这样做”的文字，也保留能再次运行的代码和观察记录。[S12](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px2.p1.1)
2. 新任务开始时先看技能简介，选择相关经验；仿真设置最多三个包，真机主实验用一个同任务包。[S13](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px3.p1.1)[S16](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)
3. 用已有经验指导动作，缺信息再探索，并通过视觉、触觉核对物理结果，避免把发出命令当作执行成功。[S4](https://arxiv.org/html/2609.37810v1#S1.p2.1)[S11](https://arxiv.org/html/2609.37810v1#S3.F2)
4. 把本轮结果用于修订技能，下轮再检索使用；技能包如何自动修订和验证，仍需阅读当前节选未覆盖的具体实现。[S10](https://arxiv.org/html/2609.37810v1#S3.p1.1)[S50](https://arxiv.org/html/2609.37810v1#S9.p1.1)

### 必要术语

- 技能包：说明、代码和记录放在一起的操作经验；它既告诉智能体如何判断，也提供可以复用的程序。[S12](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px2.p1.1)
- 首次回合成功率：不重置重试，第一次就完成的比例；这里仍允许事先有技能，不能理解成毫无经验的第一次学习。[S14](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px1.p1.1)[S17](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px4.p1.1)
- 触觉反馈：接触产生的感知信号；它补充摄像头不容易看清的物理信息，例如是否真正碰到物体。[S11](https://arxiv.org/html/2609.37810v1#S3.F2)

## 证据

LIBERO-10 主实验有 10 个任务，每个任务 4 个评测种子，共 40 组；建库种子被排除在这次评测之外。[S14](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px1.p1.1)[S34](https://arxiv.org/html/2609.37810v1#S6.SS1.p1.1) 四种智能体的首次回合成功率都提高。例如 Astra 从 72.5% 到 97.5%；Sol 从 27.5% 到 52.5%，平均耗时从 94.5 分钟到 35.9 分钟。比较对象是不保存技能的同类智能体。[S16](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)[S18](https://arxiv.org/html/2609.37810v1#S4.T1.6) 真机用 Piper 机械臂做 12 个任务，每任务 10 次：Astra 在简单任务中从 91.7% 到 100%，困难任务从 80% 到 88.3%；成功试验平均耗时分别从 20.3 到 16.6 分钟、27.0 到 23.1 分钟。[S15](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px2.p1.1)[S20](https://arxiv.org/html/2609.37810v1#S4.T2.fig1.7)[S24](https://arxiv.org/html/2609.37810v1#S4.SS2.p4.1) 这说明复用经验能减少重复摸索，但不是每项任务都改善：针孔抽线任务从 7/10 降到 5/10。[S46](https://arxiv.org/html/2609.37810v1#S7.T13.7)

## 局限

正文明确提醒：仿真平均耗时包含失败和提前结束的回合，时间短不一定等于更快成功；真机耗时则只统计成功试验，两种口径不能混算。[S17](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px4.p1.1)[S39](https://arxiv.org/html/2609.37810v1#S6.SS2.p2.1) 主实验是已有技能后的执行比较，当前节选没有把首次建库、模型调用费用和维护成本汇成完整总账，不能直接换算成“省了多少钱”。跨任务复用也不是稳赚：Opus 的首次成功率从 60% 降到 56%，但时间缩短。[S30](https://arxiv.org/html/2609.37810v1#S4.SS3.SSS0.Px2.p1.1) 跨智能体实验还包含建库种子，不能照搬主实验“未见初始条件”的解释。[S35](https://arxiv.org/html/2609.37810v1#S6.SS1.p2.1) 至于触觉和代码各贡献多少，本文有相应消融，当前节选没提供完整结果表，我不单独给它们归功。[S7](https://arxiv.org/html/2609.37810v1#S1.I1.i3)

- **判断**：如果机器人总在重复任务上从头探索，这篇很对症；先看技能怎样保存、纠错，以及积累多久才省回建库成本。

## 研究关联

一个值得试的方向是：在现有智能体上保存可执行的经验，让成功做过的步骤下次直接复用。判断它是否划算时，要把最初建库、失败重试和维护错误经验的成本一起算进去；论文的真机省时数字只统计了成功试验。

### 下一步读哪里

先读[S12](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px2.p1.1)[S13](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px3.p1.1)，看技能到底保存什么、如何被选中；再用[S16](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)分清多技能、同任务技能和无技能三种设置。核对收益时把[S18](https://arxiv.org/html/2609.37810v1#S4.T1.6)的仿真总回合计时与[S20](https://arxiv.org/html/2609.37810v1#S4.T2.fig1.7)的真机成功样本计时分开，并看[S34](https://arxiv.org/html/2609.37810v1#S6.SS1.p1.1)[S35](https://arxiv.org/html/2609.37810v1#S6.SS1.p2.1)的种子差别。最值得继续查的是完整触觉/代码消融、技能修订规则，以及把首次探索也算进去后，重复执行多少次才划算。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2609.37810v1
- 获取时间：2026-09-30T16:28:14.450861+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2609.37810v1#p1.2)
- [S2] [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents · 正文段落 2](https://arxiv.org/html/2609.37810v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2609.37810v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2609.37810v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 7](https://arxiv.org/html/2609.37810v1#S1.p5.1)
- [S6] [1 Introduction · 正文段落 8](https://arxiv.org/html/2609.37810v1#S1.F1)
- [S7] [1 Introduction · 正文段落 12](https://arxiv.org/html/2609.37810v1#S1.I1.i3)
- [S8] [Vision-Language-Action and World-Action Models · 正文段落 13](https://arxiv.org/html/2609.37810v1#S2.SS0.SSS0.Px1.p1.1)
- [S9] [Language-Model Agents for Robotics. · 正文段落 14](https://arxiv.org/html/2609.37810v1#S2.SS0.SSS0.Px2.p1.1)
- [S10] [3 Method · 正文段落 15](https://arxiv.org/html/2609.37810v1#S3.p1.1)
- [S11] [3 Method · 正文段落 16](https://arxiv.org/html/2609.37810v1#S3.F2)
- [S12] [Skills. · 正文段落 29](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px2.p1.1)
- [S13] [Skill usage. · 正文段落 31](https://arxiv.org/html/2609.37810v1#S3.SS4.SSS0.Px3.p1.1)
- [S14] [Simulation Setup. · 正文段落 32](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px1.p1.1)
- [S15] [Real Robot Setup. · 正文段落 33](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px2.p1.1)
- [S16] [Agents and Comparison Settings. · 正文段落 34](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px3.p1.1)
- [S17] [Evaluation Metrics. · 正文段落 35](https://arxiv.org/html/2609.37810v1#S4.SS1.SSS0.Px4.p1.1)
- [S18] [Evaluation Metrics. · 正文段落 37](https://arxiv.org/html/2609.37810v1#S4.T1.6)
- [S19] [Evaluation Metrics. · 正文段落 38](https://arxiv.org/html/2609.37810v1#S4.T2.fig1)
- [S20] [Evaluation Metrics. · 正文段落 39](https://arxiv.org/html/2609.37810v1#S4.T2.fig1.7)
- [S21] [4.2 Effectiveness of RoboSkill · 正文段落 40](https://arxiv.org/html/2609.37810v1#S4.SS2.p1.1)
- [S22] [4.2 Effectiveness of RoboSkill · 正文段落 41](https://arxiv.org/html/2609.37810v1#S4.SS2.p2.1)
- [S23] [4.2 Effectiveness of RoboSkill · 正文段落 42](https://arxiv.org/html/2609.37810v1#S4.SS2.p3.1)
- [S24] [4.2 Effectiveness of RoboSkill · 正文段落 43](https://arxiv.org/html/2609.37810v1#S4.SS2.p4.1)
- [S25] [Transfer with a same-task skill. · 正文段落 45](https://arxiv.org/html/2609.37810v1#S4.SS3.SSS0.Px1.p2.1)
- [S26] [Transfer with a same-task skill. · 正文段落 46](https://arxiv.org/html/2609.37810v1#S4.SS3.SSS0.Px1.p3.1)
- [S27] [Transfer with a same-task skill. · 正文段落 49](https://arxiv.org/html/2609.37810v1#S4.T4.fig1)
- [S28] [Transfer with a same-task skill. · 正文段落 50](https://arxiv.org/html/2609.37810v1#S4.T4.fig1.8)
- [S29] [Transfer with a same-task skill. · 正文段落 52](https://arxiv.org/html/2609.37810v1#S4.T5.6)
- [S30] [Transfer without a same-task skill. · 正文段落 53](https://arxiv.org/html/2609.37810v1#S4.SS3.SSS0.Px2.p1.1)
- [S31] [Cross-agent transfer in simulator. · 正文段落 54](https://arxiv.org/html/2609.37810v1#S4.SS4.SSS0.Px1.p1.1)
- [S32] [Cross-agent transfer in simulator. · 正文段落 55](https://arxiv.org/html/2609.37810v1#S4.T6.fig1)
- [S33] [Cross-agent transfer in simulator. · 正文段落 56](https://arxiv.org/html/2609.37810v1#S4.T6.fig1.8)
- [S34] [6.1 Evaluation Seeds · 正文段落 77](https://arxiv.org/html/2609.37810v1#S6.SS1.p1.1)
- [S35] [6.1 Evaluation Seeds · 正文段落 78](https://arxiv.org/html/2609.37810v1#S6.SS1.p2.1)
- [S36] [6.1 Evaluation Seeds · 正文段落 79](https://arxiv.org/html/2609.37810v1#S6.SS1.p3.1)
- [S37] [6.1 Evaluation Seeds · 正文段落 80](https://arxiv.org/html/2609.37810v1#S6.T11)
- [S38] [6.2 Simulation Tasks and Evaluation · 正文段落 82](https://arxiv.org/html/2609.37810v1#S6.SS2.p1.1)
- [S39] [6.2 Simulation Tasks and Evaluation · 正文段落 83](https://arxiv.org/html/2609.37810v1#S6.SS2.p2.1)
- [S40] [6.2 Simulation Tasks and Evaluation · 正文段落 84](https://arxiv.org/html/2609.37810v1#S6.F4)
- [S41] [6.2 Simulation Tasks and Evaluation · 正文段落 85](https://arxiv.org/html/2609.37810v1#S6.F5.fig1)
- [S42] [6.2 Simulation Tasks and Evaluation · 正文段落 86](https://arxiv.org/html/2609.37810v1#S6.T12.1)
- [S43] [6.2 Simulation Tasks and Evaluation · 正文段落 87](https://arxiv.org/html/2609.37810v1#S6.T12)
- [S44] [6.4 Real-Robot Tasks and Evaluation · 正文段落 92](https://arxiv.org/html/2609.37810v1#S6.SS4.p1.1)
- [S45] [7.1 Task-Wise Real-Robot Results · 正文段落 94](https://arxiv.org/html/2609.37810v1#S7.T13)
- [S46] [7.1 Task-Wise Real-Robot Results · 正文段落 95](https://arxiv.org/html/2609.37810v1#S7.T13.7)
- [S47] [7.1 Task-Wise Real-Robot Results · 正文段落 96](https://arxiv.org/html/2609.37810v1#S7.SS1.p2.1)
- [S48] [7.1 Task-Wise Real-Robot Results · 正文段落 97](https://arxiv.org/html/2609.37810v1#S7.T14)
- [S49] [7.1 Task-Wise Real-Robot Results · 正文段落 98](https://arxiv.org/html/2609.37810v1#S7.T14.7)
- [S50] [9 Conclusion · 正文段落 107](https://arxiv.org/html/2609.37810v1#S9.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Explore, Execute, Evolve A Skill Acquisition and Reuse Loop for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging. More recently, general-purpose multimodal agents have shown great potential for zero-shot robotic task solving. However, they often incur high execution costs by reasoning and exploring the physical world from scratch. To reduce these costs, we introduce RoboSkill, a framework that connects skill acquisition and reuse through an Explore, Execute, Evolve loop. Within this loop, the agent explores to gather task-relevant information, executes tasks while adapting to feedback, and evolves its skill library based on execution records. It then reuses these skills to guide exploration and execution in the next cycle, closing the loop. To improve loop efficiency, we complement vision with tactile feedback to reduce uncertainty during physical interaction. We further augment textual guidance with reusable code to reduce reasoning overhead during skill reuse. On LIBERO-10, RoboSkill improves first-episode success rates by 12.5--25.0 percentage points and reduces average runtime by 7.6--72.4% across four agents. On real robots, it improves success rates by 8.3 percentage points and reduces average runtime for successful trials by at least 14.4%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37810v1
- Authors: Sicheng Xie, Yitong Chen, Haidong Cao, Shunlin Lu, Zuxuan Wu, Yu-Gang Jiang
- Published: 2026-09-29T15:25:43Z
- Age days: 0

</details>
