---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20785v1"
published: "2026-07-22T23:13:05Z"
age_days: 2
score: 26
created: 2026-07-25
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# Robostral Navigate

## 为什么重要

自动筛选分数：26

连接概念：[[多模态基础模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Deploying navigation systems at scale requires a recipe that minimizes sensor
assumptions, generalizes across robot embodiments, and trains efficiently. Yet, today's
best systems depend on depth sensors, multi-camera rigs, or pre-built maps, limiting the
hardware they support and increasing deployment cost. We introduce Robostral Navigate,
an 8B vision-language model built around this scalability objective. The model consumes
only a stream of monocular RGB images - the most ubiquitous sensor across robotic
platforms and predicts waypoints by pointing to the next target location in the current
camera view. Operating purely in image space, rather than robot-specific coordinates,
makes the policy naturally robust to changes in camera intrinsics and scene scale,
enabling deployment across wheeled, legged, and aerial robots without recalibration. We
generate 2.4 million trajectories across 350k simulated scenes to reduce the reliance on
real-world data collection and scale easily. We further introduce a prefix-caching
training recipe that packs entire episodes into single training sequences, reducing
training tokens by 22x and cutting training time from months to days. A tree-based
attention mask prevents conditioning on previous ground-truth actions, encouraging
visually grounded action prediction, and reinforcement learning is used to further
improve exploration and recovery capabilities. On the Room-to-Room and Room-Across-Room
in Continuous Environments (R2R-CE and RxR-CE) benchmarks, Robostral Navigate sets a new
state of the art. On R2R-CE, it achieves a 77.4% success rate, surpassing the best
monocular method by 10.5 points and the strongest depth- or multi-camera system by 5.3
points despite using only a single RGB camera. On RxR-CE, it reaches 75.1% success rate,
outperforming all monocular baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20785v1
- Authors: Arjun Majumdar, Avinash Sooriyarachchi, Benjamin Tibi, Chris Bamford, Elliot Chane-Sane, Guillaume Lample, Khyathi Raghavi Chandu, Ludovic Ho Fuh, Mathieu Poiree, Olivier Duchenne, Rosalie Millner, Srijan Mishra, Theo Cachet, Thomas Chabal
- Published: 2026-07-22T23:13:05Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
