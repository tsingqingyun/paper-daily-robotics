---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24890v1"
published: "2026-05-24T06:28:53Z"
age_days: 2
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# QuoVLA: Quotient Space for Vision-Language-Action Models

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models commonly adapt pretrained Vision-Language Models
(VLMs) to robot control by mapping visual observations and language instructions to
continuous actions. Existing approaches typically take an action-insufficiency view,
assuming that pretrained VLM latents either lack directly usable action information or
should be shielded from action-learning signals. Against this view, our \textit{Quotient
Theory for VLA} shows that pretrained VLM latents are not action-insufficient but
action-sufficient: they already contain the information needed for control, yet remain
overcomplete by distinguishing prompt-level variations that induce the same optimal
action behavior. To operationalize this theory, we propose QuoVLA, a quotient-space
framework for VLA that compresses pretrained VLM latents into action-sufficient
representations. Specifically, QuoVLA instantiates this principle with a quantization
module and a dual-branch design with relative temporal-complexity regularization,
preserving action-relevant information while removing prompt-level redundancy. Extensive
experiments across multiple benchmarks demonstrate that QuoVLA achieves strong
performance, with particularly notable improvements in generalization under visual,
linguistic, and environmental distribution shifts. Our code will be made publicly
available.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24890v1
- Authors: Xuan Wang, Yinan Wu, Haoran Duan, Jungong Han
- Published: 2026-05-24T06:28:53Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
