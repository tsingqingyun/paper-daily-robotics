---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17520v1"
published: "2026-06-16T05:00:42Z"
age_days: 1
score: 33
created: 2026-06-18
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real"]
---

# GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments

## 为什么重要

自动筛选分数：33

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[Sim2Real]]

## 摘要

Training embodied agents in the real world requires skilled operators and expensive
hardware. Simulation environments offer a compelling alternative by enabling large-
scale, cost-effective data augmentation. Consequently, rapidly constructing high-
fidelity simulation scenes with a minimal sim-to-real gap has become a critical
objective in robot learning. While reconstruction-based methods provide superior visual
quality, current workflows are hindered by inefficient data acquisition and subpar
foreground object extraction. We thus propose GASE, a highly automated system for
simulation scene construction. GASE leverages multi-view video streams from panoramic
camera arrays to enable rapid environment scanning. To ensure high-quality asset
generation, our pipeline introduces a camera-pose-based strategy that robustly extracts
objects across frames in the 2D domain, followed by high-fidelity scene inpainting.
Foreground objects and the static background are then reconstructed independently and
seamlessly imported into physics simulators for policy training. Extensive experiments
demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation
accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore,
real-robot deployments across manipulation and navigation tasks maintains a performance
gap of less than 10\% compared to policies trained purely on real-world data. These
results confirm that GASE provides an efficient and highly effective solution for
bridging the sim-to-real gap. Code will be released.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17520v1
- Authors: Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
- Published: 2026-06-16T05:00:42Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
