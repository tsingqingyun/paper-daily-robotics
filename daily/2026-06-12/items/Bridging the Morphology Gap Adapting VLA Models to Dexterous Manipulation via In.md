---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12109v1"
published: "2026-06-10T14:03:52Z"
age_days: 1
score: 36
created: 2026-06-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot
generalization in robotic manipulation, yet the vast majority of pre-trained pipelines
remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic
priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end
joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and
acute action manifold collapse due to data scarcity. In this paper, we present InDex, a
novel, data-efficient adaptation framework rooted in cross-morphology semantic
inheritance. Rather than discarding the pre-trained 1-DoF parallel grasp output, we
repurpose it as a continuous, macroscopic virtual grasp intent proxy to sequentialize
the control topology. We implement a two-stage decoupled learning architecture: the
first stage parameter-efficiently aligns the VLA backbone to predict continuous arm
trajectories and the scalar grasp intent; the second stage freezes this spatial backbone
and leverages an intent-conditioned denoising diffusion head to decode fine-grained
joint articulations for multi-fingered end-effectors. Extensive simulation benchmarks
across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate
that InDex effectively masters intricate skills with minimal demonstration data,
substantially outperforming monolithic baselines while preserving the robust spatial
generalizability of the original VLA prior.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12109v1
- Authors: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
- Published: 2026-06-10T14:03:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
