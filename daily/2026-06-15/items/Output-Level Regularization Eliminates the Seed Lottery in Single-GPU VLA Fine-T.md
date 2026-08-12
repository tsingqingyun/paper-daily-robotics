---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13856v1"
published: "2026-06-11T19:33:11Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Fine-tuning a vision-language-action model (VLA-JEPA) on a single GPU should be simple:
load a pretrained checkpoint, run training, deploy. There is a hidden danger. Run the
same fine-tuning code thirteen times -- same data, same architecture, different random
seed -- and twelve runs produce a robot succeeding 91--94% of the time, while one run
silently degrades to 65.2%: a 29 pp gap with no error message, no warning, and no way to
predict which seed will fail. We call this the seed lottery. We trace the cause to
output collapse: the action predictor quietly learns to produce nearly identical outputs
regardless of what the robot sees. Existing weight-level methods (L2, EWC) are
structurally blind to this collapse -- they penalize weight changes, but collapse occurs
in directions weights can move freely without affecting outputs, a gap we formalize via
the Jacobian null-space. Across 7 methods x up to 13 seeds x 3 LIBERO benchmarks, three
output-level regularizers -- VICReg (n=12 seeds), Dropout (n=4), and a halved learning
rate (n=5) -- each eliminate every catastrophic seed (0/21 combined collapses vs. 1/13
Baseline; F(12,11)=28.7, p<0.001), while weight-level methods (L2, EWC) preserve the
lottery. The simplest fix is changing one number in your optimizer config.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13856v1
- Authors: Jeffrin Sam, Dzmitry Tsetserukou
- Published: 2026-06-11T19:33:11Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
