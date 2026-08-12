---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23641v1"
published: "2026-06-22T17:30:29Z"
age_days: 1
score: 34
created: 2026-06-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Flatness Preserves Instruction Following in Vision-Language-Action Models

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models have the potential for open-world generalization by
leveraging pretrained vision-language representations, yet downstream finetuning on
limited robot data often degrades these representations, leading to brittle policies
that ignore language instructions in favor of visual shortcuts, a failure mode we term
instruction blindness. We hypothesize that standard finetuning with limited data applies
gradients to a sparse set of points, which manifests as a sharp loss landscape with
high-curvature minima. We propose to address this directly through flatness-preserving
optimization while finetuning on the exact same data, where learning a flatter landscape
results in a model more robust to perturbations in the weight space. Specifically, we
demonstrate that simply applying sharpness-aware minimization during VLA finetuning
significantly improves instruction following by over 60% across multiple simulation and
real-world benchmarks without additional data, architectural modification, or
retraining. We further analyze the effect of selective sharpness, quantify its effects,
and show that our approach is complementary to existing guidance techniques. Project
page can be found at https://haochenz11.github.io/papers/flatness-vla/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23641v1
- Authors: Haochen Zhang, Yonatan Bisk
- Published: 2026-06-22T17:30:29Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
