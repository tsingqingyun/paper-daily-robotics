---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13394v1"
published: "2026-06-11T14:25:09Z"
age_days: 1
score: 28
created: 2026-06-13
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# GeoHAT: Geometry-Adaptive Hybrid Action Transformer for Mobile Manipulation

> [!summary] 一句话结论（基于摘要）
> Experiments on the ManiSkill-HAB simulation benchmark demonstrate that GeoHAT achieves a 79.3% mean success rate, surpassing the strongest baseline by 23.7%.

## 关键点

- **问题**：Whole-body mobile manipulation requires coordinating mobile base and manipulator under shifting viewpoints, posing challenges in geometric perception and action generation.
- **创新点 / 方法**：We present GeoHAT, an end-to-end diffusion-based framework built on a simple principle: geometry should be injected only where reliable and attended to only where needed.
- **证据**：Experiments on the ManiSkill-HAB simulation benchmark demonstrate that GeoHAT achieves a 79.3% mean success rate, surpassing the strongest baseline by 23.7%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Whole-body mobile manipulation requires coordinating mobile base and manipulator under
shifting viewpoints, posing challenges in geometric perception and action generation.
Current policies either rely on 2D features or sparse 3D representations that lack dense
spatial structure, and typically encode arm and base within one action vector that
ignores their distinct control demands. Moreover, existing dense fusion strategies risk
corrupting pretrained representations under noisy depth while incurring heavy
computational overhead. We present GeoHAT, an end-to-end diffusion-based framework built
on a simple principle: geometry should be injected only where reliable and attended to
only where needed. GeoHAT employs a lightweight Fourier spatial encoder that maps dense
per-pixel 3D coordinates into geometric tokens without an additional 3D vision backbone.
These tokens are then selectively injected into vision foundation model features through
per-token gated fusion modulated by depth validity, preserving the semantic prior while
enriching spatial understanding. For action generation, a Hybrid Whole-Body Action
Decoder decomposes arm and base into distinct subspaces and lets each action modality
attend to its task-relevant visual context through sparse cross-attention, while causal
temporal modeling captures intra-timestep coordination and inter-timestep dependencies.
Experiments on the ManiSkill-HAB simulation benchmark demonstrate that GeoHAT achieves a
79.3% mean success rate, surpassing the strongest baseline by 23.7%. Furthermore, real-
world experiments on diverse tasks also confirm consistent improvements over all
baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13394v1
- Authors: Xiangyu Zhu, Renjun Wu, Luzhou Ge, Jinyan Liu, Xuesong Li
- Published: 2026-06-11T14:25:09Z
- Age days: 1

</details>
