---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23641v1"
published: "2026-06-22T17:30:29Z"
age_days: 1
score: 34
created: 2026-06-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Flatness Preserves Instruction Following in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Specifically, we demonstrate that simply applying sharpness-aware minimization during VLA finetuning significantly improves instruction following by over 60% across multiple simulation and real-world benchmarks without additional data, architectural modificat…

## 关键点

- **问题**：Vision-language-action (VLA) models have the potential for open-world generalization by leveraging pretrained vision-language representations, yet downstream finetuning on limited robot data often degrades these representations, leading to brittle policies that ignore language instructions in favor of visual shortcuts…
- **创新点 / 方法**：We propose to address this directly through flatness-preserving optimization while finetuning on the exact same data, where learning a flatter landscape results in a model more robust to perturbations in the weight space.
- **证据**：Specifically, we demonstrate that simply applying sharpness-aware minimization during VLA finetuning significantly improves instruction following by over 60% across multiple simulation and real-world benchmarks without additional data, architectural modification, or retraining.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have the potential for open-world generalization by
leveraging pretrained vision-language representations, yet downstream finetuning on
limited robot data often degrades these representations, leading to brittle policies
that ignore language instructions in favor of visual shortcuts, a failure mode we term
instruction blindness. We hypothesize that standard finetuning with limited data applies
gradients to a sparse set of points, which manifests as a sharp loss landscape with
high-curvature minima. We propose to address this directly through flatness-preserving
optimization while finetuning on the exact same data, where learning a flatter landscape
results in a model more robust to perturbations in the weight space. Specifically, we
demonstrate that simply applying sharpness-aware minimization during VLA finetuning
significantly improves instruction following by over 60% across multiple simulation and
real-world benchmarks without additional data, architectural modification, or
retraining. We further analyze the effect of selective sharpness, quantify its effects,
and show that our approach is complementary to existing guidance techniques. Project
page can be found at https://haochenz11.github.io/papers/flatness-vla/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23641v1
- Authors: Haochen Zhang, Yonatan Bisk
- Published: 2026-06-22T17:30:29Z
- Age days: 1

</details>
