---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14415v1"
published: "2026-06-12T12:48:56Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["机器人学习", "具身智能评测与基准"]
---

# CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns compared to state-of-the-art primal-dual and penalty-based methods

## 关键点

- **问题**：CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary, enabling smarter recovery steps back to safety, compensating for delayed Lagrange multiplier updates, reducing oscillations near the boundary, and preserving the KKT solutions of…
- **创新点 / 方法**：In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order primal-dual method that incorporates local constraint sensitivity into policy updates.
- **证据**：Experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns compared to state-of-the-art primal-dual and penalty-based methods
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/CSPO Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying
safety constraints, typically modeled as Constrained Markov Decision Processes (CMDPs).
While primal-dual methods scale well to deep RL, they often suffer from delayed
constraint correction, leading to oscillatory behavior and prolonged safety violations.
In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order
primal-dual method that incorporates local constraint sensitivity into policy updates.
CSPO augments the primal objective with a constraint-sensitive correction derived from
the shortest signed distance to the safety boundary, enabling smarter recovery steps
back to safety, compensating for delayed Lagrange multiplier updates, reducing
oscillations near the boundary, and preserving the KKT solutions of the original
constrained problem. Experiments on navigation and locomotion benchmarks demonstrate
that CSPO achieves faster safety recovery and high reward preservation, resulting in
higher constrained returns compared to state-of-the-art primal-dual and penalty-based
methods

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14415v1
- Authors: Ayoub Belouadah, Sylvain Kubler, Yves Le Traon
- Published: 2026-06-12T12:48:56Z
- Age days: 3

</details>
