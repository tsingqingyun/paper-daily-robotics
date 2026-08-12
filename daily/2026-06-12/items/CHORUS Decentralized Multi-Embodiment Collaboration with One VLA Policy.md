---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12352v1"
published: "2026-06-10T17:26:08Z"
age_days: 1
score: 31
created: 2026-06-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Multi-robot collaboration allows robots to efficiently take on a wide range of tasks,
from moving a couch through a doorway to assembling structures on a construction site.
However, achieving such coordination in mobile multi-robot settings remains challenging:
centralized methods conditioned on the combined observations of a team scale poorly with
team size, and decentralized methods that train one policy per robot often require
explicit alignment procedures or information sharing at inference time to overcome
partial observability. Our key insight is that the visuomotor priors of pretrained
vision-language-action (VLA) models should enable reactive, decentralized collaboration
from each robot's local observations alone, without these inference-time assumptions. We
propose CHORUS, a framework that adapts a single VLA backbone to control diverse, multi-
robot teams. At inference time, each robot runs an independent copy of CHORUS,
conditioned only on its own observations and a robot-identifying prompt. In real-world
experiments including mobile tape measurement, library book handovers, and laundry
basket lifting, CHORUS achieves a 64% point improvement over decentralized, from-scratch
models, improves reactivity to teammate behavior by 40% points, and outperforms
centralized baselines. Together, these results show that a shared VLA backbone is
capable of achieving decentralized multi-robot collaboration, without per-robot policies
or inter-robot communication at inference.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12352v1
- Authors: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
- Published: 2026-06-10T17:26:08Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
