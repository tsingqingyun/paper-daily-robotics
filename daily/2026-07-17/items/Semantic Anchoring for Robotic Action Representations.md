---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13597v1"
published: "2026-07-15T08:45:15Z"
age_days: 1
score: 35
created: 2026-07-17
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Semantic Anchoring for Robotic Action Representations

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models inherit rich semantic representations from
pretrained Vision-Language Models, yet fine-tuning on limited robot demonstrations
degrades this structure and undermines generalization. A fundamental question therefore
arises: what constitutes a good action representation? Inspired by the mirror neuron
theory's insight that observation and execution share an intention-level encoding, we
examine whether a robot's action representations preserve the semantic structure
captured by pretrained encoders. Systematic probing confirms that this structure erodes
during finetuning, and that its quality synchronizes with both task success and out-of-
distribution generalization. We further introduce a plug-and-play method that anchors
action representations to a semantic manifold while decomposing representations into a
shared semantic channel and a private channel, all discarded at inference, leaving the
deployed model unchanged. Validated on different VLA backbones across simulation and
real-world benchmarks, our method yields up to +18.7% on real-world in-distribution
tasks and +21.5% on out-of-distribution generalization.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13597v1
- Authors: Yuan Xu, Youheng Shi, Chengyang Li, Wentao Zhu, Yizhou Wang
- Published: 2026-07-15T08:45:15Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
