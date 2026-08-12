---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19174v1"
published: "2026-07-21T15:12:11Z"
age_days: 3
score: 25
created: 2026-07-25
concepts: ["世界模型", "具身智能评测与基准"]
---

# Bayesian Retraction Optimization for Tissue Attachment Mapping in Surgical Dissection

## 为什么重要

自动筛选分数：25

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

With growing surgeon shortages, automating surgical sub-tasks such as tissue dissection
offers a promising step toward reducing workload and expanding patient access. Prior
work has relied on hand-crafted incision policies that cannot quantify uncertainty or
has relied on simulation-based methods that require strong modeling assumptions. We
instead view tissue attachment identification as an inherently probabilistic problem and
propose a Bayesian approach that avoids explicit tissue modeling. Our method uses a
Sequential Bayesian Hilbert Map (SBHM) to represent the likelihood that each tissue
point is attached to the underlying resection surface. An ensemble of learned
classifiers predicts attachment likelihoods from spatial data acquired during robotic
tissue retraction, with each classifier serving as a noisy information source to update
the SBHM. To plan the next retraction, we devise Bayesian Retraction Optimization (BRO)
to select the most informative action under safety constraints. As the SBHM refines over
time, regions with high attachment likelihood are selectively incised. We validate our
method in simulation across diverse tissue geometries and acquisition strategies, and
demonstrate zero-shot transfer to real robotic dissection experiments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19174v1
- Authors: Shing-Hei Ho, Bao Thach, Toan Vo, James M. Ferguson, Alan Kuntz
- Published: 2026-07-21T15:12:11Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
