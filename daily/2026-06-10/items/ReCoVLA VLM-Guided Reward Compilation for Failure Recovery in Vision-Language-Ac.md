---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09630v1"
published: "2026-06-08T15:29:09Z"
age_days: 1
score: 32
created: 2026-06-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "Sim2Real"]
---

# ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]], [[Sim2Real]]

## 摘要

Vision-language-action (VLA) policies provide strong priors for language-conditioned
manipulation, but remain brittle in off-nominal states requiring targeted recovery. We
propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a
pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the
failure mode and recovery stage, and compiles a structured reward from task-relevant
components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA
uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask
for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment
of the trained recovery policies. This decouples high-level failure understanding from
low-level corrective control to support different VLAs. Experiments across short-
horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms
the tested baselines on average. In simulation, our reward compiler improves average
success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot
sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7%
success.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09630v1
- Authors: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
- Published: 2026-06-08T15:29:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
