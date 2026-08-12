---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19889v1"
published: "2026-07-22T08:20:52Z"
age_days: 2
score: 26
created: 2026-07-25
concepts: ["多模态基础模型", "世界模型"]
---

# LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition

## 为什么重要

自动筛选分数：26

连接概念：[[多模态基础模型]], [[世界模型]]

## 摘要

Understanding instrument-tissue interactions is essential for context-aware surgical AI
and autonomous robotic surgery. Pretrained vision-language models (VLMs) and vision
encoders offer an alternative to conventional interaction classifiers by transferring
broad visual and semantic knowledge. However, adapting them to fine-grained surgical
interactions remains challenging: (1) freezing the vision encoder depends entirely on
pretrained representations that may retain noise and provide weak spatial localization,
while (2) full fine-tuning can improve global semantic alignment without ensuring that
the encoder learns meaningful features in the correct action region. We address these
limitations by introducing LAViFiT, an end-to-end latent-action-guided framework for
vision-language fine-tuning. An inverse dynamics model captures the visual changes
induced by each action, while a forward world model drives the encoder to represent
action-relevant regions. A patch-level SIG Regularizer further prevents local feature
collapse without additional supervision, such as bounding boxes or pseudo-labels.
Experiments across multiple encoders and datasets improve recognition and image-text
alignment, while representation analyses show stronger grounding over the complete
instrument-tissue interaction region and more spatially coherent features.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19889v1
- Authors: Jiajun Cheng, Subarna Tripathi, Sainan Liu, Xiaofan Yu, Shan Lin
- Published: 2026-07-22T08:20:52Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
