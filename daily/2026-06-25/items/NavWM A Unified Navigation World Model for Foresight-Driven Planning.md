---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24101v1"
published: "2026-06-23T03:30:20Z"
age_days: 1
score: 35
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型"]
---

# NavWM: A Unified Navigation World Model for Foresight-Driven Planning

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]]

## 摘要

Conventional visual navigation policies often struggle with myopic decision-making and
mode collapse in complex environments. While world models offer a promising alternative,
existing paradigms typically isolate perception, generation, and control, failing to
capture their shared spatio-temporal dynamics. In this paper, we propose NavWM, a
unified navigation world model that seamlessly integrates latent world reasoning,
multimodal action prediction, and controllable visual generation. At its core, NavWM
leverages latent world tokens to distill geometric and semantic priors, endowing the
agent with robust structural understanding. To overcome the limitations of deterministic
policies, we introduce an anchor-based multimodal trajectory forecasting framework that
generates a diverse action space. This inherent diversity explicitly empowers the
generative world model to act as a robust closed-loop planner, utilizing visual
foresight to evaluate and select the optimal path. Extensive experiments across diverse
robotics datasets demonstrate that NavWM significantly advances the state-of-the-art,
delivering remarkable improvements in both high-fidelity future state generation and
zero-shot navigation success.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24101v1
- Authors: Yanghong Mei, Longteng Guo, Ming-Ming Yu, Guiyu Zhao, Xingjian He, Jing Liu
- Published: 2026-06-23T03:30:20Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
