---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12105v1"
published: "2026-06-10T13:59:07Z"
age_days: 1
score: 38
created: 2026-06-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models inherit a shared synchronous clock from vision-
language pretraining, processing every input at one rate. This is misaligned with
physical interaction, where a high-frequency modality changes at hundreds of hertz,
vision evolves more slowly, and language stays constant across an episode. A synchronous
VLA oversamples slow modalities, undersamples fast ones, and caps action generation at
the lowest effective frequency. We hypothesize that decoupling temporal processing per
modality, letting each update and retain information at its own sensor rate, yields
stronger representations and more robust control. We present DAM-VLA, which maintains
per-modality latent buffers refreshed at sensor rates and read continuously by the
action head, integrating new high-frequency modalities through gated cross-attention
that leaves the pretrained backbone intact. Across seven contact-rich real-world
manipulation tasks, DAM-VLA more than doubles the average success rate of the strongest
synchronous baseline (95.2\% vs.\ 40.95\%) while sustaining smooth, reactive 100\,Hz
control. Project website: \href{https://intuitive-robots.github.io/DAM-VLA/}{intuitive-
robots.github.io/DAM-VLA/}

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12105v1
- Authors: Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, Moritz Reuss, Gianluca Geraci, Xinkai Jiang, Rudolf Lioutikov
- Published: 2026-06-10T13:59:07Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
