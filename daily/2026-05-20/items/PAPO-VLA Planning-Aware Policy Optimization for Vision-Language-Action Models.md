---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19580v1"
published: "2026-05-19T09:22:49Z"
age_days: 0
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models show promising ability in language-guided robotic
tasks. However, making VLA policies reliable remains challenging, because a manipulation
task is completed through closed-loop interaction, where each action affects subsequent
execution. To analyze this problem, we revisit VLA policy during execution and argue
that a VLA policy acts both as a planner, which makes task-oriented decisions that
change the direction of execution, and as an executor, which realizes these decisions
through dense continuous actions. This view suggests that improving VLA reliability
requires particular attention to planning actions. Existing optimization methods can
imitate actions or improve complete trajectories, but they usually do not explicitly
identify planning actions or measure their importance for task success. To address this
issue, we propose Planning-Aware Policy Optimization for VLA models (PAPO-VLA). PAPO-VLA
first identifies planning actions by jointly considering action variation and trajectory
outcome, then estimates their importance through causal sufficiency and causal
necessity, and finally incorporates this importance into GRPO advantage estimation. In
this way, more important planning actions receive stronger optimization emphasis, while
the whole trajectory is still optimized by trajectory-level feedback. Experiments on
multiple benchmarks demonstrate the effectiveness of PAPO-VLA.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19580v1
- Authors: Peizheng Guo, Jingyao Wang, Changwen Zheng, Wenwen Qiang
- Published: 2026-05-19T09:22:49Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
