---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14695v1"
published: "2026-07-16T07:56:43Z"
age_days: 1
score: 36
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Reflex: Real-Time VLA Control through Streaming Inference

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Flow matching Vision-Language-Action (VLA) models promise precise continuous control,
but their iterative denoising nature introduces fundamental incompatibilities with real-
time robotics: global timestep injection invalidates KV-caching, forcing a choice
between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present
\textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for
flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that
perception encoders are functionally independent of the denoising loop. Reflex
partitions the attention context into static, sliding, and dynamic regions, enabling
$O(1)$ incremental cache updates while preserving full-batch-equivalent attention
outputs for fixed inputs. To ensure stability under continuous high-frequency inference,
we introduce \textit{AdaRMSNorm}, an adaptive normalization layer that prevents BFloat16
numerical collapse by gating on flow phase. We further maximize throughput through an
\textit{async pipeline} that decouples visual encoding from action generation, combined
with \textit{operator fusion} that reduces kernel overhead. On LIBERO and Kinetix
benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming,
reducing reaction latency by up to 54\% and enabling efficient deployment without
performance degradation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14695v1
- Authors: Yuanchun Guo, Bingyan Liu
- Published: 2026-07-16T07:56:43Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
