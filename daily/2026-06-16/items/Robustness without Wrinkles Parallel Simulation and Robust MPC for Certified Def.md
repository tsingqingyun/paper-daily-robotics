---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14188v1"
published: "2026-06-12T07:10:56Z"
age_days: 3
score: 23
created: 2026-06-16
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Robustness without Wrinkles: Parallel Simulation and Robust MPC for Certified Deformable Manipulation

## 为什么重要

自动筛选分数：23

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

We present CORD-SLS, a real-time control method for safe deformable object manipulation,
with a focus on ropes and cloth. At its core is a GPU-parallel differentiable simulator
with contact smoothing which enables efficient gradient-based planning through
intermittent contact. To robustly satisfy constraints under model and sensing
uncertainty, we develop a real-time, GPU-parallel output-feedback robust model
predictive control (MPC) algorithm that plans with this simulator. We further show that
the simulator accelerates model-based RL for training neural manipulation policies. To
improve real-world robustness, we use conformal prediction to calibrate visual-feedback
and perception-error bounds for MPC, producing reachable tubes that enable high-
probability safe control. We evaluate CORD-SLS on high-dimensional, contact-rich rope
and cloth manipulation tasks in simulation and hardware, including obstacle avoidance,
routing, folding, and smoothing. Across settings, CORD-SLS achieves millisecond-speed
planning, exceeding baselines in safety, speed, and task success.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14188v1
- Authors: Wei-Chen Li, Jeffrey Fang, Sasanka Polisetti, Yuexi Song, Glen Chou
- Published: 2026-06-12T07:10:56Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
