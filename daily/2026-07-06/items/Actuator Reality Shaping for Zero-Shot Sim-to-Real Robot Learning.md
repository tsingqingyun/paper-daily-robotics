---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02205v1"
published: "2026-07-02T14:12:41Z"
age_days: 3
score: 28
created: 2026-07-06
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning

## 为什么重要

自动筛选分数：28

连接概念：[[世界模型]], [[机器人学习]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Sim-to-real transfer in robot learning is often limited by discrepancies between the
ideal actuator dynamics assumed during policy training and the nonlinear, hardware-
dependent behavior of physical motors. While conventional approaches attempt to bridge
this gap by increasing simulator fidelity through system identification, domain
randomization, or learned actuator models, we introduce an alternative paradigm:
actuator reality shaping. Instead of modifying the simulator to match the real world,
our method shapes the closed-loop behavior of physical actuators to match the idealized
second-order reference dynamics used in simulation. By equipping each joint with a two-
degree-of-freedom feedforward--feedback controller, we decouple reference-response
shaping from robust stabilization, thereby providing a standardized actuator interface
for reinforcement learning policies. As a result, policies trained only with the
prescribed reference model can be deployed zero-shot on real hardware without task-level
fine-tuning or learned actuator models. We validate the approach on a single-joint high-
gear-ratio servo under external loads and a 7-DOF robotic arm reaching task, where
actuator reality shaping substantially reduces sim-to-real tracking error and improves
zero-shot task performance compared with standard servo-control and representative real-
to-sim-to-real baselines. We further demonstrate zero-shot transfer on a wheeled-legged
robot driving over a slope and a humanoid robot walking, suggesting that actuator
reality shaping can serve as a reusable interface for robot learning across diverse
hardware platforms.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02205v1
- Authors: Satoshi Yamamori, Koji Ishihara, Kentaro Minamikawa, Kiyoharu Ohomori, Taiyo Yazaki, Norikazu Sugimoto, Jun Morimoto
- Published: 2026-07-02T14:12:41Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
