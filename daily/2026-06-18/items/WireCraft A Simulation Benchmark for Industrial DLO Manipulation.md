---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18097v1"
published: "2026-06-16T15:59:46Z"
age_days: 1
score: 41
created: 2026-06-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# WireCraft: A Simulation Benchmark for Industrial DLO Manipulation

> [!summary] 一句话结论（基于摘要）
> To bridge this gap, we introduce WireCraft, a simulation benchmark for industrial DLO manipulation with configurable difficulty and assets, spanning three task families: connector insertion, clip routing, and channel seating.

## 关键点

- **问题**：Despite their importance, policy development and comparison remain difficult: existing benchmarks are often tied to specific hardware setups, lack modular and customizable task assets, or study generic deformable-object tasks without the fixtures relevant to real-world industrial wire manipulation.
- **创新点 / 方法**：To bridge this gap, we introduce WireCraft, a simulation benchmark for industrial DLO manipulation with configurable difficulty and assets, spanning three task families: connector insertion, clip routing, and channel seating.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial
assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an
infinite-dimensional configuration space and deform continuously under contact with
grippers, fixtures, and the workspace, making them a demanding benchmark for general
dexterous manipulation. Despite their importance, policy development and comparison
remain difficult: existing benchmarks are often tied to specific hardware setups, lack
modular and customizable task assets, or study generic deformable-object tasks without
the fixtures relevant to real-world industrial wire manipulation. Few benchmarks align
simulation, real-world data, and shared evaluation protocols. To bridge this gap, we
introduce WireCraft, a simulation benchmark for industrial DLO manipulation with
configurable difficulty and assets, spanning three task families: connector insertion,
clip routing, and channel seating. It supports two complementary DLO physics models,
articulated and deformable, and the trajectories come from both simulation and a
physical UR5. We benchmark reinforcement learning (RL), imitation learning (IL), and
vision-language-action (VLA) policies under shared metrics. Privileged state-based RL
solves a representative setting in each task family with over 82\% success, confirming
the tasks are well-posed. For connector insertion, however, the transition from reaching
the socket to contact-rich alignment remains a key bottleneck for vision RL, IL, and VLA
policies. These results indicate that industrial DLO manipulation, though tractable
under privileged state, remains an open challenge for current vision-based learning. The
benchmark, data, and tools will be open-sourced upon acceptance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18097v1
- Authors: Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao, Artem Arutyunov, Seungyeon Ha, Chi-Guhn Lee
- Published: 2026-06-16T15:59:46Z
- Age days: 1

</details>
