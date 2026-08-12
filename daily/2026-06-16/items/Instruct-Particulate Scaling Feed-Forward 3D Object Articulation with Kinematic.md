---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14699v1"
published: "2026-06-12T17:59:36Z"
age_days: 3
score: 24
created: 2026-06-16
concepts: ["多模态基础模型", "世界模型"]
---

# Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control

> [!summary] 一句话结论（基于摘要）
> Experiments show that our model generalizes better across categories and to AI-generated meshes, enabling articulated asset reconstruction from real-world images via image-to-3D models.

## 关键点

- **问题**：Recent neural networks can estimate the articulated structure of 3D objects, but their generalization remains limited by the scarcity of annotated data for this task.
- **创新点 / 方法**：To address this gap, we introduce Instruct-Particulate, a model that takes a 3D mesh together with a target kinematic specification, including part descriptions, connectivity, joint types, and optional point prompts, and predicts the corresponding kinematic part segmentation and joint motion parameters.
- **证据**：Experiments show that our model generalizes better across categories and to AI-generated meshes, enabling articulated asset reconstruction from real-world images via image-to-3D models.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reconstructing articulated 3D objects is important for animation, gaming, and robotic
simulations. Recent neural networks can estimate the articulated structure of 3D
objects, but their generalization remains limited by the scarcity of annotated data for
this task. To address this gap, we introduce Instruct-Particulate, a model that takes a
3D mesh together with a target kinematic specification, including part descriptions,
connectivity, joint types, and optional point prompts, and predicts the corresponding
kinematic part segmentation and joint motion parameters. The kinematic specification
disambiguates the task and allows the model to target annotations of different
granularity, thereby making it possible to use more abundant heterogeneous training
data. At test time, the kinematic specification can be obtained automatically from
large-scale vision-language models, so the model can be applied to any input mesh. To
train our model at scale, we construct a heterogeneous dataset of more than 150,000
articulated 3D objects, extending existing publicly available collections with data
obtained by partially labelling other 3D models (monolithic or already decomposed into
parts) with kinematic labels by means of vision-language models. Experiments show that
our model generalizes better across categories and to AI-generated meshes, enabling
articulated asset reconstruction from real-world images via image-to-3D models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14699v1
- Authors: Ruining Li, Yuxin Yao, Matt Zhou, Chuanxia Zheng, Christian Rupprecht, Joan Lasenby, Shangzhe Wu, Andrea Vedaldi
- Published: 2026-06-12T17:59:36Z
- Age days: 3

</details>
