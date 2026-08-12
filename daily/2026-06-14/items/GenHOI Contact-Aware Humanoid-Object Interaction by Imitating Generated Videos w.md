---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12995v1"
published: "2026-06-11T07:31:05Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["世界模型", "机器人学习"]
---

# GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training

## 为什么重要

自动筛选分数：25

连接概念：[[世界模型]], [[机器人学习]]

## 摘要

Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet
it remains challenging due to the tight coupling between dynamic balance and stable
interaction with diverse objects. Existing methods often require time-consuming task-
specific policy training or rely on rigid trajectory replay, which limits their ability
to accommodate novel interaction scenarios. In this work, we present \textit{GenHOI}, a
simple yet effective framework that enables humanoid robots to perform diverse object-
interaction tasks in a zero-shot manner by directly imitating a single generated video,
without task-specific training or physical demonstration data. GenHOI first reconstructs
the robot-object scene in simulation and renders a first-frame image, which, together
with the language command, conditions the synthesis of a task-oriented interaction
video. The generated video is then analyzed to identify interaction-relevant contact
events and estimate hand-object contact regions, which are encoded as object-centric
geometric constraints that convert visual interaction cues into physically grounded
optimization priors. Guided by these priors, the reference motion recovered from the
video is refined and smoothed to resolve the scale ambiguity inherent in 2D video
generation, while adapting a single reference trajectory to unseen robot-object relative
poses. The optimized trajectory is finally executed by a closed-loop tracking
controller. We validate the proposed framework in extensive simulation and real-world
experiments across diverse object-interaction tasks, including box grasping, asymmetric
bimanual chair carrying, table lifting from below, and cylindrical-object enveloping.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12995v1
- Authors: Zhihai Bi, Qiang Zhang, Guoyang Zhao, Jiahang Cao, Xueyin Luo, Yushan Zhang, Jinglan Xu, Ruoyu Geng, Yulin Li, Andrew F. Luo, Jun Ma
- Published: 2026-06-11T07:31:05Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
