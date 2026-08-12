---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25901v1"
published: "2026-05-25T14:29:04Z"
age_days: 0
score: 28
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent"]
---

# AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]]

## 摘要

3D Visual Grounding (3DVG) is an essential capability for embodied AI, requiring agents
to localize objects in 3D scenes based on natural language descriptions. Recent zero-
shot methods leverage 2D vision-language models (LVLMs). However, they often rely on
existing sets of multi-view images and struggle with the limited semantic and spatial
details provided by standard 3D segmentation tools. We present $\textbf{AgentGrounder}$,
a zero-shot 3D visual grounding framework that operates directly on colored point clouds
without task-specific 3D training. Our approach follows a two-stage design: (1) an
offline stage that applies 3D model to build an Object Lookup Table (OLT) with instance
IDs, semantic labels, 3D bounding boxes; and (2) an online tool-driven agent that
decomposes each query, retrieves only relevant candidates from the OLT, performs
geometric scoring, and triggers image rendering on demand when additional visual
evidence (e.g., color, material, or viewpoint-sensitive cues) is required. Compared with
fixed anchor-target matching pipelines, this design reduces cascading matching errors
and improves context-window efficiency by avoiding prompts overloaded with irrelevant
objects. We evaluate on ScanRefer and Nr3D under a zero-shot setting and observe
consistent improvements over SeeGround in our setup, including +2.5% Acc@0.5 on
ScanRefer and +6.3% on Nr3D, with a notable +6.3% gain on Nr3D view-independent queries.
These results show that combining selective retrieval, geometric reasoning, and adaptive
visual inspection yields a practical and robust foundation for open-vocabulary 3D
grounding. Our code is available at https://github.com/be2rlab/AgentGrounder.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25901v1
- Authors: Cuong Huynh, Maxim Popov, Denis Gridusov, Sergey Kolyubin
- Published: 2026-05-25T14:29:04Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
