---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21571v1"
published: "2026-07-23T17:50:45Z"
age_days: 0
score: 28
created: 2026-07-24
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Embodied question answering (EQA) is traditionally evaluated under an episodic
formulation, where agents solve each task independently and reset internal state between
episodes. However, real-world robots operate continuously and must accumulate, retain,
and selectively reuse information acquired from prior interactions. Despite this
practical requirement, the architectural mechanisms needed to support sequential memory
in EQA remain underexplored. In this work, we investigate how different memory
architectures behave when EQA agents are evaluated sequentially, with multiple questions
answered in the same scene while memory is carried forward across queries. We find that
simply preserving existing memory is often insufficient. Agents that retain only
traversability information, such as 2D occupancy maps, remember where the robot has
explored but not the visual-semantic evidence needed for later questions. Agents trained
on short-horizon episodic data face a different challenge: when exposed to continuous,
multi-query histories, their inherited context suffers from severe temporal mismatch,
rather than forming a reusable scene representation. To overcome this architectural
bottleneck, we highlight the necessity of structured, spatially grounded memory:
architectures that map persistent visual observations onto metric 3D geometry preserve
visual-semantic evidence in a coherent scene representation. Extensive experiments in
simulated environments reveal that this form of memory breaks the accuracy-efficiency
tradeoff in sequential settings, simultaneously achieving higher answer accuracy and
lower navigation costs. We further validate these findings on a real-world mobile robot,
demonstrating that spatially grounded visual memory is critical for enabling continuous,
intelligent operation in physical environments.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21571v1
- Authors: Zikui Cai, Kaushal Janga, Tan Dat Dao, Seungjae Lee, Shivin Dass, Mingyo Seo, Kaiyu Yue, Mintong Kang, Nandhu Pillai, Monte Hoover, Aadi Palnitkar, Ruchit Rawal, Ruijie Zheng, Bo Li, Yuke Zhu, Roberto Martín-Martín, Tom Goldstein, Furong Huang
- Published: 2026-07-23T17:50:45Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
