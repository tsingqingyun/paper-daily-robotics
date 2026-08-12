---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18715v1"
published: "2026-07-21T05:13:26Z"
age_days: 3
score: 24
created: 2026-07-25
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# DWM: Separating World Effects from Actions in Latent World Models

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Latent world models underpin much of modern model-based control, yet current action-
conditioned formulations supervise the next-latent transition with a single,
undifferentiated target, forcing a monolithic learning signal to absorb every source of
state change. In real world, however, transitions arise from two heterogeneous sources:
an action-driven component induced by the agent, and an action-invariant world effect --
the change that would still occur under a null action, dictated by the environment's
intrinsic dynamics (e.g., gravity-driven sliding, inertia, contact rebound, and
persistent drift). Fusing them into a single target entangles the two inside the latent
transition, prevents the model from attributing observed changes to their underlying
causes, and undermines the transferability of the learned dynamics. We introduce DWM
(Decomposed World Model), a supervision-level framework that operationalizes this
decomposition. DWM augments the predictor of a latent world model with an auxiliary
world head, regularized by a normalized world-contrastive objective to be action-
invariant, while the original pred head is coupled to it via an orthogonality
constraint; together, the two signals induce an explicit additive decomposition of the
predicted transition into an action-invariant and a complementary action-driven
component, without altering the underlying architecture or inference pipeline. To
evaluate DWM under persistent world effects, we construct W-variants of three standard
control benchmarks -- PushT-W, Reacher-W, and TwoRoom-W -- each instantiating a distinct
action-invariant dynamic. DWM matches strong baselines on the flat counterparts and
delivers a mean absolute improvement of 13.1% in CEM planning success across the
W-variants.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18715v1
- Authors: Yi-Ge Zhang, Tianqi Du, Qi Zhang, Yisen Wang
- Published: 2026-07-21T05:13:26Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
