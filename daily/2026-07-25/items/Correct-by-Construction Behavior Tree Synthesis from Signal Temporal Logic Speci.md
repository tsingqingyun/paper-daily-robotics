---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18731v1"
published: "2026-07-21T05:43:19Z"
age_days: 3
score: 24
created: 2026-07-25
concepts: ["世界模型", "具身智能评测与基准"]
---

# Correct-by-Construction Behavior Tree Synthesis from Signal Temporal Logic Specifications with Application to Robotic Missions

> [!summary] 一句话结论（基于摘要）
> Behavior Trees (BTs) are widely adopted for complex task execution in robotics, providing modular, reactive control but lacking formal guarantees.

## 关键点

- **问题**：However, existing correct-by-construction synthesis from Linear Temporal Logic (LTL) cannot express quantitative timing constraints.
- **创新点 / 方法**：Behavior Trees (BTs) are widely adopted for complex task execution in robotics, providing modular, reactive control but lacking formal guarantees.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, existing correct-by-construction synthesis from Linear Temporal Logic (LTL) cannot express quantitative timing constraints.

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior Trees (BTs) are widely adopted for complex task execution in robotics,
providing modular, reactive control but lacking formal guarantees. However, existing
correct-by-construction synthesis from Linear Temporal Logic (LTL) cannot express
quantitative timing constraints. This letter synthesizes correct-by-construction BTs
from Signal Temporal Logic (STL) specifications. The workspace is modeled as a timed
transition system and abstracted into a zone graph, and an augmented state space
tracking both logical progress and timing constraints is introduced. A hierarchical
fixed-point algorithm computes winning sets for an STL fragment encompassing safety,
reachability, response, recurrence, and persistence, yielding BT subtrees with a runtime
constraint function. Correctness guarantees are proven and complexity bounds are
derived. Simulations demonstrate specification satisfaction with strictly positive
robustness, and a physical quadrotor experiment with six STL specifications validates
practical deployability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18731v1
- Authors: Jiaheng Dong, Jingyi Huang, Liang Han
- Published: 2026-07-21T05:43:19Z
- Age days: 3

</details>
