---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02466v1"
published: "2026-07-02T17:33:37Z"
age_days: 0
score: 38
created: 2026-07-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of
expert demonstrations -- triplets of observations, instructions, and actions that are
costly to collect at scale. We argue that this bottleneck stems from conflating two
distinct learning objectives: acquiring physical competence (how to move) and acquiring
semantic alignment (what to do). Crucially, only the latter requires language
supervision. Building on this Decomposition Hypothesis, we propose Task-Agnostic
Pretraining (TAP), a two-stage framework that first learns transferable motor priors
from cheap, unlabeled interaction data -- including discarded off-task trajectories and
autonomous robot play -- via a self-supervised Inverse Dynamics objective. A lightweight
second stage then grounds these priors in language using minimal expert data. On the
SIMPLER benchmark, TAP matches models trained on over 1M expert trajectories while using
orders of magnitude less labeled data, yielding a 10% absolute gain over standard
behavior cloning. On a real-world WidowX platform, TAP retains 25% success under camera
perturbations where internet-scale baselines collapse to 0%, demonstrating that task-
agnostic pretraining produces robust, transferable physical representations and offers a
scalable path forward for Embodied AI.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02466v1
- Authors: Junhao Shi, Siyin Wang, Xiaopeng Yu, Li Ji, Jingjing Gong, Xipeng Qiu
- Published: 2026-07-02T17:33:37Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
