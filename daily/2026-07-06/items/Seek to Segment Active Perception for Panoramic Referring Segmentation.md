---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02497v1"
published: "2026-07-02T17:56:49Z"
age_days: 3
score: 29
created: 2026-07-06
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Seek to Segment: Active Perception for Panoramic Referring Segmentation

## 为什么重要

自动筛选分数：29

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Existing referring segmentation models passively process static images captured from
fixed perspectives, limiting their applicability in Embodied AI, where agents must
perform active perception in the continuous 360$^\circ$ environments. To bridge this
gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this
setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the
360$^\circ$ environment, seeking the object specified by a user instruction for
segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented
agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker
integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual
memory. By progressively integrating sequential local observations into a unified
360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-
redundant search trajectories. Once the target is found, the agent performs active
viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-
annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning,
followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's
exploration efficiency. Extensive experiments on our newly established APRS benchmark
demonstrate that PanoSeeker achieves superior search efficiency and segmentation
accuracy, significantly outperforming adapted state-of-the-art baselines.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02497v1
- Authors: Song Tang, Shuming Hu, Xincheng Shuai, Henghui Ding, Yu-Gang Jiang
- Published: 2026-07-02T17:56:49Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
