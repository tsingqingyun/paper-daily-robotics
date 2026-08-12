---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25889v1"
published: "2026-05-25T14:16:57Z"
age_days: 0
score: 36
created: 2026-05-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models are increasingly deployed on real robots, where each
predicted action is executed and each failure carries a safety cost. They reach high
success rates on clean inputs but collapse under small adversarial perturbations. A
$16/255$ PGD attack on OpenVLA-7B drops LIBERO success from above $95\%$ to under $5\%$.
Empirical defenses recover some robustness at a cost in clean accuracy, but the
literature does not say whether the trade-off has a theoretical floor. We prove that it
does. For any VLA policy with discrete actions, the sum of capability (mutual
information between policy action and oracle action) and robustness (mutual information
preserved under adversarial perturbation, net of trivial channel leakage) is upper-
bounded by a policy-independent budget: task entropy plus adversarial channel capacity.
The proof is two applications of the Data Processing Inequality plus MI non-negativity.
The pixel-level bound is loose on current models ($\sim 10^3$ nats), but an encoder-
specific corollary restricts the channel to the policy-relevant subspace, reducing the
budget from $\sim 5{,}000$ to $\sim 31$ nats on OpenVLA; the policy already consumes
$\sim 24\%$ of this tighter budget, leaving limited room for simultaneous robustness
improvement. We validate the bound across $252$ closed-form Gaussian-VLA cells and $48$
OpenVLA-7B $\times$ LIBERO $\times$ PGD cells (zero violations). We propose encoder-
specific slack as a normalized comparison axis for defense papers, and release all code,
manifests, and results.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25889v1
- Authors: Jianwei Tai
- Published: 2026-05-25T14:16:57Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
