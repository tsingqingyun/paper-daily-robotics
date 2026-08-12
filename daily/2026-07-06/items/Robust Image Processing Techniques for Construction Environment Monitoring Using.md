---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01915v1"
published: "2026-07-02T09:12:45Z"
age_days: 3
score: 24
created: 2026-07-06
concepts: ["具身智能评测与基准"]
---

# Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots

## 为什么重要

自动筛选分数：24

连接概念：[[具身智能评测与基准]]

## 摘要

This paper proposes a robust image processing framework for underwater robot-based
construction environment monitoring, targeting complex degradations observed in real
marine environments. Unlike conventional approaches that mainly consider absorption and
backscattering, real underwater imagery is strongly affected by depth-dependent forward
scattering blur and particle-induced degradations such as marine snow. To address this,
we introduce a staged processing pipeline that sequentially models background
degradation via depth-aware forward scattering and foreground degradation using
realistic marine snow patterns extracted from real images. The resulting synthetic data
are used to retrain an existing Joint-ID network without modifying its architecture,
enabling an isolated evaluation of dataset realism. In addition, a lightweight post-
processing scheme is applied to enhance contrast and structural clarity. Experiments on
real underwater datasets collected in Korean coastal environments demonstrate consistent
improvements in visual quality and UIQM scores. The results indicate that explicitly
modeling forward scattering and realistic particle effects effectively reduces the
synthetic-to-real gap and improves practical applicability in real-world underwater
robotic operations.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01915v1
- Authors: Seunghee Yun, Geonmo Yang, Juhui Lee, Changbeom Park, Jeahyung Choi, Younggun Cho
- Published: 2026-07-02T09:12:45Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
