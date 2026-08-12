---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18594v1"
published: "2026-06-17T01:45:13Z"
age_days: 1
score: 32
created: 2026-06-19
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Benchmarking Action Spaces in Reinforcement Learning for Vision-based Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> In this study, we evaluate pose increment, pose velocity, joint position increment, and joint velocity across two vision-based manipulation tasks: object picking and pushing.

## 关键点

- **问题**：In real-world reinforcement learning (RL), the choice of action space can play a key role in shaping motion smoothness, safety, and overall task performance.
- **创新点 / 方法**：In this study, we evaluate pose increment, pose velocity, joint position increment, and joint velocity across two vision-based manipulation tasks: object picking and pushing.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In real-world reinforcement learning (RL), the choice of action space can play a key
role in shaping motion smoothness, safety, and overall task performance. In this study,
we evaluate pose increment, pose velocity, joint position increment, and joint velocity
across two vision-based manipulation tasks: object picking and pushing. We train
policies in simulation and deploy them to the real world using sim-to-real transfer. We
find that action-space representation indeed significantly affects sim-to-real
performance. In particular, we find that the joint velocity action space is best for the
vision-based picking and pushing tasks in terms of smoothness and final task
performance. We also provide practical guidance for RL practitioners in choosing action
spaces for both simulation and real-world experiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18594v1
- Authors: Seyed Alireza Azimi, Homayoon Farrahi, Abhishek Naik, Colin Bellinger, A. Rupam Mahmood
- Published: 2026-06-17T01:45:13Z
- Age days: 1

</details>
