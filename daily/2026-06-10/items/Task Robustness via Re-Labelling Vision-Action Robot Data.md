---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10918v1"
published: "2026-06-09T14:28:22Z"
age_days: 0
score: 33
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Task Robustness via Re-Labelling Vision-Action Robot Data

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

The recent trend in scaling models for robot learning has resulted in impressive
policies that can perform various manipulation tasks and generalize to novel scenarios.
However, these policies continue to struggle with following instructions, likely due to
the limited linguistic and action sequence diversity in existing robotics datasets. This
paper introduces Task Robustness via Re-Labelling Vision-Action Robot Data (TREAD), a
scalable framework that leverages large Vision-Language Models (VLMs) to augment
existing robotics datasets without additional data collection, harnessing the
transferable knowledge embedded in these models. Our approach leverages a pretrained VLM
through three stages: generating semantic sub-tasks from original instruction labels and
initial scenes, segmenting demonstration videos conditioned on these sub-tasks, and
producing diverse instructions that incorporate object properties, effectively
decomposing longer demonstrations into grounded language-action pairs. We further
enhance robustness by augmenting the data with linguistically diverse versions of the
text goals. Evaluations on LIBERO demonstrate that policies trained on our augmented
datasets exhibit improved performance on novel, unseen tasks and goals. Our results show
that TREAD enhances both planning generalization through trajectory decomposition and
language-conditioned policy generalization through increased linguistic diversity.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10918v1
- Authors: Artur Kuramshin, Özgür Aslan, Cyrus Neary, Glen Berseth
- Published: 2026-06-09T14:28:22Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
