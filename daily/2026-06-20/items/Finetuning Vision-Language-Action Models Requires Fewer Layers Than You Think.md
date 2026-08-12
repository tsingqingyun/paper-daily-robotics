---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20246v1"
published: "2026-06-18T13:57:12Z"
age_days: 1
score: 41
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

## 为什么重要

自动筛选分数：41

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have
revolutionized robotic manipulation, yet their multi-billion parameter architectures
impose prohibitive computational burdens during downstream fine-tuning and real-time
inference. In this work, we reveal a highly non-trivial architectural characteristic of
these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being
trained on diverse physical trajectories, they exhibit severe layer-wise
representational redundancy. To exploit this, we introduce a structural compression
pipeline that is entirely training-free, bypassing the need of existing methods to load
full-scale models to learn optimized token reductions or dynamic layer selectors.
Instead, using only a single forward pass via Centered Kernel Alignment to identify
redundant layer features, we remove twin layers to permanently compress the model depth
by up to 50% across both the VLM backbone and the continuous control policy head.
Downstream fine-tuning of this streamlined architecture yields a dual acceleration
benefit: a 40-50% reduction in training time and up to 30% faster real-time inference,
while matching or exceeding full-scale base model performance. We comprehensively
validate our method across three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv)
and 10 diverse real-world manipulation tasks across 4 unique robotic embodiments. These
results prove that advanced VLAs require significantly fewer layers than previously
assumed, offering a highly compute-efficient paradigm for scalable robot learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20246v1
- Authors: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le, Minh Vu, An Thai Le, Ngan Le, Daniel Sonntag, James Zou, Jan Peters, Duy M. H. Nguyen, Ngo Anh Vien
- Published: 2026-06-18T13:57:12Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
