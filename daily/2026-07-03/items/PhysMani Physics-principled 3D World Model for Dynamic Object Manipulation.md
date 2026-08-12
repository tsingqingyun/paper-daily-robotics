---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01938v1"
published: "2026-07-02T09:32:39Z"
age_days: 0
score: 36
created: 2026-07-03
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation

## 为什么重要

自动筛选分数：36

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Manipulating fast and dynamically moving targets in unstructured 3D environments remains
challenging for embodied AI. Existing visual-language-action models and world models
struggle with accurate 3D geometry and physically meaningful forecasting. We propose
PhysMani, a framework that couples a physics-principled 3D Gaussian world model with a
future-aware action policy model. The world model learns a divergence-free Gaussian
velocity field via online optimization for fast and physically grounded future dynamics
prediction. The policy model integrates the predicted 3D scene future dynamics through a
learnable token based cross-attention module. We introduce PhysMani-Bench, a dynamic
manipulation benchmark with 16 tasks, and demonstrate a superior success rate over
strong baselines in both simulation and real-world robot experiments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01938v1
- Authors: Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang
- Published: 2026-07-02T09:32:39Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
