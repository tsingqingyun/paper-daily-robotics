---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02222v1"
published: "2026-07-02T14:26:55Z"
age_days: 0
score: 34
created: 2026-07-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation

## 为什么重要

自动筛选分数：34

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language Navigation has increasingly emphasized high-level instruction reasoning,
memory, global map construction, and instruction decomposition, while the low-level
action representation remains comparatively underexplored. We propose CoFL-S, a low-
level vision-language-action framework that predicts a language-conditioned flow field
over the robot's local visible sector and generates continuous trajectories by rolling
out the predicted field. To train this low-level representation, we convert each VLN-CE
episode, originally a whole-episode instruction paired with an action sequence, into
frame-level local supervision with aligned sub-instructions and matched action,
trajectory, and dense flow-field targets. For evaluation, we introduce a continuous-time
Habitat benchmark that isolates low-level action interfaces from instruction
decomposition and executes all methods through a shared velocity-command controller,
enabling decomposition-independent closed-loop comparison across different planner
frequencies rather than fixed discrete forward-and-turn transitions in VLN-CE. Under
matched encoders and training settings, CoFL-S consistently outperforms action-token and
action-chunk baselines across planner frequencies in the continuous-time Habitat
benchmark, and zero-shot real-world closed-loop deployment further shows its advantage
over both baselines beyond simulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02222v1
- Authors: Haokun Liu, Zhaoqi Ma, Yicheng Chen, Wentao Zhang, Masaki Kitagawa, Zicen Xiong, Jinjie Li, Moju Zhao
- Published: 2026-07-02T14:26:55Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
