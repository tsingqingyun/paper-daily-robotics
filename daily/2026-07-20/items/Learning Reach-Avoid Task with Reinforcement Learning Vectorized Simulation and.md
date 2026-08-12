---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15935v1"
published: "2026-07-17T13:18:32Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark

> [!summary] 一句话结论（基于摘要）
> We achieved state-of- the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task.

## 关键点

- **问题**：Deep reinforcement learning (DRL) has a longstanding tradition in addressing the reach- avoid task problem, especially for controlling robotic arms.
- **创新点 / 方法**：In this paper, we present, for the first time, a comprehensive benchmark for the reachavoid task that accurately captures real- world complexities without simplifications.
- **证据**：We achieved state-of- the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deep reinforcement learning (DRL) has a longstanding tradition in addressing the reach-
avoid task problem, especially for controlling robotic arms. While this task serves as a
baseline environment within the research community, the ability of DRL to effectively
learn the each-avoid task in complex and realistic scenarios beyond simplified and
restricted tabletop settings remains uncertain. In this paper, we present, for the first
time, a comprehensive benchmark for the reachavoid task that accurately captures real-
world complexities without simplifications. We demonstrate a diverse range of settings
for robotic arm reach-avoid task, which can be used for evaluating DRL research. We
achieved this by utilizing the MuJoCo MJX physics engine and parallelizing both the
simulation environment and DRL algorithms using the Brax library. We achieved state-of-
the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for
the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task. Our
results indicate that while in previous works DRL agents could solve, for example, a
reach task in a simplified setting perfectly, their agents performance collapses when
evaluated in realistic scenarios. Overall, this work identifies that additional research
is still required to claim the successful resolution of the robotic arm reach-avoid task
using DRL. The environment and benchmarking code is available as open source at the
following link

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15935v1
- Authors: Jonas Weihing, Shahram Eivazi
- Published: 2026-07-17T13:18:32Z
- Age days: 2

</details>
