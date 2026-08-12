---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00889v1"
published: "2026-07-01T12:55:09Z"
age_days: 1
score: 33
created: 2026-07-03
concepts: ["世界模型"]
---

# DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors

## 为什么重要

自动筛选分数：33

连接概念：[[世界模型]]

## 摘要

We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D
Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct
reliable 3D scene graphs due to unstable 3D object representations and missing relations
caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-
level geometric 3D Gaussian distributions through depth-guided filtering and
representing each object as a probabilistic 3D node rather than a single projected
point. To mitigate relational sparsity from frame-wise inference, our framework further
aggregates spatiotemporal evidence across object pairs and refines relations using
contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and
ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and
predicate prediction, while producing temporally consistent scene structures. In
particular, our method improves triplet recall by 77.4% and predicate recall by 23.2%
over prior SoTA approaches, making it suitable for robotic manipulation and AR
applications. Our code and models are open-sourced.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00889v1
- Authors: Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo
- Published: 2026-07-01T12:55:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
