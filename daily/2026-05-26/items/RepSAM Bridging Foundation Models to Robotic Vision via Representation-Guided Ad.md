---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25495v1"
published: "2026-05-25T06:56:42Z"
age_days: 1
score: 28
created: 2026-05-26
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation

> [!summary] 一句话结论（基于摘要）
> Experimental evaluation across six benchmarks and robotic manipulation tasks demonstrates that RepSAM achieves 97.9% of full fine-tuning performance (89.0% vs.

## 关键点

- **问题**：Robotic perception in unstructured environments remains challenging despite the zero- shot capabilities of foundation models such as SAM.
- **创新点 / 方法**：Based on this observation, we propose RepSAM, a representation-guided parameter-efficient fine-tuning (PEFT) framework for adapting foundation models to robotic vision.
- **证据**：Experimental evaluation across six benchmarks and robotic manipulation tasks demonstrates that RepSAM achieves 97.9% of full fine-tuning performance (89.0% vs.
- **局限**：Robotic perception in unstructured environments remains challenging despite the zero- shot capabilities of foundation models such as SAM.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic perception in unstructured environments remains challenging despite the zero-
shot capabilities of foundation models such as SAM. This work attributes performance
degradation to non-uniform representation shifts across transformer layers: shallow
layers exhibit substantial domain gaps (CKA 0.7). Based on this observation, we propose
RepSAM, a representation-guided parameter-efficient fine-tuning (PEFT) framework for
adapting foundation models to robotic vision. RepSAM employs a theoretically grounded
CKA-guided rank allocation strategy combined with a multi-modal fusion module for robust
handling of challenging robotic scenarios, including transparent objects and cluttered
scenes. Experimental evaluation across six benchmarks and robotic manipulation tasks
demonstrates that RepSAM achieves 97.9% of full fine-tuning performance (89.0% vs. 90.9%
mIoU) while reducing trainable parameters by 158x (from 632M to 4.0M). RepSAM
outperforms DoRA by 7.9% mIoU with just 4 hours of training on a single A100 GPU (a 96x
reduction from full fine-tuning, which takes 384 GPU-hours). These improvements are
statistically significant (p < 0.01) and translate to a 12.0% absolute improvement in
robotic manipulation success rates over the LoRA (RGB) baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25495v1
- Authors: Wenhui Chu
- Published: 2026-05-25T06:56:42Z
- Age days: 1

</details>
