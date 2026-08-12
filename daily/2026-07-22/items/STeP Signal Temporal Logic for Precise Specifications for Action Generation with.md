---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18580v1"
published: "2026-07-20T23:26:32Z"
age_days: 1
score: 36
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) models have shown impressive generalization, but often lack
interpretability and can struggle to follow precise natural language instructions that
encode spatial, temporal, and logical requirements. We propose a hierarchical framework
that uses Signal Temporal Logic (STL) as a shared representation connecting high-level
language understanding with low-level robot execution. A high-level policy leverages a
VLM to decompose language instructions into high-level subtasks, generate STL
specifications for each subtask, and choose a low-level policy for executing each
subtask. The STL specifications translate language-derived intent into precise
constraints, and the low-level policy selection determines whether those constraints are
enforced directly through STL-guided model-predictive control or monitored during
execution of a learned policy for perceptually complex, or contact-rich behaviors. By
integrating STL into plan validation, low-level policy, subtask monitoring, and
replanning, our framework enables language-derived plans to be checked, optimized, and
revised at runtime using a common formal structure. We evaluate the approach on a real-
world tabletop domain, demonstrating how formal specifications can improve the
precision, reliability, and interpretability of language-conditioned robot planning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18580v1
- Authors: Kasra Torshizi, Anukriti Singh, Sidharth Mathur, Khuzema Habib, Leo Du, Pratap Tokekar
- Published: 2026-07-20T23:26:32Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
