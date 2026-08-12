---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15701v1"
published: "2026-07-17T07:23:54Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Humanoid navigation in dynamic environments requires long-horizon planning while
respecting short-horizon dynamic and safety constraints. Classical visibility-graph
planners combined with model predictive control (MPC) can efficiently generate
collision-free trajectories, but their performance depends on manually tuned parameters
and accurate system modeling. In real robotic systems, control delays, state-estimation
noise, and locomotion uncertainties can cause overshoot and constraint violations even
when the nominal path is geometrically optimal. We propose RAVEN, a hierarchical
reinforcement learning (RL)-MPC framework for robust humanoid navigation. Unlike prior
approaches that use learning to tune cost weights or replace planning entirely, RAVEN
employs RL to adapt the geometric construction of a visibility-graph planner by
modifying obstacle inflation and related graph parameters. By directly reshaping the
free-space geometry, the learned planner alters the topology of the global path to
compensate for delay and tracking imperfections. A collision-free MPC layer then tracks
the planned trajectory while explicitly enforcing velocity bounds and obstacle-avoidance
constraints. By training under realistic delays and observation noise, RAVEN learns
planning adaptations that improve robustness while retaining explicit long-horizon
geometric planning and constrained optimization, in contrast to end-to-end learning
approaches. We evaluate RAVEN against a manually tuned visibility-graph MPC baseline and
a pure RL navigation policy. Results demonstrate reduced overshoot near obstacles,
improved robustness in narrow passages, and more reliable navigation under delay and
noise. These findings indicate that reinforcement-adaptive graph construction combined
with constrained MPC provides an effective and interpretable alternative to end-to-end
learning for robust humanoid navigation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15701v1
- Authors: Ruochen Hou, Shiqi Wang, Beom Jun Kim, Hanzhang Fang, Mehak Singal, Dennis W. Hong
- Published: 2026-07-17T07:23:54Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
