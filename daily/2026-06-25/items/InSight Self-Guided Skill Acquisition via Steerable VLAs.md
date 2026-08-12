---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24884v1"
published: "2026-06-23T17:59:01Z"
age_days: 1
score: 31
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# InSight: Self-Guided Skill Acquisition via Steerable VLAs

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-language-action (VLA) models can learn manipulation skills from demonstrations,
but their capabilities are bounded by the skills in the training data. We present
InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs
steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift
upward", "pour the bottle"). InSight consists of two primary stages: (1) an automated
segmentation pipeline that partitions demonstrations into labeled primitives via VLM
plan decomposition and end-effector poses to enable VLA primitive steerability, and (2)
a VLM-guided data flywheel that identifies missing primitives required to accomplish a
novel task, autonomously attempts demonstrations of the missing primitives with VLM-
proposed low-level control, and automatically labels, stores, and integrates successful
demonstrations into the VLA training set. We evaluate InSight across simulation and
real-world manipulation tasks, including block flipping, drawer closing, sweeping,
twisting, and pouring, without any human demonstrations of these target skills. Once
learned, these primitives can be composed to execute novel, long-horizon tasks without
additional human demonstrations. Our findings demonstrate that primitive steerability
provides a practical foundation for continual skill acquisition in VLA policies. Project
website: https://insight-vla.github.io.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24884v1
- Authors: Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu, Mac Schwager
- Published: 2026-06-23T17:59:01Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
