---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18617v1"
published: "2026-05-18T16:26:22Z"
age_days: 1
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# ManiSoft: Towards Vision-Language Manipulation for Soft Continuum Robotics

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Most existing vision-language manipulation research targets rigid robotic arms, whose
fixed morphology limits adaptability in cluttered or confined spaces. Soft robotic arms
offer an appealing alternative due to their deformability, but confront challenges such
as unreliable proprioception and distributed low-level actuation. To investigate these
challenges, we introduce \ManiSoft, a benchmark for vision-language manipulation with
soft arms. ManiSoft features a tailored simulator that couples realistic soft-body
dynamics with contact-rich interactions via an elastic force constraint. On this basis,
ManiSoft defines four tasks, each highlighting distinct aspects of deformable control,
from basic end-effector coordination to obstacle avoidance. To support policy training
and evaluation, \ManiSoft{} includes an automated pipeline that generates $6{,}300$
diverse scenes and corresponding expert trajectories. To produce high-quality
trajectories at scale, we first employ a high-level planner to decompose each task into
a sequence of waypoints, followed by a low-level reinforcement learning policy that
generates torque commands to track waypoints. Benchmarking three representative policy
models shows relatively promising results in clean scenes but substantial performance
drop under randomization. Visualization analysis indicates that failures stem primarily
from inaccurate visual estimation of proprioceptive state and limited exploitation of
deformability for adaptive obstacle avoiding. We anticipate ManiSoft to serve as a
valuable testbed, bridging the gap between rigid and soft arms in the context of vision-
language manipulation. Out codes and datasets are released at https://buaa-
colalab.github.io/ManiSoft.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18617v1
- Authors: Ziyu Wei, Luting Wang, Chen Gao, Li Wen, Si Liu
- Published: 2026-05-18T16:26:22Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
