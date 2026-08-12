---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12956v1"
published: "2026-06-11T06:29:49Z"
age_days: 1
score: 35
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Long-horizon robot mobile manipulation requires continual reasoning about localization,
environment changes, and task progress, all of which are challenging to infer from image
observations alone. In this paper, we show that conditioning a mobile manipulation
policy on a spatiotemporal feature map improves reasoning over long horizons. The map
represents the environment and the articulated robot body as neural points in a shared
latent space and is updated online from egocentric observations and proprioceptive
state. We update the environment neural points using object-level rigid tracking and the
robot neural points using forward kinematics. We use our spatiotemporal environment and
robot feature (SERF) map as a state input to a vision-language-action (VLA) model by
extracting map tokens from multiple reference frames and spatial scales, providing the
policy with both local and global context. We demonstrate SERF on BEHAVIOR-1K, a
benchmark for long-horizon mobile manipulation in household environments. Experiments
show that the SERF VLA policy outperforms image-only baselines, reaches subgoals faster
by following more direct trajectories, improves robustness to scene-configuration
shifts, and recovers from object-drop failures.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12956v1
- Authors: Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov
- Published: 2026-06-11T06:29:49Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
