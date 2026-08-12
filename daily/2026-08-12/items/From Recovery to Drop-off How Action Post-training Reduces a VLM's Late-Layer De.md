---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08904v1"
published: "2026-08-09T20:31:52Z"
age_days: 2
score: 27
created: 2026-08-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability

> [!summary] 一句话结论（基于摘要）
> Second, the degradation is not uniform: while the base VLM's depth decodability improves through its final layers, the VLA's collapses, an additional late-layer drop we call the cliff.

## 关键点

- **问题**：How much of a vision-language model's (VLM) spatial understanding remains after the action post-training process of building a vision-language-action model (VLA)?
- **创新点 / 方法**：We probe depth perception, a primitive of spatiogeometric understanding, from every decoder layer of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO.
- **证据**：Second, the degradation is not uniform: while the base VLM's depth decodability improves through its final layers, the VLA's collapses, an additional late-layer drop we call the cliff.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/From Recovery to Drop-off How Action Post-training Reduces a VLM's Late-Layer De.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

How much of a vision-language model's (VLM) spatial understanding remains after the
action post-training process of building a vision-language-action model (VLA)? We probe
depth perception, a primitive of spatiogeometric understanding, from every decoder layer
of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO.
First, the VLA decodes depth worse at every layer, a persistent gap we call the floor.
Second, the degradation is not uniform: while the base VLM's depth decodability improves
through its final layers, the VLA's collapses, an additional late-layer drop we call the
cliff. We causally localize the cliff to late-layer MLP interference: ablating the late-
layer MLP writes recovers the majority of the terminal decodability cliff, while matched
attention ablations and the same intervention in the weight-matched base VLM produce no
comparable recovery. A module-level decomposition explains this dissociation: the base
VLM carries depth most accessibly in accumulated MLP writes, whereas action post-
training collapses depth decodability in the late accumulated writes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08904v1
- Authors: Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou
- Published: 2026-08-09T20:31:52Z
- Age days: 2

</details>
