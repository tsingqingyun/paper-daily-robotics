---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10405v1"
published: "2026-09-09T16:24:40Z"
age_days: 1
score: 29
created: 2026-09-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Frequency-Conditioned Flow Matching for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance, including a 9.3-point gain on LIBERO-Plus, and further demonstrates its effectiveness on six real-robot tasks.

## 问题

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions.

## 创新点或方法

We introduce \emph{FreqFM}, a frequency-conditioned Flow Matching framework for VLA models.

## 证据

Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance, including a 9.3-point gain on LIBERO-Plus, and further demonstrates its effectiveness on six real-robot tasks.


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Frequency-Conditioned Flow Matching for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot actions are temporally correlated trajectories whose frequency components encode motion at different scales with highly non-uniform energy distributions. Yet Flow Matching--based vision-language-action (VLA) models typically generate actions in temporal coordinates, without explicitly modeling or systematically leveraging this frequency heterogeneity. We introduce \emph{FreqFM}, a frequency-conditioned Flow Matching framework for VLA models. It raises action frequency from an implicit trajectory property to an explicit conditioning dimension that spans the entire generation pipeline. Concretely, in DCT frequency coordinates, FreqFM constructs a spectrum-matched source distribution, adaptively balances the objective across frequencies, and constrains per-frequency guidance residuals using the corresponding reference transport scales. FreqFM integrates into existing Flow Matching action experts without changing the VLA backbone. Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance, including a 9.3-point gain on LIBERO-Plus, and further demonstrates its effectiveness on six real-robot tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10405v1
- Authors: Haochen Niu, Shengye Dong, Hao Liu, Peiwen Lin, Wang Chuang
- Published: 2026-09-09T16:24:40Z
- Age days: 1

</details>
