---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13817v1"
published: "2026-06-11T18:46:43Z"
age_days: 3
score: 29
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

World models in robot learning predict future states from visual observations and
actions, enabling agents to reason about the consequences of their controls. However,
many action-conditioned models are evaluated in settings where motion is dominated by
immediate control, whereas aquatic surface vehicles and other real-world objects
continue moving under inertia and are displaced by hidden ambient drift, such as water
currents or wind. We propose FlowMo-WM, an end-to-end trainable visual world model that
infers object-centric motion state and a predictive long-history context associated with
hidden drift from image-action histories without direct supervision of flow fields.
FlowMo-WM factorizes image-action history into a short-history latent state, trained to
summarize object-centric motion, and a longer-history context, trained to summarize
slowly varying exogenous influences. A zero-context residual transition separates
action-conditioned base dynamics from context-dependent drift effects during latent
rollout. In simulated aquatic surface-vehicle environments with diverse hidden flows,
disturbances, and randomized vehicle dynamics, FlowMo-WM improves long-horizon rollout
accuracy over representative action-conditioned latent world models. Prediction-time
context ablations, in which the inferred context is zeroed or shuffled during rollout,
show that the ambient context is important for stable prediction under hidden drift,
while frozen linear probes characterize information encoded in the learned factors.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13817v1
- Authors: Yitao Jiang, Luyang Zhao, Muhao Chen, Devin Balkcom
- Published: 2026-06-11T18:46:43Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
