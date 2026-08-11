---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09138v1"
published: "2026-08-10T05:31:41Z"
age_days: 1
score: 30
created: 2026-08-11
concepts: ["机器人学习", "具身智能评测与基准"]
---

# SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning

## 为什么重要

自动筛选分数：30

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

While learned robotic policies hold promise for advancing generalizable manipulation,
their practical deployment is often hindered by suboptimal execution speeds. Imitation
learning policies are inherently limited by hardware constraints and the speed of the
operator during data collection. In addition, there are no established methods for
accelerating policies learned via imitation, and the empirical relationship between
execution speed and task success remains underexplored. To address these issues, we
introduce SpeedTuning, a reinforcement learning framework specifically designed to
enhance the speed of manipulation policies. SpeedTuning learns to predict the optimal
execution speed for actions, thereby complementing a base policy without necessitating
additional data collection. We provide empirical evidence that SpeedTuning achieves
substantial improvements in execution speed, exceeding 2.4x speed-up, while preserving
an adequate success rate compared to both the original task policy and straightforward
speed-up methods such as linear interpolation at a fixed speed. We evaluate our approach
across a diverse set of dynamic and precise tasks, including pouring, throwing, and
picking, demonstrating its effectiveness and robustness in enhancing real-world robotic
manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09138v1
- Authors: David D. Yuan, Tony Z. Zhao, Kaylee Burns, Chelsea Finn
- Published: 2026-08-10T05:31:41Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
