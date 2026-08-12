---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18060v1"
published: "2026-07-20T15:27:13Z"
age_days: 1
score: 29
created: 2026-07-22
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Long-horizon robotic tasks require diverse capabilities that no single policy can
reliably provide. Heterogeneous policies offer complementary strengths, but
orchestrating them requires reasoning over uncertain capability boundaries and cross-
policy distribution mismatch, which are largely overlooked by existing planning methods
built on homogeneous, predefined skills with fixed applicability. We propose
RoboHarness, a unified framework that encapsulates independently developed robot control
systems as reusable agentic skills. Although instantiated in this work with VLAs, RL
policies, and task-and-motion planning (TAMP) systems, RoboHarness is designed as a
general framework compatible with a broader range of robot policies, such as navigation
policies, model predictive controllers, and world-action models. RoboHarness uses multi-
modal execution memory and online evidence to characterize policy capability boundaries
for capability-aware decomposition and routing. To stabilize policy handoffs, its Memory
Bridge retrieves execution trajectories associated with the next policy, estimates its
in-distribution state region, and guides the robot toward that region without joint
policy retraining. Extensive experiments on three public benchmarks, 500 customized
tasks, and 135 real-robot experiments demonstrate effective capability-aware routing and
stable policy orchestration, yielding substantial improvements in zero-shot long-horizon
planning and out-of-distribution robustness.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18060v1
- Authors: Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang
- Published: 2026-07-20T15:27:13Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
