---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17046v1"
published: "2026-06-15T17:58:03Z"
age_days: 2
score: 52
created: 2026-06-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Geometric Action Model for Robot Policy Learning

> [!summary] 一句话结论（基于摘要）
> We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding.

## 关键点

- **问题**：The predicted future tokens are then routed through the remaining GFM blocks for feature propagation and decoding, allowing a single backbone to produce both future geometry and actions.
- **创新点 / 方法**：We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：52
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-18/Geometric Action Model for Robot Policy Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies must follow user instructions while reasoning about how
objects, cameras, and robot actions interact in the 3D physical world. Recent vision-
language-action models (VLAs) and video world-action models (WAMs) inherit strong
semantic or temporal priors from large-scale foundation models, but they still operate
primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D
geometry required for contact-rich manipulation. We propose the Geometric Action Model
(GAM), a language-conditioned manipulation policy that directly repurposes a pretrained
geometric foundation model (GFM) as a shared substrate for perception, temporal
prediction, and action decoding. GAM splits the GFM at an intermediate layer: the
shallow layers serve as an observation encoder, and a causal future predictor inserted
at the split layer forecasts future latent tokens conditioned on language,
proprioception, and action history. The predicted future tokens are then routed through
the remaining GFM blocks for feature propagation and decoding, allowing a single
backbone to produce both future geometry and actions. This design equips the GFM with
language-conditioned temporal world modeling through minimal architectural modification
while preserving its rich geometric priors. Across a broad suite of simulation and real-
robot manipulation benchmarks, GAM is more accurate, more robust, faster, and lighter
than current foundation-model-scale baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17046v1
- Authors: Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
- Published: 2026-06-15T17:58:03Z
- Age days: 2

</details>
