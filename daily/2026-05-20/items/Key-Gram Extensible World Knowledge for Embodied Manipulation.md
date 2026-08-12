---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18556v1"
published: "2026-05-18T15:37:02Z"
age_days: 1
score: 34
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Key-Gram: Extensible World Knowledge for Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> Across RoboTwin2.0, LIBERO/LIBERO-Plus, and real-world dual-arm manipulation, Key-Gram consistently improves both $π_{0}$ and $π_{0.5}$ backbones, with average relative gains of $29.5\%/9.9\%$ on RoboTwin2.0, $35.8\%/4.5\%$ on LIBERO-Plus transfer without tar…

## 关键点

- **问题**：However, current vision- language-action policies and world-action models often couple linguistic knowledge with visual computation in a shared backbone or conditioning pathway, leading to modality competition and making knowledge extension dependent on backbone updates.
- **创新点 / 方法**：In this paper, we introduce Key-Gram, a conditional-memory framework that separates language-derived world knowledge from visual-state reasoning for embodied control.
- **证据**：Across RoboTwin2.0, LIBERO/LIBERO-Plus, and real-world dual-arm manipulation, Key-Gram consistently improves both $π_{0}$ and $π_{0.5}$ backbones, with average relative gains of $29.5\%/9.9\%$ on RoboTwin2.0, $35.8\%/4.5\%$ on LIBERO-Plus transfer without target-domain fine-tuning, and $15.4\%/8.1\%$ on real-world lon…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied control increasingly requires models to follow compositional language
instructions while reasoning over dynamic visual states. However, current vision-
language-action policies and world-action models often couple linguistic knowledge with
visual computation in a shared backbone or conditioning pathway, leading to modality
competition and making knowledge extension dependent on backbone updates. In this paper,
we introduce Key-Gram, a conditional-memory framework that separates language-derived
world knowledge from visual-state reasoning for embodied control. At its core is a
memory module that decomposes an instruction into task-specific key-grams, retrieves
static linguistic priors through deterministic hashed lookup, and injects the retrieved
entries into selected hidden layers through context-aware gating and lightweight
convolutional fusion. This design allows the backbone to devote its main capacity to
visual reasoning and action inference, while reusable instruction knowledge is stored in
an extensible external memory. The logical memory table can be conveniently partitioned
during training and, due to its $O(1)$ lookup pattern, efficiently placed on host memory
during inference. Across RoboTwin2.0, LIBERO/LIBERO-Plus, and real-world dual-arm
manipulation, Key-Gram consistently improves both $π_{0}$ and $π_{0.5}$ backbones, with
average relative gains of $29.5\%/9.9\%$ on RoboTwin2.0, $35.8\%/4.5\%$ on LIBERO-Plus
transfer without target-domain fine-tuning, and $15.4\%/8.1\%$ on real-world long-
horizon tasks. These results demonstrate that externalized linguistic memory provides an
effective and extensible mechanism for improving compositional grounding, transfer, and
real-world manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18556v1
- Authors: Jingjing Fan, Siyuan Li, Botao Ren, Zhidong Deng
- Published: 2026-05-18T15:37:02Z
- Age days: 1

</details>
