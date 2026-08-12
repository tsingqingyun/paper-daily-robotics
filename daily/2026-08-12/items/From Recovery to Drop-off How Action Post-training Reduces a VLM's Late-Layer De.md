---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08904v1"
published: "2026-08-09T20:31:52Z"
age_days: 2
score: 27
created: 2026-08-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08904v1
- Authors: Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou
- Published: 2026-08-09T20:31:52Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
