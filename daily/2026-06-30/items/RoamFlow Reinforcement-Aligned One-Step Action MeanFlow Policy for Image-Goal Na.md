---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29934v1"
published: "2026-06-29T08:10:43Z"
age_days: 1
score: 34
created: 2026-06-30
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# RoamFlow: Reinforcement-Aligned One-Step Action MeanFlow Policy for Image-Goal Navigation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments in both Habitat simulation and real-world robotic platforms demonstrate that RoamFlow achieves efficient inference while maintaining strong navigation performance under real- time constraints.

## 关键点

- **问题**：Image-goal navigation is a key challenge in embodied robotics, where an agent must reach a target specified solely by a goal image.
- **创新点 / 方法**：To address this limitation, we propose RoamFlow, a generative navigation framework that leverages MeanFlow to predict the average velocity field for trajectory synthesis, enabling efficient few-step generation and reducing inference latency.
- **证据**：Extensive experiments in both Habitat simulation and real-world robotic platforms demonstrate that RoamFlow achieves efficient inference while maintaining strong navigation performance under real- time constraints.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Image-goal navigation is a key challenge in embodied robotics, where an agent must reach
a target specified solely by a goal image. While existing reinforcement learning
approaches map perceptual observations directly to actions, they struggle to model long-
horizon dependencies, often leading to suboptimal trajectories. To address this
limitation, we propose RoamFlow, a generative navigation framework that leverages
MeanFlow to predict the average velocity field for trajectory synthesis, enabling
efficient few-step generation and reducing inference latency. We further adopt a two-
stage training strategy that combines expert imitation for stable initialization with
reinforcement learning for task-specific policy refinement. Extensive experiments in
both Habitat simulation and real-world robotic platforms demonstrate that RoamFlow
achieves efficient inference while maintaining strong navigation performance under real-
time constraints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29934v1
- Authors: Zixuan Zhang, Yuqi Chen, Junjie Gao, Siyuan Song, Yongzhou Pan, Beichen Wang, Mir Feroskhan
- Published: 2026-06-29T08:10:43Z
- Age days: 1

</details>
