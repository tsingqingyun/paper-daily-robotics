---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12299v1"
published: "2026-06-10T16:34:49Z"
age_days: 3
score: 28
created: 2026-06-14
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-Language-Action (VLA) models provide a natural language interface to robot
control, but the mapping from language to behavior is often brittle and unintuitive:
semantically similar instructions can induce drastically different behaviors, while some
capabilities may not be elicitable through prompting alone. As a result, both human
instructions and zero-shot language models can fail to reliably steer VLAs toward
successful task execution. In this work, we propose a framework that interactively
searches for language sequences that improve closed-loop VLA task performance, distills
these sequences into a test-time language feedback policy (LFP), and learns an
improvement head that predicts when language steering will improve performance. We
conformalize this improvement head to prevent harmful steering interventions, where the
LFP decreases task performance relative to the original instruction on out-of-
distribution scenarios. Crucially, our approach operates on arbitrary frozen pre-trained
VLAs, requiring neither access to the original training distribution nor fine-tuning of
the underlying model. On seen environments, our conformalized LFP improves base VLA
performance by 24.7% in simulation and 65.0% in hardware. On visual and semantic
perturbations, our conformalized LFP has strong harmlessness guarantees, and produces
recovery behaviors not observed with open-loop prompting.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12299v1
- Authors: Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy
- Published: 2026-06-10T16:34:49Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
