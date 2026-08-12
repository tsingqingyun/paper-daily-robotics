---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29934v1"
published: "2026-06-29T08:10:43Z"
age_days: 1
score: 34
created: 2026-06-30
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# RoamFlow: Reinforcement-Aligned One-Step Action MeanFlow Policy for Image-Goal Navigation

## 为什么重要

自动筛选分数：34

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

Image-goal navigation is a key challenge in embodied robotics, where an agent must reach
a target specified solely by a goal image. While existing reinforcement learning
approaches map perceptual observations directly to actions, they struggle to model long-
horizon dependencies, often leading to suboptimal trajectories. To address this
limitation, we propose RoamFlow, a generative navigation framework that leverages
MeanFlow to predict the average velocity field for trajectory synthesis, enabling
efficient few-step generation and reducing inference latency. We further adopt a two-
stage training strategy that combines expert imitation for stable initialization with
reinforcement learning for task-specific policy refinement. Extensive experiments in
both Habitat simulation and real-world robotic platforms demonstrate that RoamFlow
achieves efficient inference while maintaining strong navigation performance under real-
time constraints.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29934v1
- Authors: Zixuan Zhang, Yuqi Chen, Junjie Gao, Siyuan Song, Yongzhou Pan, Beichen Wang, Mir Feroskhan
- Published: 2026-06-29T08:10:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
