---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13778v1"
published: "2026-05-13T16:57:51Z"
age_days: 0
score: 31
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

Diffusion-based vision-language-action models (dVLAs) are promising for embodied
intelligence but are fundamentally limited in real-time deployment by the high latency
of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that
eliminates most full inference calls during replanning by introducing a lightweight
draft model with parallel verification via the main model's Action Expert and a phase-
aware fallback mechanism that reverts to the full inference pipeline when needed. This
design enables low-latency, high-frequency replanning without sacrificing reliability.
Experiments show that on LIBERO, FLASH largely preserves task performance by replacing
many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering
task-level average inference latency to 19.1 ms (3.04x speedup). We additionally
demonstrate effectiveness on real-world conveyor-belt sorting, highlighting its
practical impact for latency-critical embodied tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13778v1
- Authors: Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang, Xing Hu, Ying Wang, Huawei Li
- Published: 2026-05-13T16:57:51Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
