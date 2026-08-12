---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15982v1"
published: "2026-07-17T14:18:20Z"
age_days: 2
score: 26
created: 2026-07-20
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Data and Learning Where it Matters for Contact-Rich Manipulation

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Learned policies trained end-to-end on large datasets often remain brittle in high-
precision tasks and struggle with generalization. We find that these limitations largely
stem from a lack of structure and focus in data collection. Our key insight is to
leverage dense data collection only for the critical segment of contact-rich tasks and
to rely on traditional planning during simple free-space motion. We propose an automated
data-collection scheme in combination with offline deep reinforcement learning for the
critical segment of the task, eliminating reliance on a teleoperator's skill and on
online policy updates. Across four challenging real-world tasks, using only 2 to 2.5
hours of autonomous data collection, we achieve an average success rate of 96%, compared
to the strongest baseline at 55%. Notably, performance remains high in out-of-
distribution scenarios where end-to-end approaches struggle. Our results pave the way
for targeted data collection for contact-rich tasks and for high success rates in
precision applications.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15982v1
- Authors: Oliver Hausdörfer, Linus Schwarz, Gabor Marko, Christian Dietz, Timo Class, Luka Hofer, Jim Yun-Jin Li, Johannes Hechtl, Ralf Römer, Angela P. Schoellig
- Published: 2026-07-17T14:18:20Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
