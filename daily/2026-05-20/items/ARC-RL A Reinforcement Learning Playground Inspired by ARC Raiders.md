---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19503v1"
published: "2026-05-19T07:54:40Z"
age_days: 0
score: 34
created: 2026-05-20
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders

## 为什么重要

自动筛选分数：34

连接概念：[[世界模型]], [[机器人学习]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Reinforcement learning for legged locomotion has matured into a stack of multi-component
reward functions and physics-engine benchmarks whose morphologies are uniformly derived
from real commercial hardware. Game NPCs, however, are bound by stylistic constraints
absent from sim-to-real robotics and routinely take the form of creatures with no real-
robot counterpart. We introduce ARC-RL, a suite of four MuJoCo continuous-control
environments featuring robotic morphologies inspired by the bestiary of ARC Raiders: the
18-DoF tall hexapod Queen, the 12-DoF armoured hexapod Bastion, the 18-DoF compact
hexapod Tick, and the 12-DoF quadruped Leaper. All four robots share a unified
observation template, action convention, simulation cadence, and a single closed-form
multi-component reward function whose only per-morphology variation lives in a small set
of weights and parameters. The reward fuses a velocity-tracking tent, a healthy survive
bonus, a phase-locked gait-compliance bonus/cost pair, action regularisers, three safety
penalties, and a posture anchor; no motion-capture data enters the reward at any point.
We additionally provide hand-crafted Central Pattern Generator demonstrators per
morphology, which serve both as fixed expert references and as sources of prior data for
offline-to-online training. On this playground, we conduct a controlled empirical study
comparing standard online algorithms (SAC, SPEQ, SOPE-EO) and methods augmented with
prior data (SACfD, SPEQ-O2O, SOPE), and characterise how each paradigm copes with the
playground's morphological diversity and animation-style stylistic constraints.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19503v1
- Authors: Carlo Romeo, Andrew D. Bagdanov
- Published: 2026-05-19T07:54:40Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
