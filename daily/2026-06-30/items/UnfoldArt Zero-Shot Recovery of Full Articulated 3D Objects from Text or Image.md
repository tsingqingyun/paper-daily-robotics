---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30608v1"
published: "2026-06-29T17:44:53Z"
age_days: 0
score: 29
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent"]
---

# UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]]

## 摘要

Articulated 3D objects are essential for interactive environments in embodied AI,
robotics, and virtual reality, but reconstructing their structure and motion from sparse
observations remains challenging. Existing approaches remain largely constrained by lack
of supervised data or lack the priors needed to reliably recover articulation, hidden
geometry, and internal object structure. We present the first debate-driven agentic
approach to articulated 3D object reconstruction from text or image inputs that both
grounds articulation reasoning in concrete motion and exposes the occluded geometry
revealed under articulation. High-level agents reason about object semantics and motion
using knowledge from vision-language and video models, while low-level agents estimate
articulation parameters and interaction points; together, they engage in a two-round
structured debate that first exploits global--local disagreement and then grounds the
agents in freely generated video. The same video prior, conditioned on the agreed
articulation, then drives each part through its motion to expose occluded interiors and
geometry that cannot be inferred from a single static view. By combining agentic
reasoning with a video generative prior, our approach jointly infers articulation and
reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal
structure, and motion-consistent states beyond directly observed surfaces.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30608v1
- Authors: Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai
- Published: 2026-06-29T17:44:53Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
