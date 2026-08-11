---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09410v1"
published: "2026-08-10T10:35:47Z"
age_days: 0
score: 45
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation

## 为什么重要

自动筛选分数：45

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

Modern vision-language-action (VLA) policies have acquired broad manipulation skills,
but typically generate each action chunk from the current observation or a short fixed-
length history. However, real-world manipulation is often non-Markovian, requiring
robots to retain and reason over task-relevant information from long-horizon interaction
histories to determine the next action. To address this challenge, we propose HyMeS, a
hybrid learning framework that leverages the reasoning and memory-management
capabilities of coding agents to steer a Markovian VLA for memory-dependent
manipulation. Specifically, HyMeS learns low-level motor skills through gradient-based
imitation learning, while a coding agent acquires high-level memory-management
strategies through heuristic learning by iteratively updating an executable heuristic
system from rollout feedback. Furthermore, we close the loop between steering and
execution through multimodal stage-completion verification, which updates memory using
proprioceptive signals and multi-frame VLM judgments. Compared with end-to-end memory-
augmented VLAs, HyMeS requires demonstrations only for reusable motor skills rather than
for every history-dependent task configuration, enabling data-efficient compositional
generalization. On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to
66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem
by 4.5 points in cumulative success and 14.5 points in task success.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09410v1
- Authors: Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu
- Published: 2026-08-10T10:35:47Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
