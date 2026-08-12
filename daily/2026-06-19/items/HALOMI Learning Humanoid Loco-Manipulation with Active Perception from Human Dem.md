---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18772v1"
published: "2026-06-17T07:33:37Z"
age_days: 1
score: 28
created: 2026-06-19
concepts: ["机器人学习", "具身智能评测与基准"]
---

# HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations

## 为什么重要

自动筛选分数：28

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Human demonstrations, which can be collected at scale and naturally capture active hand-
eye coordination, are a promising data source for learning humanoid loco-manipulation.
However, directly transferring human demonstrations to humanoids requires a precise
world-frame tracking controller, which is often brittle under Out-of-Distribution(OOD)
targets, while human-to-humanoid gaps persist in both egocentric observation and action
execution. To address these challenges, we present HALOMI, a scalable framework for
learning humanoid loco-manipulation with active perception from human demonstrations.
HALOMI extends Universal Manipulation Interface (UMI) with egocentric sensing to collect
ego-view and wrist-view observations along with head-hand trajectories at scale. We
further propose a manifold-constrained controller that plans in a learned latent
behavior manifold to enable precise and robust head-hand tracking in the world frame. To
bridge the human-to-humanoid gap, we perform ego-view alignment and introduce a
controller-aware reference trajectory adaptation to reduce mismatch in both observation
and action execution. We validate HALOMI on a Unitree G1 humanoid robot with an actuated
neck across five real-world tasks involving navigation, grasping, bimanual manipulation,
whole-body coordination, and dynamic behaviors. Across the three quantitatively
evaluated tasks, HALOMI achieves an average success rate of 85\%, while additional
qualitative demonstrations show its ability to support dynamic tossing and deep-squat
grasping.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18772v1
- Authors: Zehui Zhao, Yuxuan Zhao, Gaojing Zhang, Chenxi Liu, Maolin Zheng, Wenzhao Lian
- Published: 2026-06-17T07:33:37Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
