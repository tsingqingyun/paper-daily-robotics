---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25782v1"
published: "2026-05-25T12:29:47Z"
age_days: 0
score: 26
created: 2026-05-26
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion

## 为什么重要

自动筛选分数：26

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Humanoid parkour requires locomotion policies to coordinate whole-body dynamics across
rapidly changing terrains such as stairs, gaps, slopes, and obstacles. Existing
reinforcement learning policies are largely reactive, mapping observations directly to
actions without explicitly modeling future body states. Such modeling becomes critical
in agile locomotion tasks where successful motion execution depends strongly on
anticipating upcoming contact transitions and body dynamics.We present ParkourFormer, a
Transformer-based sequence modeling framework that reformulates humanoid locomotion as a
future-conditioned decision-making problem. The current robot state queries historical
sensorimotor trajectories through cross-attention, while a lightweight prediction head
forecasts short-horizon future proprioceptive states. The predicted future states,
trained with supervised signals, are fused with temporal features to generate actions,
enabling the policy to jointly reason over motion history and anticipated future
dynamics. We evaluate ParkourFormer on a diverse multi-terrain humanoid parkour
benchmark including stairs, gaps, slopes, rough terrain, and obstacle traversal.
Experiments in simulation and on a real humanoid robot show that ParkourFormer achieves
a 93.85% average traversal success rate on highly challenging terrains, with
improvements of up to 42.73% over strong MLP, MoE-based MLP, and vanilla Transformer
baselines, while maintaining a single unified policy across all terrain types. These
results demonstrate that explicit future-state modeling significantly improves
robustness and generalization for agile whole-body locomotion.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25782v1
- Authors: Yanheng Mai, Wenhao Xu, Zirui Huang, Yifei Fu, Shengwei Dong, Xinjue Wang, Kailun Huang, Yanzhe Xie, Renjing Xu
- Published: 2026-05-25T12:29:47Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
