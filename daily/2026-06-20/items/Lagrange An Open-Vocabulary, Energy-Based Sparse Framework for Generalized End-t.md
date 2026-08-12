---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20274v1"
published: "2026-06-18T14:18:01Z"
age_days: 1
score: 31
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving

> [!summary] 一句话结论（基于摘要）
> To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving framework based on Masked Latent Fields (MLF).

## 关键点

- **问题**：Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning.
- **创新点 / 方法**：To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving framework based on Masked Latent Fields (MLF).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling end-to-end autonomous driving to complex, open-world environments requires
perceptual models that generalize to anomalous scenarios and planners that produce
kinematically valid trajectories. Existing paradigms face a distinct dichotomy between
representational efficiency and generalization capacity. Dense models (e.g., occupancy
networks), while geometrically robust, incur critical computational bottlenecks and
struggle with high-level semantic reasoning. Conversely, sparse, query-based planners
are efficient but reliant on closed-set definitions, rendering them vulnerable to out-
of-distribution (OOD) events. Although recent Vision-Language-Action (VLA) models offer
open-vocabulary reasoning, their autoregressive, discrete token generation fundamentally
conflicts with the continuous, high-frequency control requirements of vehicle dynamics.
To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving
framework based on Masked Latent Fields (MLF). Rather than relying on dense volumetric
reconstructions or closed-set query mechanisms, Lagrange exploits Vision-Language Models
(VLMs) to encode class-agnostic object proposals into continuous semantic visual tokens.
We introduce an intent-driven masked cross-attention module that temporally filters
irrelevant entities, decoding the attended tokens into an implicit continuous energy
field defined over spatial coordinates. By framing decision-making as a Lagrangian
action minimization problem spanning this energy field, we enforce strict compliance
with vehicle kinematics while executing collision avoidance. Extensive offline
evaluations on both standard (nuScenes) and long-tail (CODA) benchmarks demonstrate that
Lagrange establishes a promising framework for robust, interpretable, and kinematically
feasible open-world autonomy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20274v1
- Authors: Shihao Ji, HongXi Li, Zihui Song, Mingyu Li
- Published: 2026-06-18T14:18:01Z
- Age days: 1

</details>
