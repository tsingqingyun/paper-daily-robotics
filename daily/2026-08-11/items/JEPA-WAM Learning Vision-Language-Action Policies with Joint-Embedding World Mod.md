---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09381v1"
published: "2026-08-10T09:57:54Z"
age_days: 0
score: 39
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Robust robot control benefits from explicitly modeling state transitions, but video-
generation world action models (WAMs) introduce substantial deployment cost. Existing
latent WAMs avoid explicit future generation, but often compress predictive
representations or separate predictive modeling from the representations used for action
generation. We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space,
which couples latent transition prediction with continuous action generation through a
shared predictor. JEPA-WAM predicts a spatially structured joint current-future target
that captures task-shared visual temporal structure between current and future
observations, while preserving dense patch-level correspondence. Through the shared
predictor, transition supervision directly shapes the backbone, from which dedicated
representations are extracted for action prediction. The same design can also be
instantiated in pretrained VLA policies while preserving their original perception and
action pathways. On LIBERO-Plus, JEPA-WAM achieves 79.2%, the best result without large-
scale robot-policy pretraining, while its pretrained $π_{0.5}$ instantiation reaches
86.3%, achieving the best overall performance. Experiments on RoboTwin 2.0 and real-
world bimanual manipulation further demonstrate strong generalization under visual and
spatial shifts.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09381v1
- Authors: Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li, Xiaobo Wang, Yan Wang, Cheng Chi, Jing Zhang
- Published: 2026-08-10T09:57:54Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
