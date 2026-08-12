---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29247v1"
published: "2026-06-28T07:29:25Z"
age_days: 2
score: 40
created: 2026-06-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models represent a promising direction for embodied
intelligence in surgical robotics. Despite the prevalence of VLA benchmarks for general
robotics, standardized evaluation platforms specifically designed for surgical contexts
remain absent. To address this limitation, we present SurgVLA-Bench, the first
comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics.
Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy
ranging from atomic actions to complete surgical procedures, complemented by a multi-
dimensional evaluation framework assessing action accuracy and semantic consistency. We
then systematically evaluate two representative paradigms, including autoregressive
models such as OpenVLA, and flow matching models such as $π_{0}$, $π_{0.5}$, and
SmolVLA. Our experiments show that autoregressive models tend to excel in semantic
understanding, while flow matching models often achieve higher task precision but may
face generalization trade-offs. However, even the best-performing models remain far from
satisfactory, as the constrained endoscopic field of view, restricted viewing angles,
and frequent occlusions persist as fundamental physical bottlenecks. The code and data
are available at https://github.com/VCL-HNU/SurgVLA

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29247v1
- Authors: Jiashuo Sun, Yue He, Wenxuan Liu, Tao Mao, Jiazheng Wang, Xiang Chen, Min Liu
- Published: 2026-06-28T07:29:25Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
