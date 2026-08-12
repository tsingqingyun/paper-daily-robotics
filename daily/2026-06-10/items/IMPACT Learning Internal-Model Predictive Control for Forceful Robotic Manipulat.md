---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10818v1"
published: "2026-06-09T13:00:56Z"
age_days: 0
score: 30
created: 2026-06-10
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive simulation and real-world experiments demonstrate that the proposed framework achieves higher success rates and improved generalization to unseen object weights, as well as better safety and energy efficiency.

## 关键点

- **问题**：However, implicit approaches generalize poorly across object weights, while explicit approaches require specialized hardware and increase system complexity.
- **创新点 / 方法**：In this work, we propose IMPACT, a framework that decouples these forceful tasks into task-planning and internal-model- based predictive control.
- **证据**：Extensive simulation and real-world experiments demonstrate that the proposed framework achieves higher success rates and improved generalization to unseen object weights, as well as better safety and energy efficiency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world robotic manipulation tasks often involve forceful interactions with the
environment, such as using tools of varying weights, transporting objects with different
masses, and performing contact-rich tasks like table wiping. Previous learning-based
approaches typically employ imitation learning policies that output target end-effector
poses tracked by low-level impedance controllers. In these systems, forceful
interactions are either implicitly realized through steady-state tracking errors or
explicitly commanded using wrist force/torque or tactile sensors. However, implicit
approaches generalize poorly across object weights, while explicit approaches require
specialized hardware and increase system complexity. In this work, we propose IMPACT, a
framework that decouples these forceful tasks into task-planning and internal-model-
based predictive control. Extensive simulation and real-world experiments demonstrate
that the proposed framework achieves higher success rates and improved generalization to
unseen object weights, as well as better safety and energy efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10818v1
- Authors: Jiawei Gao, Chaoqi Liu, Peilin Wu, Haonan Chen, Yilun Du
- Published: 2026-06-09T13:00:56Z
- Age days: 0

</details>
