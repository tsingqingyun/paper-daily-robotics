---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13092v1"
published: "2026-06-11T09:21:28Z"
age_days: 2
score: 27
created: 2026-06-14
concepts: ["世界模型", "具身智能评测与基准"]
---

# Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models

## 为什么重要

自动筛选分数：27

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Scale buys interpolation; structure buys a certified horizon. A world model's average
error says nothing about whether a particular prediction can be trusted, or for how
long. For equivariant latent world models we give a computable, multi-step certificate
of the predictable horizon: $T$-step rollout error is provably constant over each
symmetry orbit (Theorem A) and stratified channel-by-channel by the predictor's Lyapunov
spectrum, $T_j(ε)\sim\log(1/ε)/λ_j$. The horizon is two-sided -- a matching lower bound
makes approximate equivariance provably horizon-limited -- and the certificate is
exclusive to structure: orbit-constant error characterizes equivariance, so no non-
equivariant model has it at any scale. Empirically, on 40-D Lorenz-96 only a
$\mathbb{Z}_N$-equivariant network recovers the full Lyapunov spectrum ($R^2{=}0.98$);
dense and recurrent baselines fail. Because the spectrum is faithful, the certificate
acts, a priori: under a fixed sensing budget a $c\times$-inflated certificate provably
needs $c\times$ the budget, and the equivariant certificate meets a budget its inflated
dense counterpart cannot -- with zero calibration data. The same read-out, unchanged,
audits public pretrained world models training-free: TD-MPC2 checkpoints land on the
certificate's own scope taxonomy -- calibrated where strongly expansive (ratio
0.94-1.02), optimistic where weakly expansive, correctly abstaining where contracting --
a map a deployed monitor replicates cell-by-cell, out-of-sample. Across the official
1M-317M multitask ladder, calibration does not improve with parameters. On V-JEPA 2-AC
(1B, real robot data) the measured cross-check correctly overrides an over-promising
tangent spectrum -- the cross-validated audit, not the raw number, is the deployable
object. Scale buys interpolation, not a calibrated horizon.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13092v1
- Authors: Hongbo Wang
- Published: 2026-06-11T09:21:28Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
