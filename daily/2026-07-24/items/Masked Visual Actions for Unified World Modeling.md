---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19343v1"
published: "2026-07-21T17:59:11Z"
age_days: 2
score: 29
created: 2026-07-24
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Masked Visual Actions for Unified World Modeling

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Video models absorb rich priors over how the visual world moves, interacts, and responds
to contact, making them promising substrates for robotic world modeling. The central
challenge is how to communicate action to such models in a form aligned with the visual
space in which they learned these interaction priors, yet still grounded in physical
manipulation. We introduce Masked Visual Actions, a pixel-space control interface that
expresses action as a partially revealed trajectory of an arbitrary entity in a video.
Revealing robot motion makes the model act as a forward dynamics model that predicts the
scene's response to low-level robot actions, while revealing desired object motion makes
the same model recover robot behavior consistent with that outcome. Finetuned with only
15 hours of masked examples from real videos and simulation, a single checkpoint
achieves strong visual fidelity and controllability across diverse scenes and multiple
embodiments. In downstream manipulation settings, the model produces imagined rollouts
whose outcomes correlate with real-world execution for policy evaluation, improves
decision making by ranking candidate futures in model-based planning, and supports
inverse modeling by synthesizing robot motion from desired object motion.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19343v1
- Authors: Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang, Maneesh Agrawala, Gordon Wetzstein, Li Fei-Fei, Yilun Du, Jiajun Wu, Jia-Bin Huang
- Published: 2026-07-21T17:59:11Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
