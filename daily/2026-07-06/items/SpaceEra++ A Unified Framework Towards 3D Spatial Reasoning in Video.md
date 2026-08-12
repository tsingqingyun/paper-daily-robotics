---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01784v1"
published: "2026-07-02T06:56:29Z"
age_days: 4
score: 23
created: 2026-07-06
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SpaceEra++: A Unified Framework Towards 3D Spatial Reasoning in Video

## 为什么重要

自动筛选分数：23

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Visual-spatial understanding, defined as the ability to infer object relationships and
scene layouts from visual inputs, is fundamental to downstream tasks such as robotic
navigation and embodied interaction. However, pre-trained vision-language models (VLMs)
remain constrained by spatial uncertainty stemming from inherently 2D observations and
by the scarcity of data for 3D spatial understanding. To address these limitations, we
proposed a novel framework, SpaceEra, in the NeurIPS 2025 Spotlight paper. Although it
achieved significant performance gains, we further observed that its effectiveness is
hindered by insufficient input from scanning videos and weak reasoning constraints. To
tackle these newly emerged challenges, we extend the original framework into a
comprehensive system, termed SpaceEra++, which spans data construction, model design,
training optimization, and prompting inference. Specifically, to alleviate input
insufficiency, we introduce ScenePick, a frame sampling strategy that balances spatial
coverage with object semantics to produce compact yet comprehensive scene
representations. In addition, to enhance spatial reasoning, we develop SpaceAlign, which
enforces pairwise object constraints by jointly exploiting absolute coordinates and
relative spatial relations, thereby aligning optimization with spatial accuracy.
Extensive experiments across multiple benchmarks demonstrate consistent improvements
over strong baselines, while ablation studies validate both the individual and joint
contributions of each component, and further analyses provide guidance for future
research.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01784v1
- Authors: Weili Guan, Haoyu Zhang, Meng Liu, Qianlong Xiang, Yaowei Wang, Liqiang Nie
- Published: 2026-07-02T06:56:29Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
