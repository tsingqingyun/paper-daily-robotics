---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13429v1"
published: "2026-07-15T04:13:54Z"
age_days: 1
score: 35
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior
cloning (BC) has become the standard recipe for vision-language-action (VLA) policies.
However, BC finetuning progressively overwrites the pretrained representations that
support visual and semantic generalization. Co-training on web image-text data, a common
remedy, does not prevent this; it applies language and action losses to separate
observations, leaving VLAs with language-action misalignment that standard manipulation
benchmarks do not expose. We propose Anchor-Align, which augments BC with two
objectives: Vision-Language Anchoring distills layer-wise representations from a frozen
VLM copy to prevent this drift, while Language-Action Alignment converts each action
target into a discrete motion-direction label and jointly trains language and action
prediction on the same robot observation. On a physical xArm7 robot, across two widely
used VLA architectures, Anchor-Align improves real-robot success on both (28% to 54% and
37% to 60%). At scale in simulation, we demonstrate consistent improvements on OOD
perturbations, perceptual robustness, and long-horizon control across LIBERO-PRO,
LIBERO-Plus, and CALVIN, respectively, suggesting that preserving pretrained
representations and effective action learning are not fundamentally at odds. Project
page: anchoralignvla.github.io

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13429v1
- Authors: Dwip Dalal, Shivansh Patel, Chahit Jain, Jeonghwan Kim, Utkarsh Mishra, Alex Baratian, Hyeonjeong Ha, Heng Ji, Svetlana Lazebnik, Unnat Jain
- Published: 2026-07-15T04:13:54Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
