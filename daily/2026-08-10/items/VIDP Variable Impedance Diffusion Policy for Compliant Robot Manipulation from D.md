---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06210v1"
published: "2026-08-06T16:03:00Z"
age_days: 3
score: 28
created: 2026-08-10
concepts: ["机器人学习", "具身智能评测与基准"]
---

# VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations

> [!summary] 一句话结论（基于摘要）
> Real-world experiments show that VIDP significantly outperforms fixed-impedance baselines in task success rate while reducing interaction forces with respect to high stiffness controllers and tracking errors with respect to low stiffness baselines.

## 关键点

- **问题**：Contact-rich manipulation requires precise tracking and mechanical compliance, where variable impedance control can improve robustness in task success, whereas static compliance cannot adapt to varying contact constraints.
- **创新点 / 方法**：Variable impedance skills can be learned from demonstrations, avoiding complex modeling, but compliance is a hidden variable in force-agnostic kinematic data.
- **证据**：Real-world experiments show that VIDP significantly outperforms fixed-impedance baselines in task success rate while reducing interaction forces with respect to high stiffness controllers and tracking errors with respect to low stiffness baselines.
- **局限**：Contact-rich manipulation requires precise tracking and mechanical compliance, where variable impedance control can improve robustness in task success, whereas static compliance cannot adapt to varying contact constraints.

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich manipulation requires precise tracking and mechanical compliance, where
variable impedance control can improve robustness in task success, whereas static
compliance cannot adapt to varying contact constraints. Variable impedance skills can be
learned from demonstrations, avoiding complex modeling, but compliance is a hidden
variable in force-agnostic kinematic data. While existing methods infer compliance from
trajectory variations, these variations may reflect geometric adaptation and not
intentional compliance when subject to changing spatial layouts. Therefore, this letter
introduces Variable Impedance Diffusion Policy (VIDP), an imitation learning-based
variable impedance control framework leveraging a Task-Parameterized Directionality-
Aware Mixture Model (TP-DAMM) to extract physically consistent trajectory distributions
from diverse demonstrations. By mapping distributions to stiffness profiles, VIDP
jointly predicts pose actions and task compliance without force sensors. Real-world
experiments show that VIDP significantly outperforms fixed-impedance baselines in task
success rate while reducing interaction forces with respect to high stiffness
controllers and tracking errors with respect to low stiffness baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06210v1
- Authors: Hisham Khalil, Neil Fernandes, Thomas M. Kwok, Hsiu-Chin Lin, Yue Hu
- Published: 2026-08-06T16:03:00Z
- Age days: 3

</details>
