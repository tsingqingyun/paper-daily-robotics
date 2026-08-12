---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12965v1"
published: "2026-06-11T06:49:39Z"
age_days: 2
score: 26
created: 2026-06-14
concepts: ["机器人学习", "具身智能评测与基准"]
---

# EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment

> [!summary] 一句话结论（基于摘要）
> Compared with Cartesian-only execution, EmbodiSteer reduces collision rate by 46.1% and improves task success rate by 28.5% across 9 simulated robots, and further achieves 90.0% collision rate reduction and 36.7% success rate increase on two physical robots i…

## 关键点

- **问题**：However, end-effector-only abstraction leaves Cartesian policies unaware of the deployed robot body, making them brittle under robot- specific constraints such as whole-body collision avoidance.
- **创新点 / 方法**：To overcome this limitation, we present EmbodiSteer, a training-free framework that steers embodiment- agnostic visuomotor policies toward zero-shot, embodiment-aware deployment.
- **证据**：Compared with Cartesian-only execution, EmbodiSteer reduces collision rate by 46.1% and improves task success rate by 28.5% across 9 simulated robots, and further achieves 90.0% collision rate reduction and 36.7% success rate increase on two physical robots in highly constrained scenarios.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scalable robot imitation learning relies on large-scale heterogeneous data from diverse
robots or body-free data, making Cartesian end-effector actions a key interface for
embodiment-agnostic policy learning. However, end-effector-only abstraction leaves
Cartesian policies unaware of the deployed robot body, making them brittle under robot-
specific constraints such as whole-body collision avoidance. To overcome this
limitation, we present EmbodiSteer, a training-free framework that steers embodiment-
agnostic visuomotor policies toward zero-shot, embodiment-aware deployment. EmbodiSteer
keeps policy learning in Cartesian space while efficiently lifting inference-time
diffusion sampling into the target robot's joint space via forward kinematics and
Jacobian-based updates. With whole-body collision-aware guidance over joint trajectories
after each denoising step, the arm can be steered away from collisions while preserving
learned end-effector behavior. Compared with Cartesian-only execution, EmbodiSteer
reduces collision rate by 46.1% and improves task success rate by 28.5% across 9
simulated robots, and further achieves 90.0% collision rate reduction and 36.7% success
rate increase on two physical robots in highly constrained scenarios. Our project page
is at https://frankwang67.github.io/EmbodiSteer-Page.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12965v1
- Authors: Shihefeng Wang, Kangchen Lv, Mingrui Yu, Xiang Li
- Published: 2026-06-11T06:49:39Z
- Age days: 2

</details>
