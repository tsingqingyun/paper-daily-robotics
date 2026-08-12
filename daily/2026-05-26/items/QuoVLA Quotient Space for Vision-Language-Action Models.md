---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24890v1"
published: "2026-05-24T06:28:53Z"
age_days: 2
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# QuoVLA: Quotient Space for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across multiple benchmarks demonstrate that QuoVLA achieves strong performance, with particularly notable improvements in generalization under visual, linguistic, and environmental distribution shifts.

## 关键点

- **问题**：Existing approaches typically take an action-insufficiency view, assuming that pretrained VLM latents either lack directly usable action information or should be shielded from action-learning signals.
- **创新点 / 方法**：To operationalize this theory, we propose QuoVLA, a quotient-space framework for VLA that compresses pretrained VLM latents into action-sufficient representations.
- **证据**：Extensive experiments across multiple benchmarks demonstrate that QuoVLA achieves strong performance, with particularly notable improvements in generalization under visual, linguistic, and environmental distribution shifts.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models commonly adapt pretrained Vision-Language Models
(VLMs) to robot control by mapping visual observations and language instructions to
continuous actions. Existing approaches typically take an action-insufficiency view,
assuming that pretrained VLM latents either lack directly usable action information or
should be shielded from action-learning signals. Against this view, our \textit{Quotient
Theory for VLA} shows that pretrained VLM latents are not action-insufficient but
action-sufficient: they already contain the information needed for control, yet remain
overcomplete by distinguishing prompt-level variations that induce the same optimal
action behavior. To operationalize this theory, we propose QuoVLA, a quotient-space
framework for VLA that compresses pretrained VLM latents into action-sufficient
representations. Specifically, QuoVLA instantiates this principle with a quantization
module and a dual-branch design with relative temporal-complexity regularization,
preserving action-relevant information while removing prompt-level redundancy. Extensive
experiments across multiple benchmarks demonstrate that QuoVLA achieves strong
performance, with particularly notable improvements in generalization under visual,
linguistic, and environmental distribution shifts. Our code will be made publicly
available.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24890v1
- Authors: Xuan Wang, Yinan Wu, Haoran Duan, Jungong Han
- Published: 2026-05-24T06:28:53Z
- Age days: 2

</details>
