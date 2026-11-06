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
url: "https://arxiv.org/abs/2611.06475v1"
published: "2026-11-04T13:16:32Z"
age_days: 1
score: 33
created: 2026-11-06
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboCasa-Mem 让移动操作机器人在后续步骤用到已经看不见的信息，并用 Behavior-Conditioned Evaluation 按机器人自己早先的动作决定后来该做什么。基线 HMAP 用结构化记忆选子任务，再用带几何信息的控制器执行。

## 问题

移动操作机器人常要离开一个地点再回来，或在几项操作之间切换。它得记住物体的位置、属性和关系，也得记住哪些步骤已经完成、哪些还在等。现有基准较少在关键决策处测这些能力。如果正确目标从一开始就固定，策略还可能靠熟悉的位置或路线得分，评分因此难以区分它有没有用到自己的交互历史。

### 用一个例子理解

理解用例（非论文实验）：机器人可把杯子先放进左柜或右柜，随后离开去拿托盘。等它回来时两扇柜门都关着，评估器按它之前实际放杯子的柜子确定正确目标。策略读出自己的存放记录，把打开对应柜子交给低层控制器，最终取回杯子。

## 创新点或方法

任务允许多条有效路径时，评估器先根据机器人实际做过的动作确定后续约束，再检查后续行为是否符合这段历史。HMAP 则从策略侧处理这个问题。执行时，高层规划器查实体与过程记忆来决定下一项子任务，低层视觉语言动作控制器用子目标构造查询，把 VGGT-Omega 提供的几何信息用到动作生成中。论文提供成功示范供策略训练，摘要没有交代 HMAP 如何用这些示范训练、如何写入记忆，或几何特征如何与动作控制器融合。

### 方法如何工作

1. 执行允许多条有效路径的任务，让早先的选择产生不同的后续要求。
2. 评估器从实际执行历史推导后续约束，得到与该次行动路径对应的评分依据。
3. HMAP 的高层查实体状态和任务进度，输出当前该做的子任务，使早先的信息能影响接下来的决策。
4. 低层控制器结合子目标和几何线索输出动作，评估器再检查执行结果是否符合这次任务的历史。

### 必要术语

- 环境记忆：记住物体在哪、有什么属性、与其他物体怎样摆放；本文用它支撑离开后再次寻找或操作。
- 过程记忆：记住做过哪一步、接下来还有什么要做；本文用它支撑长任务和多任务调度。
- 行为条件评估：按机器人早先实际采取的行为确定后续正确条件；本文用它减少固定目标造成的评分捷径。
- 子目标条件查询：用当前子任务决定去取哪些信息；HMAP 用它引入与当前动作相关的几何线索。

## 证据

据摘要，基准包含 9 个移动操作任务和 1,800 条成功示范，任务覆盖环境记忆和过程记忆。HMAP 是作者提供的基线。摘要没有给出实验平台配置、其他对比策略、评分指标的定义或基线成绩，因此目前能判断的是任务和评分想测什么，HMAP 的表现以及各记忆组件的贡献还需查结果。

## 局限

作者称按行为评分可以减少固定目标带来的捷径。我会核查关键决策处是否还留有可直接辨认的视觉线索，以及移除或打乱历史后性能会怎样。通过任务能说明行为与历史一致，要把得分归因于策略使用了记忆，还得看这些对照。

- **判断**：优先读任务定义和评分规则。想复用 HMAP，再追到记忆如何写入、何时读取，以及移除记忆后成绩怎么变。

## 研究关联

设计记忆测试时，可以先让机器人在几个有效选项中做一次选择，再让这次选择改变后面怎样才算做对。如果能构造当前观测相近、历史不同且正确动作也不同的情形，就能更有针对性地检查策略有没有保留过去的信息。

### 下一步读哪里

找同一任务下两条有效历史及其后续评分条件，检查当前画面是否足以猜对。读 HMAP 时，重点看实体与过程记忆的写入依据、子目标如何查询几何信息，以及有没有分离记忆与几何贡献的对照。

- **概念**：智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/Robocasa-Mem Benchmarking Environment and Process Memory in Long-Horizon Mobile.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specifically, the tasks are grouped into two categories of memory: One is environment memory, which captures spatial locations, object attributes, and object relationships. The other is process memory, which captures single-task progress and multi-task scheduling. Particularly, we introduce Behavior-Conditioned Evaluation. For tasks with multiple valid execution paths, instead of fixing a single target or trajectory, the evaluator derives later task constraints from the robot's earlier actions. This allows us to evaluate whether later behavior is consistent with the robot's own interaction history while reducing shortcuts based on fixed target assignments. We provide 1,800 successful demonstrations for policy training. We also develop a baseline on our benchmark, namely Hierarchical Memory-Augmented Policy(HMAP). Its high-level planner uses structured entity and process memories to generate subtasks. Its low-level VLA controller uses subgoal-conditioned queries to incorporate VGGT-Omega geometry into action generation. Together, RoboCasa-Mem and HMAP baseline support systematic evaluation of memory-dependent behavior and the development of memory-aware mobile manipulation policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06475v1
- Authors: Sihang Chen, Chen Ye, Wei Chen, Xiaohan Lei, Zhipeng Tang, Sha Zhang, Yuan Zhang, Zixuan Chen, Jiajun Deng, Houqiang Li, Yanyong Zhang
- Published: 2026-11-04T13:16:32Z
- Age days: 1

</details>
