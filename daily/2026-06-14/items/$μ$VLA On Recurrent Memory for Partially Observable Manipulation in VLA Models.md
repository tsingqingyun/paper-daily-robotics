---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12497v1"
published: "2026-06-10T13:26:40Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models

> [!summary] 一句话结论（基于摘要）
> On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline.

## 关键点

- **问题**：Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible.
- **创新点 / 方法**：We present a controlled isolation study of recurrence in a strong pretrained VLA backbone.
- **证据**：On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models predict chunks of future actions from the current
observation, an assumption that fails under partial observability, where decisions
depend on information no longer visible. Existing memory-augmented VLAs simultaneously
introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical
memory, or task-specific architectural changes, so the contribution of recurrence itself
remains entangled with surrounding machinery. We present a controlled isolation study of
recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer
with a small set of learnable memory tokens carried across timesteps and updated through
self-attention, trained end to end with truncated backpropagation through time, with no
auxiliary losses and no architectural changes. We instantiate this as $μ$VLA, a family
of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory
update rule (cross-step gradients or a detached EMA), so that recurrence is the only
varying factor. On MIKASA-Robo, $μ$VLA improves average success rate on five training
tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with
the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring
different memory structure, performance remains near baseline. On LIBERO, the strongest
recurrent variant achieves 96.2% average success, indicating no regression under full
observability. We interpret these results as a calibration of the capability envelope of
minimal in-backbone recurrence, identifying the regime in which it is sufficient and the
regime where additional memory structure is required. Demos and videos can be found in
https://avanturist322.github.io/mu-vla/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12497v1
- Authors: Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev
- Published: 2026-06-10T13:26:40Z
- Age days: 3

</details>
