---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29501v1"
published: "2026-06-28T17:01:55Z"
age_days: 1
score: 32
created: 2026-06-30
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Transferable Dynamics Priors from Action to World Modeling

## 为什么重要

自动筛选分数：32

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

We study action-conditioned world modeling as a scalable way to learn transferable
dynamics priors for robot learning. By pretraining a model to predict how actions drive
visual scene evolution, the resulting world model captures reusable interaction dynamics
beyond appearance-level video generation. Concretely, we pretrain a multi-view
interactive base diffusion world model, A2World, on large-scale robot manipulation data
with real action annotations. We validate the learned dynamics priors from two
complementary perspectives. First, we adapt A2World into a task- or scene-specialized
real-world simulator, A2World-sim, whose long-horizon rollouts support simulator-based
policy evaluation and scalable what-if analysis by replacing real-robot rollouts with
world model rollouts. Second, starting from the same pretrained weights, we adapt
A2World into a video-action joint prediction model, A2World-policy, that predicts
actions under visual and instruction conditioning. Experiments across simulation
benchmarks and real-robot settings demonstrate that action-conditioned world model
pretraining yields transferable dynamics priors that benefit both simulator-centric and
policy-centric robot learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29501v1
- Authors: Ze Huang, Jiahui Zhang, Hairuo Liu, Chenxi Zhang, Ran Cheng, Li Zhang
- Published: 2026-06-28T17:01:55Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
