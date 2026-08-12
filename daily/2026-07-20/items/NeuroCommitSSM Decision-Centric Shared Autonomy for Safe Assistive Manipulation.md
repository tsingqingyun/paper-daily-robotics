---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15395v1"
published: "2026-07-16T18:49:44Z"
age_days: 3
score: 26
created: 2026-07-20
concepts: ["智能体 Agent"]
---

# NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG-EMG-ET Commit Readiness

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]]

## 摘要

We present NeuroCommitSSM, a decision-centric framework that models when to execute, not
just what to do, for safe commit-to-execute control in assistive robotic manipulation.
NeuroCommitSSM predicts a continuous commit-readiness score c_t in [0,1] from
synchronized electroencephalography (EEG), electromyography (EMG), and eye-tracking
(ET), and converts it into discrete commit events through dwell and hysteresis
filtering. A three-state finite-state supervisor, HOLD-ASSIST-COMMIT (HAC), gates
execution by requiring both a sustained commit-readiness signal from the neural model
and real-time perception and robot-state feasibility, including target visibility,
inverse kinematics solvability, and collision-free planning, before initiating motion.
We evaluate the framework on N=32 subjects performing five activities of daily living
(ADL) tasks aligned with the International Classification of Functioning, Disability and
Health (ICF), using leave-one-subject-out (LOSO) cross-validation and seven sensor-
dropout scenarios (S0-S6). NeuroCommitSSM achieves 0.950 action-balanced accuracy with
0.75 false commit events per 1000 REST windows (FP/1k REST), and maintains low false
commits and stable state transitions under sensor loss. For example, in the EEG-only
condition, it achieves 0.785 balanced accuracy and 0.29 FP/1k REST, whereas the Temporal
Convolutional Network baseline produces 99.95 FP/1k REST under the same condition.
Hardware-in-the-loop (HIL) validation on a Kinova Gen3 arm shows that feasibility-
checked execution reduces false starts and decision instability without sacrificing task
success. Supplementary materials, including code, datasets, videos, and additional
analyses, are available at https://madibabaiasl.github.io/NeuroCommitSSM/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15395v1
- Authors: Tipu Sultan, Param Sangani, Kody Cool, Pascal Sikorski, Guangping Liu, Hadi Akbarpour, Madi Babaiasl
- Published: 2026-07-16T18:49:44Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
