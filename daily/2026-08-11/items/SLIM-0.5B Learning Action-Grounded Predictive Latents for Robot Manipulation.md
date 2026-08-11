---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09771v1"
published: "2026-08-10T15:58:39Z"
age_days: 0
score: 53
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation

## 为什么重要

自动筛选分数：53

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action policies rely on large multimodal backbones to jointly perform
perception, language conditioning, and action generation at every control step. Much of
this capacity supports open-domain semantics, whereas continuous robot manipulation
primarily requires compact representations of observations, actions, and the transitions
induced by actions. Pixel-level world models provide another route, but predicting
visual details irrelevant to control can be unnecessarily expensive. We propose SLIM
(Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction
policy. SLIM learns action-grounded predictive latents that capture both action-
conditioned future transitions and the actions that explain observed changes. SLIM
learns these representations through self-supervised masked trajectory prediction,
combining action reconstruction with future-latent prediction. A compact Mixture-of-
Transformers (MoT) backbone models interactions between observation latents and action
tokens. The resulting policy is trained with flow matching for language-conditioned
action generation. Across simulation benchmarks and real-world evaluation, SLIM matches
or exceeds representative large-scale VLA and world-action-model baselines with fewer
parameters, no additional embodied pretraining, lower inference latency, and
substantially lower GPU memory usage.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09771v1
- Authors: Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
- Published: 2026-08-10T15:58:39Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
