---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20912v1"
published: "2026-07-23T04:46:19Z"
age_days: 1
score: 27
created: 2026-07-24
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning-based manipulation policies usually predict robot actions from sensory
observations and leave their execution to a separate low-level controller. In rigid
contact, this separation can be problematic: the same motion to a virtual target or
compliant motion command can lead to unstable contact, tracking error, excessive
loading, or tool damage, depending on the low-level controller. In this paper, we
propose a \textit{Unified Robot Control-Policy Framework} (URF), which connects
compliant action prediction with unified impedance-admittance control. Given multimodal
observations, URF predicts a virtual target, a stiffness matrix, and an impedance-
admittance switch ratio. The switch ratio determines when the controller should behave
more like admittance control for accurate motion tracking and when it should move toward
impedance control for safer rigid contact. Because demonstration data do not provide
ground-truth environment stiffness, we construct switch-ratio labels from measured
contact forces and use them to supervise controller-mode prediction. Across box-flipping
and line-pressing tasks, URF achieves higher task success rates while reducing failure
modes observed with admittance-only execution, including rapid force buildup, large
force oscillations, tool breakage, and robot safety stops. These results suggest that
contact-aware policies benefit from predicting not only compliant actions but also the
controller behavior used to execute them. Project page:
https://jiyou384.github.io/urf_project_page/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20912v1
- Authors: Jiyou Shin, Youngjin Seo, Jaeseog Won, Sungwon Seo, Hyunjun Kim, Seokmin Yoon, Tuan Luong, Hyungpil Moon
- Published: 2026-07-23T04:46:19Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
