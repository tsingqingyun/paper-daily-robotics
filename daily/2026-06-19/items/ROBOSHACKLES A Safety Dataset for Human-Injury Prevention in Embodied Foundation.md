---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18632v1"
published: "2026-06-17T03:03:16Z"
age_days: 1
score: 39
created: 2026-06-19
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models

## 为什么重要

自动筛选分数：39

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Embodied Foundation Models (EFMs) integrate multimodal understanding, future-state
reasoning, and executable robot actions. Yet their safety alignment for human-injury
prevention remains underexplored, primarily because real-world data of robots harming
humans or creating hazardous household situations cannot be safely or ethically
collected. To address this challenge, we propose a safety-critical data construction
pipeline for human-injury prevention in EFMs.Starting from real DROID observations, our
construction pipeline proceeds through scene understanding, hazard-aware image editing,
temporal prompt generation, and single-pass rollout synthesis. The temporal prompts
specify the expected scene evolution, while Wan2.7 synthesizes realistic robotic
rollouts from the edited hazardous states in a single pass. Using this pipeline, we
construct ROBOSHACKLES, a 10,000-clip robotic video dataset derived from real DROID
observations, spanning two direct-harm and four indirect-harm categories. To ensure
dataset quality, we assess task completion and visual quality with automatic metrics,
and evaluate six representative EFMs under a refusal-based safety criterion. Results
show that all evaluated models produce unsafe actions in the tested safety-critical
scenarios, yielding a 100% unsafe action generation rate. ROBOSHACKLES serves as a
scalable benchmark and training resource for refusal learning and hazard anticipation
before robot action execution.The dataset is publicly available at
https://huggingface.co/datasets/YZW00/RoboShackles.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18632v1
- Authors: Zhuowen Yin, Chongyang Liu, Wenzhang Yang, Renjue Li, Yinxing Xue
- Published: 2026-06-17T03:03:16Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
