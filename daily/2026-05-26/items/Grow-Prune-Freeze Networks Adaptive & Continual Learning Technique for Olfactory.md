---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25170v1"
published: "2026-05-24T17:03:30Z"
age_days: 1
score: 35
created: 2026-05-26
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation

> [!summary] 一句话结论（基于摘要）
> Grounding GPFs in non-linear random matrix theory, we show that the work of Pennington & Worth (2017) can be extended from single hidden layers to n-layer continual-learning models, and that eigenvalue composition of network weights is preserved as successive…

## 关键点

- **问题**：We show that GPFs based on Expected SARSA achieve a 94% success rate on turbulent plume navigation - a partially observable, non-stationary task representative of the "big world" challenges that motivate adaptive learning in robotics - and provide supporting methodology for applying GPFs in other world models.
- **创新点 / 方法**：We introduce an adaptive framework called Grow-Prune-Freeze (GPF) networks that enable an agent to continually learn through growing, pruning, and freezing early layers of its policy in response to world complexity.
- **证据**：Grounding GPFs in non-linear random matrix theory, we show that the work of Pennington & Worth (2017) can be extended from single hidden layers to n-layer continual-learning models, and that eigenvalue composition of network weights is preserved as successive layers are added.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training data for olfaction is scattered through disparate, non-standardized datasets
that limit the ability to build representative world models. Olfactory navigation is a
highly dynamic and non-stationary task that benefits from real-time continual learning.
We introduce an adaptive framework called Grow-Prune-Freeze (GPF) networks that enable
an agent to continually learn through growing, pruning, and freezing early layers of its
policy in response to world complexity. Grounding GPFs in non-linear random matrix
theory, we show that the work of Pennington & Worth (2017) can be extended from single
hidden layers to n-layer continual-learning models, and that eigenvalue composition of
network weights is preserved as successive layers are added. We show that GPFs based on
Expected SARSA achieve a 94% success rate on turbulent plume navigation - a partially
observable, non-stationary task representative of the "big world" challenges that
motivate adaptive learning in robotics - and provide supporting methodology for applying
GPFs in other world models. Further experiments amount evidence that GPFs may generalize
well to other machine learning tasks such as reinforcement learning in Atari, image
classification, and autoregressive language models. We open source all code and data to
encourage improvements on and more research in olfactory robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25170v1
- Authors: Kordel K. France, Ovidiu Daescu
- Published: 2026-05-24T17:03:30Z
- Age days: 1

</details>
