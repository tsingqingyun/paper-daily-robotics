---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00716v1"
published: "2026-07-01T10:03:11Z"
age_days: 4
score: 26
created: 2026-07-06
concepts: ["世界模型", "具身智能评测与基准"]
---

# Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach

## 为什么重要

自动筛选分数：26

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Skeleton-based action recognition has achieved remarkable success by exploiting joint
coordinates and their topological connections, yet prevailing methods overwhelmingly
assume complete and clean skeleton inputs. In real-world deployments, such as egocentric
vision, crowded surveillance, wearable devices, or edge robotics, limited field-of-view
(FoV) frequently causes substantial joint visibility dropout, leading to severe
performance degradation that existing models are largely unprepared to handle. To bridge
this critical yet underexplored gap, we introduce PartialVisGraph, a novel hypergraph
framework tailored for robust skeleton action recognition under constrained FoV. We
first construct highly expressive hypergraphs by introducing learnable virtual
hyperedges that form a soft incidence matrix, capturing flexible high-order dependencies
beyond conventional pairwise graphs. We then propose the Single-Head Sample-Adaptive
Transformer, which adaptively aggregates joint features onto hyperedges while explicitly
incorporating a visibility prior. This prior selectively gates information flow,
preventing occluded or out-of-view joints from corrupting reliable feature propagation.
We further establish rigorous evaluation protocols with realistic FoV simulation
benchmarks on NTU RGB+D 60 and 120. Extensive experiments demonstrate that
PartialVisGraph consistently achieves state-of-the-art accuracy under partial
visibility, with gains of up to 68.8\% on subsets with severe FoV restrictions compared
to recent strong baselines, while remaining superior on full-visibility settings. Our
approach offers a principled and practical pathway toward deployable skeleton-based
action understanding in unconstrained environments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00716v1
- Authors: Yingjie Dai, Tianyang Xu, Yanglin Deng, Xiao-Jun Wu, Josef Kittler
- Published: 2026-07-01T10:03:11Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
