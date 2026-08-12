---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18955v1"
published: "2026-06-17T11:37:59Z"
age_days: 1
score: 44
created: 2026-06-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos

## 为什么重要

自动筛选分数：44

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Training generalist Vision-Language-Action(VLA) models typically requires massive,
diverse robotic datasets with high-fidelity action annotations. While egocentric human
manipulation videos are abundant and capture significant environmental diversity, the
absence of action labels makes them difficult to use in conventional training paradigms.
To address this, we propose a latent-action-based framework designed to extract general
action priors from unlabeled human videos. The architecture features a Hybrid
Disentangled VQ-VAE that decouples motion dynamics from environmental backgrounds
through physical masks, enabling the construction of a cross-embodiment action codebook.
By pre-training on human videos with the codebook, the VLM backbone learns deep
representations of action intent. For adaptation to specific embodiments, we introduce
an intent-perception decoupling strategy where the VLM predicts the action intent while
a separate frozen visual encoder provides state-specific features to the action expert,
thereby reducing action hallucinations. Results in simulation and real-world
environments show that our method, pre-trained exclusively on unlabeled human videos,
performs competitively with state-of-the-art VLA models trained on massive annotated
datasets, requiring only 50 trajectories for downstream adaptation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18955v1
- Authors: Runze Xu, Yiluo Zhang, Jian Wang, Yu Wang, Jincheng Yu
- Published: 2026-06-17T11:37:59Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
