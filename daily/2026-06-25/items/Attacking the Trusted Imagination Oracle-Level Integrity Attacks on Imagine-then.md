---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22966v1"
published: "2026-06-22T07:45:34Z"
age_days: 2
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models

## 为什么重要

自动筛选分数：30

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A
world-action model (WAM) first imagines a short future as a latent trajectory z~, on
which the action is then conditioned. We identify this trusted imagination, rather than
the reactive policy, as the exposed attack surface. A downstream oracle, such as a
safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check
verifier, consumes z~ as a prediction of the future. The robustness of the policy
therefore does not entail the robustness of systems that rely on the WAM. The underlying
phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only
displacing z~ from its natural-future manifold. Steering it precisely is hard, since it
must reach a specified on-manifold target. We adopt a capability-based threat model with
an L-infinity-bounded observation perturbation. The attacker applies projected gradient
descent through the fully differentiable observation-to-imagination map. The same off-
manifold property motivates a parameter-free denoiser detector. We evaluate three
targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x
stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An
adaptive attacker evades detection only by forgoing corruption. The reactive policy
remains robust to corrupted imagination. A native imagination-driven MPC, however,
exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus
0.05; Fisher p < 10^-4).

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22966v1
- Authors: Linghan Chen, Kaiyan Ji, Minyu Guo
- Published: 2026-06-22T07:45:34Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
