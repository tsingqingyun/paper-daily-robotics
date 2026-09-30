---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09925v1"
published: "2026-09-09T09:16:49Z"
age_days: 1
score: 29
created: 2026-09-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> Relative to the same-source base, TFGCA improves in-distribution LIBERO by +1.5 on average, the OOD LIBERO-Plus by +6.3, the randomized average under RoboTwin domain randomization by +28.5, and the overall success rate on three real-robot AgiBot A2 tasks by +…

## 问题

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass.

## 创新点或方法

We introduce Time-Frequency Geometric Cross-Attention (TFGCA), a drop-in module repairing both blind spots.

## 证据

Relative to the same-source base, TFGCA improves in-distribution LIBERO by +1.5 on average, the OOD LIBERO-Plus by +6.3, the randomized average under RoboTwin domain randomization by +28.5, and the overall success rate on three real-robot AgiBot A2 tasks by +11.67 points, with larger gains out of distribution.


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：多模态基础模型 视觉语言动作模型 VLA Sim2Real 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entangles them. Second, cross-phase geometry: motions of different phases (reach, contact, grasp adjustment, settling) unfold along very different, near-orthogonal directions in representation space, yet are tightly related for the task and arise across the time axis. Dot-product attention scores alignment by an inner product, so it favors aligned tokens and is least sensitive near orthogonality, leaving such relationships for the network to recover through a detour. We introduce Time-Frequency Geometric Cross-Attention (TFGCA), a drop-in module repairing both blind spots. TFGCA uses a per-dimension learnable stationary wavelet transform to decompose the action chunk into time-frequency tokens, and each time token retrieves information from them via a cross-attention that fuses the dot product (similarity) with the wedge-product magnitude (sensitive to near-orthogonality) through a learnable weight. A zero-initialized residual reproduces the base behavior at initialization, so it can be dropped onto a pretrained VLA and fine-tuned jointly. Relative to the same-source base, TFGCA improves in-distribution LIBERO by +1.5 on average, the OOD LIBERO-Plus by +6.3, the randomized average under RoboTwin domain randomization by +28.5, and the overall success rate on three real-robot AgiBot A2 tasks by +11.67 points, with larger gains out of distribution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09925v1
- Authors: Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang, Shanmin Pang
- Published: 2026-09-09T09:16:49Z
- Age days: 1

</details>
