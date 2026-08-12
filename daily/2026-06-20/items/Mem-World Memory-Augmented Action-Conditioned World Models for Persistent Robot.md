---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18960v2"
published: "2026-06-17T11:42:00Z"
age_days: 2
score: 29
created: 2026-06-20
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation

## 为什么重要

自动筛选分数：29

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Action-conditioned world models have emerged as a promising paradigm for robot learning,
offering a scalable alternative to costly real-world experimentation by generating
action-consistent video rollouts. However, persistent world modeling remains challenging
in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the
current observation insufficient for predicting future views, causing models to forget
or hallucinate scene details seen in earlier frames. Existing memory retrieval
strategies often fail to identify informative history in dynamic manipulation scenarios.
To address this limitation, we propose Mem-World, a memory-augmented multi-view action-
conditioned world model. At its core, we present W-VMem, a 4D wrist-view-centered
surfel-indexed memory that anchors historical observations to temporally evolving
surface elements. By explicitly modeling when and where scene elements are observed,
W-VMem enables geometry-aware retrieval of relevant history frames conditioned on future
actions. During generation, relevant history frames are selected via surfel-based
rendering and scoring, providing informative and non-redundant context for prediction.
Extensive experiments show that Mem-World generates persistent rollouts in complex
manipulation scenarios, enables more reliable policy evaluation than Ctrl-World,
improving the Pearson correlation with real-world performance by 14.5\%, and supports
effective policy improvement through synthetic data generation, increasing success rates
from 58\% to 72\% on long-horizon tasks.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18960v2
- Authors: Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
- Published: 2026-06-17T11:42:00Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
