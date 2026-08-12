---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22836v1"
published: "2026-06-22T04:16:05Z"
age_days: 1
score: 40
created: 2026-06-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model
with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist
camera. The end-effector occupies a large and consistent region of the wrist view and
masking it allows for embodiment-agnostic visual reasoning. Cloak renders a mask in
simulation from the robot's known geometry, accurately and in real time, with no
segmentation or generative models. During training, we augment the mask so the model
generalizes to embodiments unseen at training time. We demonstrate the recipe with
Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset. No data of
new embodiments is ever collected. Cloak-VLA transfers zero-shot to various unseen
embodiments, including another gripper, another arm, and a five-fingered hand, while
preserving the source embodiment's performance. By decoupling the wrist view from its
own embodiment, Cloak allows data to outlive the hardware it was collected on.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22836v1
- Authors: Michael Piseno, Guy Tevet, C. Karen Liu
- Published: 2026-06-22T04:16:05Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
