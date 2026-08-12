---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19531v1"
published: "2026-06-17T19:25:28Z"
age_days: 2
score: 31
created: 2026-06-20
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?

## 为什么重要

自动筛选分数：31

连接概念：[[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

World Action Models (WAMs) commonly rely on video generation to bridge visual world
modeling and robot control. However, video-based WAMs face three coupled limitations:
dense multi-frame future tokens make inference costly, full video prediction spends
capacity on action-irrelevant temporal and appearance details, and long-horizon future
imagination may introduce errors that mislead action prediction. These issues raise a
simple question: Does world action model really need video generation? We propose
ImageWAM, a simple WAM framework that repurposes pretrained image editing models for
robot action prediction. In contrast to video generation, image editing provides a
better-matched prior: it only needs to model a target-frame transformation, focuses on
action-relevant current-to-target visual differences, and grounds task instructions to
localized visual changes through edit pretraining. In practice, ImageWAM does not decode
the target frame at inference time; instead, it conditions a flow-matching action expert
on the KV caches produced by image-editing denoising, using them as a compact world-
action context. ImageWAM outperforms standard VLA baselines and matching competitive
WAMs without additional policy pretraining across different simulator and real-world
experiments. It also reduces FLOPs to 1/6 and latency to 1/4 of video-based WAMs.
Attention analysis further shows that editing caches focus on task-relevant change
regions, supporting image editing as an effective alternative to video-based world-
action modeling.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19531v1
- Authors: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin
- Published: 2026-06-17T19:25:28Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
