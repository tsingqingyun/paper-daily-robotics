---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20345v1"
published: "2026-07-22T16:30:51Z"
age_days: 1
score: 40
created: 2026-07-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Closing the gap between benchmark performance and reliable real-world operation remains
a central challenge for Vision-Language-Action (VLA) humanoid robots, which must handle
execution errors, distribution shifts, and environmental variability. This paper
presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems-
level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu
humanoid robot and the GR00T N1.6 foundation model. DEED comprises three key components:
(1) a data-efficient post-training pipeline with control-frequency alignment, data
curation, task-relevant visual highlighting, and reduced VLA dependence; (2) a real-
world study of experience-driven refinement, adapted from RECAP via a text-based
advantage prefix and a vision-language value function; and (3) a latent-space analysis
tool for studying in- and out-of-distribution behavior. Our results suggest that
bridging the lab-to-store gap is primarily a systems integration challenge rather than
an architectural one: careful data design and targeted post-training can transform a
policy that fails under naive fine-tuning into a competent real-world system using only
a single GPU.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20345v1
- Authors: Roger Sala Sisó, Tiago Silvério, Jakob Sand, Tran Nguyen Le
- Published: 2026-07-22T16:30:51Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
