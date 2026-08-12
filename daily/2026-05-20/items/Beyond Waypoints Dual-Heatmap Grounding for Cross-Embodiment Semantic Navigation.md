---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19420v1"
published: "2026-05-19T06:12:59Z"
age_days: 0
score: 29
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Beyond Waypoints: Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that our framework achieves state-of-the-art performance among comparable 8B baselines.

## 关键点

- **问题**：Grounding open-ended semantic instructions into physically executable local goals is a fundamental challenge in human-robot interaction.
- **创新点 / 方法**：To bridge the gap between abstract semantic intent and physical reachability, we propose a unified Vision-Language framework that abandons single-point regression in favor of a Dual-Heatmap representation.
- **证据**：Extensive experiments demonstrate that our framework achieves state-of-the-art performance among comparable 8B baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/Beyond Waypoints Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Grounding open-ended semantic instructions into physically executable local goals is a
fundamental challenge in human-robot interaction. While existing navigation frameworks
often regress deterministic waypoints, this rigid formulation collapses spatial
uncertainty and frequently targets non-traversable object centers, leading to severe
execution failures. In this work, we focus on the practical setting of in-FOV semantic
navigation, where a robot receives concise, interleaved multimodal (text and image)
prompts. To bridge the gap between abstract semantic intent and physical reachability,
we propose a unified Vision-Language framework that abandons single-point regression in
favor of a Dual-Heatmap representation. Our framework predicts a navigation affordance
heatmap that captures continuous reachable regions, coupled with a facing heatmap for
orientation constraints. These dense outputs inherently function as a differentiable
semantic potential field, integrating seamlessly with downstream local planners. To
support this paradigm, we build a fully automated, foundation-model-assisted synthetic
data pipeline and establish a comprehensive simulation benchmark. Extensive experiments
demonstrate that our framework achieves state-of-the-art performance among comparable 8B
baselines. Crucially, a feature-fusion study and simulation studies across diverse robot
embodiments (Jetbot, H1, Aliengo) reveal that explicit heatmap prediction drastically
improves the Affordance Rate (AR). By placing targets reliably in executable free space,
our framework effectively mitigates the brittleness of point regression, offering a
transferable path toward safe cross-embodiment semantic navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19420v1
- Authors: Kaijie Yun, Yue Chen
- Published: 2026-05-19T06:12:59Z
- Age days: 0

</details>
