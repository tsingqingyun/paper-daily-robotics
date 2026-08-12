---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01804v1"
published: "2026-07-02T07:18:53Z"
age_days: 1
score: 39
created: 2026-07-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) foundation models have recently achieved strong progress in
embodied intelligence. To reduce policy-call frequency while preserving temporal
coherence, most generative policies adopt an action chunk mechanism, executing multiple
future actions in an open-loop manner under a fixed action horizon. However, this
"predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-
rich physical interactions, even small local perturbations can rapidly amplify within
the open-loop blind spot, leading to compounding errors and ultimately task failure. To
address this limitation, we propose VLA-Corrector, a lightweight corrective inference
framework for action-chunked VLA policies. Without modifying the backbone policy
weights, VLA-Corrector introduces a lightweight Latent-space Vision Monitor (LVM) that
continuously compares predicted and actual visual feature evolution, enabling online
detection of visual dynamics deviations. Once persistent deviation is detected, the
system triggers a truncation event, discards the remaining stale actions, and invokes
corrective replanning via Online Gradient Guidance (OGG). The detect-and-correct
mechanism of VLA-Corrector naturally induces an event-triggered adaptive action horizon:
it preserves long-horizon execution when the current chunk remains reliable, and invokes
short-horizon corrective replanning when execution begins to drift. In doing so, VLA-
Corrector mitigates the trade-off imposed by static horizons between execution
robustness and policy-call frequency. It can be integrated into different VLA models
without further retraining the VLA backbone, interrupting compounding errors while
preserving much of the efficiency benefit of action chunking and substantially improving
robustness in long-horizon, contact-rich robotic manipulation tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01804v1
- Authors: Yi Pan, Miao Pan, Qi Lu, Jiaming Huang, Man Zhang, Siteng Huang, Xin Li, Jie Zhang, Yongliang Shen, Xuhong Zhang, Wenqi Zhang
- Published: 2026-07-02T07:18:53Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
