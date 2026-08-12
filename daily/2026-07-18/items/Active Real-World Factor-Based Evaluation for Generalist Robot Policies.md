---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14439v1"
published: "2026-07-16T00:21:54Z"
age_days: 1
score: 33
created: 2026-07-18
concepts: ["具身智能评测与基准"]
---

# Active Real-World Factor-Based Evaluation for Generalist Robot Policies

## 为什么重要

自动筛选分数：33

连接概念：[[具身智能评测与基准]]

## 摘要

Generalist robot manipulation policies trained on large, diverse datasets have shown
remarkable promise across a wide range of tasks. However, rigorously evaluating these
policies remains a fundamental challenge. Real-world performance depends on a large
combinatorial space of task factors including object poses and camera viewpoints, making
full, exhaustive evaluation intractable. Additionally, real hardware evaluation is slow
and resource-intensive, so current practice is to use narrow test suites that can miss
critical failure modes and misrepresent true deployment readiness. We propose an active
evaluation framework that addresses this challenge by treating policy evaluation as a
sequential experimental design problem. Our approach fits a probabilistic surrogate
model over a structured space of task factors and adaptively selects evaluation
configurations to maximize information gain over the policy's performance distribution,
allowing for sample-efficient characterization of policy behavior across unseen
conditions and a systematic identification of failure-prone regions. We conduct 2331
real-world evaluations across 3 tasks with 3 factor variations and find that our
approach typically saves the evaluator at least 20-40% of trials compared to typical
random testing.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14439v1
- Authors: Andrew Liao, Hanchen Cui, Karthik Desingh, Aryan Deshwal
- Published: 2026-07-16T00:21:54Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
