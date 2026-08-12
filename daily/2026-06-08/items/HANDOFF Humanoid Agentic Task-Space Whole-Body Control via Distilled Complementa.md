---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.06493v1"
published: "2026-06-04T17:59:50Z"
age_days: 3
score: 30
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

For a humanoid robot to be deployed in the real world, the choice of command space
(i.e., the interface between task planning and whole-body control) is crucial. Existing
whole-body controllers typically demand dense kinematic or spatial references that
planners struggle to synthesize from task semantics. We instead propose a compact,
explicit interface that is intuitive, general, modular, and expressive enough for
diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid whole-
body controller that follows this interface and is distilled via multi-teacher KL
distillation under a context-conditioned gating scheme into a mixture-of-experts student
from three complementary specialists: whole-body motion tracking with safety-filtered
data, locomotion, and fall-recovery. On the Unitree G1, HANDOFF matches state-of-the-art
velocity tracking and offers one of the largest robust manipulation workspaces. We
further demonstrate hardware feasibility through multiple natural-language-driven task
roll-outs, powered by a VLM-driven agentic planner with no task-specific data or
controller fine-tuning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.06493v1
- Authors: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames
- Published: 2026-06-04T17:59:50Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
