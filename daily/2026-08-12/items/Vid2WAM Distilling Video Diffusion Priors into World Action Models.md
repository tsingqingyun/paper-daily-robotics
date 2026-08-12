---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08558v1"
published: "2026-08-09T08:02:49Z"
age_days: 2
score: 24
created: 2026-08-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Vid2WAM: Distilling Video Diffusion Priors into World Action Models

## 为什么重要

自动筛选分数：24

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

World Action Models (WAMs) improve robot policy learning by jointly modeling future
visual dynamics and actions. However, their scalability and generalization remain
constrained by their reliance on costly expert demonstrations. We challenge this by
asking whether future supervision for WAMs must originate from target-task expert
trajectories. In this paper, we propose Vid2WAM, an offline distillation framework that
transfers visual diffusion priors from a large video foundation model into a compact WAM
student. Given an observation and language instruction, Vid2WAM distills supervision
through two complementary channels: task-conditioned future rollouts directly supervise
the student's future prediction branch, while an inverse dynamics model recovers
embodiment-specific pseudo-actions for action learning. To robustly integrate synthetic
and real supervision, we introduce source-aware residual action adaptation that learns
source-specific corrections around a shared action backbone and mitigates interference
from noisy pseudo-actions. During inference, both the video teacher and inverse dynamics
model are discarded, leaving only the WAM student for efficient deployment. Simulation
and real-world experiments demonstrate that Vid2WAM improves novel-task generalization
and data efficiency under limited expert demonstrations while preserving low-latency
inference.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08558v1
- Authors: Chenhao Qiu, Ruixiang Wang, Runyi Zhao, Sixu Lin, Songen Gu, Shufeng Nan, Guiliang Liu, Kui Jia, Yanwei Fu, Simo Wu
- Published: 2026-08-09T08:02:49Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
