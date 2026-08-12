---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25308v1"
published: "2026-05-25T00:13:15Z"
age_days: 1
score: 27
created: 2026-05-26
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Stabilizing Streaming Video Geometry via Dynamic Feature Normalization

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Consistent 3D geometry estimation from streaming RGB input is crucial for real-world
applications such as autonomous driving, embodied AI, and large-scale reconstruction.
While modern monocular geometry foundation models achieve strong single-image accuracy,
they exhibit severe temporal inconsistency on continuous input, notably dominated by
scale--shift drifting. Through targeted empirical analysis, we trace this instability to
its root cause: fluctuations in latent feature statistics, whose mean and variance
directly determine the predicted depth's scale and shift. Building on this insight, we
introduce Dynamic Feature Normalization (DyFN), a lightweight, causal recurrent module
that dynamically and robustly modulates feature statistics to maintain stable geometry
over time. We adapt powerful pretrained monocular geometry models for streaming by
finetuning only DyFN, a mere 2\% additional parameters, while keeping the backbone
frozen, thereby achieving temporal consistency without compromising single-image
accuracy. Extensive experiments across four benchmarks show that DyFN effectively
eliminates temporal artifacts such as disjointed layering and positional jitter, and
achieves state-of-the-art temporal stability, improving over prior streaming methods by
up to 14\% and even outperforming heavier non-causal video baselines. Project Page:
https://shawlyu.github.io/DyFN

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25308v1
- Authors: Xiaoyang Lyu, Muxin Liu, Xiaoshan Wu, Ruicheng Wang, Yi-Hua Huang, Yang-Tian Sun, Shaoshuai Shi, Xiaojuan Qi
- Published: 2026-05-25T00:13:15Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
