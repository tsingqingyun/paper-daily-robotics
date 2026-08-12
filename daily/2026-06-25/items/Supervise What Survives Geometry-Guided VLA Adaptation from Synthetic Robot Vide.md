---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24448v1"
published: "2026-06-23T11:35:13Z"
age_days: 1
score: 33
created: 2026-06-25
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models require large-scale video-action pairs, yet real
teleoperation remains scarce. While generated robot videos offer a scalable alternative,
existing methods treat them as real robot data by recovering pseudo-actions from
synthesized pixels. We argue that deriving low-level control from generated visuals is a
mismatched abstraction. A video captures only \emph{geometry}: the spatial trajectory
representing the \emph{where} of a task. A real demonstration captures \emph{control}:
the exact motor commands representing the \emph{how}. Human-to-robot video generation
preserves these unequally: the visible geometry survives the generation process, while
the underlying control signals are lost. This \textbf{Asymmetric Preservation Principle}
dictates a clean rule: this surviving geometry should solely supervise visual
perception, leaving control to real demonstrations. Following this principle, we propose
\textbf{GRA} (\textbf{G}eometry-guided \textbf{R}epresentation \textbf{A}lignment),
which extracts the geometric content as future 2D end-effector waypoints, computed from
the source human video through pose estimation, retargeting, simulation, and calibrated
projection, and routes them to the VLA vision backbone via an auxiliary 2D head. The
action head is trained on real demonstrations only. During fine-tuning, the waypoint
loss persists as a \textbf{spatial representation anchor} that prevents the backbone
from losing its geometric grounding. On real-robot tasks, GRA outperforms pseudo-action
baselines under matched data budgets and narrows the gap to policies trained with
substantially more real demonstrations, suggesting that correctly routed geometry
bridges generated videos to robot policies more reliably than recovered actions.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24448v1
- Authors: Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao, Mike Zheng Shou
- Published: 2026-06-23T11:35:13Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
