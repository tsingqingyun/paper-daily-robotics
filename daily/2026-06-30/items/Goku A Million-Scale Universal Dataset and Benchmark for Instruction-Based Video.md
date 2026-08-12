---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30599v1"
published: "2026-06-29T17:38:15Z"
age_days: 0
score: 30
created: 2026-06-30
concepts: ["具身智能评测与基准"]
---

# Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing

## 为什么重要

自动筛选分数：30

连接概念：[[具身智能评测与基准]]

## 摘要

Existing instruction-based video editing datasets commonly focus on single-task
appearance editing, failing to meet the complex creative demands of real-world
scenarios. To bridge this gap, we present Goku, a large-scale dataset featuring 2
million high-quality, instruction-aligned video editing pairs, which is the first to
extend task boundaries from basic appearance editing to multi-task and structural
manipulations(e.g., precise control of subject movement). To tackle the data synthesis
challenges inherent in these complex tasks, we design an efficient data synthesis
pipeline that decomposes complex edits into controllable sub-problems and introduce a
progressive filtering system for data reliability throughout the whole process.
Furthermore, we explore the optimal network structures on Goku, and propose Goku-Edit.
To deeply comprehend complex editing instructions, Goku-Edit leverages an MLLM as its
text encoder and adopts a decoupled dual-branch design: a dedicated mask branch handles
structural control, freeing the main branch for appearance rendering. A comprehensive
video editing benchmark, Goku-Bench, is also proposed with 1,000 human-verified test
cases and 7 novel editing-specific metrics. Evaluated on Goku-Bench, Goku-Edit obtains
up to +8% improvement on other open-source models in terms of instruction following.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30599v1
- Authors: Sen Liang, Cong Wang, Zhentao Yu, Fengbin Guan, Zhengguang Zhou, Teng Hu, Youliang Zhang, Yuan Zhou, Xin Li, Qinglin Lu, Zhibo Chen
- Published: 2026-06-29T17:38:15Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
