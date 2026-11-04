---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.39429"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 39
created: 2026-11-04
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> ScheduleGen 从少量示范生成多臂操作数据，但不只是改写各只手的运动：它把动作规划和技能排程一起处理，让多臂约束参与决定动作如何安排。目标是减少生成示范中的危险或失败行为，再用这些示范训练策略。

## 问题

多臂机器人有机会缩短作业时间，却要处理多臂同时活动带来的约束，安全控制和数据采集都更困难。已有自动示范生成算法虽然能扩充少量示范，但摘要指出它们忽略多臂约束，因而常生成不安全或不能完成任务的行为。

### 用一个例子理解

理解用例（非论文实验）：输入少量双臂装配示范和一个新布局；系统规划两臂动作并安排技能时序，让一只手固定零件、另一只手装入，输出可用于模仿学习的新示范。

## 创新点或方法

旧方法生成新示范时没有充分处理多臂约束；ScheduleGen 将规划与排程整合，让技能如何运动、何时执行共同受约束。这样有望在生成数据时先避开执行冲突，而不是把问题留给模仿学习策略。数据生成发生在策略训练之前，策略再学习生成的示范；摘要未说明部署时是否继续使用排程器，也未提供约束形式、技能切分和求解算法，不能据名称补全这些细节。

### 方法如何工作

1. 从少量源示范出发生成新操作示范，减少逐条采集多臂数据的需求；源示范如何解析，摘要未说明。
2. 整合动作规划与技能排程，把多臂约束纳入生成过程，减少互相冲突的执行安排。
3. 获得生成示范并用于模仿学习，训练能完成任务的策略；失败数据的处理方式未说明。
4. 在仿真任务及真机迁移设置中评估策略，分别检查数据生成和最终执行两个环节的成功情况。

### 必要术语

- 技能排程：安排技能何时执行及相互次序；本文把它与运动规划共同处理。
- 模仿学习：从示范中学习如何行动；本文用生成示范训练多臂策略。
- 零样本仿真到现实：不依靠目标现实任务的新训练样本直接迁移；本文将其作为真机验证路线之一。
- 现实到仿真再到现实：先将现实示范或任务带入仿真，再把所得策略迁回现实；具体实现需核查正文。

## 证据

摘要报告，在 28 个仿真任务变体中，平均数据生成成功率为 79.6%，训练出的策略平均成功率为 65.5%；其中包含 7 个外部作者提供的 RoboDojo 任务，以及此前系统无法处理的设置。策略胜过使用先进数据生成基线训练的策略，但摘要未给基线名称或差值。通过零样本仿真到现实、现实到仿真再到现实迁移，八个真机变体的成功率为 50–80%。这些结果支持生成数据可用于训练，但不能证明所有约束均得到严格安全保证。

## 局限

数据生成成功率与策略成功率衡量不同环节，不能互换。还需核查失败示范如何处理、真机试验次数，以及迁移依赖多少场景建模；摘要也没有说明 50–80% 如何对应两种迁移路线。

- **判断**：值得读规划与排程如何耦合的细节，因为能否复用取决于约束和技能如何表示，不能仅凭最终成功率决定。

## 研究关联

可借鉴的是在合成训练数据时就处理多执行器的相互制约。如果数据本身包含不合理的同时动作，单靠增加示范数量未必解决问题；先改进数据的可执行性，是另一条直接路径。

### 下一步读哪里

先查技能定义、约束表达和规划排程的接口，再看同任务同源示范的基线比较；真机部分核查两种迁移路线各自的准备条件与试验规模。

- **概念**：智能体 Agent 世界模型 机器人学习 Sim2Real
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/ScheduleGen Demonstration Generation via Skill Scheduling for Multi-Arm Imitatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.39429v2 Announce Type: replace Abstract: Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints. The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose multi-arm manipulation, but the acquisition of large multi-arm manipulation datasets remains a bottleneck. Automated demonstration generation can alleviate this burden by synthesizing new demonstrations from a handful of source demonstrations, but existing algorithms ignore multi-arm constraints and as a result often induce unsafe and unsuccessful behaviors. We address this limitation by introducing ScheduleGen, an integrated planning & scheduling algorithm for multi-arm demonstration generation. We evaluate ScheduleGen on 28 simulation task variants, including seven externally authored RoboDojo tasks and settings inaccessible to prior systems; it achieves 79.6% mean data-generation success and trains policies with 65.5% mean success. ScheduleGen policies outperform those trained on a state-of-the-art data generation baseline, and achieve 50-80% success across eight real-world variants through zero-shot sim-to-real and real-to-sim-to-real transfer. Videos and more at: https://njawale42.github.io/ScheduleGen/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39429
- Authors: Neel Jawale, Stephan Pleines, Soha Pouya, Yuke Zhu, Ajay Mandlekar, Caelan Garrett
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
