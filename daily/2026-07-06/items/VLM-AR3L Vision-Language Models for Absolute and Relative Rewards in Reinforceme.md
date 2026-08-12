---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00483v2"
published: "2026-07-01T06:11:59Z"
age_days: 5
score: 28
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Designing effective reward functions remains a major challenge in reinforcement learning
(RL), particularly in open-ended environments where task goals are abstract and
difficult to quantify. In this work, we present VLM-AR3L, a framework that leverages
Vision-Language Models (VLMs) to provide both absolute and relative rewards for RL. VLM-
AR3L interprets an agent's visual observations in the context of a natural language task
goal, and learns both absolute and relative rewards from VLM-generated preference
labels. The absolute reward model predicts scalar evaluations for individual states,
while the relative reward model compares consecutive observations to infer progress or
regression toward the task goal. Their integration combines the stability of state-based
evaluation with the robustness of comparative supervision. We evaluate VLM-AR3L across
benchmarks spanning classic control, manipulation, and open-world embodied tasks, with a
particular focus on Minecraft given its visual complexity and long-horizon decision-
making requirements. Experimental results show that VLM-AR3L consistently outperforms
prior VLM-based reward learning methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00483v2
- Authors: Kuan-Chen Chen, Winston Chen, Wei-Fang Sun, Min-Chun Hu
- Published: 2026-07-01T06:11:59Z
- Age days: 5

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
