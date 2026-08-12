---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12616v1"
published: "2026-06-10T19:16:31Z"
age_days: 2
score: 31
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Closed-loop driving simulators typically populate their environments with non-ego
traffic agents that behave largely the same way, produced either by rule-based traffic
managers or by learned models trained toward a single behavioral mode. Recent work
introduces style variation through post-hoc labels on observational data or LLM-inferred
reward weights, but these signals act as proxies for what a style should reward rather
than demonstrations of humans explicitly asked to drive in that style. We introduce
PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on
retrieved demonstrations from a style-instructed human driving dataset, in which
participants drive CARLA leaderboard routes under aggressive, neutral, and conservative
instructions on a driver-in-the-loop rig. The pipeline has three stages: (i) offline
triplet mining over per-style human driving data using a combined image-text similarity
score; (ii) training a lightweight retrieval head that fuses frozen visual features with
a small control encoder over per-style databases; and (iii) fine-tuning a single VLA
backbone to treat retrieved context points as in-context behavioral demonstrations
during waypoint prediction. At inference, the same backbone is conditioned on any style
by swapping which per-style database the retrieval head queries, so selecting a style
requires no per-style retraining while enabling human-style, style-diverse non-ego
agents for closed-loop simulation. On Bench2Drive, PersonaDrive (no style) improves the
driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning
attains the highest driving score in every style within a roughly 2% band (its weakest
style surpassing the strongest baseline, DMW, by 5.4%), while average speed and
acceleration rise by 18% and 25% from the conservative to the aggressive instruction.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12616v1
- Authors: Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki
- Published: 2026-06-10T19:16:31Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
