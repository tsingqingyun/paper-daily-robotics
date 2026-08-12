---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22998v2"
published: "2026-06-22T08:14:35Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["世界模型"]
---

# TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation

## 为什么重要

自动筛选分数：31

连接概念：[[世界模型]]

## 摘要

Text-conditioned motion generation is a promising interface for programming humanoid
robots, yet current generators are often trained on human motion datasets retargeted to
robot morphologies. Although such data provides rich semantic and kinematic priors, it
fails to capture the nuances of whole-body tracking controllers, including balance,
contact dynamics, actuation limits, and controller-specific failure modes. As a result,
generated motions can be semantically plausible but difficult or impossible for the
robot to execute. We introduce TEXEDO, a test-time scaling framework for humanoid motion
generation that improves motion quality without requiring a stronger underlying
generator. Given a text prompt, TEXEDO samples multiple candidate motions from a
pretrained text-conditioned generator and selects the best motion that is both
executable and task-aligned. The reward model combines a dynamic feasibility verifier,
distilled from whole-body tracking rollouts to predict physical executability, with a
semantic alignment verifier that measures text-motion alignment in a learned co-
embedding space. Our pipeline treats dynamic feasibility as a hard constraint and
semantic alignment as the selection objective within the feasible set. Through large-
scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we
show that TEXEDO consistently improves both tracking fidelity and text alignment. These
results demonstrate that grounded verification is an effective path toward deployable
language-guided humanoid motion generation. Project website:
https://jianuocao.github.io/TEXEDO/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22998v2
- Authors: Jianuo Cao, Yuxin Chen, Yuzhen Song, Masayoshi Tomizuka, Chenran Li, Thomas Tian
- Published: 2026-06-22T08:14:35Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
