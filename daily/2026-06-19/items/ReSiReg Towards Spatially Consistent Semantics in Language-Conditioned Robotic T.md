---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19088v1"
published: "2026-06-17T13:58:06Z"
age_days: 1
score: 29
created: 2026-06-19
concepts: ["多模态基础模型"]
---

# ReSiReg: Towards Spatially Consistent Semantics in Language-Conditioned Robotic Tasks

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]]

## 摘要

Vision-Language Models (VLMs) enable robots to follow open-language instructions.
However, dense VLM embeddings have shown to be noisy and lack spatial consistency. This
is problematic for robotic applications, which require simultaneous reasoning over
semantics and 3D space. We examine spatial structure across recent VLMs and propose
ReSiReg, a feature reconstruction method that uses spatially consistent VLM
intermediates to improve dense language-grounded retrieval. ReSiReg clusters
intermediates into visual prototypes, derives their language descriptors, and
reconstructs each patch as a soft mixture of prototype-level language embeddings. We
evaluate quantitatively on OVSS and 3D mapping across backbones, and qualitatively in
real-world manipulation scenes. Quantitative results show improved dense retrieval;
manipulation scenes show more spatially consistent target activations. We further
provide a compact 25M dense VLM for robotic applications, substantially smaller than and
competitive with ViT-B baselines. Available at https://resireg.github.io

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19088v1
- Authors: Simon Schwaiger, David Seyser, Alessandro Scherl, Wilfried Wöber, Gerald Steinbauer-Wagner
- Published: 2026-06-17T13:58:06Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
