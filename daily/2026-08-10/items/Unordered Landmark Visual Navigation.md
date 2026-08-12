---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06833v1"
published: "2026-08-07T05:45:06Z"
age_days: 3
score: 28
created: 2026-08-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# Unordered Landmark Visual Navigation

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Image-goal navigation is a fundamental capability for embodied AI, yet its practical
deployment is strained by strong prior assumptions. Existing methods predominantly rely
on temporally ordered video streams or auxiliary sensors (e.g., depth, LiDAR) to
maintain spatial consistency. These sequential and multimodal dependencies severely
restrict scalability, especially when deploying robots using crowd-sourced or pre-
recorded unordered image collections. When temporal priors are removed, current methods
struggle with severe perceptual aliasing, noisy associations, and catastrophic mapping
failures. To address this underexplored challenge, we propose Unordered Landmark Visual
Navigation (ULVN), a unified RGB-only framework free from temporal and odometric priors.
ULVN systematically mitigates error accumulation by integrating mapping, localization,
and planning. Specifically, it constructs a robust 2D topological map directly from
unstructured images via calibrated geometric verification and maximum spanning forest
refinement. For closed-loop execution, ULVN abandons sequential heuristics, utilizing a
graph-based belief propagation filter with entropy-adaptive fusion for global
localization and dynamic subgoal planning. Extensive experiments in simulation and real-
world deployments demonstrate that ULVN significantly outperforms state-of-the-art
methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06833v1
- Authors: Hao Ren, Junzhe Zhu, Yihan Li, Zetong Bi, Le Zheng, Zhi Li, Yiqing Yuan, Zhaoliang Wan, Dizhe Zhang, Lu Qi, Hui Cheng
- Published: 2026-08-07T05:45:06Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
