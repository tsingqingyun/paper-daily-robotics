---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14609v1"
published: "2026-07-16T06:12:05Z"
age_days: 1
score: 35
created: 2026-07-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-
rich manipulation, where critical interaction states are often hidden from vision.
Future tactile prediction is a promising way to use touch because it turns tactile
outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain
representations with different roles, from perceptual encoding to motor prediction,
making it unclear where this supervision should be applied. We study this as a
representation-alignment problem. Through a linear probe analysis, we find that future
tactile states are most predictable from intermediate action-expert features, rather
than from vision-language features or final action states. Motivated by this
observation, we introduce a lightweight Latent Tactile Predictor (LTP), which predicts
compact future tactile embeddings from the identified intermediate representation. By
avoiding direct prediction of noisy raw tactile signals, LTP provides an action-outcome
grounding signal that aligns intermediate action representations with future contact
consequences. Experiments on real-world contact-rich manipulation tasks show that
representation-aligned tactile grounding outperforms less aligned or multi-interface
tactile prediction, highlighting the importance of where tactile supervision is applied.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14609v1
- Authors: Ruilin Chen, Jingkai Jia, Tong Yang, Xinyu Zhou, Qiao Sun, Jiangwei Zhong, Shizeng Zhang, Nuo Chen, Bailin He, Wei Li, Wenqiang Zhang
- Published: 2026-07-16T06:12:05Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
