---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17598v1"
published: "2026-06-16T07:04:13Z"
age_days: 1
score: 46
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

## 为什么重要

自动筛选分数：46

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Humans naturally leverage diverse sensing modalities to interact with the physical
world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB
observations. This limits their ability to perceive physical properties that are
difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar
response. We present MuseVLA, an adaptive multimodal sensing VLA model that integrates
novel sensors as on-demand tools for robotic manipulation. Given a task instruction and
visual context, MuseVLA first generates a sensor token and target description that
select the sensing modality to invoke and what to attend to, analogous to a tool call
with arguments. It then converts the selected sensor measurement into a grounded sensor
image, a unified intermediate representation that encodes heterogeneous readings for
multimodal fusion and action generation. This design decouples sensor-specific
processing from the VLA backbone, enabling efficient integration of diverse modalities.
To reduce the need for expensive multisensory robot datasets, we further introduce a
data synthesis pipeline that augments existing RGB video datasets with grounded sensor
images, enabling generalization to unseen sensor-guided tasks. We evaluate MuseVLA on a
real-world robot across challenging dexterous hand manipulation tasks that require
multimodal sensing inputs, including temperature-guided pick-and-place, audio-driven
object search, and radar-assisted hidden object retrieval. MuseVLA achieves 80.6%
success rate on average, outperforming RGB-only and multisensory VLA baselines
significantly, and exhibits strong zero-shot capabilities on unseen tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17598v1
- Authors: Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
- Published: 2026-06-16T07:04:13Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
