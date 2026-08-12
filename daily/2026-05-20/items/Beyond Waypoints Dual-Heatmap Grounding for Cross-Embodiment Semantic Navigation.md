---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19420v1"
published: "2026-05-19T06:12:59Z"
age_days: 0
score: 29
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Beyond Waypoints: Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Grounding open-ended semantic instructions into physically executable local goals is a
fundamental challenge in human-robot interaction. While existing navigation frameworks
often regress deterministic waypoints, this rigid formulation collapses spatial
uncertainty and frequently targets non-traversable object centers, leading to severe
execution failures. In this work, we focus on the practical setting of in-FOV semantic
navigation, where a robot receives concise, interleaved multimodal (text and image)
prompts. To bridge the gap between abstract semantic intent and physical reachability,
we propose a unified Vision-Language framework that abandons single-point regression in
favor of a Dual-Heatmap representation. Our framework predicts a navigation affordance
heatmap that captures continuous reachable regions, coupled with a facing heatmap for
orientation constraints. These dense outputs inherently function as a differentiable
semantic potential field, integrating seamlessly with downstream local planners. To
support this paradigm, we build a fully automated, foundation-model-assisted synthetic
data pipeline and establish a comprehensive simulation benchmark. Extensive experiments
demonstrate that our framework achieves state-of-the-art performance among comparable 8B
baselines. Crucially, a feature-fusion study and simulation studies across diverse robot
embodiments (Jetbot, H1, Aliengo) reveal that explicit heatmap prediction drastically
improves the Affordance Rate (AR). By placing targets reliably in executable free space,
our framework effectively mitigates the brittleness of point regression, offering a
transferable path toward safe cross-embodiment semantic navigation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19420v1
- Authors: Kaijie Yun, Yue Chen
- Published: 2026-05-19T06:12:59Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
