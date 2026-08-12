---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13548v1"
published: "2026-05-13T13:55:37Z"
age_days: 0
score: 41
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AttenA+: Rectifying Action Inequality in Robotic Foundation Models

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Existing robotic foundation models, while powerful, are predicated on an implicit
assumption of temporal homogeneity: treating all actions as equally informative during
optimization. This "flat" training paradigm, inherited from language modeling, remains
indifferent to the underlying physical hierarchy of manipulation. In reality, robot
trajectories are fundamentally heterogeneous, where low-velocity segments often dictate
task success through precision-demanding interactions, while high-velocity motions serve
as error-tolerant transitions. Such a misalignment between uniform loss weighting and
physical criticality fundamentally limits the performance of current Vision-Language-
Action (VLA) models and World-Action Models (WAM) in complex, long-horizon tasks. To
rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes
kinematically critical segments via velocity-driven action attention. By reweighting the
training objective based on the inverse velocity field, AttenA+ naturally aligns the
model's learning capacity with the physical demands of manipulation. As a plug-and-play
enhancement, AttenA+ can be integrated into existing backbones without structural
modifications or additional parameters. Extensive experiments demonstrate that AttenA+
significantly elevates the ceilings of current state-of-the-art models. Specifically, it
improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to
92.4% (+0.6%) on RoboTwin 2.0. Real-world validation on a Franka manipulator further
showcases its robustness and cross-task generalization. Our work suggests that mining
the intrinsic structural priors of action sequences offers a highly efficient, physics-
aware complement to standard scaling laws, paving a new path for general-purpose robotic
control.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13548v1
- Authors: Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie, Jian Guo, Ping Luo, Andrew F. Luo, Boyu Zhou, Jun Ma
- Published: 2026-05-13T13:55:37Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
