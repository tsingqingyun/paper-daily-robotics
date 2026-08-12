---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02417v1"
published: "2026-07-02T16:48:43Z"
age_days: 0
score: 31
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# LIME: Learning Intent-aware Camera Motion from Egocentric Video

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Autonomous robots often need to move their camera before they can act: to inspect an
object, reveal an occluded region, or obtain a view that responds to a user's intent.
While vision-language navigation translates instructions to base motion and vision-
language-action policies map instructions to manipulation actions, language-conditioned
camera motion remains comparatively underexplored as a first-class action. We formulate
language-conditioned camera motion generation: given a current RGB observation and a
free-form natural-language intent, predict a relative target camera pose for the next
observation. This task is inherently non-trivial: viewpoint changes are driven by latent
perceptual intentions, and a valid motion may operate at different semantic granularity,
from entering a room to looking around a corner, inspecting a visible object, or
revealing an occluded detail. To model this structure, we mine multi-intention camera-
motion supervision from egocentric video, pairing plausible intents and observation-gain
descriptions with relative SE(3) target poses. We propose LIME, a vision-language
camera-motion generator that combines an auto-regressive observation-gain output with a
continuous flow-matching pose head. This design lets the model jointly predict what the
next view should reveal while representing multi-hypothesis target views. Across
experiments and downstream robotic tasks, we show that LIME can learn to actively choose
camera poses from passive human video, turning ordinary egocentric recordings into
supervision for intent-aware active perception.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02417v1
- Authors: Boyang Sun, Jiajie Li, Yung-Hsu Yang, Chenyangguang Zhang, Tim Engelbracht, Sunghwan Hong, Cesar Cadena, Marc Pollefeys, Hermann Blum
- Published: 2026-07-02T16:48:43Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
