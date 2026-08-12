---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14561v1"
published: "2026-06-12T15:38:34Z"
age_days: 2
score: 29
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# ORCA: A Platform for Open-Source Dexterity Research

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Robotics manipulation research increasingly focuses on two-finger parallel grippers for
their effectiveness, affordability, and ease of teleoperation. Grippers are nonetheless
limited by their form factor, often requiring bimanual setups even for simple
reorientation tasks. Anthropomorphic hands are a more natural platform for dexterous
robot learning -- closer to the human hand, and capable of learning from human video --
yet they remain hard to use in learning research: even where open and accessible hand
hardware exists, the software for control, simulation, teleoperation, and retargeting is
scattered in one-off code bases, and largely disconnected from the robot-learning
ecosystem. In this work, we introduce the \orca~learning stack, an open-source research
stack for dexterity as a first-class robot learning domain. Our \orca~stack unifies low-
level control, simulation, teleoperation from a range of consumer platforms, and hand
retargeting, behind a single interface, and integrates natively with popular robot-
learning frameworks such as \lerobot, so dexterous hand researchers can leverage the
same data, training, and evaluation pipelines used for non-dexterous robot learning. We
demonstrate a complete end-to-end workflow, collecting expert demonstrations of an in-
hand reorientation task by teleoperation with a consumer-grade VR headset, training an
autonomous policy with \lerobot, and evaluating the learned policy in a fully
reproducible and observable setup. We open-source the entire stack as a shared,
reproducible foundation for dexterous-manipulation research.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14561v1
- Authors: Francesco Capuano, Maximilian Eberlein, Fabrice Bourquin, Clemens Claudio Christoph
- Published: 2026-06-12T15:38:34Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
