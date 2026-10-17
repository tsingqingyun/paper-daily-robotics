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
url: "https://arxiv.org/abs/2610.22184v1"
published: "2026-10-15T16:40:48Z"
age_days: 1
score: 31
created: 2026-10-17
concepts: ["智能体 Agent", "Sim2Real"]
---

# Whole-Body Dexterity

> [!summary] 这篇论文到底做了什么（基于摘要）
> Whole-Body Dexterity（WBD）让机器人用手臂、躯干等身体表面一起托住和移动大物体。它先在仿真里练习不同全身接触姿态之间的转换，再把多个专家压成一个可由人粗略引导的控制策略。

## 问题

具体任务是把篮球、箱子等物体移动到身体周围不同位置，并在搬运中保持接触。仅靠末端执行器和简单抓握，难以利用把物体夹在腋下、靠着胸口滑动等动作；真正困难的是转换接触方式时仍能稳定控制物体。

### 用一个例子理解

理解用例（非论文实验）：输入机器人当前关节状态、箱子几何和“把箱子移到左腋下”的粗略参考；策略协调手臂与躯干，使箱子逐步靠向身体，输出连续控制动作并维持夹持。

## 创新点或方法

旧做法主要控制手部抓握；WBD 把身体及附肢都纳入接触面。训练先生成可行全身抓持数据，再抽取初始和目标抓持，训练强化学习专家完成任意两种抓持间的重定位，最后蒸馏成单一策略。真机推理使用本体感觉、物体几何及人的粗略运动参考，无需真机适配训练。奖励、专家划分和物体几何获取方式摘要未说明。

### 方法如何工作

1. 在仿真中生成可行全身抓持，得到能支撑物体的接触状态，避免从大量无效姿态开始学习。
2. 从数据中抽取初始与目标抓持，让强化学习专家练习状态间转换，学习移动过程中如何维持接触。
3. 把多个专家蒸馏为单一策略，使部署时无需逐个选择专家。
4. 在 G1 上输入本体感觉、物体几何及人的运动参考，持续输出控制动作；更细的控制接口摘要只说明到此。

### 必要术语

- 全身抓持：用手以外的身体表面共同固定物体；是本文训练任务的基本状态。
- 本体感觉：机器人自身关节位置、运动等信息；帮助策略判断身体当前姿态。
- 策略蒸馏：让一个策略学习多个专家的行为；用于合并部署控制器。
- 零样本迁移：仿真训练后的策略直接用于真机；本文据此检验仿真所学能否落地。

## 证据

摘要报告策略零样本迁移到 Unitree G1，能重定位篮球和纸箱，并完成从架子取箱、夹在一侧手臂下搬到桌边再放置的长时任务。真实全身操作试验成功率为 90%，直接重定向为 18%，通用全身控制器为 4%。未提供试验次数、任务占比及成功判据，因此数字支持所测任务中的优势，不能外推到任意物体。

## 局限

真机执行由人提供粗略运动参考，因此结果证明的是交互控制能力，不能当作自主完成任务规划的证据。我的待核查问题包括陌生物体、摩擦变化和几何估计误差下的稳定性；摘要未交代对应测试。

- **判断**：值得细读抓持数据生成与任意姿态转换目标，它们最能解释全身接触能力如何被系统地练出来。

## 研究关联

这里值得借鉴的是，把稳定的身体接触状态作为训练起点和目标。复杂搬运因此可以拆成可练习的接触转换；当物体适合倚靠或夹持、且能生成足够可行抓持时，这种任务组织方式值得尝试。

### 下一步读哪里

先检查可行抓持如何筛选、目标姿态如何采样，再看蒸馏保留了哪些输入。实验重点核查 90% 的任务构成，以及各对比方法是否获得相同的人类参考和物体信息。

- **概念**：智能体 Agent Sim2Real
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/Whole-Body Dexterity.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp and manipulate objects. Our sim-to-real pipeline first generates a dataset of feasible whole-body grasps, then trains reinforcement-learning experts on a general any-to-any repositioning objective by sampling initial and goal grasps from the dataset, and distills these experts into a single policy that uses proprioception and object geometry. We show that the distilled policy transfers zero-shot to a real Unitree G1, where it repositions a basketball and a cardboard box to regions around the torso and completes a long-horizon task that stows a box under one arm, carries it from a shelf to a table, and places it. The controller operates interactively, steered by coarse motion references from a human teleoperator. Across real-world whole-body manipulation tasks, the distilled controller completes 90% of trials, compared with 18% for direct retargeting and 4% for a generalist whole-body controller.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22184v1
- Authors: Conor Mc Gartoll, An Dang, Pranay Thangeda, Arjun Gupta, Carolina Higuera, Nima Fazeli, Mustafa Mukadam, Manikantan Nambi
- Published: 2026-10-15T16:40:48Z
- Age days: 1

</details>
