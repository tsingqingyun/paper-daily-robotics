---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25363v1"
published: "2026-09-21T20:01:04Z"
age_days: 2
score: 38
created: 2026-09-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments

> [!summary] 先说人话（基于摘要）
> HOTICE 让人形机器人搬着物体穿过拥挤环境，同时照顾身体和货物的避障。它把上下肢控制分给两个强化学习智能体，再将多个场景专家蒸馏成一个部署策略。

## 问题

搬运时，可通行空间同时受机器人身体和载荷形状约束，现有方法在杂乱环境中容易顾此失彼；全身移动操作的高维动作空间也增加了学习难度。

## 创新点或方法

Humanoid-Object Decoupled Potential Fields 分别表达身体与载荷的避碰引导；上下身策略通过共享状态和奖励保持协调。带特权信息的教师策略经专家到通用策略蒸馏，形成单一学生策略。

## 证据

在 MuJoCo 和真实 Unitree G1 上评估了不同形状物体的杂乱场景搬运。摘要报告未见环境泛化、全身协调和 sim2real 效果，未给出可核查的结果数字。

## 局限

需核查学生策略部署时需要哪些物体与障碍信息，以及未见场景和物体变化的测试范围。

- **判断**：做全身搬运值得细读势场与上下身协调机制，效果强弱仍需查看量化评测。

## 研究关联

对全身机器人学习与 Sim2Real 研究者，价值在于把载荷几何纳入控制目标，并提供高维控制的分解方法。这里的双智能体指控制分工，摘要未体现世界模型贡献。

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/HOTICE Whole-Body Humanoid Object Transportation in Cluttered Environments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments, yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First, we introduce Humanoid-Object Decoupled Potential Fields, which jointly encode collision-avoidance guidance for the robot and the carried object, enabling coordinated, obstacle-aware motion for both. Second, to address the large action space inherent to whole-body loco-manipulation, we design a dual-agent reinforcement learning architecture that decouples upper- and lower-body control while preserving whole-body coordination via shared state observations and rewards. To train a policy that generalizes across diverse cluttered scenes, we further employ a specialist-to-generalist distillation strategy, in which privileged teacher policies are distilled into a single deployable student policy. We evaluate HOTICE in MuJoCo simulation and on a real Unitree G1 humanoid, demonstrating effective and robust object transportation across cluttered scenarios for objects of varying shapes. Our results show that HOTICE reliably coordinates whole-body motion and object-aware collision avoidance, generalizing effectively to previously unseen cluttered environments while achieving strong performance in sim2real deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25363v1
- Authors: Toan Nguyen, Weiduo Yuan, Siheng Zhao, Yue Wang, Daniel Seita
- Published: 2026-09-21T20:01:04Z
- Age days: 2

</details>
