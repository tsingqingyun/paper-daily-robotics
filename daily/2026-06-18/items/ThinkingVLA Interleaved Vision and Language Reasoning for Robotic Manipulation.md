---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17937v1"
published: "2026-06-16T13:45:17Z"
age_days: 1
score: 38
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on simulation and real-world benchmarks demonstrate that ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large gains on long-horizon manipulation tasks.

## 关键点

- **问题**：However, those methods lack a unified architecture for effective cross-modal reasoning and fail to explicitly include inverse reasoning ability based on the target state.
- **创新点 / 方法**：We propose \textbf{ThinkingVLA}, a generative model that realizes this decomposition within a unified Mixture-of-Transformers architecture.
- **证据**：Extensive experiments on simulation and real-world benchmarks demonstrate that ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large gains on long-horizon manipulation tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most Vision-Language-Action (VLA) models map observations directly to actions without
explicit reasoning, limiting their capacity for reasoning-intensive long-horizon tasks.
To address this, existing approaches adopt Chain-of-Thought (CoT) reasoning to enable
subgoal decomposition and spatial anticipation. However, those methods lack a unified
architecture for effective cross-modal reasoning and fail to explicitly include inverse
reasoning ability based on the target state. We argue that manipulation planning
naturally decomposes into prediction, anticipating the next visual state, and inverse
dynamics, inferring the actions to reach it. Bridging both requires a unified
autoregressive architecture that interleaves textual and visual reasoning in a single
generation process. We propose \textbf{ThinkingVLA}, a generative model that realizes
this decomposition within a unified Mixture-of-Transformers architecture. ThinkingVLA
consists of a forward CoT that identifies the immediate subgoal and guides the visual
forecasting; the predicted image then serves as the target state, grounding an inverse
CoT that reasons about spatial relationships and action intent based on the predicted
image; and the final action is generated conditioned on this full reasoning context.
Extensive experiments on simulation and real-world benchmarks demonstrate that
ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large
gains on long-horizon manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17937v1
- Authors: Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu, Xingyao Lin, Guojin Zhong, Ziyi Ye, Peng Wang, Zuxuan Wu, Yu-Gang Jiang
- Published: 2026-06-16T13:45:17Z
- Age days: 1

</details>
