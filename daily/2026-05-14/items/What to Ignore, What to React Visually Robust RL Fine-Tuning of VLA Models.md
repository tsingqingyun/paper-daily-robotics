---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13105v1"
published: "2026-05-13T07:15:37Z"
age_days: 0
score: 34
created: 2026-05-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Reinforcement learning (RL) fine-tuning has shown promise for Vision-Language-Action
(VLA) models in robotic manipulation, but deployment-time visual shifts pose practical
challenges. A key difficulty is that standard task rewards supervise task success, but
offer limited guidance on whether a visual change is task-irrelevant or changes the
behavior required for manipulation. We propose PAIR-VLA (Paired Action Invariance &
Sensitivity for Visually Robust VLA), an RL fine-tuning framework to address this
difficulty by adding two auxiliary objectives over paired visual variants during PPO
optimization: an invariance term that reduces the discrepancy between action
distributions for a task-preserving pair (e.g., different distractors), and a
sensitivity objective that encourages separable action distributions for a task-altering
pair (e.g., target object in a different pose). Together, these objectives turn visual
variants from mere observation diversity into behavior-level guidance on policy
responses during RL fine-tuning. We evaluate on ManiSkill3 across two representative VLA
architectures, OpenVLA and $π_{0.5}$, under diverse out-of-distribution visual shifts
including unseen distractors, texture changes, target object pose variation, viewpoint
shifts, and lighting changes. Our method consistently improves over standard PPO,
achieving average improvements of 16.62% on $π_{0.5}$ and 9.10% on OpenVLA. Notably,
ablations further show generalization across visual shifts: invariance guidance learned
from distractor and texture variants transfers to target-pose and lighting shifts, while
adding sensitivity guidance on target-pose variants further improves robustness to
nuisance shifts, highlighting the broader transferability of behavior-level RL guidance.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13105v1
- Authors: Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian, Mingyu Liu, Ling Zhang, Jun Zhang, Rui Wang
- Published: 2026-05-13T07:15:37Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
