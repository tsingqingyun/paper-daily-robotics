---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29384v1"
published: "2026-06-28T13:19:11Z"
age_days: 1
score: 42
created: 2026-06-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Event-VLA: Action-Conditioned Event Fusion for Robust Vision-Language-Action Model

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have become an important paradigm of embodied AI.
However, existing VLA models typically assume well-lit and stable indoor settings, while
real-world embodied manipulation may involve degraded RGB observations caused by
illumination shifts, posing critical challenges for robust robotic manipulation. To
address this gap, we propose \textbf{Event-VLA}, an event-enhanced VLA framework for
generalizable manipulation across varying illumination conditions. We formulate VLA-
based manipulation under degraded visibility as a practical robustness problem for RGB-
centric policies, and introduce event streams as an illumination-robust, motion-
sensitive complementary observation to improve robustness across visibility levels.
Specifically, unlike conventional multimodal fusion that directly merges event features
into the global semantic token space, Event-VLA injects event information through an
action-query routing pathway. It uses learnable action queries to extract task-relevant
semantics from the VLA reasoning process, and selectively aggregates event tokens via
gated cross-attention to construct event-aware action representations. This design
preserves the pretrained RGB-language semantic priors while effectively leveraging event
information for robust action prediction. Experiments in simulation and real-world
deployment show that Event-VLA maintains strong manipulation performance under normal
lighting and improves success rates under low-light degradation and near-dark real-world
settings.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29384v1
- Authors: Jiaxin Liu, Xun Xu, Zhenhao Zhang, Hanqing Wang, Ruiqi Chen, Shi Chang, Weiyu Guo, Laurent Kneip
- Published: 2026-06-28T13:19:11Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
