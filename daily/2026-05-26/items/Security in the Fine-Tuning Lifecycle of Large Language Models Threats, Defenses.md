---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25073v1"
published: "2026-05-24T13:34:47Z"
age_days: 1
score: 28
created: 2026-05-26
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Background: Fine-tuning is central to adapting pre-trained Large Language Models (LLMs)
to downstream tasks, but its reliance on training data, parameter updates, and reusable
components opens entry points for attackers. Threats have evolved from data poisoning
and weight tampering to agent manipulation and interface exploitation, yet existing
reviews lack a unified framework spanning the full fine-tuning lifecycle. Objective:
This paper presents a systematic survey of LLM fine-tuning security and establishes a
lifecycle-based framework for comparing attacks and defenses, complemented by unified
empirical evaluation. Methods: We divide attack and defense mechanisms into three phases
by intervention timing: pre-tuning, during-tuning, and post-tuning. Within each phase,
strategies are reviewed and contrasted to expose their evolution and limitations.
Representative methods are then evaluated under a unified model, hardware, and protocol
setup, with cross-phase experiments pairing attacks and defenses from different phases.
Results: Attack effectiveness is highly model-dependent and non-monotonic with scale:
weight-editing attacks effective on earlier models lose impact on modern open-source
LLMs; cross-lingual backdoor transfer, reported as near-perfect at larger scales, fails
entirely on tested 1B-4B models; and purely benign samples can compromise safety
alignment in instruction-tuned models. Single-phase defenses rarely generalize across
phases, and defense effectiveness depends jointly on model architecture and alignment
state. Conclusion: We identify key open problems (configuration-robust defense, cross-
phase defense composition, and embedding-space attacks beyond behavioral assumptions)
and propose concrete future research directions.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25073v1
- Authors: Wenjuan Li, Yitao Liu, Runze Chen, Rajkumar Buyya
- Published: 2026-05-24T13:34:47Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
