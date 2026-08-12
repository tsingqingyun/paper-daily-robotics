---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09215v1"
published: "2026-06-08T08:50:14Z"
age_days: 1
score: 38
created: 2026-06-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

World Action Models (WAMs) couple a video dynamics prior to the policy and have shown
encouraging results on tabletop manipulation, but iterative denoising over high-
dimensional video-action latents leaves them too slow for real-time humanoid loco-
manipulation. The problem is compounded by the dominant hierarchical paradigm, in which
a high-level manipulation policy controls only the upper body while a low-level
controller tracks coarse base commands -- placing upper and lower body in inconsistent
action spaces and reducing the legs to balance-preserving locomotion. We present
MotionWAM, a real-time WAM that drives autonomous humanoid loco-manipulation from a
single egocentric camera by conditioning the policy on the intermediate denoising
features of a video world model. MotionWAM replaces the upper-lower split with a unified
motion latent and predicts whole-body motion tokens that jointly cover locomotion, torso
motion, height regulation, foot interaction, and hand manipulation in a single action
space. A three-stage learning framework progressively adapts the video world model to
egocentric visual dynamics and to the target humanoid embodiment. On nine real-world
Unitree G1 tasks, MotionWAM runs in real time, substantially outperforms Vision-
Language-Action (VLA) baselines fine-tuned on the same demonstrations by over 30% in
overall success rate, and executes task-driven foot interaction that decoupled upper-
lower policies cannot reach. Our results suggest that video-pretrained WAMs can be
lifted from tabletop manipulation to coordinated, human-like whole-body humanoid
control.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09215v1
- Authors: Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang, Junwei Liang
- Published: 2026-06-08T08:50:14Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
