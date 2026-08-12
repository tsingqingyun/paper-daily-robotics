---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23589v1"
published: "2026-06-22T16:57:43Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies

## 为什么重要

自动筛选分数：31

连接概念：[[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Long-horizon robot manipulation remains challenging because similar observations may
occur at different execution stages, while the appropriate action depends on previously
completed operations. Memory can address this ambiguity by enabling policies to infer
task progress from execution history. However, existing memory-augmented approaches
often either retain dense histories that require compression or rely primarily on recent
context that may discard earlier task-relevant events. In this work, we propose propose
KEMO, a lightweight plug-in memory framework that automatically selectively preserves
keyframes associated with task-relevant state changes for VLA policies. KEMO combines
robot kinematics with visual filtering to detect events, encodes the selected keyframes
as compact temporally ordered memory tokens, and integrates them with current visual
features through cross-attention and gated residual fusion for VLA training. The
detected events also define higher-weight training samples near critical transitions. We
evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored
subtasks, and trajectory length ranging from 830 steps to 2846 execution steps
(durations from 28 to 95 seconds). Compared with the memory-free baseline (e.g.,
$π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion
Rate by 34.1\%. Ablations show that event-driven keyframe selection outperforms uniform
sampling and recent-frame retention, while the proposed gated fusion and keyframe-
aligned loss weighting provide complementary gains.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23589v1
- Authors: Yihan Zeng, Minghao Ye, Yiyuan Chen, Yide Shentu, Philipp Wu, Zike Yan, Zhongyu Li
- Published: 2026-06-22T16:57:43Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
