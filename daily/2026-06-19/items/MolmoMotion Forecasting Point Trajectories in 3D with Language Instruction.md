---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18558v1"
published: "2026-06-17T00:19:00Z"
age_days: 2
score: 28
created: 2026-06-19
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Motion forecasting is central to visual intelligence: agents must anticipate how objects
will move in order to plan actions, reason about physical interactions, and synthesize
realistic futures. We argue that 3D points in world coordinates provide a general
representation that is class-agnostic, view-stable, compact, and directly useful for
downstream tasks. We formalize the task of goal-conditioned 3D point motion forecasting:
given a short visual history, a set of 3D query points on an object of interest, and a
language description of the intended goal, the model predicts the future 3D trajectory
of each point. We introduce a full stack to study this task at scale: (1) MolmoMotion-1M
is a large corpus of action-described, object-grounded 3D point trajectories annotated
from 1.16M unconstrained videos; (2) PointMotionBench is a human-verified benchmark
spanning 111 object categories and 61 motion types; and (3) MolmoMotion is a general
motion forecasting model that supports both autoregressive coordinate prediction and
flow-matching-based trajectory generation. MolmoMotion accurately predicts diverse
motion patterns with different language instructions, and significantly outperforms
existing motion prediction baselines on PointMotionBench. Finally, we show that the
learned 3D motion prior transfers well to downstream applications: it improves training
efficiency and generalization for robot manipulation, and its predicted trajectories
provide effective motion guidance for generative models to synthesize videos with more
realistic object motion.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18558v1
- Authors: Jianing Zhang, Chenhao Zheng, Yajun Yang, Max Argus, Rustin Soraki, Winson Han, Taira Anderson, Chun-Liang Li, Shuo Liu, Jiafei Duan, Zhongzheng Ren, Jieyu Zhang, Ranjay Krishna
- Published: 2026-06-17T00:19:00Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
