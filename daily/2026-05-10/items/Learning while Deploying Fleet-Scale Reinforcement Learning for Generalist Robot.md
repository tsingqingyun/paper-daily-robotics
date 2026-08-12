---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.00416v1"
published: "2026-05-01T05:20:26Z"
score: 35
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Generalist robot policies increasingly benefit from large-scale pretraining, but offline
data alone is insufficient for robust real-world deployment. Deployed robots encounter
distribution shifts, long-tail failures, task variations, and human correction
opportunities that fixed demonstration datasets cannot fully capture. We present
Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning
framework for continual post-training of generalist Vision-Language-Action (VLA)
policies. Starting from a pretrained VLA policy, LWD closes the loop between deployment,
shared physical experience, policy improvement, and redeployment by using autonomous
rollouts and human interventions collected across a robot fleet. To stabilize learning
from heterogeneous, sparse-reward fleet data, LWD combines Distributional Implicit Value
Learning (DIVL) for robust value estimation with Q-learning via Adjoint Matching (QAM)
for policy extraction in flow-based VLA action generators. We validate LWD on a fleet of
16 dual-arm robots across eight real-world manipulation tasks, including semantic
grocery restocking and 3--5 minute long-horizon tasks. A single generalist policy
improves as fleet experience accumulates, reaching an average success rate of 95%, with
the largest gains on long-horizon tasks.

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.00416v1
- Authors: Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo
- Published: 2026-05-01T05:20:26Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
