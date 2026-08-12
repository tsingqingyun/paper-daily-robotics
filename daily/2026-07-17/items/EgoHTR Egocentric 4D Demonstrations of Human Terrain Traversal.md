---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13472v1"
published: "2026-07-15T06:02:41Z"
age_days: 1
score: 34
created: 2026-07-17
concepts: ["机器人学习", "具身智能评测与基准"]
---

# EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal

## 为什么重要

自动筛选分数：34

连接概念：[[机器人学习]], [[具身智能评测与基准]]

## 摘要

Deploying humanoid robots in unstructured terrain remains an open problem. While classic
reinforcement learning struggles with the sheer complexity of real-world interactions,
more promising methods leveraging human priors remain limited to models lacking
contextual awareness. The restricted motion synthesis is a direct consequence of
existing dataset pipelines failing to capture human-scene sequences in challenging
environments. To bridge this gap between humanoid learning and scene reconstruction, we
introduce the Egocentric Human-Terrain Reconstruction (EgoHTR) dataset. We develop and
open-source a reconstruction pipeline capturing 55 scene-aligned 4D human motion
sequences in diverse, complex environments using a multi-sensor setup of egocentric
wearables and a portable 3D scanner. The resulting dataset comprises over 150k frames,
which we evaluate against motion-capture ground truth, demonstrating state-of-the-art
accuracy and establishing a rigorous benchmark for human motion analysis and synthesis.
Further, we leverage this data to train perceptive locomotion policies, demonstrating
hardware deployment on a Unitree G1 for reconstructed reference motions. Our pipeline
enables community-driven dataset extensions and factors the problem to help researchers
build foundational, context-aware robots that reliably traverse uneven terrain.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13472v1
- Authors: Alex Brandes, Haig Conti Georges Sajelian, Manthan Patel, Dominik Hollidt, Chenhao Li, Matthias Heyrman, Oliver Hausdoerfer, Manuel Kaufmann, Xi Wang, Jonas Frey, Angela P. Schoellig, Christian Holz, Marc Pollefeys, Marco Hutter
- Published: 2026-07-15T06:02:41Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
