---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13461v1"
published: "2026-07-15T05:46:34Z"
age_days: 1
score: 32
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Joint On-and-Off Policy Learning for Vision-and-Language Navigation

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Vision-and-Language Navigation (VLN) necessitates an embodied agent to navigate in the
physical world by adhering to natural language instructions. Recent advancements in
Vision-Language Models (VLM) have propelled the development of VLM-based VLN methods
with two predominant paradigms: (1) imitation learning (IL) on expert demonstrations,
followed by the Dataset Aggregation (DAgger) algorithm to bolster error recovery
capabilities; (2) reinforcement learning (RL) driven by verifiable rewards to enhance
reasoning and exploration. A notable gap is the absence of integration between these two
distinct paradigms. This paper introduces JOP-VLN, a novel VLN framework that
synergistically combines off-policy imitation learning and on-policy exploration within
a three-stage training pipeline. Initially, IL is employed on expert demonstrations to
acquire basic navigation skills. Subsequently, the DAgger algorithm is utilized to
generate heuristic exploration trajectories, which are then used for imitation learning
to improve error recovery capabilities. Finally, a joint on-and-off policy learning
framework is implemented, featuring high-entropy trajectory sampling to enhance RL
training efficiency and an error-correction-prioritized trajectory sorting strategy for
effective error correction. Extensive experiments demonstrate the efficacy of JOP-VLN,
achieving success rates of 69.9% and 68.0% on the VLN-CE R2R and RxR benchmarks,
respectively, setting a new state-of-the-art on R2R. Project page:
https://qingrongh.github.io/JOP-VLN.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13461v1
- Authors: Qingrong He, Lin Zhao, Kevin Zheng, Liang Lin
- Published: 2026-07-15T05:46:34Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
