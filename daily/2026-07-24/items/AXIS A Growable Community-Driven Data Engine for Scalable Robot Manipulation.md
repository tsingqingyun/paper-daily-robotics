---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21588v1"
published: "2026-07-23T17:58:08Z"
age_days: 0
score: 38
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learning effective robot manipulation policies requires diverse, high-quality
demonstrations, yet existing data pipelines are often difficult to scale because they
rely on specialized hardware, centralized operators, or fixed task suites. We present
AXIS, a growable community-driven data engine and benchmark for scalable robot learning,
which enables browser-based teleoperation for large-scale demonstration collection,
automatically generates and validates new manipulation tasks, and transforms community-
collected demonstrations into training-ready data through automated success checking,
quality filtering, trajectory smoothing, and visual and physics-based augmentation. The
AXIS dataset currently contains 207 diverse tasks and 50K+ trajectories. Meanwhile, AXIS
organizes data into task snapshots and evaluates policies with a systematic held-out
protocol. We compare vision-language-action (VLA) policies under a unified AXIS
evaluation suite and analyze scaling behavior across different data volumes. Continual
pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by
5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent
scaling with increasing data volume, with the largest gains observed under layout,
sensor-noise, and camera perturbations.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21588v1
- Authors: Mengfei Zhao, Dihong Huang, Yikai Tang, Peihao Li, Mingxuan Yan, Ruiqi Zhuang, Yanjia Huang, Jie Wang, Hai Zhai, Tony Zhou, Rui Zhang, Zhexi Luo, Yuchen Huang, Jianfei Yang, Jiachen Li
- Published: 2026-07-23T17:58:08Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
