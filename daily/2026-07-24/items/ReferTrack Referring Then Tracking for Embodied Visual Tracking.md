---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.20061v1"
published: "2026-07-22T12:05:13Z"
age_days: 1
score: 45
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# ReferTrack: Referring Then Tracking for Embodied Visual Tracking

## 为什么重要

自动筛选分数：45

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Embodied visual tracking (EVT) requires a mobile agent to continuously follow a specific
target described in natural language using only onboard vision. While recent vision-
language-action (VLA) policies unify target identification and trajectory planning,
their chain-of-thought (CoT) reasoning often operates in abstract spatial latents that
are difficult to supervise and weakly aligned with explicit image-space detections. To
address this, we introduce ReferTrack, a referring-then-tracking paradigm that grounds
EVT using a single forward-facing camera. Our model first selects the target from an
indexed set of bounding boxes, then decodes tracking waypoints conditioned on this
image-grounded decision. To preserve target motion cues over time, ReferTrack maintains
a sliding-window queue of previously selected bounding boxes, injecting their geometric
features into the visual history via temporal-viewpoint-bbox indicator (TVBI) tokens. We
further enhance target identification by co-training on a custom Refer-QA dataset. On
EVT-Bench, ReferTrack achieves state-of-the-art single-view performance with success
rates of 89.4%, 73.3%, and 74.1% on the single-target, distracted, and ambiguity
tracking splits, respectively -- matching or even surpassing several multi-camera
baselines on identification-heavy tasks. Finally, real-world deployments on legged and
humanoid robots validate its robust sim-to-real transfer capabilities. Code is available
at https://github.com/MedlarTea/referTrack.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.20061v1
- Authors: Hanjing Ye, Tianle Zeng, Jiazhao Zhang, Shaoan Wang, Zibo Zhang, Weisi Situ, Yuchen Zhou, Yonggen Ling, Hong Zhang
- Published: 2026-07-22T12:05:13Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
