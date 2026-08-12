---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21522v1"
published: "2026-07-23T17:04:36Z"
age_days: 0
score: 32
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# GS-Agent: Creating 4D Physical Worlds With Generative Simulation

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Creating dynamic and physically realistic 4D worlds from natural language descriptions
is both fascinating and challenging. Traditional computer graphics methods rely on
manual creation, requiring extensive human effort to fine-tune materials, motions, and
visual fidelity. Recent advances in generative foundation models have sparked interest
in learning to generate such 4D worlds from large-scale data; however, existing methods
still struggle to ensure physical plausibility and controllability. In this work, we
take a different path by leveraging foundation models to construct an agentic system
that emulates how humans traditionally create 4D worlds, yet automates the entire
process. We present GS-Agent, an end-to-end multi-agent framework that integrates
physics engines in the loop to generate realistic, dynamic, and controllable 4D physical
worlds from natural language. Inspired by how humans build 4D worlds, GS-Agent
decomposes the task into entity management, covering 3D asset curation, material tuning,
placement, and motion control, and rendering configuration, including camera and
lighting manipulation. Multiple agents with distinct expertise interact with the physics
engine via code, seek multimodal feedback, and collaborate to iteratively construct 4D
worlds that align with the given descriptions. Experimental results show that GS-Agent
effectively converts natural language into diverse and physically plausible 4D worlds
exhibiting rich interactions among liquids, deformable objects, and rigid bodies, while
achieving cinematic camera and lighting control. We envision GS-Agent as a foundation
for a new paradigm in 4D world generation, empowering creative content creation and
physical AI. Project page at https://umass-embodied-agi.github.io/gs-agent/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21522v1
- Authors: Hongxin Zhang, Chunru Lin, Junyan Li, Zhou Xian, Tsun-Hsuan Wang, Chuang Gan
- Published: 2026-07-23T17:04:36Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
