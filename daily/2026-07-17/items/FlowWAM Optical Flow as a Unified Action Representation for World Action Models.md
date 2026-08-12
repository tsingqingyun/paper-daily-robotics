---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13017v1"
published: "2026-07-14T17:57:12Z"
age_days: 2
score: 35
created: 2026-07-17
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FlowWAM: Optical Flow as a Unified Action Representation for World Action Models

## 为什么重要

自动筛选分数：35

连接概念：[[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

World Action Models (WAMs) are able to leverage pretrained video generators for both
world modeling and action prediction. However, directly leveraging such video generators
for control raises a new challenge: how to represent actions in a suitable form that
aligns with pretrained video generators while carrying enough motion cues for accurate
control. Existing numerical actions fail to satisfy the former, and prior visual action
representations overlook the temporal motion structure across frames. We address this
issue with FlowWAM, a dual-stream diffusion framework that adopts optical flow as a
unified, video-native action representation. Flow videos share the same format as RGB
videos and encode rich per-pixel displacement. By jointly modeling them within a shared
pretrained video generator, FlowWAM can naturally implement two modes of WAMs. In policy
mode, FlowWAM generates flow for action prediction, while in world-model mode, it uses
target flow sequences to guide future video generation. Moreover, since flow can be
easily extracted from raw videos without action labels, FlowWAM can leverage large-scale
action-unlabeled video datasets for pretraining. We empirically find that our flow-based
action representation delivers gains across both modes. On RoboTwin manipulation,
FlowWAM raises the success rate to 92.94% on the Clean setting and 92.14% on Random,
outperforming both VLA and WAM baselines. On WorldArena world modeling, it achieves the
best overall EWMScore (63.71) with an 18.4% relative improvement in trajectory accuracy.
More results can be found on our project website: https://flow-wam.github.io .

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13017v1
- Authors: Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang, Kai Wang, Jianhua Yang, Dong An, He Guan, Gaoteng Liu, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
- Published: 2026-07-14T17:57:12Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
