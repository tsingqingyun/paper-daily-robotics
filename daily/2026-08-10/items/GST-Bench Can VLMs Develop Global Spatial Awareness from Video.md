---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05747v1"
published: "2026-08-06T08:33:13Z"
age_days: 4
score: 25
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Spatial intelligence is fundamental to embodied agents, yet existing benchmarks focus on
local spatial perception from single or few viewpoints, overlooking global spatial
awareness over continuous, long-horizon visual streams. To address this limitation, we
introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global
spatial intelligence in video understanding, comprising human-verified questions derived
from 6,790 minutes of synthetically generated video. It requires models to perform
accurate spatial inference from novel viewpoints unseen in the input video and to map
egocentric observations onto global top-down images. A comprehensive evaluation of 22
state-of-the-art VLMs exposes a striking gap between models and humans: the strongest
zero-shot model attains only 42.68, far below the human score of 79.08. To probe the
cause of this gap, we construct GST-Bench-Local and find that models, despite strong
local spatial understanding under the same task formulation, still fail to consolidate
long-horizon observations into a globally consistent scene representation. We further
provide GST-Train, a dataset for global spatial reasoning, as a complementary resource
to facilitate future research on this challenge.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05747v1
- Authors: Qifeng Zhang, Kaixiang Huang, Heng Dong, Huang Fang, Junting Chen, Junjie Zhu, Yonghang Chen, Zhiyu Zhang, Wei Li
- Published: 2026-08-06T08:33:13Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
