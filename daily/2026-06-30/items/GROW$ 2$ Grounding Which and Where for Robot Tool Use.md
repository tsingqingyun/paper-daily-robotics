---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30632v1"
published: "2026-06-29T17:56:53Z"
age_days: 0
score: 27
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# GROW$^2$: Grounding Which and Where for Robot Tool Use

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Can the robot use a plate to cut a cake if no knife is available? Tool use greatly
expands robot capabilities, but to use tools creatively beyond their intended functions,
the robot faces the challenge of $\textit{open-world affordance grounding}$: select an
open-category object to act as a tool and localize its specific region of action. To
this end, we introduce GROW$^2$ (GROunding Which and Where), which leverages object
parts as a natural abstraction to split the grounding process hierarchically into
semantic and geometric levels, thus bypassing the need for data-heavy, end-to-end
training. Semantically, GROW$^2$ harnesses the commonsense reasoning of Vision-Language
Models (VLMs) to parse a natural-language task instruction, select a suitable object as
the tool, and identify task-relevant parts on the tool and the target object.
Geometrically, vision foundation models then ground the selected parts into precise 3D
regions from a single RGB-D image. Experiments on established benchmarks show that
GROW$^2$ outperforms state-of-the-art baselines on affordance prediction benchmarks.
Further, it achieves zero-shot generalization over open-category objects and outperforms
baselines in both simulated and real-world robot tool use experiments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30632v1
- Authors: Yuhong Deng, Yuyao Liu, David Hsu
- Published: 2026-06-29T17:56:53Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
