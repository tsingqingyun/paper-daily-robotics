---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21302v1"
published: "2026-07-23T13:26:57Z"
age_days: 0
score: 30
created: 2026-07-24
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Expert Behavior Prior Reinforcement Learning

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Behavior prior reinforcement learning (BPRL) has emerged as a promising paradigm to
improve sample efficiency in online reinforcement learning (RL) by leveraging policy
priors derived from offline demonstrations. However, most existing BPRL methods rely on
static offline datasets, which often suffer from low data diversity and suboptimal
trajectory quality. This reliance restricts the effectiveness of policy priors,
hindering both policy exploitation and stability during online training. Consequently,
agents are prone to inefficient exploration and unstable learning dynamics. To address
these limitations, we deviate from existing offline pre-training methods and propose an
Expert Behavior Prior (EBP) algorithm. Specifically, we introduce a Q-guided conditional
variational autoencoder (Q-CVAE) that learns to generate expert policy priors directly
from the online replay buffer. This enables the generation of high-value actions for
guiding policy updates without relying on pre-collected expert trajectories. To further
enhance policy exploitation, we propose an expert policy guidance (EPG) mechanism that
selects expert actions from a generative support set, and we integrate a policy gradient
correction (PGC) module to harmonize Q-guidance with expert supervision, promoting
stable and consistent policy improvement. Extensive experiments conducted on robotic
control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that
EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher
sample efficiency and more stable convergence.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21302v1
- Authors: Gong Gao, Weidong Zhao, Xianhui Liu, Ning Jia
- Published: 2026-07-23T13:26:57Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
