---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16146v1"
published: "2026-07-17T17:27:08Z"
age_days: 2
score: 28
created: 2026-07-20
concepts: ["具身智能评测与基准"]
---

# VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds

> [!summary] 一句话结论（基于摘要）
> Evaluated on a new benchmark of 100 real-world objects, VTLoc improves single-touch contact localization by reducing local-to-global correspondence ambiguity.

## 关键点

- **问题**：Integrating these modalities for contact localization, i.e., predicting the location of touch on an object's surface, poses significant challenges due to the need for accurate spatial alignment between tactile data and visual geometry.
- **创新点 / 方法**：To address this challenge, we propose VTLoc, a novel visual-tactile framework that localizes contact points from tactile readings using a 3D point cloud as visual input.
- **证据**：Evaluated on a new benchmark of 100 real-world objects, VTLoc improves single-touch contact localization by reducing local-to-global correspondence ambiguity.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision and touch are complementary modalities essential for robotic perception and
manipulation. While vision provides global object context, touch offers precise local
information at contact points. Integrating these modalities for contact localization,
i.e., predicting the location of touch on an object's surface, poses significant
challenges due to the need for accurate spatial alignment between tactile data and
visual geometry. To address this challenge, we propose VTLoc, a novel visual-tactile
framework that localizes contact points from tactile readings using a 3D point cloud as
visual input. VTLoc introduces two key components: a geometric multi-modal alignment
module, which reconstructs a pseudo-point cloud from fused visual-tactile features and
aligns it with the visual point cloud to enforce spatial consistencies across
modalities; and an iterative localizing updater, which iteratively refines the predicted
contact location using fused visual-tactile features. Evaluated on a new benchmark of
100 real-world objects, VTLoc improves single-touch contact localization by reducing
local-to-global correspondence ambiguity.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16146v1
- Authors: Zhiyuan Wu, Zhuo Chen, Shan Luo
- Published: 2026-07-17T17:27:08Z
- Age days: 2

</details>
