---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24472v1"
published: "2026-06-23T12:02:36Z"
age_days: 1
score: 37
created: 2026-06-25
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) models have made rapid progress in generalist robot
manipulation by harnessing semantic knowledge from pretrained vision-language backbones,
but their visual tokens remain grounded in 2D image coordinates rather than the
calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-
camera setups, where views are coupled by known intrinsics and extrinsics yet processed
as independent images. We propose G$^3$VLA, a camera-aware geometric module that injects
calibrated structure into the visual-token stream of a pretrained VLA without altering
its action space or imitation objective, combining intrinsic-conditioned ray embeddings,
projective positional encoding (PRoPE), and bidirectional cross-view fusion. Geometric
supervision is provided either from ground-truth point maps when available, or from
confidence-gated $π^3$X teacher predictions, requiring no depth sensors or manual
annotations. Instantiated on $π_0$, G$^3$VLA yields consistent gains across the LIBERO
suites, RoboCasa24, RoboTwin2.0, and real-robot settings, with the largest improvements
on spatially and object-sensitive tasks. We further validate on $π_{0.5}$ and GR00T 1.5,
with results suggesting that geometric transfer is most effective when geometry-aware
tokens have direct access to the action generation pathway. Our project page is at
https://sites.google.com/view/g3vla

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24472v1
- Authors: Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo
- Published: 2026-06-23T12:02:36Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
