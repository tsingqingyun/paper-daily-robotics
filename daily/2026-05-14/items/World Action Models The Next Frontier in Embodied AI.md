---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12090v1"
published: "2026-05-12T13:10:52Z"
age_days: 1
score: 42
created: 2026-05-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# World Action Models: The Next Frontier in Embodied AI

## 为什么重要

自动筛选分数：42

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models have achieved strong semantic generalization for
embodied policy learning, yet they learn reactive observation-to-action mappings without
explicitly modeling how the physical world evolves under intervention. A growing body of
work addresses this limitation by integrating world models, predictive models of
environment dynamics, into the action generation pipeline. We term this emerging
paradigm World Action Models (WAMs): embodied foundation models that unify predictive
state modeling with action generation, targeting a joint distribution over future states
and actions rather than actions alone. However, the literature remains fragmented across
architectures, learning objectives, and application scenarios, lacking a unified
conceptual framework. We formally define WAMs and disambiguate them from related
concepts, and trace the foundations and early integration of VLA and world model
research that gave rise to this paradigm. We organize existing methods into a structured
taxonomy of Cascaded and Joint WAMs, with further subdivision by generation modality,
conditioning mechanism, and action decoding strategy. We systematically analyze the data
ecosystem fueling WAMs development, spanning robot teleoperation, portable human
demonstrations, simulation, and internet-scale egocentric video, and synthesize emerging
evaluation protocols organized around visual fidelity, physical commonsense, and action
plausibility. Overall, this survey provides the first systematic account of the WAMs
landscape, clarifies key architectural paradigms and their trade-offs, and identifies
open challenges and future opportunities for this rapidly evolving field.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12090v1
- Authors: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu, Chenchen Yang, Yikang Zhou, Zhaoye Fei, Jingjing Gong, Jinlan Fu, Mike Zheng Shou, Xuanjing Huang, Xipeng Qiu, Yu-Gang Jiang
- Published: 2026-05-12T13:10:52Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
