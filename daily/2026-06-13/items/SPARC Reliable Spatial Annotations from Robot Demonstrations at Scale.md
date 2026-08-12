---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13497v1"
published: "2026-06-11T15:46:28Z"
age_days: 1
score: 40
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

This work introduces Spatial Annotations from Robot Demonstrations with Reliability
Calibration (SPARC), a risk-aware framework that automatically labels robot
demonstrations with structured spatial annotations and assigns each annotation a
reliability score. Structured spatial annotations, such as bounding boxes, object
trajectories, and manipulation phase labels, benefit a broad range of robotics
applications from training grounded robot policies and embodied foundation models to
motion planning and hierarchical task composition. Existing automated pipelines generate
such annotations at scale but provide no reliable quality signal: detector confidence is
poorly calibrated for annotation correctness, forcing a choice between accepting noisy
labels or discarding useful samples. In contrast to existing automated pipelines, SPARC
leverages the spatio-temporal structure inherent to robot tasks to generate a
reliability signal, reducing noisy labels and retaining more useful samples. We further
introduce Interaction-Aware Bench (IA-Bench), a benchmark that measures model accuracy
in grounding the locations of interacted objects in robot demonstrations. On 1.7k human-
annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly
outperforms detection-only baselines in localization accuracy while retaining three
times more samples at high-precision operating points. Our experiments demonstrate that
models finetuned on our annotations achieve state-of-the-art results on object-grounding
and pointing benchmarks among similarly sized models, while remaining competitive on
broader spatial-reasoning suites without manually verified or annotated training data.
Furthermore, policies trained on SPARC-generated annotations outperform baselines in
cluttered, visually ambiguous real-world scenes. Code, data, and models are available at
intuitive-robots.github.io/sparc-labeling.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13497v1
- Authors: Nils Blank, Paul Mattes, Maximilian Xiling Li, Jakub Suliga, Thomas Roth, Moritz Reuss, Pankhuri Vanjani, Rudolf Lioutikov
- Published: 2026-06-11T15:46:28Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
