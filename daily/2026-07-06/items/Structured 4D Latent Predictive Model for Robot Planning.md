---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01166v1"
published: "2026-07-01T16:52:49Z"
age_days: 4
score: 28
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型"]
---

# Structured 4D Latent Predictive Model for Robot Planning

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[世界模型]]

## 摘要

Video predictive models are emerging as a powerful paradigm in robotics, offering a
promising path toward task generalization, long-horizon planning, and flexible decision-
making. However, prevailing approaches often operate on 2D video sequences, inherently
lacking the 3D geometric understanding necessary for precise spatial reasoning and
physical consistency. We introduce a Structured 4D Latent Predictive Model, which
predicts the evolution of a scene's 3D structure in a structured latent space
conditioned on observations and textual instructions. Our representation encodes the
scene holistically and can be decoded into diverse 3D formats, enabling a more complete
and 3D consistent scene understanding. This structured 4D latent predictive model serves
as a planner, generating future scenes that are translated into executable actions by a
goal-conditioned inverse dynamics module. Experiments demonstrate that our model
generates futures with strong visual quality, substantially better 3D consistency and
multi-view coherence compared to state-of-the-art video-based planners. Consequently,
our full planning pipeline achieves superior performance on complex manipulation tasks,
exhibits robust generalization to novel visual conditions, and proves effective on real-
world robotic platforms. Our website is available at
https://structured-4d-model.github.io/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01166v1
- Authors: Zhiyi Li, Peilin Wu, Xiaoshen Han, Ruojin Cai, Yilun Du
- Published: 2026-07-01T16:52:49Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
