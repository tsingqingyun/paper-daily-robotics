---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15935v1"
published: "2026-07-17T13:18:32Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Deep reinforcement learning (DRL) has a longstanding tradition in addressing the reach-
avoid task problem, especially for controlling robotic arms. While this task serves as a
baseline environment within the research community, the ability of DRL to effectively
learn the each-avoid task in complex and realistic scenarios beyond simplified and
restricted tabletop settings remains uncertain. In this paper, we present, for the first
time, a comprehensive benchmark for the reachavoid task that accurately captures real-
world complexities without simplifications. We demonstrate a diverse range of settings
for robotic arm reach-avoid task, which can be used for evaluating DRL research. We
achieved this by utilizing the MuJoCo MJX physics engine and parallelizing both the
simulation environment and DRL algorithms using the Brax library. We achieved state-of-
the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for
the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task. Our
results indicate that while in previous works DRL agents could solve, for example, a
reach task in a simplified setting perfectly, their agents performance collapses when
evaluated in realistic scenarios. Overall, this work identifies that additional research
is still required to claim the successful resolution of the robotic arm reach-avoid task
using DRL. The environment and benchmarking code is available as open source at the
following link

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15935v1
- Authors: Jonas Weihing, Shahram Eivazi
- Published: 2026-07-17T13:18:32Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
