---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18016v1"
published: "2026-07-20T14:52:46Z"
age_days: 1
score: 38
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action policies are a promising foundation for general robot control,
but long-horizon humanoid loco-manipulation requires the robot to treat task objects as
persistent physical entities across movement, contact, occlusion, and recovery. We study
this problem as object-state divergence: the object state used to condition a whole-body
action can differ from the state used to decide whether the action achieved the intended
physical relation. We propose \emph{Persistent Object Tokenization} (POT), which
maintains role-indexed 3D object records from RGB-D observations and converts them into
object tokens for a whole-body action expert. Instantiated as \emph{POT-VLA}, the same
object records condition action generation and support geometric predicate checks,
yielding a closed-loop execution system in which object state is both actionable and
verifiable. On a Unitree G1, POT-VLA improves a matched direct GR00T-N1.7 baseline from
39/80 to 71/80 successes over eight real-world task families. In an external
Being-0-aligned reference, POT-VLA achieves 44/50 successes on aligned service tasks,
compared with the 37/50 success reported by the Being-0 paper. The largest gains occur
on tasks requiring maintained 3D relations, suggesting that persistent object-centered
state is a useful abstraction for verifiable humanoid VLA execution.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18016v1
- Authors: Peng Ren, Haoyang Ge, Jiang Zhao, Cong Huang, Yukun Shi, Pei Chi, Kai Chen
- Published: 2026-07-20T14:52:46Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
