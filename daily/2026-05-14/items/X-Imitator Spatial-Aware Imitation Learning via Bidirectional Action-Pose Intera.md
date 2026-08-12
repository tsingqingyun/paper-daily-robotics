---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12162v1"
published: "2026-05-12T14:13:06Z"
age_days: 1
score: 29
created: 2026-05-14
concepts: ["机器人学习"]
---

# X-Imitator: Spatial-Aware Imitation Learning via Bidirectional Action-Pose Interaction

## 为什么重要

自动筛选分数：29

连接概念：[[机器人学习]]

## 摘要

Effectively handling the interplay between spatial perception and action generation
remains a critical bottleneck in robotic manipulation. Existing methods typically treat
spatial perception and action execution as decoupled or strictly unidirectional
processes, fundamentally restricting a robot's ability to master complex manipulation
tasks. To address this, we propose X-Imitator, a versatile dual-path framework that
models spatial perception and action execution as a tightly coupled bidirectional loop.
By reciprocally conditioning current pose predictions on past actions and vice versa,
this framework enables continuous mutual refinement between spatial reasoning and action
generation. This joint modeling exactly mimics human internal forward models. Designed
as a modular architecture, the system can be seamlessly integrated into various
visuomotor policies. Extensive experiments across 24 simulated and 3 real-world tasks
demonstrate that our framework significantly outperforms both vanilla policies and prior
methods utilizing explicit pose guidance. The code will be open sourced.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12162v1
- Authors: Kai Xiong, Hongjie Fang, Lixin Yang, Cewu Lu
- Published: 2026-05-12T14:13:06Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
