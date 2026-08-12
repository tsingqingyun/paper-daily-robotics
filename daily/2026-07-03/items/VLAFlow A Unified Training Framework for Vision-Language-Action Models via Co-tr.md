---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01586v1"
published: "2026-07-02T01:38:16Z"
age_days: 1
score: 35
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet
the effects of different robot-data pre-training paradigms remain difficult to compare
because existing models often differ in architecture, data, action space, and evaluation
protocol. We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching
framework for controlled comparison of VLA training objectives. Using a heterogeneous
robot corpus, OXEMix, containing approximately 5,000 hours of data from DROID, OpenX-
Embodiment, OpenX-Augmented, and RoboCOIN, we evaluate four paradigms under the same
pi0-style architecture, shared VLM backbone, action expert, and 14-dimensional action
space: action-only modeling (MindPI), language-supervised co-training (MindLPI), future
latent alignment (MindWPI), and their combination (MindLWPI). Experiments on LIBERO,
LIBERO-Plus, and SimplerEnv show that action-only pre-training is sensitive to
heterogeneous data. In contrast, language supervision helps preserve vision-language
generalization, while future latent alignment improves state-transition and action-
outcome modeling. By combining both signals, MindLWPI achieves the most stable overall
transfer performance across benchmarks. These results suggest a meta-action space view:
language and future latent representations provide complementary intermediate
constraints that make heterogeneous action supervision smoother and more transferable.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01586v1
- Authors: Guoyang Xia, Fengfa Li, Hongjin Ji, Lei Ren, Fangxiang Feng, Kun Zhan, Yan Xie
- Published: 2026-07-02T01:38:16Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
