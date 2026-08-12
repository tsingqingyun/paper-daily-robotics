---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23293v1"
published: "2026-06-22T13:05:55Z"
age_days: 2
score: 29
created: 2026-06-25
concepts: ["AI 核心知识地图"]
---

# Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation

## 为什么重要

自动筛选分数：29

连接概念：[[AI 核心知识地图]]

## 摘要

6D pose estimation is a key task in computer vision and embodied AI, widely used in
robotic manipulation, augmented reality, etc. Existing methods directly regress in a
high-dimensional continuous space, facing two key challenges in category-level pose
estimation: limited accuracy due to noise and local optima, and inefficient search over
an infinite space that hinders real-time performance. This paper proposes Flow6D, a
hierarchical flow matching framework with a two-stage discrete latent space
localization-continuous pose regression strategy. Rotation and translation parameters
are first discretized into bins, with a discrete flow matching model locking the latent
space around the true pose to reduce search complexity. Then, by sampling in the latent
space, a continuous flow matching model predicts local pose residuals to optimize the
estimate and regress to an accurate pose. The framework also naturally extends to
articulated objects, outperforming state-of-the-art methods on synthetic and real
datasets with real-time inference at 70 FPS. Project website: https://flow6d.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23293v1
- Authors: Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
- Published: 2026-06-22T13:05:55Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
