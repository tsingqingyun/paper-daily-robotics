---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08749v1"
published: "2026-08-09T14:53:19Z"
age_days: 1
score: 30
created: 2026-08-11
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Long-horizon robot manipulation requires policies to track completed subtasks and
critical interaction events. However, existing memory mechanisms heavily rely on
external models or predefined update rules. To address this, we propose OnEvoMemory, a
value-guided memory module for pretrained robot policies. It maintains recent context,
high-value experiences, and salient transitions, while learning which experiences should
be retained from trajectory outcomes. Offline demonstrations initialize the memory
prior, whereas successful and unsuccessful online rollouts refine memory selection,
helping the policy recognize task-stage transitions and avoid repeating completed
subtasks. Experiments on long-horizon manipulation benchmarks show that OnEvoMemory
improves the performance of the base VLA policy through both offline initialization and
online memory evolution.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08749v1
- Authors: Zhongxi Chen, Shenqi Zong
- Published: 2026-08-09T14:53:19Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
