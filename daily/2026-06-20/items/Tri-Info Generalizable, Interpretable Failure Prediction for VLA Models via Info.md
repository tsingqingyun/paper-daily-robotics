---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19998v1"
published: "2026-06-18T09:34:22Z"
age_days: 1
score: 30
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet
they remain black boxes whose physical interactions can cause irreversible harm, making
generalizable and interpretable failure detection essential. We observe that successful
and failed rollouts carry systematically different information-theoretic signatures.
Building on this, we formalize VLA control as a closed-loop information pipeline and
derive the Triple Information-theoretic (Tri-Info) signals that capture whether actions
remain diverse, temporally consistent, and coupled to state transitions. Across six VLA
models and three benchmark environments, Tri-Info matches the strongest baselines in-
domain. Moreover, Tri-Info transfers across architectures, environments, and the sim-to-
real gap without retraining, reaching 83\% accuracy on real-world tasks where prior
detectors collapse to chance. This establishes Tri-Info as a simple yet powerful method
that not only detects failures with strong cross-domain generalization, but also
delivers interpretable diagnostics of the underlying failure modes.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19998v1
- Authors: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang
- Published: 2026-06-18T09:34:22Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
