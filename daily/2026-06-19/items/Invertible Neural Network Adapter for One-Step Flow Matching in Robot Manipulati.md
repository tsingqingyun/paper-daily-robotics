---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19194v1"
published: "2026-06-17T15:35:27Z"
age_days: 1
score: 41
created: 2026-06-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> Compared with conventional iterative flow- matching policies, the proposed framework substantially reduces inference complexity while maintaining strong action prediction accuracy and stability.

## 关键点

- **问题**：This paper presents an invertible neural network adapter for general robotic manipulation, designed to generate precise high-dimensional actions conditioned on multimodal observations, including visual, linguistic, and proprioceptive inputs, through a one-step denoising process.
- **创新点 / 方法**：Built upon a flow-matching formulation, the proposed adapter effectively constrains the action generation trajectory within an invertible latent space, thereby enabling efficient and high-quality dexterous action synthesis with only a single inference step.
- **证据**：Compared with conventional iterative flow- matching policies, the proposed framework substantially reduces inference complexity while maintaining strong action prediction accuracy and stability.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper presents an invertible neural network adapter for general robotic
manipulation, designed to generate precise high-dimensional actions conditioned on
multimodal observations, including visual, linguistic, and proprioceptive inputs,
through a one-step denoising process. Built upon a flow-matching formulation, the
proposed adapter effectively constrains the action generation trajectory within an
invertible latent space, thereby enabling efficient and high-quality dexterous action
synthesis with only a single inference step. Compared with conventional iterative flow-
matching policies, the proposed framework substantially reduces inference complexity
while maintaining strong action prediction accuracy and stability. Extensive experiments
are conducted across a diverse set of simulation benchmarks and real-world robotic
platforms to evaluate the effectiveness of the proposed method. Across simulation
benchmarks, the proposed adapter consistently demonstrates superior or near state-of-
the-art performance on a wide range of manipulation tasks. Furthermore, real-world
experiments reveal a significant improvement in inference efficiency for vision-
language-action (VLA) models, reducing the average inference latency from 110 ms to 61
ms while maintaining strong task performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19194v1
- Authors: Yu Zhang, Kangyi Ji, Yongxiang Zou, Rongtao Xu, Feng Zheng, Long Cheng
- Published: 2026-06-17T15:35:27Z
- Age days: 1

</details>
