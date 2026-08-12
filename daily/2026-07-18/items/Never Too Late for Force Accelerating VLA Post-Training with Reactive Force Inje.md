---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14236v1"
published: "2026-07-15T18:01:05Z"
age_days: 2
score: 33
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Pretrained vision-language-action (VLA) policies provide strong language-conditioned
manipulation knowledge, but they remain largely vision-driven and can struggle once
manipulation enters contact states where the scene is occluded, depth is ambiguous, or
small force errors push execution off the offline demonstration distribution. We present
LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-
training framework that adds contact reactivity to a pretrained VLA policy while
preserving its general manipulation knowledge. LIFT grafts a reactive action expert
beside the original action expert, initializes it from pretrained action weights, and
injects recent 6D end-effector force through causal force memory and zero-initialized
cross attention, enabling actions to be refreshed during execution. To address the
policy-dependent distribution shift of contact feedback, LIFT further couples reactive
force injection with an online DAgger loop that trains on a mixture of offline task-
alignment data and human-corrected online rollouts. Across towel folding, book
insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance
than vision-only post-training, while ablations show that reactive force memory and
online corrective data are both important for robust contact-rich manipulation. Our code
and data will be publicly available.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14236v1
- Authors: Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li, Wenye Yu, Zhijie Chen, Hao Yang, Jun Lv, Chuan Wen, Cewu Lu
- Published: 2026-07-15T18:01:05Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
