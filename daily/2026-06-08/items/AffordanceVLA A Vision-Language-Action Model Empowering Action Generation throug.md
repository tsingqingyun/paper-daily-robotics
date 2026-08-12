---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06155v1"
published: "2026-06-04T13:28:51Z"
age_days: 3
score: 42
created: 2026-06-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-Language-Action (VLA) models leverage the rich world knowledge of pretrained
vision-language models (VLMs) to enable instruction-following robotic manipulation.
However, the structural mismatch between VLM semantic spaces and embodied control
policies often hinders the learning of precise perception--action mappings. To address
this challenge, we propose \textbf{AffordanceVLA}, a unified framework that introduces
structured affordance forecasting as a task-oriented intermediate representation to
establish a more precise and robust perception--action mapping. Specifically, we
progressively model manipulation priors through three complementary components: 1)
\textbf{Which2Act} for object-centric grounding via visual latent prediction to suppress
distractions; 2) \textbf{Where2Act} for 2D interaction localization via affordance map
estimation; and 3) \textbf{How2Act} for 3D geometric reasoning to guide manipulation
policies. These affordance cues provide spatially grounded, semantically conditioned,
and action-coupled intermediate representations, thereby naturally bridging vision,
language and action. We integrate these modules into a Mixture-of-Transformer (MoT)
architecture with specialized experts and train the model using a three-stage training
strategy with a progressive data curriculum. To overcome the scarcity of dense
affordance labels in robotic datasets, we also develop a robust automated data
augmentation pipeline. Extensive experiments on simulation and real-world demonstrate
that AffordanceVLA achieves strong performance across diverse manipulation scenarios.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06155v1
- Authors: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
- Published: 2026-06-04T13:28:51Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
