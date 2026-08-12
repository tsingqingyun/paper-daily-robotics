---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17806v1"
published: "2026-07-20T10:48:48Z"
age_days: 1
score: 28
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-
language instruction and predict actions from temporally ordered visual observations.
Adapting a multimodal large language model to VLN requires visual-language alignment,
compact temporal inputs, action-space grounding, and stable training on the target
hardware. This technical report presents PGN (Pangu Navigator), an offline VLN action-
prediction system built on OpenPangu-7B. Training proceeds in two stages. First, PGMM
aligns a frozen EVA-ViT-G/14 vision encoder with the frozen language backbone by
training a Q-Former and a two-layer MLP projector. Second, PGN adapts the aligned model
to expert navigation trajectories using five-observation windows, epoch-dependent
temporal sampling, and a reasoning-then-action output format; this stage freezes the
aligned visual pathway and updates three structural-token embeddings and LoRA adapters.
The implementation combines mixed-precision computation, selective FP32 computation, and
DeepSpeed ZeRO-2 on eight Ascend 910B NPUs. Under teacher-forced, open-loop evaluation
on 500 held-out expert trajectories, V9 reports a 62.29% Normalized Action Match (NAM)
and a 100.00% Non-empty Rate (NER). These metrics quantify offline expert-action
alignment rather than closed-loop navigation success; evaluating error accumulation,
path efficiency, and goal completion remains future work.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17806v1
- Authors: Li Xian, Mingxi Li, Yizheng Wang, Yiming Shen, Qi Chen, Zhuoling Xiao
- Published: 2026-07-20T10:48:48Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
