---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07100v1"
published: "2026-06-05T09:51:25Z"
age_days: 2
score: 41
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LARA: Latent Action Representation Alignment for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> We demonstrate LARA versatility and effectiveness for pre-training, post- training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real- world rob…

## 关键点

- **问题**：Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets.
- **创新点 / 方法**：To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment.
- **证据**：We demonstrate LARA versatility and effectiveness for pre-training, post- training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real- world robotic manipulation benchmarks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual-language action (VLA) models enable robots to predict actions directly from
observations and language instructions, but their performance depends on large-scale,
high-quality data and is limited by the scarcity of real-world robot action datasets. To
facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models
(LAM) learn latent action representations from visual dynamics to provide additional
supervision for VLA learning. However, LAM and VLA are typically trained separately,
leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM
representations. To address these issues, we propose Latent Action Representation
Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via
representation alignment. This enables reciprocal benefits where LAMs learn with action
trajectories to avoid spurious visual changes, while VLAs are regularized by forward
dynamics learned within LAMs to reduce hallucinations of functionally ineffective
trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-
training enhancement of pre-trained VLA models, and LAM refinement, achieving an average
of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-
world robotic manipulation benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07100v1
- Authors: Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, Siyuan Huang
- Published: 2026-06-05T09:51:25Z
- Age days: 2

</details>
