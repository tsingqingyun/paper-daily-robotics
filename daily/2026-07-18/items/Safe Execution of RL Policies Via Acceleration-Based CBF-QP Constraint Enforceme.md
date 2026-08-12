---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14488v1"
published: "2026-07-16T02:00:11Z"
age_days: 1
score: 30
created: 2026-07-18
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments

> [!summary] 一句话结论（基于摘要）
> Under aggressive velocity commands on H1, Acc-CBF-QP improves execution by preventing constraint-induced shutdowns, yielding longer survival times.

## 关键点

- **问题**：Reinforcement Learning (RL) has demonstrated remarkable capabilities for solving complex robotic control problems, but its lack of safety guarantees severely limits deployment on hardware.
- **创新点 / 方法**：To address this, we introduce Acc-CBF-QP, an acceleration-based Quadratic Program (QP) safety filter using Control Barrier Functions (CBFs) that constrains any RL policy onto a safe set at runtime without modifying training.
- **证据**：Under aggressive velocity commands on H1, Acc-CBF-QP improves execution by preventing constraint-induced shutdowns, yielding longer survival times.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforceme.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement Learning (RL) has demonstrated remarkable capabilities for solving complex
robotic control problems, but its lack of safety guarantees severely limits deployment
on hardware. In particular, as legged robots and manipulators often operate near safety-
critical boundaries, out-of-distribution states can lead to failure upon deployment. To
address this, we introduce Acc-CBF-QP, an acceleration-based Quadratic Program (QP)
safety filter using Control Barrier Functions (CBFs) that constrains any RL policy onto
a safe set at runtime without modifying training. The method applies to unconstrained
and Safe-RL policies, and enforces joint position, velocity, torque, and collision
constraints within a unified optimization framework. A key contribution is the
formulation of RL+QP tasks that regulate deviation from the RL command when constraints
would otherwise be violated. We introduce a TorqueTask, minimizing torque deviation, and
a Forward Dynamics Task, minimizing induced acceleration deviation, thus providing
principled control over safety-performance trade-offs. Experiments on a 7-DoF Kinova
Gen3 manipulator and a 19-DoF Unitree H1 humanoid, both in simulation and on hardware,
highlight substantial reductions in constraint violations. On the real H1 hardware, a
Safe-RL policy alone yielded 10.04 violations/s, which were reduced by 92% to 0.80
violations/s when augmented with Acc-CBF-QP. On the Kinova Gen3, Acc-CBF-QP fully
eliminated violations. Nominal task performance of the RL objective is preserved in
violation-free regimes. Under aggressive velocity commands on H1, Acc-CBF-QP improves
execution by preventing constraint-induced shutdowns, yielding longer survival times.
The full pipeline is open-source.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14488v1
- Authors: Bastien Muraccioli, Alice Cariou, Pierre-Alexandre Leziart, Mathieu Celerier, Arnaud Demont, Gentiane Venture, Mehdi Benallegue
- Published: 2026-07-16T02:00:11Z
- Age days: 1

</details>
