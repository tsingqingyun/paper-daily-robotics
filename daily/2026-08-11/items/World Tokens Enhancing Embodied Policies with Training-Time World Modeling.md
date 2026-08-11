---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09730v1"
published: "2026-08-10T15:30:38Z"
age_days: 0
score: 35
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies.
They excel at efficient closed-loop control but do not explicitly model how physical
scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage
pretrained video world models to capture spatiotemporal evolution, yet retaining future
generation or a large video backbone in the control loop substantially increases
inference cost. We introduce World Tokens, an embodied policy architecture built around
a World Adapter that bridges visual-language understanding, world-dynamics modeling, and
action generation. It uses world modeling during training to enhance the action policy
while preserving efficient deployment. Specifically, the World Adapter transforms VLM
features into a fixed set of world tokens, which condition a jointly fine-tuned future-
video denoiser and simultaneously serve as the action expert's sole visual-language
context. This shared conditioning allows gradients from future-video denoising to
directly shape the representation used for action prediction, while exclusive routing
prevents the policy from bypassing that representation. At deployment, the world-model
branch is removed, leaving only the VLM, World Adapter, and action expert, with no
online video-model inference. With a 2B backbone and no embodied action pretraining,
World Tokens is highly competitive on LIBERO, attains the best reported averages on
SIMPLER, substantially improves real-world R1 Pro success over a matched action-only
baseline, and generates each action chunk at VLA-level latency.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09730v1
- Authors: Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo, Junlan Feng
- Published: 2026-08-10T15:30:38Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
