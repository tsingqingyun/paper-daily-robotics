---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13119v1"
published: "2026-05-13T07:40:34Z"
age_days: 0
score: 36
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-language-action (VLA) models are effective robot action executors, but they
remain limited on long-horizon tasks due to the dual burden of extended closed-loop
planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy
that distributes this burden across a high-level vision language model (VLM) agent for
temporal reasoning and a family of specialized VLA tools for diverse local physical
operations. The VLM handles scene analysis, global planning, and recovery, while each
VLA tool executes a bounded subtask. To tightly couple agent planning with VLA tool
execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes
explicit tool selection and in-execution progress feedback, enabling efficient event-
triggered agent replanning without continuous agent polling. To obtain diverse
specialized VLA tools that faithfully follow agent invocations, we further propose Tool-
Aligned Post-Training (TAPT), which constructs invocation-aligned training units for
instruction following and adopts tool-family residual adapters for efficient tool
specialization. Experiments show that VLAs-as-Tools improves the success rate of
$π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances
invocation fidelity by 15.0 points as measured by Non-biased Rate. Code will be
released.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13119v1
- Authors: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
- Published: 2026-05-13T07:40:34Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
