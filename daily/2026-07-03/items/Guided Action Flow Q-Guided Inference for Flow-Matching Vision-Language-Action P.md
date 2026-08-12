---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02092v1"
published: "2026-07-02T12:30:50Z"
age_days: 0
score: 32
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Flow-matching vision-language-action policies generate robot action chunks through an
iterative transport process, creating an opportunity for test-time guidance without
retraining the base policy. We study this opportunity in Guided Action Flow, an
inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a
learned action-chunk critic to guide its reverse-time flow sampler. The critic is
trained from real success and failure rollouts, can condition on task-description
features from the frozen SmolVLA language pathway, and is used only through action
gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A
single-task critic improves success from 68.0% to 82.0% on one seed window and from
82.0% to 86.0% on another. A multi-family task-description critic improves validation
success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest,
from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for
frozen flow-matching VLA policies, while showing that critic generalization and
uncertainty-aware guidance remain the central bottlenecks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02092v1
- Authors: Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang
- Published: 2026-07-02T12:30:50Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
