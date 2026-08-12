---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14635v1"
published: "2026-07-16T06:59:39Z"
age_days: 3
score: 27
created: 2026-07-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "Sim2Real"]
---

# Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> In zero-shot sim-to-real navigation, Action QFormer improves average closed- loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations.

## 关键点

- **问题**：Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction.
- **创新点 / 方法**：To address this tension, we introduce Action QFormer, a query-based action- facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation.
- **证据**：In zero-shot sim-to-real navigation, Action QFormer improves average closed- loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action supervision in vision-language-action (VLA) models is often treated as a
downstream objective for learning action prediction. In this paper, we study it instead
as a force that shapes inherited multimodal representations. We show that this shaping
has a dual effect: it is necessary for forming action-compatible representations, but
when action supervision is applied too directly to the inherited multimodal pathway, it
can also destabilize representations that support language-side processing and object
grounding. To address this tension, we introduce Action QFormer, a query-based action-
facing interface that uses instruction-conditioned queries to reorganize inherited
multimodal information into action-facing representations before downstream action
generation. In zero-shot sim-to-real navigation, Action QFormer improves average closed-
loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation
correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction
generations. Further analyses show that Action QFormer changes how action supervision
shapes inherited multimodal representations, reducing broad upstream rewriting while
preserving targeted and sometimes constructive action-supervised adaptation. These
results suggest that improving VLA performance requires not only stronger pretrained
backbones, but also better ways of selecting and organizing inherited multimodal
information while controlling how it is shaped under action supervision.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14635v1
- Authors: Yufeng Ji, Wenhao Tang, Haoyi Niu, Koushil Sreenath, Yi Wu, Zhongyu Li
- Published: 2026-07-16T06:59:39Z
- Age days: 3

</details>
