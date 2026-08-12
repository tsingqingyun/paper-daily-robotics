---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13681v1"
published: "2026-07-15T10:24:51Z"
age_days: 1
score: 30
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Towards Spatial Supersensing in the Wild

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Humans can efficiently parse continuous sensory streams, from hours to years,
scaffolding an internal world model that grounds spatial reasoning and prediction. To
mimic this capacity, spatial supersensing challenges multimodal models to move beyond
linguistic understanding toward true world modeling. However, their benchmark relies on
synthetic long videos, formed by concatenating random short clips, and is mostly limited
to household scenes, leaving real-world continuity and diversity underexplored. To
address the gap, we introduce $\textbf{VSI-Super-Wild}$, a large-scale benchmark for
evaluating spatial supersensing over long temporal horizons in diverse in-the-wild
scenes. Notably, inspired by cognitive studies on how humans structure experience, we
systematically probe the full triad of world state: the agent (observer), objects (scene
items), and the environment (places and global layout). In total, VSI-Super-Wild
contains $\textbf{6,980}$ human-verified question-answer pairs derived from
$\textbf{442}$ real-world videos spanning 8 scene categories, including long-form
recordings exceeding 4 hours. Results on VSI-Super-Wild expose a fundamental disconnect:
despite advances in static image understanding, models consistently fail at tasks that
require coherent world-state tracking over time. We characterize how performance
degrades with world-state complexity and temporal horizon, and diagnose four failure
modes: spatial collapse, semantic shortcuts, insufficient update, and instance
confusion. This taxonomy reveals that models lack mechanisms to bind objects, agents,
and environments into a unified spatial world model, a fundamental gap that defines the
path forward for spatial supersensing.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13681v1
- Authors: Tianjun Gu, Tianyu Xin, Kuan Zhang, Bowen Yang, Kok-Chung Chua, Peize Li, Xinran Zhang, Yupeng Chen, Qiyue Zhao, Qinlei Xie, Jianhang Liu, Yucheng Lu, Yinan Han, Marco Pavone, Yiming Li
- Published: 2026-07-15T10:24:51Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
