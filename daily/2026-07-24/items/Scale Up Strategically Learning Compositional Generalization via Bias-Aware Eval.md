---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21582v1"
published: "2026-07-23T17:57:09Z"
age_days: 0
score: 27
created: 2026-07-24
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation

## 为什么重要

自动筛选分数：27

连接概念：[[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Compositional generalization is essential for robot to follow diverse instructions.
However, pretrained policies are known to take shortcuts, deferring to salient cues
rather than grounding language. We introduce a diagnostic framework that localizes this
failure to individual \textit{instruction factors}, \textit{e.g.,} reusable semantic
components such as color, verb, object, size, and spatial attribute. Our framework
formalizes instruction factor bias, the tendency of fine-tuned policies to over-rely on
dominant factors as shortcuts, and quantifies it through two metrics: Factor Dominance
Rate (FDR), capturing pairwise bias between factors, and Factor Dominance Hierarchy
(FDH), aggregating these into a global ranking. Evaluation on six foundation policies
reveals broadly consistent ordering, \textit{i.e.}, color $\geq$ object $\geq$ spatial
$\geq$ verb $\geq$ size, with color dominant, and verb and size most under-grounded. We
further show the diagnosis is actionable: a bias-aware data collection strategy that
reallocates a fixed budget toward under-grounded factors outperforms baselines in
simulation and on a real robot using half the demonstrations, thereby enabling more
sample-efficient and generalizable policy learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21582v1
- Authors: Yu Qi, Zhang Ye, Xinyi Xu, Yuxuan Lu, Amitoj Sandhu, Boce Hu, Haojie Huang, Jonathan Tremblay, Lawson L. S. Wong
- Published: 2026-07-23T17:57:09Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
