---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Embodied AI and Robotics"
url: "https://arxiv.org/abs/2605.05714v1"
published: "2026-05-07T05:57:49Z"
age_days: 
score: 34
created: 2026-05-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> Prior work improves transferability through structured intermediate representations that objectify visual content.

## 关键点

- **问题**：Vision-language-action (VLA) models perform well on training-seen robotic tasks but struggle to generalize to unseen scenes and objects.
- **创新点 / 方法**：Based on this observation, we propose TriRelVLA, a triadic relational VLA framework for generalizable embodied manipulation.
- **证据**：Prior work improves transferability through structured intermediate representations that objectify visual content.
- **局限**：A key limitation lies in their implicit visual representations, which entangle object appearance, background, and scene layout.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models perform well on training-seen robotic tasks but
struggle to generalize to unseen scenes and objects. A key limitation lies in their
implicit visual representations, which entangle object appearance, background, and scene
layout. This makes policies sensitive to visual variations. Prior work improves
transferability through structured intermediate representations that objectify visual
content. However, these representations mainly capture scene semantics instead of
action-relevant relations. As a result, action prediction remains tied to appearance
statistics. We observe that manipulation actions depend on the object-hand-task
relational structure, which governs interactions among task requirements, robot states,
and object properties. Based on this observation, we propose TriRelVLA, a triadic
relational VLA framework for generalizable embodied manipulation. Our approach consists
of three components: 1) We construct explicit object-hand-task triadic representations
from multimodal inputs as relational primitives. 2) We build a task-grounded relational
graph. Task-guided cross-attention forms nodes, and a relation-aware graph transformer
models interactions among them. 3) We perform relation-conditioned action generation.
The relational structure is compressed into a bottleneck space and projected into the
LLM for action prediction. This triadic relational bottleneck reduces reliance on
appearance statistics and enables transfer across scenes, objects, and task
compositions. We further introduce a real-world robotic dataset for fine-tuning.
Experiments show strong performance on fine-tuned tasks and clear gains in cross-scene,
cross-object, and cross-task generalization.

### 来源

- Source: arXiv Daily - Embodied AI and Robotics
- URL: https://arxiv.org/abs/2605.05714v1
- Authors: Hanyu Zhou, Chuanhao Ma, Gim Hee Lee
- Published: 2026-05-07T05:57:49Z
- Age days: 

</details>
