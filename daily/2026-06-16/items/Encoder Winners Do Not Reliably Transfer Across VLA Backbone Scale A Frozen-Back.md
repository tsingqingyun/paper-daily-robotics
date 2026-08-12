---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14153v1"
published: "2026-06-12T06:27:00Z"
age_days: 3
score: 25
created: 2026-06-16
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic

> [!summary] 一句话结论（基于摘要）
> We introduce a frozen-backbone grafting diagnostic: the vision tower of a released VLA is replaced by a candidate encoder under a fixed protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector), with the language model and action…

## 关键点

- **问题**：Vision-language-action (VLA) policies typically inherit their vision encoder from upstream VLM releases, but it is unclear whether an encoder choice validated on a small VLA transfers to a larger backbone.
- **创新点 / 方法**：We introduce a frozen-backbone grafting diagnostic: the vision tower of a released VLA is replaced by a candidate encoder under a fixed protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector), with the language model and action expert frozen.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Across four encoders, two LIBERO suites, two backbones (SmolVLA-450M and $π_{0.5}$-3.3B), and two-to-three seeds per cell (40 main grafting runs plus native, LoRA, pooling, and zero-/shuffled-image controls, all scored by offline action MSE), the small-backbone winner does not reliably select the large-backbone top ti…

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies typically inherit their vision encoder from
upstream VLM releases, but it is unclear whether an encoder choice validated on a small
VLA transfers to a larger backbone. We introduce a frozen-backbone grafting diagnostic:
the vision tower of a released VLA is replaced by a candidate encoder under a fixed
protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector),
with the language model and action expert frozen. Across four encoders, two LIBERO
suites, two backbones (SmolVLA-450M and $π_{0.5}$-3.3B), and two-to-three seeds per cell
(40 main grafting runs plus native, LoRA, pooling, and zero-/shuffled-image controls,
all scored by offline action MSE), the small-backbone winner does not reliably select
the large-backbone top tier: SigLIP is best on SmolVLA across both suites, while on
$π_{0.5}$ DINOv2-small leads the spatial suite and the object suite is a seed-sensitive
near-tie band; three of the four backbone-suite comparisons (and 11 of 12 seed-level
cells) support backbone-dependent rankings. The grafting wrapper is itself non-neutral
with opposite sign across backbones (+45-56% MSE on the SmolVLA native tower, -50-52% on
$π_{0.5}$), so all conclusions are conditional on the fixed grafting protocol. We
position frozen grafting as a cheap target-backbone diagnostic to run before committing
to an encoder at scale, not as a closed-loop deployment claim.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14153v1
- Authors: Qingping Zeng, Fei She
- Published: 2026-06-12T06:27:00Z
- Age days: 3

</details>
