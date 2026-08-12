---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01067v1"
published: "2026-07-01T15:26:26Z"
age_days: 1
score: 40
created: 2026-07-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

As an essential modality for dexterous and contact-rich tasks, tactile sensing provides
precise force feedback that cannot be reliably inferred from vision. However, limited by
hardware and data collection systems, existing datasets with tactility remain small in
scale and narrow in contact coverage. Meanwhile, Vision-Language-Action (VLA) models
with tactile modality are constrained on dynamics-agnostic post-training, which limits
the performance ceiling on downstream tasks. In this paper, we present H-Tac, a large-
scale tactile-action dataset with 160-hour egocentric human videos containing more than
300 tasks and 135k episodes. Building upon this, we propose Transferable Tactile Pre-
Training (TTP), a system of tactile-based pre-training on human data for fine-grained
robotic tasks. To bridge the gap between humans and robots, we use unified tactile and
action spaces throughout the pre-training and post-training phases, preserving prior
knowledge during human-to-robot transfer. By leveraging a tactile expert for future
tactile prediction, our framework explicitly models the contact dynamics and precise
physical interactions. Extensive experiments in simulation and on real robots
demonstrate that our model achieves superior performance, exhibiting robust
generalization and fine-grained manipulation capabilities. TTP paves the way for
scalable tactile pre-training via human-to-robot transfer.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01067v1
- Authors: Chi Zhang, Penglin Cai, Ziheng Xi, Haoqi Yuan, Hao Luo, Wanpeng Zhang, Sipeng Zheng, Chaoyi Xu, Zongqing Lu
- Published: 2026-07-01T15:26:26Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
