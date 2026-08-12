---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13553v1"
published: "2026-07-15T07:57:26Z"
age_days: 1
score: 30
created: 2026-07-17
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Flow-aware Optimal Navigation in Unsteady Flows through Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> Numerical results demonstrate that an agent that is able to sense and remember a set number of flow velocity measures achieves the highest performance.

## 关键点

- **问题**：Autonomous robotic navigation in nonstationary time-varying fluid flows remains a fundamental challenge due to partial observability and the unpredictability of realistic environments.
- **创新点 / 方法**：In this work we present a reinforcement learning approach using the TD3 algorithm to train autonomous agents to reach arbitrary targets within a parametric, chaotic double-gyre flow.
- **证据**：Numerical results demonstrate that an agent that is able to sense and remember a set number of flow velocity measures achieves the highest performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous robotic navigation in nonstationary time-varying fluid flows remains a
fundamental challenge due to partial observability and the unpredictability of realistic
environments. While classical optimal control frameworks employed in robotics require
unrealistic a-priori global flow knowledge, biological systems are able to navigate
successfully by exploiting localized sensory cues. In this work we present a
reinforcement learning approach using the TD3 algorithm to train autonomous agents to
reach arbitrary targets within a parametric, chaotic double-gyre flow. To investigate
optimal sensory mechanisms, we evaluate five bio-inspired observation strategies based
on relative position, local velocity or local vorticity measures, and short-term memory
variants. Additionally, we analyze the impact of providing agents with explicit global
flow parameters. Numerical results demonstrate that an agent that is able to sense and
remember a set number of flow velocity measures achieves the highest performance. The
experiments reveal a trade-off in sensor utility: velocity-aware agents optimize energy
efficiency, whereas vorticity sensors provide superior structural mapping and achieve
better target proximity. Incorporating explicit global flow parameters is shown to
decrease navigation performance. This behavior suggests that reinforcement learning-
based autonomous systems develop more robust and general policies when restricted to
implicit flow representations. The presented results offer insights for improving the
transition of bio-inspired robotic navigation from simulation to real-world
environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13553v1
- Authors: Andrea Maria Braghin, Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni, Gabriele Cazzulani
- Published: 2026-07-15T07:57:26Z
- Age days: 1

</details>
