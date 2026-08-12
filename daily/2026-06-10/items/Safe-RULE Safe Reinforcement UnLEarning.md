---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09559v1"
published: "2026-06-08T14:33:40Z"
age_days: 1
score: 32
created: 2026-06-10
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Safe-RULE: Safe Reinforcement UnLEarning

## 为什么重要

自动筛选分数：32

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Offline safe reinforcement learning (Safe RL) enables policy learning without online
interactions, making it suitable for safety-critical systems such as robotics systems.
However, its reliance on static datasets exposes offline Safe RL to data poisoning
attacks, where adversaries inject malicious samples that compromise safety and induce
unsafe policy behavior. In this work, we propose a new learning paradigm, named safe
reinforcement unlearning (Safe-RULE), used as a defense framework to remove the
influence of poisoned data without retraining from scratch or requiring access to the
original training environment. We further extend reinforcement unlearning to offline
Safe RL by explicitly accounting for both task performance and safety constraints during
the unlearning process. Experiments across benchmark Safe RL tasks demonstrate that our
approach effectively enhances safety performance against data poisoning attacks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09559v1
- Authors: Shixiong Jiang, Taozheng Zhu, Fanxin Kong
- Published: 2026-06-08T14:33:40Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
