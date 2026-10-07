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
url: "https://arxiv.org/abs/2610.08320v1"
published: "2026-10-06T13:22:30Z"
age_days: 0
score: 28
created: 2026-10-07
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Humanoid Horizon: Extending Task Horizon in Whole-Body Loco-Manipulation via Parallel Training, Dynamic Starting, and Reward Gating

> [!summary] 这篇论文到底做了什么（基于摘要）
> Humanoid Horizon 要让人形机器人在一轮任务里连续搬好多个物体。它让不同搬运阶段同时训练，用前一阶段真实结束的状态启动后一阶段，并在机器人碰坏刚完成的摆放时停止后续奖励。

## 问题

机器人要在杂乱室内依次走到物体旁、抓取、搬运并准确放置，整个任务不中断。现有训练容易只学到前面较容易拿奖励的部分；转而集中训练后面，又可能忘掉前面的动作。即使每段单独会做，段与段之间也可能接不上。

### 用一个例子理解

理解用例（非论文实验）：机器人先把箱子放到墙边，再搬椅子。训练第二段时，输入起点来自第一段实际结束的位置和物体状态；策略据此移动、抓取和放置椅子。若途中把刚放好的箱子撞偏超过阈值，剩余奖励归零，促使学习兼顾新任务与已有摆放。

## 创新点或方法

顺序优化各阶段容易顾此失彼；本文把 N 个场景组织成 S 路并行阶段训练流，所有阶段共同更新同一个策略。训练起点也不固定：后续环境接收上游执行产生的终止状态，逐渐接触更多实际交接情况。奖励门控则规定，在后续阶段中，若紧邻前一个物体偏离已放位置超过阈值，本轮剩余奖励归零。三者分别针对训练偏向、阶段交接和破坏已有成果。训练中的这些安排服务于测试时一个共享策略连续完成任务；摘要未说明策略结构和具体输入。

### 方法如何工作

1. 把连续搬运任务划成阶段训练流，让后段无需等前段完全学好才获得训练。
2. 各训练流共同更新共享策略，使前后阶段持续练习，减少训练重心转移造成的遗忘。
3. 用上游执行的终止状态更新下游起点，让后段学会接住前段实际留下的状态。
4. 后段若移动了刚放好的物体，停止本轮剩余奖励，让继续获利依赖于保存已有成果。

### 必要术语

- 全身移动操作：走路、平衡与物体操作需要一起协调；本文任务不能只训练机械臂动作。
- 灾难性遗忘：学新阶段时旧阶段能力退步；并行阶段更新针对这一问题。
- 奖励门控：满足特定条件后关闭奖励；本文用它约束对刚放好物体的干扰。

## 证据

摘要报告：在双物体 LHM-Humanoid 基准上，使用 350 个训练场景、66 个留出场景，各阶段成功率超过 80%。物体数量超过两个后，成功率随任务变长下降，但相比所有基线的骤降，下降较缓。摘要未给出基线名称、多物体具体数字或完整任务成功率；各阶段超过 80% 不能换算成整轮超过 80%。摘要也未明确这些结果属于仿真还是真机。

## 局限

作者明确指出，搬运物体增加后性能仍下降，所以它没有消除任务长度的影响。还需核查门控只监视紧邻前一个物体时，更早放好的物体如何受到保护，以及奖励归零后训练是否变得稀疏。

- **判断**：值得细读训练组织和起点更新机制，因为它直接处理连续任务中“会做每段却接不起来”的问题。

## 研究关联

长任务失败不一定说明单段动作能力不够，也可能是训练时后段拿不到足够更新，或只见过理想起点。值得借鉴的是把前段实际产生的状态交给后段训练，并持续保留前段练习机会。

### 下一步读哪里

下一步核查阶段如何划分、上游状态多久更新一次，以及物体位移阈值如何设定。优先看完整任务成功率、各机制消融和更多物体的结果，并确认测试载体及留出场景的变化范围。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/Humanoid Horizon Extending Task Horizon in Whole-Body Loco-Manipulation via Para.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Cluttered indoor environments, where large and heavy objects are scattered across diverse surfaces, require humanoid robots to sequentially navigate, grasp, transport, and accurately place each item at its target location within a single uninterrupted episode. This long-horizon, whole-body loco-manipulation task remains a significant challenge for current methods. Previous approaches often suffer from two main issues: easy-reward bias, where training overemphasizes early transport stages at the expense of later ones, and catastrophic forgetting, where focusing on later stages leads to a decline in earlier-stage performance. In this work, we introduce Humanoid Horizon, a unified policy framework designed to overcome these limitations through three interrelated mechanisms. The Parallel Training Strategy organizes $N$ scenes into $S$ concurrent stage streams governed by a shared policy, ensuring all transport stages receive continuous gradient updates and removing the bottleneck of sequential optimization. The Dynamic Starting Mechanism updates each environment's initial state with terminal states from upstream rollouts, gradually broadening transition coverage and enhancing robustness at stage boundaries. Reward Gating sets the reward to zero for the rest of the episode in later-stage streams when the immediately preceding object is displaced beyond a set threshold, so the shared policy learns not to disturb a just-placed object and earlier placements are preserved throughout the episode. Collectively, these strategies achieve per-stage success rates exceeding 80\% on the two-object LHM-Humanoid benchmark (350 training scenes, 66 held-out scenes). As the number of sequentially transported objects grows beyond two, success declines with the horizon, but the degradation is graceful relative to the sharp drop seen in all baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.08320v1
- Authors: Haozhuo Zhang, Qiang Zhang, Jian Tang, Mingzhe Ni, Michele Caprio, Angelo Cangelosi, Wei Pan
- Published: 2026-10-06T13:22:30Z
- Age days: 0

</details>
