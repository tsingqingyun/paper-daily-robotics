---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07386v1"
published: "2026-06-05T15:23:54Z"
age_days: 2
score: 28
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Spline Policy: A Structured Representation for Robot Policies

> [!summary] 一句话结论（基于摘要）
> This paper studies Spline Policy (SP), a structured representation that replaces action chunks with spline parameters while keeping the policy backbone unchanged.

## 关键点

- **问题**：Modern imitation-learning policies for robot manipulation often represent actions as fixed-resolution action chunks, which are simple and effective but expose limited geometric and temporal structure before execution.
- **创新点 / 方法**：This paper studies Spline Policy (SP), a structured representation that replaces action chunks with spline parameters while keeping the policy backbone unchanged.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern imitation-learning policies for robot manipulation often represent actions as
fixed-resolution action chunks, which are simple and effective but expose limited
geometric and temporal structure before execution. This paper studies Spline Policy
(SP), a structured representation that replaces action chunks with spline parameters
while keeping the policy backbone unchanged. The predicted spline can be decoded as a
compact continuous trajectory, queried at different temporal resolutions, constrained or
edited in parameter space, and passed to downstream controllers. For quadratic spline
outputs, the same representation can also be converted into a state-dependent vector
field through an analytical distance-field construction. Under the regularity and
projection assumptions of this construction, the induced dynamics do not increase the
distance to the generated spline, yielding a principled local corrective mechanism
around the predicted motion. The spline output further supports uncertainty propagation
from observations to spline parameters, trajectories, and flow fields, and can be
combined with classical control mechanisms such as null-space collision avoidance
without retraining the policy backbone. We instantiate SP with diffusion, flow-matching,
transformer-based, and vision-language-action backbones. Experiments in low-dimensional
motion learning, simulated manipulation under matched backbones, dexterous manipulation,
and real-robot case studies show that SP remains compatible with modern policy learners
while exposing useful motion-structure properties, including compact decoding, temporal
resampling, local correction around predicted motions, uncertainty evaluation, and
controller compatibility.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07386v1
- Authors: Mengze Tian, Yiming Li, Sichao Liu, Auke Ijspeert, Sylvain Calinon
- Published: 2026-06-05T15:23:54Z
- Age days: 2

</details>
