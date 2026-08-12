---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14280v1"
published: "2026-07-15T18:39:13Z"
age_days: 2
score: 33
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# DiMaS: Distribution Matching for Steering Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Representation steering is a well- established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs.

## 关键点

- **问题**：Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations.
- **创新点 / 方法**：We propose DiMaS, a Distribution-Matching Steering strategy tailored to flow-matching VLAs, which transports between representation distributions rather than shifting along a fixed direction, and show that it effectively controls behavior across two state-of-the-art VLAs.
- **证据**：Representation steering is a well- established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/DiMaS Distribution Matching for Steering Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-matching-based vision-language-action (VLA) models have emerged as powerful
policies for robotic manipulation, yet a critical capability remains underexplored:
fine-grained behavioral control, the ability to govern how a robot performs a task by
intervening on its internal representations. Representation steering is a well-
established interpretability tool for language and vision-language models, where
behavioral features are typically encoded as linear directions, but we show that these
classic methods fall short in VLAs. We propose DiMaS, a Distribution-Matching Steering
strategy tailored to flow-matching VLAs, which transports between representation
distributions rather than shifting along a fixed direction, and show that it effectively
controls behavior across two state-of-the-art VLAs. We further examine the
generalizability of this strategy as the tasks it is learned from and evaluated on grow
increasingly dissimilar, characterizing where behavioral control transfers and where it
weakens. Finally, through an analysis of the representation structure of the action
expert, we explain why classical linear steering falls short in the visuomotor setting:
behavioral features are linearly decodable but not linearly steerable, which motivates
the distribution-matching design of DiMaS. Our code is publicly available at
https://github.com/pegah-kh/dimas, with additional results and videos at https://pegah-
kh.github.io/dimas/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14280v1
- Authors: Pegah Khayatan, Sara Meziane, Jayneel Parekh, Matthieu Cord
- Published: 2026-07-15T18:39:13Z
- Age days: 2

</details>
