---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17055v1"
published: "2026-06-15T17:59:55Z"
age_days: 2
score: 36
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# T-Rex: Tactile-Reactive Dexterous Manipulation

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

The ability to react dynamically to tactile signals has long been considered crucial to
agile human-level dexterity. Yet contemporary learning-based Vision-Language-Action
(VLA) models for robotic manipulation generally either overlook the tactile modality or
are limited to encoders with static cues, due in part to the scarcity of diverse
training data and standardized evaluation, architectural constraints in current VLA
models, and limitations of static tactile encoders. In this paper, we push the frontier
of tactile-reactive manipulation by addressing all of these limitations. We propose a
large-scale, 100-hour tactile-rich dataset collected via a novel, data-efficient recipe
that prioritizes elementary motor primitives. To effectively exploit naturally high-
frequency touch signals without sacrificing the existing capabilities of existing VLAs,
we introduce a variable-rate Mixture-of-Transformers (MoT) architecture equipped with a
novel temporal tactile VQ-VAE encoder. We demonstrate the effectiveness of tactile-
reactive policies on 12 manipulation tasks requiring delicate force control and
deformable object manipulation, achieving over 30% higher average success rate than the
strongest baseline.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17055v1
- Authors: Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin, Anirudh Pai, Yuvan Sharma, Stefano Saravalle, Ruijie Zheng, Jing Wang, Ryan Punamiya, Mengda Xu, Yuqi Xie, Yunfan Jiang, Letian Fu, Konstantinos Kallidromitis, Matteo Gioia, Junyi Zhang, Jiaxin Ge, Haiwen Feng, Fabio Galasso, Wei Zhan, David M. Chan, Yutong Bai, Roei Herzig, Jiahui Lei, Fei-Fei Li, Ken Goldberg, Jitendra Malik, Pieter Abbeel, Yuke Zhu, Danfei Xu, Jim, Fan, Trevor Darrell
- Published: 2026-06-15T17:59:55Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
