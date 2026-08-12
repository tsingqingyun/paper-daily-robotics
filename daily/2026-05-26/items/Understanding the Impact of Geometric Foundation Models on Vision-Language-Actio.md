---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24642v1"
published: "2026-05-23T16:18:41Z"
age_days: 2
score: 27
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Recent work explores new opportunities at the intersection of vision-language-action
models (VLAs) and geometric foundation models (GFMs) for 3D reconstruction, such as
VGGT. While the resulting geometric VLAs often show improved performance, it remains
unclear (i) if modern VLAs already have sufficient geometric understanding to start
with, (ii) what is the best architecture to inject geometric understanding into a VLA,
and (iii) what is the effect of other design choices that affect geometric VLAs. In this
paper we provide a rigorous experimental analysis to shed light on these questions, for
a specific choice of VLA (GR00T-N1.5) and GFM (VGGT). Our first contribution is to
formalize prior work's intuition that current VLAs lack geometric understanding, by
providing a rigorous analysis based on linear probing. The analysis quantifies, for the
first time, the "geometric gap" between VLAs and GFMs. Our second contribution is to
identify and compare different strategies to bridge GFMs with VLAs. We implement three
different architectures, which differ in the way they inject geometry in the VLA, while
keeping low-level implementation details as similar as possible, to ensure a fair
comparison. Finally, we analyze the impact of non-architectural choices (e.g., training
data, number of cameras, reconstruction quality) on the performance of the geometric
VLAs.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24642v1
- Authors: Yurou Yang, Muyuan Lin, Roberto Martin-Martin, Martin Labrie, Shreekant Gayaka, Cheng-Hao Kuo, Luca Carlone
- Published: 2026-05-23T16:18:41Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
