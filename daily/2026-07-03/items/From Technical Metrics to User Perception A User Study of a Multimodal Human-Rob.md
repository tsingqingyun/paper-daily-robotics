---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00530v1"
published: "2026-07-01T07:19:00Z"
age_days: 2
score: 31
created: 2026-07-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection and Grasping

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Improvements in the technical performance of human--robot interaction (HRI) systems do
not automatically translate into differences that human users can detect during live
interaction. This paper investigates whether a 15 percentage point gain in end-to-end
task success (from 75% in a multimodal baseline system to 90% in an improved
configuration identified through a prior ablation study) is sufficient to produce
consistent and measurable differences in user perception. The baseline system combines
Whisper for speech recognition, Florence-2 for open-vocabulary object detection, LLaMA
3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
execution. The improved configuration replaces the perception and language modules with
Grounding DINO + SAM and Qwen 3.5 9B, respectively, while retaining the same controller.
A within-subject user study with 24 participants compared both systems on the same
tabletop object-grasping task. After interacting with each configuration, participants
rated perceived speed, reliability, and overall competence and fluency on a 7-point
Likert scale. Results show that 17 out of 24 participants (70.83%) preferred the
improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual
constructs were rated significantly higher for the improved configuration after Holm
correction, with large to very large effect sizes (p < 0.001). These findings confirm
that the identified technical improvements are perceptible to users in direct
interaction and underscore the importance of complementing benchmark evaluation with
user-centred evidence when assessing robotic manipulation pipelines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00530v1
- Authors: Jian Song, Tian Zi, Shen Guanting
- Published: 2026-07-01T07:19:00Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
