---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13403v1"
published: "2026-05-13T11:58:02Z"
age_days: 0
score: 44
created: 2026-05-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# RotVLA: Rotational Latent Action for Vision-Language-Action Model

## 为什么重要

自动筛选分数：44

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Latent Action Models (LAMs) have emerged as an effective paradigm for handling
heterogeneous datasets during Vision-Language-Action (VLA) model pretraining, offering a
unified action space across embodiments. However, existing LAMs often rely on discrete
quantization encode and decode pipelines, which can lead to trivial frame reconstruction
behavior, limited representational capacity, and a lack of physically meaningful
structure. We introduce RotVLA, a VLA framework built on a continuous rotational latent
action representation. Latent actions are modeled as elements of SO(n), providing
continuity, compositionality, and structured geometry aligned with real-world action
dynamics. A triplet frame learning framework further enforces meaningful temporal
dynamics while avoiding degeneration. RotVLA consists of a VLM backbone and a flow-
matching action head, pretrained on large-scale cross-embodiment robotic datasets and
human videos with latent-action supervision. For downstream robot control, the flow-
matching head is extended into a unified action expert that jointly denoises latent and
robot actions. Here, latent actions serve as a latent planner, providing high-level
guidance that conditions action generation. With only 1.7B parameters and 1700+ hours of
pretraining data, RotVLA achieves 98.2% on LIBERO and 89.6% / 88.5% on RoboTwin2.0 under
clean and randomized settings, respectively. It also demonstrates strong real-world
performance on manipulation tasks, consistently outperforming existing VLA models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13403v1
- Authors: Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou, Hangjun Ye, Jiahuan Zhou, Yadong Mu
- Published: 2026-05-13T11:58:02Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
