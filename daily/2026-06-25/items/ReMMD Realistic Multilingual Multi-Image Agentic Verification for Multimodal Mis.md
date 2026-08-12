---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24112v1"
published: "2026-06-23T03:56:53Z"
age_days: 1
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Multimodal misinformation detection is increasingly important because viral posts now
combine long multilingual narratives, several images, mixed provenance, and subtle text
--image framing errors. Existing benchmarks and methods remain poorly matched to this
setting: they usually isolate short captions, single images, binary labels, or one
manipulation source, while agentic verification remains costly under realistic evidence
search. We present ReMMD, a realistic multilingual multi-image agentic verification
framework for multimodal misinformation detection. ReMMD includes ReMMDBench, a real-
world multimodal misinformation detection benchmark with 500 samples, 2,756 images, five
monolingual languages, two cross-lingual settings, three text-length tiers, multi-image
posts, five-way veracity labels, eight distortion labels, evidence provenance, and
rationales. It also includes ReMMD-Agent, a persistent-memory verifier that decomposes
posts into atomic points, builds a reusable evidence set, and predicts structured
L1/L2/L3 outputs. Across proprietary systems, open LVLMs, MMD-Agent, and T2-Agent,
ReMMD-Agent obtains the best five-way veracity performance, with 41.80% accuracy and
39.12% macro-F1 using GPT-5.2, while reducing cost by 17.5% relative to MMD-Agent and
79.9% relative to T2-Agent. The project is available at https://dang-ai.github.io/ReMMD.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24112v1
- Authors: Chenhao Dang, Dantong Zhu, Jun Yang, Conghui He, Weijia Li
- Published: 2026-06-23T03:56:53Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
