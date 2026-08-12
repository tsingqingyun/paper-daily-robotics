---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17778v1"
published: "2026-07-20T10:09:12Z"
age_days: 1
score: 31
created: 2026-07-22
concepts: ["具身智能评测与基准"]
---

# CDIS: Cross-Dimensional Class-Agnostic 3D Instance Segmentation via 2D Mask Tracking and 3D-2D Projection Merging

> [!summary] 一句话结论（基于摘要）
> Experiments on benchmark datasets demonstrate that CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods, while remaining efficient and scalable to diverse real-world environments.

## 关键点

- **问题**：Experiments on benchmark datasets demonstrate that CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods, while remaining efficient and scalable to diverse real-world environments.
- **创新点 / 方法**：We introduce Cross-Dimensional Class-Agnostic 3D Instance Segmentation (CDIS), a zero-shot framework that explicitly tracks 2D instance masks across frames and associates them with 3D superpoints, creating a feedback loop between 2D and 3D.
- **证据**：Experiments on benchmark datasets demonstrate that CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods, while remaining efficient and scalable to diverse real-world environments.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Class-agnostic 3D instance segmentation is critical for robotic systems operating in
unknown environments, enabling perception of previously unseen objects for reliable
manipulation and navigation. Existing approaches typically project per-frame 2D instance
masks into 3D and merge them, which often breaks object identities across time and
yields fragmented 3D instances. We introduce Cross-Dimensional Class-Agnostic 3D
Instance Segmentation (CDIS), a zero-shot framework that explicitly tracks 2D instance
masks across frames and associates them with 3D superpoints, creating a feedback loop
between 2D and 3D. This cross-dimensional reasoning links temporally stable 2D tracks
with spatially coherent 3D regions, producing globally consistent 3D instance labels
without any 3D-specific training. Experiments on benchmark datasets demonstrate that
CDIS achieves higher accuracy and consistency than state-of-the-art zero-shot methods,
while remaining efficient and scalable to diverse real-world environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17778v1
- Authors: Juno Kim, Hye-Jung Yoon, Yesol Park, Byoung-Tak Zhang
- Published: 2026-07-20T10:09:12Z
- Age days: 1

</details>
