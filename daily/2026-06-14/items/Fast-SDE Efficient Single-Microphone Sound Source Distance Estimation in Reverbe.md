---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12339v1"
published: "2026-06-10T17:08:14Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["世界模型"]
---

# Fast-SDE: Efficient Single-Microphone Sound Source Distance Estimation in Reverberant Environments

## 为什么重要

自动筛选分数：28

连接概念：[[世界模型]]

## 摘要

Sound source distance estimation (SDE) is a critical capability in human-robot
interaction. An inappropriate interaction distance not only reduces the reliability of
speech acquisition and understanding, but also compromises the naturalness and comfort
of the interaction. Most existing SDE methods rely on microphone arrays, however, multi-
microphone systems typically require careful hardware synchronization, geometric
calibration, and additional space and computational resources, which limits
applicability to size-constrained and computability-limited embodied platforms. To
alleviate these issues, we propose Fast-SDE, a lightweight single-microphone SDE
framework that is suited for deployment on robot platforms with limited computational
resources and strict size constraints. Specifically, Fast-SDE employs a subband-based
backbone that decomposes the frequency axis into multiple subbands, rather than
processing the entire spectrum with a wide full-band backbone. A shared subband encoder
then maps each subband to a compact latent representation and learns the relationship
between acoustic structure and time-frequency patterns. Finally, a lightweight
regression head converts the fused subband representations into the estimated distance.
Extensive simulation and real-world experiments demonstrate the merits of the proposed
method. To benefit the broader research community, we have open-sourced our code at
https://github.com/JiangWAV/FAST-SDE.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12339v1
- Authors: Jiang Wang, Runwu Shi, Yaozhong Kang, Benjamin Yen, Takeshi Ashizawa, Kazuhiro Nakadai
- Published: 2026-06-10T17:08:14Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
