---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13901v1"
published: "2026-06-11T20:48:38Z"
age_days: 4
score: 23
created: 2026-06-16
concepts: ["世界模型", "具身智能评测与基准"]
---

# SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting

## 为什么重要

自动筛选分数：23

连接概念：[[世界模型]], [[具身智能评测与基准]]

## 摘要

Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to
conventional neural networks, demonstrating strong performance in computer vision and
robotics. More recently, SNNs have been applied to time series forecasting (TSF), with
methods exploring spiking temporal backbones, spike-compatible positional encodings,
Fourier-domain processing, and redesigned neuron dynamics. However, existing SNN
forecasting approaches process variables independently, lacking explicit mechanisms for
modeling inter-variable dependencies. This is a critical limitation in multivariate
settings, where cross-variable correlations carry substantial predictive information. We
propose Spiking Fourier Graph Operators (SpikF-GO), which addresses this gap by
combining a hypervariate graph formulation in which every scalar observation becomes a
graph node with spike-driven spectral processing. SpikF-GO introduces a Hard Concrete
frequency gate for learnable sparse frequency selection and a Complex LIF gate that
applies independent spiking neurons to real and imaginary Fourier components, preserving
binary, event-driven computation throughout the spectral domain. We further present a
variant incorporating Central Pattern Generator-based positional encodings for stronger
long-range temporal modeling. Evaluated on eight benchmarks under a unified experimental
protocol, SpikF-GO achieves the best average rank among all SNN methods and outperforms
its ANN counterpart, FourierGNN, at reduced energy cost. SpikF-GO maintains competitive
accuracy even at substantially smaller embedding dimensions, thereby achieving
significant energy reductions. To our knowledge, this is among the first works to bring
graph-based multivariate modeling into the spiking domain for TSF and the first to
provide a unified comparison across SNN forecasting architectures under a common
experimental protocol.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13901v1
- Authors: Jafar Bakhshaliyev, Niels Landwehr
- Published: 2026-06-11T20:48:38Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
