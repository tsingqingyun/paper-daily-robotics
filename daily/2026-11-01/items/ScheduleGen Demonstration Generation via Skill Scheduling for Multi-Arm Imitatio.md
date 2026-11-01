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
url: "https://arxiv.org/abs/2610.39429v1"
published: "2026-10-29T06:07:04Z"
age_days: 2
score: 39
created: 2026-11-01
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> ScheduleGen用少量已有示范生成多臂操作数据，同时安排各项技能怎样执行、何时执行。关键是把多臂约束纳入规划和调度，避免生成的示范看似完整，却让机械臂发生不安全或失败的行为。

## 问题

双臂和人形机器人能通过多臂协作缩短任务周期，但安全控制更难，大规模示范也难采集。已有自动生成方法能从少数示范扩增数据，却忽略多臂约束，因此不能直接保证多条手臂组合起来仍可执行。瓶颈既是数据量，也是合成示范的有效性。

### 用一个例子理解

理解用例（非论文实验）：输入是少量“双手分别取物再放入盒中”的示范。系统生成新摆放条件下的执行安排，在两臂都需经过盒口时协调先后，输出供模仿学习使用的新示范；具体避让方式需查正文。

## 创新点或方法

旧做法生成新示范时没有充分处理多臂约束；ScheduleGen把规划与技能调度结合，在生成示范时一起考虑执行安排。调度为何有用？单个技能能够完成，不代表多个技能同时或先后组合也安全。训练阶段用生成的数据学习策略，部署时由策略执行任务；摘要没有说部署是否仍调用调度器，也未说明技能如何提取、约束怎样表达、轨迹如何调整，不能据此补出算法细节。

### 方法如何工作

1. 从少量源示范出发构造新示范任务，减少逐条人工采集的需求。
2. 联合规划与技能调度，把多臂约束纳入执行安排，减少组合后不安全或失败的行为。
3. 生成示范并评估是否成功，得到用于训练的候选数据；具体筛选流程摘要未说明。
4. 用生成数据训练操作策略，再分别测试仿真执行和真实环境迁移，检查数据是否真正有用。

### 必要术语

- 技能调度：安排动作技能何时、按什么关系执行；本文用来协调多臂行为。
- 模仿学习：从示范学习动作策略；本文用生成示范训练机器人。
- 零样本仿真到现实：无需目标现实环境中的额外训练就迁移；本文以真实任务测试这种能力。

## 证据

摘要给出28种仿真任务变体，包括7个由外部人员编写的RoboDojo任务，以及既有系统无法处理的设置；平均数据生成成功率为79.6%，训练所得策略平均成功率为65.5%。这两个指标分别衡量示范生成和策略执行，不能混用。策略优于使用一种最先进数据生成基线训练的策略，但摘要未给差值。在8种真实任务变体上，经零样本仿真到现实及现实到仿真再到现实迁移，成功率为50%—80%；各路线对应哪些任务未说明。

## 局限

真机结果支持特定任务上的迁移可行性，不能推出任意双臂平台都能直接使用。需要核查生成失败的原因、约束检查是否覆盖实际碰撞风险，以及成功率的试验次数。摘要未提供这些信息，不代表全文没有。

- **判断**：若要理解双臂示范为何不能简单拼接，值得读到规划与调度算法细节，并重点看它怎样判断生成结果可执行。

## 研究关联

这里值得借鉴的是，把数据扩增当成受约束的任务执行问题。对多执行器任务，增加轨迹数量之前，先处理技能之间的执行关系，可能比继续复制单臂扩增方式更关键。

### 下一步读哪里

核查技能边界、调度变量和多臂约束定义；对照生成成功与策略成功的评估规则，再看基线是否使用同样源示范、数据预算，以及8种真机变体的迁移路线和逐项结果。

- **概念**：智能体 Agent 世界模型 机器人学习 Sim2Real
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/ScheduleGen Demonstration Generation via Skill Scheduling for Multi-Arm Imitatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints. The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose multi-arm manipulation, but the acquisition of large multi-arm manipulation datasets remains a bottleneck. Automated demonstration generation can alleviate this burden by synthesizing new demonstrations from a handful of source demonstrations, but existing algorithms ignore multi-arm constraints and as a result often induce unsafe and unsuccessful behaviors. We address this limitation by introducing ScheduleGen, an integrated planning & scheduling algorithm for multi-arm demonstration generation. We evaluate ScheduleGen on 28 simulation task variants, including seven externally authored RoboDojo tasks and settings inaccessible to prior systems; it achieves 79.6% mean data-generation success and trains policies with 65.5% mean success. ScheduleGen policies outperform those trained on a state-of-the-art data generation baseline, and achieve 50-80% success across eight real-world variants through zero-shot sim-to-real and real-to-sim-to-real transfer. Videos and more at: https://schedulegen.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39429v1
- Authors: Neel Jawale, Stephan Pleines, Soha Pouya, Yuke Zhu, Ajay Mandlekar, Caelan Garrett
- Published: 2026-10-29T06:07:04Z
- Age days: 2

</details>
