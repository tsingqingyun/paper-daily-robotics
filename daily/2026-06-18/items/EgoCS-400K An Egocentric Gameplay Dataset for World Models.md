---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18180v1"
published: "2026-06-16T17:13:58Z"
age_days: 1
score: 35
created: 2026-06-18
concepts: ["智能体 Agent", "世界模型"]
---

# EgoCS-400K: An Egocentric Gameplay Dataset for World Models

## 为什么重要

自动筛选分数：35

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

The shift from video generation to interactive world modeling places new demands on
data: beyond captioned videos, world models require temporally aligned video-action-
language trajectories grounded in the actions, camera motion, states, and events that
drive future scene changes. However, such data is difficult to obtain at scale. Web
video datasets offer broad visual coverage but lack executable actions and reliable
states; robotic datasets provide action and state supervision but are costly and limited
in scene diversity; and existing simulators often lack large-scale human-driven
interaction trajectories. In this paper, we introduce EgoCS-400K, a large-scale replay-
grounded egocentric Counter-Strike dataset for world models, built from public
professional CS and CS2 match demos that preserve human gameplay trajectories and enable
parsing, replaying, rendering, and temporal alignment. We extract player states, view
directions, movements, keyboard/button inputs, view-angle changes, weapon usage, game
events, and round-level context, and render clean first-person videos from the same
trajectories. EgoCS-400K contains over 400,000 first-person videos and 10,000 hours of
gameplay from more than 1,000 matches and 40,000 rounds, covering 13 maps and 10 player
viewpoints per round. It supports a range of interactive visual modeling tasks,
including action-conditioned future prediction, state- and event-aware scene rollout,
replay-grounded captioning, and agent egocentric action understanding. By connecting
visual observations with human actions, camera motion, game states, and events at scale,
EgoCS-400K serves as a practical bridge between passive web videos, controllable game
simulation, and costly real-world embodied data.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18180v1
- Authors: Rongjin Guo, Dong Liang, Yuhao Liu, Fang Liu, Tianyu Huang, Gerhard P. Hancke, Rynson W. H. Lau
- Published: 2026-06-16T17:13:58Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
