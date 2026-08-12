---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01410v1"
published: "2026-07-01T19:15:17Z"
age_days: 4
score: 25
created: 2026-07-06
concepts: ["世界模型", "Sim2Real"]
---

# BIFROST: Bridging Invariant Feature Representation for Observation-space Sim2Real Transfer

## 为什么重要

自动筛选分数：25

连接概念：[[世界模型]], [[Sim2Real]]

## 摘要

Sim2real transfer for robot policy learning suffers due to mismatch between simulation
and reality. Existing methods typically address each gap in isolation through separate
adaptation modules, which are composed or layered when both gaps coexist. Yet the basis
for attempting sim2real in the first place is that there is shared structure between a
task in simulation and reality, where equivalent actions from equivalent configurations
produce equivalent long term outcomes regardless of domain specific differences in
rendering or physics. In this paper, we study whether we can identify and exploit this
shared structure from raw observations to train a policy that enables zero shot
transfer. We introduce BIFROST, which learns a shared history encoder on paired cross-
domain data via cross-domain bisimulation objective: observation-action sequences
leading to equivalent long-term behavior are mapped to nearby latent states, regardless
of domain. Policies trained on these latent states in simulation transfer zero-shot to
reality. We provide empirical evidence on sim2sim visual navigation and sim2real contact
rich manipulation task and visual servoing task that BIFROST achieves effective transfer
where domain adaptation and co-training baselines fail under both visual and dynamics
domain gaps.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01410v1
- Authors: Yunfu Deng, Josiah P. Hanna
- Published: 2026-07-01T19:15:17Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
