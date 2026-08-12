---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12936v1"
published: "2026-06-11T05:58:38Z"
age_days: 1
score: 42
created: 2026-06-13
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics

## 为什么重要

自动筛选分数：42

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical
experiments, but scaling their learning requires customizable simulators for safe and
reproducible task generation, open editable laboratory assets, and efficient pipelines
that turn limited demonstrations into usable training data. We present Pipette, an
embodied simulation platform, benchmark, and data-efficient augmentation framework for
wet-lab robot learning. Pipette releases over 43 open-source and re-editable wet-lab
assets, together with an extensible asset-building pipeline. A key component of Pipette
is its simulation-based data augmentation pipeline, replaying human demonstrations in
simulation, applies lighting, camera, speed, and action perturbations, and filters
generated episodes with automatic task success checks, rapidly expanding usable training
data from limited manual demonstrations. We further introduce an 11-task wet-lab
embodied benchmark covering sample handling, culture-ware manipulation, device
operation, and precision placement. With only 30 demonstrations per task, ACT achieves
65.5% average success rate, while simulation augmentation improves SmolVLA from 44.1% to
74.7% and π0 from 40.4% to 46.5%, validating the effectiveness of Pipette for data-
efficient VLA training and evaluation. Pipette also supports natural-language-driven
scene construction and task registration, lowering the barrier for non-expert users to
define new wet-lab robotic tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12936v1
- Authors: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao
- Published: 2026-06-11T05:58:38Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
