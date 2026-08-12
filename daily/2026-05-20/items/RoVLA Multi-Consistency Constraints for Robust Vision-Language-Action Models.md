---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19678v1"
published: "2026-05-19T11:10:20Z"
age_days: 0
score: 40
created: 2026-05-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have shown strong performance on embodied
manipulation, yet they remain brittle under visual observation changes, paraphrased
language instructions, and compounded perturbations. This limitation suggests that
existing methods still rely heavily on shallow correlations in the training
distribution, rather than learning stable couplings among task semantics, environment
states, and action generation. Although recent efforts improve robustness through
larger-scale training, post-training adaptation, or enhanced predictive modeling, they
rarely enforce invariance-oriented consistency within the end-to-end policy itself. To
address this issue, we propose RoVLA, a robust vision-language-action framework with
multi-consistency constraints. RoVLA enforces consistency under three complementary
transformations: instruction semantics, trajectory evolution, and observation
perturbation. Specifically, Instructional Consistency (IC) promotes stable grounding
under semantically equivalent instruction rewrites, Evolutionary Consistency (EC)
preserves coherent action intent throughout the generation process, and Observational
Consistency (OC) improves robustness to visual and proprioceptive perturbations by
enforcing consistent predictions before and after targeted disturbances. By explicitly
modeling these invariances during training, RoVLA reduces reliance on superficial
correlations and improves robustness and generalization. Experiments on LIBERO-Plus,
RoboTwin 2.0, and real-world manipulation tasks show that RoVLA consistently outperforms
strong baseline methods and exhibits superior robustness under diverse task and
observation shifts. These results demonstrate the effectiveness of multi-consistency
learning for robust embodied control. Codes will be available at
https://github.com/HCPLab-SYSU/RoVLA.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19678v1
- Authors: Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin
- Published: 2026-05-19T11:10:20Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
