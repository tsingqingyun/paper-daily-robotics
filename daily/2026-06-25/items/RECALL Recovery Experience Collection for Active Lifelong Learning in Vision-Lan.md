---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23617v1"
published: "2026-06-22T17:12:50Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation
learning, where additional demonstrations are collected for tasks where the policy
performs poorly. This approach incurs several downsides: it requires the robot to fail
before data collection is triggered, provides little guidance about which states require
supervision, and wastes demonstrator effort on redundant parts of the task where the
policy already performs well. In this paper, we propose an active, continual learning
paradigm for VLAs. We demonstrate that active, uncertainty-guided data collection leads
to more efficient fine-tuning than when using passively-collected demonstrations.
However, we also find that fine-tuning only on actively-collected recovery data leads to
catastrophic forgetting. We evaluate techniques for continual learning, including
replay-based data mixing and elastic weight consolidation, and identify tradeoffs
between plasticity to uncertainty-guided recovery data and retention of previously
learned behaviors. Overall, our work contributes an empirical study of active continual
learning for autoregressive VLAs, establishing that uncertainty-guided recovery
demonstrations can improve adaptation efficiency while also revealing open challenges
when targeted new data is incorporated into large robot policies.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23617v1
- Authors: Ulas Berk Karli, Tesca Fitzgerald
- Published: 2026-06-22T17:12:50Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
