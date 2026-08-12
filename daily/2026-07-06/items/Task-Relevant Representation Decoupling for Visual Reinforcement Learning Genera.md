---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00796v1"
published: "2026-07-01T11:26:25Z"
age_days: 4
score: 26
created: 2026-07-06
concepts: ["智能体 Agent", "机器人学习"]
---

# Task-Relevant Representation Decoupling for Visual Reinforcement Learning Generalization

> [!summary] 一句话结论（基于摘要）
> T2RD achieves State-Of-The-Art (SOTA) generalization performance and sample efficiency in the DeepMind Control Suite and Robotic Manipulation tasks.

## 关键点

- **问题**：However, generalizing learned policies to new environments remains a major challenge, as agents often overfit to task-irrelevant features in the training environment.
- **创新点 / 方法**：To solve this problem, we introduce the concept of decoupling observations into task-relevant and task-irrelevant representations.
- **证据**：T2RD achieves State-Of-The-Art (SOTA) generalization performance and sample efficiency in the DeepMind Control Suite and Robotic Manipulation tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual Reinforcement Learning (VRL) has achieved considerable success in solving control
tasks. However, generalizing learned policies to new environments remains a major
challenge, as agents often overfit to task-irrelevant features in the training
environment. To solve this problem, we introduce the concept of decoupling observations
into task-relevant and task-irrelevant representations. Building on this idea, we
propose a self-supervised Task-Relevant Representation Decoupling (T2RD) algorithm for
VRL. This algorithm consists of three components: task-relevant representation
consistency, cross-reconstruction, and cross-dynamic prediction. The first two
components achieve the decoupling of content and style features, but the resulting
content representations are not necessarily task-relevant. To further refine task-
relevant features from content representations, we design the third component that
introduces dynamic prediction. T2RD achieves State-Of-The-Art (SOTA) generalization
performance and sample efficiency in the DeepMind Control Suite and Robotic Manipulation
tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00796v1
- Authors: Jinwen Wang, Youfang Lin, Xiaobo Hu, Qian Xu, Shuo Wang, Zhuo Chen, Kai Lv
- Published: 2026-07-01T11:26:25Z
- Age days: 4

</details>
