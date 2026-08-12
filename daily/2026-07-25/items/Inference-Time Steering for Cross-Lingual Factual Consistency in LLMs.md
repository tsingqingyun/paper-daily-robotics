---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19243v1"
published: "2026-07-21T16:15:05Z"
age_days: 3
score: 26
created: 2026-07-25
concepts: ["具身智能评测与基准"]
---

# Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs

## 为什么重要

自动筛选分数：26

连接概念：[[具身智能评测与基准]]

## 摘要

Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their
internal knowledge representations remain disproportionately biased toward high-resource
languages. This leads to cross-lingual factual inconsistency, where they shift their
empirical answer distributions based solely on the prompt language. We investigate
whether these biases can be mitigated at inference time, forcing an English-prompted
model to answer as if it were queried in target languages (German, Spanish, Bulgarian),
and evaluate four intervention strategies: zero-shot contextual steering (persona
prompting), internal representation manipulation via Contrastive Activation Addition
(CAA), and lightweight weight modification via Direct Preference Optimization (DPO)
trained on benchmark-derived factual data as well as conceptual generalization data. To
assess alignment, we curate a multilingual factual dataset alongside a novel
generalization benchmark comprising culturally rooted queries to determine whether
factual interventions transfer to broader target-centric preferences. Experiments on
Gemma 3 12B Instruct reveal persona prompting to be the strongest overall intervention,
balancing efficacy, safety, and out-of-domain generalization. While CAA yields sharp
inconsistency benchmark shifts, it is configuration-sensitive and risks knowledge
degradation. DPO-based adapters offer permanent, yet narrower and less transferable
gains. These findings suggest that cross-lingual inconsistency is at least partly a
selection problem, and that simple contextual interventions may outperform more invasive
methods for robust, transferable alignment.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19243v1
- Authors: Alexander Manev
- Published: 2026-07-21T16:15:05Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
