---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25802v1"
published: "2026-05-25T12:51:35Z"
age_days: 0
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Rethinking VLM Representation for VLA Initialization

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-Language-Action (VLA) models widely adopt pretrained Vision-Language Models
(VLMs) as policy backbones, yet it remains unclear what kind of pretrained VLM
representation is useful as a VLA initialization. In this paper, we study VLA
initialization as a controlled representation-design problem along three axes:
capability-level embodied VQA supervision, parameter-update strategy, and robot-data
pretraining. Our experiments show that the original pretrained VLM representation is a
key source of action performance. However, embodied VQA adaptation does not yield
uniform gains: its benefit depends on downstream bottlenecks, and gains from different
capability domains are not simply additive. For update strategy, LoRA provides a more
reliable initialization than Full Finetune, indicating that overly reshaping the
pretrained representation can weaken VLA initialization. Robot-data pretraining further
improves VLA initialization, with the strongest variant obtained by staged LoRA-based
training. Together, these findings suggest that effective VLM-to-VLA adaptation should
inject action-relevant embodied and robot-trajectory signals while preserving the
pretrained VLM representation that remains useful for action learning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25802v1
- Authors: Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An, Xinyu Wei, Jianbo Liu, Hongsheng Li
- Published: 2026-05-25T12:51:35Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
