---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13239v1"
published: "2026-06-11T11:53:32Z"
age_days: 4
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm

## 为什么重要

自动筛选分数：22

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Existing computer-use agents remain fundamentally limited in professional software
manipulation: GUI-based agents suffer from fragile visual grounding and long-horizon
error accumulation, while API-basedapproaches struggle with heterogeneous protocols and
inaccessible commercial interfaces. In this work,we identify the Component Object Model
(COM) as a unified executable abstraction, proposing COM-as-Action: a new paradigm that
reframes professional software interaction as deterministic program synthesisrather than
sequential visual control. To validate this paradigm in the most demanding environments,
weintroduce ComCADBench, the first benchmark for agents operating real industrial CAD
software. Ourexperiments reveal a substantial paradigm gap: frontier proprietary models
achieve near-zero successunder GUI-based interaction, whereas COM-based execution yields
substantial immediate gains. Tobridge the remaining gap between syntactic correctness
and geometric accuracy, we develop ComActor, aself-correcting agent trained through a
progressive three-stage framework, alongside ComForge, a scalableplatform for large-
scale training in Windows containers. Extensive experiments show that ComActorachieves
state-of-the-art performance on ComCADBench, with strong resilience in long-horizon
taskswhere baselines collapse, and generalizes to external CAD benchmark.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13239v1
- Authors: Jiaxin Ai, Tao Hu, Xuemeng Yang, Shu Zou, Hairong Zhang, Daocheng Fu, Yu Yang, Hongbin Zhou, Nianchen Deng, Pinlong Cai, Zhongyuan Wang, Botian Shi, Kaipeng Zhang, Licheng Wen
- Published: 2026-06-11T11:53:32Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
