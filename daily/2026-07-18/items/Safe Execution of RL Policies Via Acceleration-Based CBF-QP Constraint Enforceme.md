---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14488v1"
published: "2026-07-16T02:00:11Z"
age_days: 1
score: 30
created: 2026-07-18
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments

## 为什么重要

自动筛选分数：30

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Reinforcement Learning (RL) has demonstrated remarkable capabilities for solving complex
robotic control problems, but its lack of safety guarantees severely limits deployment
on hardware. In particular, as legged robots and manipulators often operate near safety-
critical boundaries, out-of-distribution states can lead to failure upon deployment. To
address this, we introduce Acc-CBF-QP, an acceleration-based Quadratic Program (QP)
safety filter using Control Barrier Functions (CBFs) that constrains any RL policy onto
a safe set at runtime without modifying training. The method applies to unconstrained
and Safe-RL policies, and enforces joint position, velocity, torque, and collision
constraints within a unified optimization framework. A key contribution is the
formulation of RL+QP tasks that regulate deviation from the RL command when constraints
would otherwise be violated. We introduce a TorqueTask, minimizing torque deviation, and
a Forward Dynamics Task, minimizing induced acceleration deviation, thus providing
principled control over safety-performance trade-offs. Experiments on a 7-DoF Kinova
Gen3 manipulator and a 19-DoF Unitree H1 humanoid, both in simulation and on hardware,
highlight substantial reductions in constraint violations. On the real H1 hardware, a
Safe-RL policy alone yielded 10.04 violations/s, which were reduced by 92% to 0.80
violations/s when augmented with Acc-CBF-QP. On the Kinova Gen3, Acc-CBF-QP fully
eliminated violations. Nominal task performance of the RL objective is preserved in
violation-free regimes. Under aggressive velocity commands on H1, Acc-CBF-QP improves
execution by preventing constraint-induced shutdowns, yielding longer survival times.
The full pipeline is open-source.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14488v1
- Authors: Bastien Muraccioli, Alice Cariou, Pierre-Alexandre Leziart, Mathieu Celerier, Arnaud Demont, Gentiane Venture, Mehdi Benallegue
- Published: 2026-07-16T02:00:11Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
