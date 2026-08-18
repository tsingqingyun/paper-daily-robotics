---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15816v1"
published: "2026-08-16T15:46:11Z"
age_days: 1
score: 39
created: 2026-08-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ViTaR: Visuo-Tactile Residual Adaptation for Foundation VLA Manipulation

> [!summary] 一句话结论（基于摘要）
> On the UniVTAC benchmark spanning seven contact-rich tasks, ViTaR achieves 61.3% average success, a 30.6 percentage-point improvement over its frozen VLA base that also surpasses purpose-built tactile baselines.

## 关键点

- **问题**：As Vision-Language-Action (VLA) models scale toward real-world deployment, contact-rich manipulation exposes a critical blind spot: these policies encode broad visual-semantic priors yet remain unaware of local contact events, producing identical actions whether contact is established, lost, or destabilized.
- **创新点 / 方法**：We introduce ViTaR, which reframes tactile feedback from an action-generating perceptual input to an execution modulator that selects and scales bounded residual corrections atop a frozen VLA, preserving pretrained capabilities by construction.
- **证据**：On the UniVTAC benchmark spanning seven contact-rich tasks, ViTaR achieves 61.3% average success, a 30.6 percentage-point improvement over its frozen VLA base that also surpasses purpose-built tactile baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/ViTaR Visuo-Tactile Residual Adaptation for Foundation VLA Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As Vision-Language-Action (VLA) models scale toward real-world deployment, contact-rich manipulation exposes a critical blind spot: these policies encode broad visual-semantic priors yet remain unaware of local contact events, producing identical actions whether contact is established, lost, or destabilized. Existing remedies either modify VLA internals, risking catastrophic forgetting, or demand online reinforcement under near-failure contact conditions. Both grant tactile unbounded influence over action generation, conflicting with the priors that make VLAs generalizable. We introduce ViTaR, which reframes tactile feedback from an action-generating perceptual input to an execution modulator that selects and scales bounded residual corrections atop a frozen VLA, preserving pretrained capabilities by construction. ViTaR decomposes adaptation into two stages: Effect-Guided Modeling determines whether and which correction is locally justified via outcome-grounded preference evidence, and Residual Action Modulation converts this evidence into a residual choice with continuously scaled gain from real-time visuotactile observations. On the UniVTAC benchmark spanning seven contact-rich tasks, ViTaR achieves 61.3% average success, a 30.6 percentage-point improvement over its frozen VLA base that also surpasses purpose-built tactile baselines. Physical-robot experiments confirm that bounded tactile modulation transfers to real sensor noise and dynamics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15816v1
- Authors: Yi Wang, Renjun Wu, Jinyan Liu, Xuesong Li
- Published: 2026-08-16T15:46:11Z
- Age days: 1

</details>
