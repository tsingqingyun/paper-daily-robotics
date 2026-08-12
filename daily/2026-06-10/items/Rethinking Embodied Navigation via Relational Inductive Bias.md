---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.10348v1"
published: "2026-06-09T02:57:34Z"
age_days: 0
score: 30
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Rethinking Embodied Navigation via Relational Inductive Bias

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Object navigation requires an agent to locate a target in an unknown environment through
visual observations. Existing methods typically rely on open-vocabulary detectors or
vision-language models (VLMs) to answer where to search, but often overlook what not to
trust - which semantic cues are unreliable. Open-vocabulary perception is prone to
systematic misleading evidence: false positives, outdated static priors, and repeated
failed exploration due to lack of embodied verification, which contaminates mapping and
decision-making. Such errors are rooted in structured object relations in real-world
scenes. To address this, we propose DB-Nav, a framework that reshapes the search space
via dual relational biases. It factorizes target-centric relations into an Activation
Bias (propagates contextual evidence) and an Inhibition Bias (suppresses unreliable
regions via perceptual confusion and action-level falsification). These biases are
unified into a Relational Activation-Inhibition Exploration Graph that modulates
frontier exploration values using online observations and failed accesses. Experiments
on ObjectNav benchmarks show that DB-Nav significantly outperforms existing methods in
success rate (SR) and Success weighted by Path Length (SPL), offering a lightweight,
interpretable, and robust navigation framework without costly online VLM reasoning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.10348v1
- Authors: Weitao An, Chenghao Xu, Xu Yang, Cheng Deng
- Published: 2026-06-09T02:57:34Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
