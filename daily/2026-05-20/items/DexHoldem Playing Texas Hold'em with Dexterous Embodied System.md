---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18727v1"
published: "2026-05-18T17:51:34Z"
age_days: 1
score: 31
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# DexHoldem: Playing Texas Hold'em with Dexterous Embodied System

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Evaluating embodied systems on real dexterous hardware requires more than isolated
primitive skills: an agent must perceive a changing tabletop scene, choose a context-
appropriate action, execute it with a dexterous hand, and leave the scene usable for
later decisions. We introduce DexHoldem, a real-world system-level benchmark built
around Texas Hold'em dexterous manipulation with a ShadowHand. DexHoldem provides 1,470
teleoperated demonstrations across 14 Texas Hold'em manipulation primitives, a
standardized physical policy benchmark, and an agentic perception benchmark that tests
whether agents can recover the structured game state needed for embodied decision
making. On primitive execution, $π_{0.5}$ obtains the highest task completion rate
($61.2\%$), while $π_{0.5}$ and $π_0$ tie on scene-preserving success rate ($47.5\%$).
On agentic perception, Opus 4.7 obtains the best strict problem-level accuracy
($34.3\%$), while GPT 5.5 obtains the best average field-wise accuracy ($66.8\%$),
exposing a gap between isolated visual sub-capabilities and complete routing-relevant
state recovery. Finally, we instantiate the full embodied-agent loop in three case
studies, where waiting, recovery dispatches, human-help requests, and repeated primitive
execution reveal how perception and policy errors accumulate during closed-loop
deployment. DexHoldem therefore evaluates dexterous tabletop execution, agentic
perception, and embodied decision routing in a shared physical setting. Project page:
https://dexholdem.github.io/Dexholdem/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18727v1
- Authors: Feng Chen, Tianzhe Chu, Li Sun, Pei Zhou, Zhuxiu Xu, Shenghua Gao, Yuexiang Zhai, Yanchao Yang, Yi Ma
- Published: 2026-05-18T17:51:34Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
