---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17819v1"
published: "2026-08-18T14:18:48Z"
age_days: 3
score: 25
created: 2026-08-22
concepts: ["AI 核心知识地图"]
---

# Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Aerial Manipulation

> [!summary] 一句话结论（基于摘要）
> We show that a four-rotor tiltable configuration provides a balance between interference-free propeller sizing and hovering efficiency across different attitudes, and its null-space redundancy is crucial for traversing singular configurations under physical c…

## 关键点

- **问题**：Aerial manipulation extends robotic operations to previously inaccessible aerial environments.
- **创新点 / 方法**：To address disturbances, we propose a dual strategy consisting of a modified integral term for model error and an acceleration-based estimator for external wrenches.
- **证据**：We show that a four-rotor tiltable configuration provides a balance between interference-free propeller sizing and hovering efficiency across different attitudes, and its null-space redundancy is crucial for traversing singular configurations under physical constraints.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Ae.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Aerial manipulation extends robotic operations to previously inaccessible aerial environments. Unlike arm-equipped aerial systems, tiltable-multirotors can directly generate six-degree-of-freedom wrenches through their flight bases, enabling both efficient movement and omnidirectional operation by tilting the thrust direction. This work presents a design analysis and a wrench-based control framework for tiltable-multirotors in aerial manipulation. We show that a four-rotor tiltable configuration provides a balance between interference-free propeller sizing and hovering efficiency across different attitudes, and its null-space redundancy is crucial for traversing singular configurations under physical constraints. We further show that an upward end-effector placement yields a favorable trade-off between geometric clearance and available wrench. To address disturbances, we propose a dual strategy consisting of a modified integral term for model error and an acceleration-based estimator for external wrenches. Building on these insights, we develop an effector-centric nonlinear model predictive control (NMPC) framework that integrates design choices, singularity handling, and disturbance compensation into a unified formulation. The proposed framework runs fully onboard at 100 Hz on a custom-built tiltable-quadrotor. Real-world experiments, including a 90-deg step cartwheel rotation, whiteboard pushing, and continuous 360-deg valve turning, demonstrate the feasibility of wrench-based omnidirectional manipulation with singularity traversal on a one-DoF-per-arm tiltable-quadrotor.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17819v1
- Authors: Jinjie Li, Yicheng Chen, Johannes Kübel, Haokun Liu, Junichiro Sugihara, Moju Zhao
- Published: 2026-08-18T14:18:48Z
- Age days: 3

</details>
