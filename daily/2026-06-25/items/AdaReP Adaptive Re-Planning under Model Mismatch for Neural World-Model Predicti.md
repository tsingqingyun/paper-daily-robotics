---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23079v1"
published: "2026-06-22T09:27:50Z"
age_days: 2
score: 29
created: 2026-06-25
concepts: ["智能体 Agent", "世界模型"]
---

# AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Neural world models coupled with model predictive control (MPC) replan at every
environment step to bound accumulated prediction error, but this incurs substantial
computational overhead. Reusing a cached plan reduces this overhead, yet its
effectiveness depends on how prediction mismatch propagates through the local dynamics.
We analyze this trade-off with a perturbation-based dynamic-regret framework and show
that stale-plan penalties scale with the reuse tolerance, the accumulated mismatch since
the last replanning step, and the local dynamics sensitivity. Based on this structure,
we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online
using the current deviation from the cached rollout and a local sensitivity estimate,
without modifying the learned world model or planner. Across image-space planning,
latent-space control, and real-world robotic manipulation, AdaReP substantially reduces
planner-side computation while maintaining comparable task performance, including over
80% fewer queries on a 50-trial physical robot study.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23079v1
- Authors: Yutian Cheng, Xiaojian Ma, Xianhao Wang, Min Yang, Rongpeng Su, Hangxin Liu, Xi Chen, Shuai Li, Qing Li
- Published: 2026-06-22T09:27:50Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
