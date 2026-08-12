---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13970v1"
published: "2026-06-11T23:24:38Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "机器人学习"]
---

# An Attention-based Model for Robust Forecasting with Missing Modality

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[机器人学习]]

## 摘要

Learning with missing modalities is a fundamental challenge in multimodal robot
learning, as real-world robotic systems often operate in environments with incomplete
sensor data. Attention-based models are appealing for processing multimodal data because
they can handle multiple modalities with a single backbone network. However, most
multimodal models assume that all modalities are available during both training and
inference, limiting their applicability in robotic perception and decision-making. In
this paper, we introduce a multimodal model designed to handle missing modalities during
both training and inference. The model is formulated as a conditional variational
autoencoder (CVAE) and incorporates a transformer-based architecture that leverages
attention mechanisms to learn a unified, fixed-dimensional representation, even when
some modalities are missing. We show that our proposed model can be trained with missing
modalities while approximating a robust representation of all modalities. We evaluate
our approach on five multimodal datasets across two robot learning tasks: human
trajectory prediction and robot manipulation forecasting. Experimental results
demonstrate that our model effectively learns from incomplete data and is superior to
prior multimodal fusion approaches.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13970v1
- Authors: Zhitian Zhang, Wenjie Zi, Yunduz Rakhmangulova, Saghar Irandoust, Hossein Hajimirsadeghi, Thibaut Durand
- Published: 2026-06-11T23:24:38Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
