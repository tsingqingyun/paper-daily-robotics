---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15974v1"
published: "2026-07-17T14:07:46Z"
age_days: 2
score: 30
created: 2026-07-20
concepts: ["智能体 Agent", "世界模型"]
---

# Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection

## 为什么重要

自动筛选分数：30

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

This paper studies how to adapt a computer vision object detector to an unknown
environment under both a robot navigation time and annotation budget constraint. Our
approach selects informative robot trajectories and image samples to retrain the
detector, explicitly targeting its failure cases. Formally, the approach is an embodied
variant of batch active learning, where at each round an agent has a limited navigation
budget to collect candidate samples and a limited annotation budget for the most
relevant images. We leverage spatial consistency to identify images with inconsistent
labels, which are likely to provide the greatest improvement to the vision model. We
evaluate the approach using different active learning objectives on large scenes from
the AI2-THOR simulator and on a real-world setup using a Boston Dynamics Spot robot with
the real-time object detector YOLOv5. Through comparison against several baselines, our
experimental results show that spatial inconsistency helps guide the agent and select
relevant images without external supervision, achieving the highest detection accuracy
at the end of the adaptation process under the same budget. The open-source project can
be found at https://mkabouri.github.io/embodied-active-learning-od

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15974v1
- Authors: Hadrien Crassous, Mohamed Yassine Kabouri, Minahil Raza, Joni Pajarinen, Riad Akrour
- Published: 2026-07-17T14:07:46Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
