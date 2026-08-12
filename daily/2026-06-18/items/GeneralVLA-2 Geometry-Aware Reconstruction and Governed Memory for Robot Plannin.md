---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17480v1"
published: "2026-06-16T03:45:24Z"
age_days: 1
score: 33
created: 2026-06-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning

> [!summary] 一句话结论（基于摘要）
> Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% a…

## 关键点

- **问题**：GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end- effector paths, but two bottlenecks remain.
- **创新点 / 方法**：To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance.
- **证据**：Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist vision-language-action systems need object-centric 3D evidence and reusable
manipulation experience to plan reliable robot trajectories. GeneralVLA provides a
hierarchical interface for converting language and RGB-D observations into 3D end-
effector paths, but two bottlenecks remain. First, monocular SAM3D-style object
reconstruction can hallucinate pose and unseen geometry, while manipulation benefits
from stable object shape when calibrated multi-view observations are available. Second,
the original KnowledgeBank mainly retrieves semantically similar snippets and appends
new knowledge, which makes it difficult to control memory quality, conflicts,
confidence, and geometric relevance. To address the first challenge, we introduce
GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies
external geometry cues with input-view masks, applies soft visual-hull support, performs
axis-wise refinement, and fuses only geometry while preserving appearance. To address
the second challenge, we upgrade KnowledgeBank into a governed long-term memory system
with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together
with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on
GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D
improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while
increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over
ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while
reducing AS by 4.95% and 5.65%, respectively. Code:
https://github.com/AIGeeksGroup/GeneralVLA-2. Website:
https://aigeeksgroup.github.io/GeneralVLA-2.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17480v1
- Authors: Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi, Hao Tang
- Published: 2026-06-16T03:45:24Z
- Age days: 1

</details>
