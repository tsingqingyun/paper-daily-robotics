---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18671v1"
published: "2026-08-19T08:21:58Z"
age_days: 1
score: 34
created: 2026-08-21
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI

> [!summary] 一句话结论（基于摘要）
> Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior.

## 关键点

- **问题**：This perspective is increasingly important for wearable intelligence, assistive systems, human--robot interaction, and embodied AI, yet it introduces challenges including ego-motion, occlusion, small active objects, viewpoint-dependent appearance, and long-range temporal dependencies.
- **创新点 / 方法**：Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Across the reviewed literature, a consistent limitation emerges: current models recognize visible objects more reliably than evolving interactions, actions, and user intent, especially over long activities.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Vision-Language Models for Egocentric Video From Hand-Object Interaction to Embo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior. This perspective is increasingly important for wearable intelligence, assistive systems, human--robot interaction, and embodied AI, yet it introduces challenges including ego-motion, occlusion, small active objects, viewpoint-dependent appearance, and long-range temporal dependencies. Vision--language models (VLMs) offer a promising foundation for addressing these challenges by linking visual observations with semantic knowledge and natural-language supervision. This survey presents a critical review of VLMs for egocentric video understanding, tracing the progression from conventional recognition architectures to multimodal foundation models and embodied systems. We organize the literature around tasks, datasets, hand--object interaction understanding, temporal reasoning, frame and clip selection, multimodal representation learning, prompting, semantic alignment, and model adaptation. Particular attention is given to graph-based and object-centric reasoning as mechanisms for modeling relations among hands, objects, actions, and scene context over time. We further examine how first-person perception and multimodal foundation models support wearable assistance, robot skill learning, human-to-robot transfer, and embodied decision making. Across the reviewed literature, a consistent limitation emerges: current models recognize visible objects more reliably than evolving interactions, actions, and user intent, especially over long activities. We therefore identify temporally grounded reasoning, interaction-aware supervision, efficient long-video processing, multimodal fusion, graph-enhanced representations, cross-domain generalization, privacy, and trustworthy evaluation as key priorities for deployable embodied intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18671v1
- Authors: Mohammad Zamani, Fatemeh Ziaeetabar
- Published: 2026-08-19T08:21:58Z
- Age days: 1

</details>
