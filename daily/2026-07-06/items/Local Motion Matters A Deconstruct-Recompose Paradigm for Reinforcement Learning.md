---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00808v1"
published: "2026-07-01T11:36:27Z"
age_days: 4
score: 26
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

Pre-training on large-scale videos to improve reinforcement learning efficiency is
promising yet remains challenging. Existing methods typically treat the agent as an
indivisible entity, modeling motion patterns globally. Such global modeling is tightly
coupled with the morphology, hindering transfer across domains. In contrast, despite the
vast disparity in global motions, the local components exhibit similar motion patterns
across different agents. Building on this insight, we propose a novel Deconstruct-
Recompose Paradigm (DRP) for learning transferable local motion representations.
Specifically, in the Deconstruct phase, we identify multiple local points and track
their frame-wise motions, defining each as an Atomic Action. We introduce a Dual-
Attention Encoder (DAE) to learn local motion representations from these Atomic Actions,
capturing their spatiotemporal relationships. In the Recompose phase, we compose local
motion representations with a learnable Motion Aggregation Token [MAT] via latent
dynamics model learning. Additionally, an adapter bridges local motion and downstream
action-specific dynamics to accelerate policy learning. Extensive experiments
demonstrate that our method effectively transfers to diverse robotic control and
manipulation tasks, significantly improving sample efficiency and performance.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00808v1
- Authors: Jinwen Wang, Youfang Lin, Xiaobo Hu, Shuo Wang, Kai Lv
- Published: 2026-07-01T11:36:27Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
