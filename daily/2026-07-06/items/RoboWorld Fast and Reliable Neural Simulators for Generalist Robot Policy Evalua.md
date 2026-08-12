---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01060v1"
published: "2026-07-01T15:22:41Z"
age_days: 4
score: 28
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Video world models are emerging as a scalable alternative for evaluating generalist
robot policies, bypassing the physical constraints and engineering burdens of real-world
deployment. However, evaluating policies with video world models remains challenging, as
world-model errors can make generated rollouts unreliable and slow inference limits
large-scale throughput. We introduce RoboWorld, an automated evaluation pipeline that
pairs a fast autoregressive video world model with a task-progress-aware vision-language
model scoring. To enable reliable long-horizon autoregressive world-model rollouts, we
propose Step Forcing, which combines anchored and one-step self-forwarded contexts to
reduce train--test mismatch while preserving action--observation dynamics. Together,
these components enable RoboWorld to align strongly with real-world robot evaluation
across tasks and environments, achieving Pearson's r = 0.989 and Spearman's \r{ho} =
0.970.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01060v1
- Authors: Byeongguk Jeon, Seonghyeon Ye, JaeHyeok Doo, Sungdong Kim, Minjoon Seo, Hyungmok Son, Kimin Lee
- Published: 2026-07-01T15:22:41Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
