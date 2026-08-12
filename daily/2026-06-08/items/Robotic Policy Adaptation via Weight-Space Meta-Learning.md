---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07217v1"
published: "2026-06-05T12:29:28Z"
age_days: 2
score: 35
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Robotic Policy Adaptation via Weight-Space Meta-Learning

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-Language-Action (VLA) models are emerging as a promising paradigm for robotic
manipulation, enabling general-purpose policies trained from large corpora of
demonstrations and action labels. However, adapting these models to new tasks still
typically requires task-specific demonstrations, action annotations, and additional
fine-tuning, making deployment costly and difficult to scale. We propose WIZARD, a
weight-space meta-learning framework that sidesteps task-specific fine-tuning by
generating task-specific LoRA parameters for a frozen VLA policy. Given only a language
instruction and a short demonstration video, WIZARD predicts the corresponding
adaptation weights in a single forward pass, without target-task action labels or test-
time optimization. During meta-training, WIZARD learns to map task evidence directly to
expert LoRA updates, capturing relationships between tasks in weight space. Experiments
on LIBERO show that WIZARD improves performance by up to ~2x on unseen dataset
collections and up to ~14x on unseen tasks. On a Franka Emika Panda, WIZARD consistently
improves over a real-domain adapted baseline, showing that generated adapters provide
task-level specialization beyond simulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07217v1
- Authors: Christian Bianchi, Siamak Yousefi, Alessio Sampieri, Andrea Roberti, Luca Rigazio, Fabio Galasso, Luca Franco
- Published: 2026-06-05T12:29:28Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
