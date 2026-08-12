---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06836v1"
published: "2026-06-05T02:23:05Z"
age_days: 2
score: 33
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Language-guided UAV agents must execute long-horizon semantic instructions while
producing smooth, physically feasible continuous flight commands, yet existing Vision-
Language Navigation (VLN) benchmarks typically use discrete or coarse actions and
existing UAV Vision-Language-Action (VLA) tasks focus on short, atomic maneuvers. To
address this gap in UAV task settings, we introduce \textbf{FLIGHT}, a \textbf{F}ine-
grained \textbf{L}ong-horizon \textbf{I}nstruction-\textbf{G}uided benchmark for
\textbf{H}ybrid UAV navigation and reasoning \textbf{T}asks, which combines multi-stage
instructions with dense 6-DoF trajectory annotations across two dataset splits: Fine-
grained VLN and Long-horizon Flow. To endow the UAV agent with the capability of real-
time in-flight reasoning over task execution status and mission planning, while
simultaneously accommodating high-frequency, real-time precise control, we further
propose \textbf{FLIGHT VLA}, an asynchronous architecture that decouples a low-frequency
Streaming Pilot Vision-Language Model (VLM) for task-state reasoning from a high-
frequency diffusion action model for continuous control, supervised by explicit
\textbf{Pilot Reasoning} texts that summarize the current flight state and anticipate
the next subgoal. In closed-loop evaluation, FLIGHT VLA consistently surpasses
representative VLN and VLA baselines on our FLIGHT benchmarks, achieving stronger multi-
stage completion, subgoal adherence, and terminal control. Its trained Streaming Pilot
Reasoning VLM further improves UAV video reasoning, validating the effectiveness of our
design.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06836v1
- Authors: Xiangyi Zheng, Xiangyu Wang, Qinan Liao, Zimu Tang, Yue Liao, Dongyue Lyu, Guodong Wang, Junjie Liu, Si Liu
- Published: 2026-06-05T02:23:05Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
