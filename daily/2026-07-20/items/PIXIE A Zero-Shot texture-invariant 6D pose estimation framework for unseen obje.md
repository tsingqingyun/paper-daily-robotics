---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16015v1"
published: "2026-07-17T14:48:43Z"
age_days: 2
score: 31
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects

> [!summary] 一句话结论（基于摘要）
> We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model.

## 关键点

- **问题**：6D pose estimation remains a key challenge in robotics and computer vision, particularly in industrial environments.
- **创新点 / 方法**：We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

6D pose estimation remains a key challenge in robotics and computer vision, particularly
in industrial environments. The deployment of currently available data-driven methods is
often limited by resource-intensive data pipelines, reliance on textured 3D models, and
sensitivity to geometric deviations caused by damages or assembly defects. We present
PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image
using only an untextured 3D model. Synthetic depth and normal maps are rendered from
sampled reference viewpoints and matched to the query image via a pretrained cross-
modality feature matcher. Matched keypoints are back-projected to obtain 2D--3D
correspondences for PnP-based pose estimation. Relying exclusively on geometry makes the
method inherently robust to lighting and texture variation, while correspondence
filtering handles geometric deviations between the model and physical object. We
evaluate on widely-used public benchmarks, reporting state-of-the-art results on
texture-less objects without object-specific training, and introduce a novel dataset
with assembly defects, texture variations, and occlusion to demonstrate real-world
applicability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16015v1
- Authors: Leon Jungemeyer, Alejandro Magaña, Gautham Mohan, Matthias Karl, Daniel Werdehausen
- Published: 2026-07-17T14:48:43Z
- Age days: 2

</details>
