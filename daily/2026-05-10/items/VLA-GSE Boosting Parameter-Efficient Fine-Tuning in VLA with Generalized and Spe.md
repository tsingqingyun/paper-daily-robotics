---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Embodied AI and Robotics"
url: "https://arxiv.org/abs/2605.06175v1"
published: "2026-05-07T12:56:58Z"
score: 31
created: 2026-05-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models inherit rich visual-semantic priors from pre-trained
vision-language backbones, but adapting them to robotic control remains challenging.
Full fine-tuning (FFT) is prone to overfitting on downstream robotic data and
catastrophic forgetting of pretrained vision-language capabilities. Parameter-efficient
fine-tuning (PEFT) better preserves pre-trained knowledge, yet existing PEFT methods
still struggle to adapt effectively to robot control tasks. To address this gap, we
propose VLA-GSE, a parameter-efficient VLA fine-tuning framework that improves control
adaptation while retaining PEFT's knowledge preservation advantage. Specifically, VLA-
GSE (Generalized and Specialized Experts) is initialized by spectrally decomposing the
frozen backbone, assigning leading singular components to generalized experts (shared
experts) and disjoint residual components to specialized experts (routed experts). This
decomposition improves adaptation capacity under a fixed trainable-parameter budget.
Under a comparable parameter budget, VLA-GSE updates only 2.51% of the full model
parameters and consistently outperforms strong FFT and PEFT baselines. It achieves 81.2%
average zero-shot success on LIBERO-Plus, preserves pre-trained VLM capability
comparably to LoRA on multimodal understanding benchmarks, and improves real-world
manipulation success under multiple distribution shifts. Code is available at:
https://github.com/YuhuaJiang2002/VLA-GSE

## 来源

- Source: arXiv Daily - Embodied AI and Robotics
- URL: https://arxiv.org/abs/2605.06175v1
- Authors: Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao
- Published: 2026-05-07T12:56:58Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
