---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06904v1"
published: "2026-06-05T04:42:56Z"
age_days: 2
score: 36
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# ActionMap: Robot Policy Learning via Voxel Action Heatmap

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) models have advanced rapidly across backbones, training
recipes, and data scale, yet the action decoder, which converts the backbone's hidden
state into a continuous control signal, has barely changed and remains a single-point
predictor across the majority of current VLAs. Whether implemented via autoregressive
token bins, L1 regression, or flow-matching denoising, the resulting decoder treats the
action space as unstructured, leaving the geometric proximity of neighboring actions
unexploited during training. To advance this, we introduce ActionMap, a voxel heatmap
action head that drops into an existing VLA in place of its native action decoder. For
each new action, the head predicts a voxel heatmap over the action space, where each
voxel directly stores the probability of the corresponding action. Across LIBERO
simulation and real-world Franka manipulation, our heatmap head surpasses two
architecturally distinct backbones at matched training steps (e.g., +8.2% over OpenVLA-
OFT's L1 regression head on the LIBERO four-suite average), converges at comparable or
faster rates on both backbones, and remains markedly more data-efficient at low training
data. The cross-backbone consistency indicates that action representation is a real
lever for VLA performance, distinct from further backbone or recipe scaling. Project
Page: https://github.com/showlab/ActionMap.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06904v1
- Authors: Pei Yang, Hai Ci, Yanzhe Chen, Qi Lv, Han Cai, Mike Zheng Shou
- Published: 2026-06-05T04:42:56Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
