---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20653v1"
published: "2026-07-22T18:25:57Z"
age_days: 2
score: 26
created: 2026-07-25
concepts: ["世界模型"]
---

# PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics

## 为什么重要

自动筛选分数：26

连接概念：[[世界模型]]

## 摘要

Predicting how deformable objects evolve under robotic manipulation is a longstanding
challenge. Existing approaches typically rely on per-object optimization to fit material
parameters, which can be slow and cannot generalize, while end-to-end learned
alternatives extrapolate poorly and often violate basic physical structure. We present
PhysCoRe, a physics-corrected residual world model that couples a differentiable
Material Point Method (MPM) simulator with two feed-forward neural networks. A material
refinement module, Material from Motion (MfM), infers per-particle elasticity from
visual observations, grounding the simulator in object-specific physics. A residual
correction module, Residual from Dynamics (RfD), learns the discrepancy and predicts
corrections to the simulator's internal dynamics, absorbing systematic biases that the
analytical model cannot capture. This design also supports online material
identification on novel objects. MfM adapts from limited interactions, and its
predictive uncertainty steers further exploration toward the regions where its estimate
is least confident. Experiments on real deformable-object manipulation sequences show
that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that
its predicted confidence forms a reliable distribution across the object's geometry,
providing a natural signal for future confidence-guided exploration.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20653v1
- Authors: Haocheng Yin, Shuohan Tao, Yongsheng Chen, Lu Gan
- Published: 2026-07-22T18:25:57Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
