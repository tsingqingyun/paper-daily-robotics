---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23138v1"
published: "2026-08-24T11:43:49Z"
age_days: 1
score: 43
created: 2026-08-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation

> [!summary] 一句话结论（基于摘要）
> Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging 72.9\% across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution.

## 关键点

- **问题**：Vision-language-action (VLA) models often expose spatial grounding through autoregressive text coordinates or opaque action tokens, creating brittle interfaces between multimodal reasoning and robot execution.
- **创新点 / 方法**：We present Pointing-VLA, a typed hidden-state spatial readout built on Embodied-R1.
- **证据**：Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging 72.9\% across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Pointing-VLA Typed Spatial Grounding Interfaces for Vision-Language-Action Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models often expose spatial grounding through autoregressive text coordinates or opaque action tokens, creating brittle interfaces between multimodal reasoning and robot execution. We present Pointing-VLA, a typed hidden-state spatial readout built on Embodied-R1. Geometry-specific heads predict normalized points, object-functional grounding (OFG) heatmaps, and visual trajectories without serializing geometry as text. For the evaluated Bridge/WidowX and physical pick-place deployments, an explicit execution contract assigns PICK to source-conditioned OFG and PLACE to Pointing, providing direct stage-aligned spatial targets. Pointing-VLA achieves SOTA performance on Bridge/WidowX, averaging 72.9\% across the evaluated four-task set without Bridge-specific finetuning under collision-enabled CuRobo execution. Pointing and OFG show complementary strengths across native and cross-dataset evaluations. The OFG/contact readout transfers to NORA-1.5, preserving or improving success while reducing recorded controller time by more than 20$\times$; typed heads are also 6.68--6.90$\times$ faster than Embodied-R1 text decoding on a shared external suite. When integrated as spatial guidance for a $π_{0.5}$ action policy, Pointing-VLA raises autonomous real-robot success from 52.7\% to 80.7\% across three visual contexts. These results establish typed spatial readouts as an efficient, inspectable interface between embodied reasoning and robot execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23138v1
- Authors: Xiwen Chen, Zelin Li, Zhiruo Zhou, Huiming Chen, Chenwei Wang, Xiaojun Zhu
- Published: 2026-08-24T11:43:49Z
- Age days: 1

</details>
