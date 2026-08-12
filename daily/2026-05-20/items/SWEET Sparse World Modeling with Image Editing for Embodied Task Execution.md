---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19319v1"
published: "2026-05-19T03:54:46Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["智能体 Agent", "世界模型"]
---

# SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Visual prediction has emerged as a promising paradigm for embodied control, where future
observations are generated and then translated into actions. However, dense video
generation is computationally expensive and often unnecessary for many manipulation
tasks, whose progress can be summarized by a small number of task-relevant visual
states. In this work, we study whether image editing models can serve as sparse visual
world models for robot manipulation by predicting task-level future states without dense
video rollout. We first conduct a controlled comparison between the video generation
model Wan2.2 and the image editing model FLUX-Kontext under the same robotic data
setting, and find that image editing produces more reliable task-level keyframes with
better visual fidelity and substantially lower inference cost. Motivated by this
observation, we propose SWEET, a one-shot sparse visual planning framework that
progressively generates a sequence of task-relevant manipulation keyframes through
successive image editing, conditioned on language instructions and optional arrow-based
spatial guidance. A goal-conditioned diffusion action predictor then converts adjacent
imagined keyframes into executable action chunks. To reduce the mismatch between real
and edited visual subgoals, we further introduce a mixed-training strategy with filtered
edited targets. Experiments on DROID and RoboMimic show that SWEET improves keyframe
prediction across seen and unseen scenes and enables a full pipeline from sequential
keyframe planning to executable robot actions, suggesting that image editing is a
promising and underexplored direction for embodied visual prediction.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19319v1
- Authors: Yiren Song, Yihan Wang, Xiyao Deng, Zhuoran Yan, Mike Zheng Shou
- Published: 2026-05-19T03:54:46Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
