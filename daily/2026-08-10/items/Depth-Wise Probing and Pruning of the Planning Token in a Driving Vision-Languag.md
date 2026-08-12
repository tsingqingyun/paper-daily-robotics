---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07361v1"
published: "2026-08-07T16:02:34Z"
age_days: 2
score: 25
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Language-Action Model

> [!summary] 一句话结论（基于摘要）
> Our diagnostic shows that semantic intent is linearly decodable early: command-probe accuracy reaches 97.7\% after the first decoder layer, compared with 16.7\% chance.

## 关键点

- **问题**：These findings are limited to the evaluated ORION checkpoint and Bench2Drive setup.
- **创新点 / 方法**：Vision-language-action (VLA) models route driving decisions through a deep language model, but it is unclear how much of that depth the action itself requires.
- **证据**：Our diagnostic shows that semantic intent is linearly decodable early: command-probe accuracy reaches 97.7\% after the first decoder layer, compared with 16.7\% chance.
- **局限**：These findings are limited to the evaluated ORION checkpoint and Bench2Drive setup.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Languag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models route driving decisions through a deep language
model, but it is unclear how much of that depth the action itself requires. We study a
representative driving VLA whose entire plan is carried by a single planning token that
a generative planner decodes into a trajectory. Borrowing the planner as a trajectory-
space logit lens, we decode the planning token from every one of the 32 decoder layers
and measure two signals: the linear decodability of the navigation command and
trajectory compatibility with the frozen native planner. Our diagnostic shows that
semantic intent is linearly decodable early: command-probe accuracy reaches 97.7\% after
the first decoder layer, compared with 16.7\% chance. In contrast, compatibility with
the frozen native planner improves gradually across depth, with open-loop Avg-L2
reaching its minimum of 2.11\,m only at the final layer. Learned readouts from the first
layer recover much of this gap, indicating that planning information is already present
early but is not yet represented in the format expected by the deployed planner. Ranking
decoder layers by the angular deviation they induce in the planning token permits
removal of 8 of 32 layers within an approximately 5\% relative open-loop error increase
and yields a measured 1.33$\times$ decoder speedup. At the evaluated sample size, no
family-specific degradation is statistically resolved. These findings are limited to the
evaluated ORION checkpoint and Bench2Drive setup.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07361v1
- Authors: Harisankar Babu, Benjamin Coors, Christopher Lang, Hendrik Berkemeyer, Tamim Asfour, Simon Foell
- Published: 2026-08-07T16:02:34Z
- Age days: 2

</details>
