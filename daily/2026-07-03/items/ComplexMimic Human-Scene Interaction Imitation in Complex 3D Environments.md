---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02034v1"
published: "2026-07-02T11:01:20Z"
age_days: 0
score: 30
created: 2026-07-03
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# ComplexMimic: Human-Scene Interaction Imitation in Complex 3D Environments

## 为什么重要

自动筛选分数：30

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Physics-based Human-Scene Interaction (HSI) imitation learning is crucial for embodied
intelligence as it bridges the gap between kinematic 3D motions and real-world dynamics.
However, most existing methods focus on simplified scene settings, leaving complex
environments largely unexplored, which limits their applicability in real-world
scenarios. In this paper, we focus on HSI mimicry in complex environments. Under this
complex setting, we observe an inherent trade-off between successfully performing
interaction and maintaining natural, physically plausible motions. To address this
challenge, we propose ComplexMimic, a framework that reconstructs diverse HSI by
interpreting imperfect MoCap data. First, we introduce a Dual Flow Strategy, which
learns two complementary experts: an imitation expert for accurate motion tracking and
an interaction expert for collision-aware adaptation in complex scenes. Second, naive
multi-expert distillation, which treats all experts equally, often under-samples
challenging behaviors, limiting effective learning. To mitigate this issue, we propose a
difficulty-aware distillation strategy that adaptively weights supervision and
prioritizes hard-yet-learnable trajectories guided by failure statistics and learning
progress signals. Extensive experiments on three benchmark datasets demonstrate that our
approach outperforms current state-of-the-art methods. Our implementation is available
at https://github.com/LuPan23/ComplexMimic.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02034v1
- Authors: Lu Pan, Hongwei Zhao
- Published: 2026-07-02T11:01:20Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
