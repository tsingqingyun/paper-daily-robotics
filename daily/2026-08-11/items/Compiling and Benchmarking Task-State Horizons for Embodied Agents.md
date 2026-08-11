---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08036v1"
published: "2026-08-08T09:45:01Z"
age_days: 2
score: 28
created: 2026-08-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Compiling and Benchmarking Task-State Horizons for Embodied Agents

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Frontier agentic models are increasingly deployed as high-level planners for long-
horizon embodied tasks. Existing robotic benchmarks have advanced long-horizon
evaluation, but primarily characterize difficulty through action-sequence length and
subtask complexity, overlooking a distinct challenge: agents must track evolving task-
relevant world states induced by both their exploration and environmental dynamics. We
define the span of task-relevant state transitions that an agent must track as task-
state horizon (TSH). To evaluate how agent performance varies with TSH, we introduce
RoboGraph, a robotic task compiler that translates state-transition dependencies into
executable symbolic graphs. Specifically, RoboGraph constructs task-state horizons from
spatial and temporal causal dependencies, including those induced by unexpected failures
and interventions during task execution. Building on RoboGraph, we release a benchmark
comprising 588 episodes across 84 scenes with varying TSHs. Experiments evaluating 15
advanced agentic models in both semantic and visual closed-loop environments show that
most models struggle with demanding TSHs, revealing substantial gaps in maintaining,
exploring, and updating task-relevant state over long horizon.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08036v1
- Authors: Meiqi Wang, Shichao Li
- Published: 2026-08-08T09:45:01Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
