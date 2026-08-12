---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10267v1"
published: "2026-06-09T00:24:00Z"
age_days: 1
score: 38
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents

> [!summary] 一句话结论（基于摘要）
> In this paper, we present a systematic study of Hi-VLA design for robot manipulation.

## 关键点

- **问题**：Despite recent empirical progress, there is a lack of unified design principles for these systems: existing Hi-VLA systems differ in how they choose and connect planners, controllers, mechanisms to switch between the two, and how observations and memory are represented in the planner.
- **创新点 / 方法**：In this paper, we present a systematic study of Hi-VLA design for robot manipulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Hierarchical vision-language-action (Hi-VLA) systems have emerged as a promising
paradigm for complex robot manipulation, by using high-level VLM planners to decompose
tasks into language subgoals executed by low-level VLA controllers. Despite recent
empirical progress, there is a lack of unified design principles for these systems:
existing Hi-VLA systems differ in how they choose and connect planners, controllers,
mechanisms to switch between the two, and how observations and memory are represented in
the planner. In this paper, we present a systematic study of Hi-VLA design for robot
manipulation. We unify representative Hi-VLA agents under an options-style control
framework and benchmark core design choices across short-horizon, long-horizon, and
reasoning-intensive tasks. Our analysis distills practical principles for building Hi-
VLA systems, showing how model choices and interface mechanisms jointly shape
performance. Applying these principles yields a substantially stronger system than
either flat VLA control or a naively designed hierarchy, across experiments both in
simulation and on a real ALOHA robot. Overall, our results provide a foundation for
building more capable, robust, and principled hierarchical VLA agents. More information
and video at jiahenghu.github.io/hi-vla.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10267v1
- Authors: Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang, Jie Tan, Annie Xie
- Published: 2026-06-09T00:24:00Z
- Age days: 1

</details>
