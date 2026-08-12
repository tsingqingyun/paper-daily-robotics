---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12356v1"
published: "2026-07-14T05:08:50Z"
age_days: 2
score: 35
created: 2026-07-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA- Adapter baseline on challenging out-of-distribution tasks.

## 关键点

- **问题**：However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints.
- **创新点 / 方法**：In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning.
- **证据**：Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA- Adapter baseline on challenging out-of-distribution tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/VistaVLA Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for
robotic manipulation by mapping language instructions and 2D visual inputs directly to
actions. However, these models lack an explicit, scene-level 3D representation, limiting
their ability to reason over spatial layouts and geometric constraints. While recent
efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve
geometric awareness, they primarily capture low-level structures and lack high-level
semantic grounding in 3D space. In human cognition, interaction with the physical world
relies on a 3D semantic cognitive map - an internal mental model that integrates spatial
layouts with semantic context to enable persistent, viewpoint-invariant reasoning. In
light of this, we present VistaVLA, a novel two-stage framework that constructs a
geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives
and grounds it as compact context tokens for VLA policy learning. Specifically, VistaVLA
lifts multi-view vision-language features into 3D Gaussian primitives, forming geometry-
anchored semantic tokens that align view-consistent spatial grounding with 2D visual
feature spaces. To make this 3D representation computationally tractable for effective
VLA control, we introduce Merge-then-Query (MtQ), a token summarization mechanism. MtQ
compresses dense Gaussian primitives into a highly compact set of spatially informative
tokens, achieving a 99% token reduction while preserving action-relevant 3D layouts and
semantic context. Extensive evaluations in both simulated and real-world environments
demonstrate the effectiveness of VistaVLA. Notably, in real-world scenarios, VistaVLA
improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA-
Adapter baseline on challenging out-of-distribution tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12356v1
- Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
- Published: 2026-07-14T05:08:50Z
- Age days: 2

</details>
