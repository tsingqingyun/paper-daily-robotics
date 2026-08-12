---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18431v2"
published: "2026-05-18T14:04:26Z"
age_days: 1
score: 35
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Seeing Together: Multi-Robot Cooperative Egocentric Spatial Reasoning with Multimodal Large Language Models

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Multimodal Large Language Models (MLLMs) have made substantial progress in egocentric
video understanding, but their ability to reason cooperatively from multiple embodied
viewpoints remains largely unexplored. We study this problem through multi-robot
cooperative dynamic spatial reasoning, where a model must answer spatial, temporal,
visibility, and coordination questions by integrating synchronized egocentric videos
from a team of moving robots. To support this setting, we introduce CoopSR, the first
benchmark for this task, together with EgoTeam, a multi-robot egocentric QA dataset.
EgoTeam contains 114,227 QA pairs spanning 19 question types, four difficulty tiers, and
three team sizes in Habitat and iGibson, along with a real-world test set of around
2,326 QAs collected using two quadruped robots. We further propose SP-CoR (Spectral and
Physics-Informed Cooperative Reasoner), an MLLM framework for fine-grained cooperative
spatial reasoning. SP-CoR combines dynamics-aware multi-robot frame sampling, spectral-
and physics-guided view fusion, and physics-aligned prompt distillation, enabling the
model to benefit from privileged robot-pose supervision during training while requiring
only egocentric videos at test time. Across 22 MLLM baselines, SP-CoR consistently
improves cooperative reasoning, outperforming the strongest fine-tuned baseline by
+3.87% on Habitat and +7.12% on iGibson. It also shows stronger generalization to unseen
team sizes and real-world robot tests. Code can be found at
https://github.com/KPeng9510/seeing-together.git.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18431v2
- Authors: Kunyu Peng, Zhikun Zhou, Kailun Yang, Di Wen, Ruiping Liu, Yufan Chen, Junwei Zheng, Hao Shi, Yi Zhou, M. Saquib Sarfraz, Danda Pani Paudel, Luc Van Gool
- Published: 2026-05-18T14:04:26Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
