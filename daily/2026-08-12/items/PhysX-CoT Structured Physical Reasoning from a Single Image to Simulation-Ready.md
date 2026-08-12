---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08053v1"
published: "2026-08-08T10:39:09Z"
age_days: 3
score: 27
created: 2026-08-12
concepts: ["多模态基础模型", "世界模型"]
---

# PhysX-CoT: Structured Physical Reasoning from a Single Image to Simulation-Ready 3D Assets

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[世界模型]]

## 摘要

Simulation-ready 3D assets are central to robotics and embodied AI. Generating them from
a single image is usually framed as a vision-language model that emits a serialized
asset for a decoder to turn into geometry and physical fields, leaving the image-to-3D
reasoning implicit. We argue the limiting factor is this output-centric view: part
placement and local shape are entangled in one global-coordinate token stream, and the
intermediate physical states are never exposed for supervision, conditioning, or
verification. PhysX-CoT instead casts single-image asset generation as an explicit
structured physical reasoning process, an ordered and machine-parseable trajectory of
part-level states covering decomposition, 2D and 3D grounding, relations, coarse
geometry, and surface cues that we separately supervise, use to condition geometry, and
treat as reward targets. Geometry is factorized so that 3D boxes carry placement and
local codes carry shape, and CoT-aligned GRPO optimizes parse validity, grounding,
geometry, placement, and physical consistency. Under a unified protocol that retrains
all learned baselines on the same backbone, data, and frozen decoder, PhysX-CoT
outperforms the closest full-task baseline across geometry, scale, and physical-
attribute metrics. Oracle, token-matched, and state-order controls show the explicit
states are functional rather than cosmetic, and in Unreal Engine~5 the generated assets
parse, collide, and articulate at high validity.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08053v1
- Authors: Jie Huang, Xiaohe Li, Jiahao Li, Fangli Mou, Chen Qian, Yuqiang Fang, Junhao Fan, Kaixin Zhang, Zide Fan
- Published: 2026-08-08T10:39:09Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
