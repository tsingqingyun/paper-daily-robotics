---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14698v1"
published: "2026-07-16T08:01:49Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color

> [!summary] 一句话结论（基于摘要）
> We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undef…

## 关键点

- **问题**：Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general- purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations.
- **创新点 / 方法**：We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals.
- **证据**：We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undefended baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-
purpose robot manipulation; however, their transition to real-world environments reveals
vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized
physical spotlight attack framework that exploits these vulnerabilities via targeted
illuminations, dropping baseline task success rates to zero without any access to model
internals. While adversarial training is the standard countermeasure, we identify a
critical and previously underestimated defensive pitfall: naive data augmentations
incorrectly condition VLA models to discard color as noise, collapsing their visual
perception into a purely shape-biased processor. We expose this degradation through a
diagnostic grayscale evaluation, in which the defended model maintains high success
rates on grayscale inputs, while its success rate on benign, color-dependent real-world
tasks drops to at most 47.5%, well below the undefended baseline. To address this, we
propose ChromaGuard, a chroma-preserving adversarial training method. On a physical
6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success
rates in benign and attacked color-dependent tasks, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14698v1
- Authors: Marino Watanabe, Takami Sato, Kentaro Yoshioka
- Published: 2026-07-16T08:01:49Z
- Age days: 1

</details>
