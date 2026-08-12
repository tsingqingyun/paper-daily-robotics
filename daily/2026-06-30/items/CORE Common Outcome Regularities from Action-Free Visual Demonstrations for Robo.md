---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29517v1"
published: "2026-06-28T17:27:23Z"
age_days: 1
score: 29
created: 2026-06-30
concepts: ["机器人学习", "具身智能评测与基准"]
---

# CORE: Common Outcome Regularities from Action-Free Visual Demonstrations for Robot Manipulation

## 为什么重要

自动筛选分数：29

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Robot imitation learning often relies on costly robot demonstrations, while abundant
action-free visual demonstrations, such as human videos, are difficult to use because
they lack robot-executable actions and suffer from embodiment gaps. We propose CORE, a
policy learning framework that extracts Common Outcome Regularities from visual
demonstrations. Rather than transferring explicit actions across embodiments, CORE
exploits a key observation: although successful trajectories for the same task can be
diverse, their terminal states often share stable object configurations, spatial
relations, and contact constraints. CORE first trains a terminal outcome encoder with
contrastive and auxiliary temporal objectives, then aggregates successful terminal
embeddings into visual goal prototypes, and finally injects these prototypes as global
goal conditions into robot policies. Compared with language instructions, visual goal
prototypes provide more concrete geometric and physical constraints for task completion.
Across Meta-World, RoboTwin 2.0, and real-world manipulation, CORE improves the average
success rate of the corresponding policy backbones by up to +3.9, +11.1, and +17.0
percentage points, respectively, and outperforms text-conditioned variants under the
evaluated settings.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29517v1
- Authors: Juyi Sheng, Jincheng Li, Mingxin Tan, Mengyuan Liu
- Published: 2026-06-28T17:27:23Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
