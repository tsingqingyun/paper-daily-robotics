---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19469v1"
published: "2026-05-19T07:21:53Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Sampling-Based Safe Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Empirically, SBSRL achieves safe and efficient exploration both in simulation and in real robotic hardware, and readily extends to practical deep-ensemble implementations that scale to high-dimensional continuous control problems.

## 关键点

- **问题**：Safe exploration remains a fundamental challenge in reinforcement learning (RL), limiting the deployment of RL agents in the real world.
- **创新点 / 方法**：We propose Sampling-Based Safe Reinforcement Learning (SBSRL), a model-based RL algorithm that maintains safety throughout the learning process by enforcing constraints jointly across a finite set of dynamics samples.
- **证据**：Empirically, SBSRL achieves safe and efficient exploration both in simulation and in real robotic hardware, and readily extends to practical deep-ensemble implementations that scale to high-dimensional continuous control problems.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe exploration remains a fundamental challenge in reinforcement learning (RL),
limiting the deployment of RL agents in the real world. We propose Sampling-Based Safe
Reinforcement Learning (SBSRL), a model-based RL algorithm that maintains safety
throughout the learning process by enforcing constraints jointly across a finite set of
dynamics samples. This formulation approximates an intractable worst-case optimization
over uncertain dynamics and enables practical safety guarantees in continuous domains.
We further introduce an exploration strategy based on constraining epistemic
uncertainty, eliminating the need for explicit exploration bonuses. Under regularity
conditions, we derive high-probability guarantees of safety throughout learning and a
finite-time sample complexity bound for recovering a near-optimal policy. Empirically,
SBSRL achieves safe and efficient exploration both in simulation and in real robotic
hardware, and readily extends to practical deep-ensemble implementations that scale to
high-dimensional continuous control problems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19469v1
- Authors: Luca Vignola, Bruce D. Lee, Manish Prajapat, Manuel Wendl, Melanie Zeilinger, Andreas Krause, Yarden As
- Published: 2026-05-19T07:21:53Z
- Age days: 0

</details>
