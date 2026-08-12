---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22907v1"
published: "2026-06-22T06:46:26Z"
age_days: 1
score: 36
created: 2026-06-24
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Improving Robotic Imitation Learning via Trajectory Standardization

## 为什么重要

自动筛选分数：36

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Imitation learning for robotic manipulation relies on large sets of human demonstration
trajectories, which are often noisy and temporally irregular due to variable operator
speed, intermittent pauses, and inconsistent action density. A common preprocessing
strategy is time-uniform downsampling to shorten sequences, but it cannot effectively
remove speed-induced non-uniformity or redundant pauses. This mismatch degrades data
quality and hinders policy learning. To address this issue, we propose Information-
Standardized Trajectory Resampling (ISR), an offline preprocessing method for effective
imitation learning. ISR resamples each trajectory by enforcing approximately equal
information distance between adjacent points. Specifically, we map trajectories onto an
information-modulated Riemannian manifold and perform geodesic-equidistant
parameterization. We construct an information-intensity field from velocity and
acceleration norms: the velocity term removes small-motion redundancy, while the
acceleration term preserves high-curvature and fine-manipulation phases. We evaluate ISR
on three real-world manipulation tasks with mainstream imitation learning policies.
Compared with the baseline time-uniform 3x downsampling, ISR improves task success rates
by about 25%, remains robust across datasets collected from different operators, and
reduces both dataset size and training cost. The code and videos are publicly available
at https://d-robotics-ai-lab.github.io/isr.page.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22907v1
- Authors: Licheng Yang, Lingfeng Qian, Fei Zheng, Yonghao He, Wei Sui, Shuangshuang Li, Hu Su
- Published: 2026-06-22T06:46:26Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
