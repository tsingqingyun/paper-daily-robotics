---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13279v1"
published: "2026-06-11T12:33:55Z"
age_days: 1
score: 35
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

In bimanual robotic manipulation, task-relevant visual information varies with the task
stage and context, while the interaction of the two arms shifts between independent and
coordinated modes, making policy learning challenging. However, existing monolithic
Vision-Language-Action (VLA) policies process diverse visual inputs and interaction
patterns through a single shared representation and action generation pathway, often
failing to separately account for visual relevance and bimanual interaction structure.
To address this issue, we propose a bimanual manipulation VLA framework based on Dual-
Level Structural Decomposition. The View-Selective Visual Router dynamically adjusts
wrist-view contributions to emphasize relevant visual cues, while the Interaction-Aware
Action Mixture-of-Experts (MoE) decomposes action generation into coordinated and arm-
wise pathways to adapt to varying bimanual interaction modes. We evaluate the proposed
method on six simulated bimanual manipulation tasks in RoboTwin 2.0 and three long-
horizon real-world tasks. Our model improves the overall average success rate over a
monolithic baseline by 27.7% in simulation and 43.3% in real-world evaluation, while
consistently outperforming single-module variants across both settings. These results
demonstrate that jointly considering selective visual processing and explicit
decomposition of bimanual interaction structures provides an effective inductive bias
for robust bimanual manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13279v1
- Authors: Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim
- Published: 2026-06-11T12:33:55Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
