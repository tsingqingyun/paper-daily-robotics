---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20823v1"
published: "2026-08-21T07:44:00Z"
age_days: 3
score: 23
created: 2026-08-24
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Natural Sit-to-Stand Motion Synthesis For Humanoids via Guided Assistance Curricula and Staged Rewards

> [!summary] 一句话结论（基于摘要）
> We synthesise natural humanoid STS motion from scratch using reinforcement learning, without demonstrations or reference trajectories.

## 问题

A humanoid has infinitely many ways to stand up from sitting while maintaining balance, making sit-to-stand (STS) a challenging control problem.

## 创新点或方法

We synthesise natural humanoid STS motion from scratch using reinforcement learning, without demonstrations or reference trajectories.

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/Natural Sit-to-Stand Motion Synthesis For Humanoids via Guided Assistance Curric.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A humanoid has infinitely many ways to stand up from sitting while maintaining balance, making sit-to-stand (STS) a challenging control problem. We synthesise natural humanoid STS motion from scratch using reinforcement learning, without demonstrations or reference trajectories. A single Proximal Policy Optimisation policy learns smooth, human-like rising driven by three complementary components. (i) A coupled force/chair-height curriculum is used. A vertical pelvis-assist force aids early trajectory exploration and decays over training. Taller chairs are unlocked with decaying assisting force. This ensures that the policy masters a viable STS trajectory at each chair height before being exposed to harder ones, avoiding the premature distribution shift that otherwise collapses generalisation. (ii) Motion robustness is achieved by randomly sampling from a large number of inverse kinematics-generated initial and target poses spanning over eight chair heights. (iii) A set of rewards is defined inspired from biomechanics and optimal control studies. They shape the robot's angular momentum for seat-off, and enable support-region transition via centre of pressure attraction function to ensure smooth low-effort actuation. On a deterministic force-free evaluator, the policy attains more than 97% balanced-standing success across eight chair heights. The policy generalises smooth motion across chair heights and enables the robot to rise from substantially deep-seated postures as compared to the state of the art.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20823v1
- Authors: Meet Pal Singh, Vyankatesh Ashtekar, Ashish Dutta
- Published: 2026-08-21T07:44:00Z
- Age days: 3

</details>
