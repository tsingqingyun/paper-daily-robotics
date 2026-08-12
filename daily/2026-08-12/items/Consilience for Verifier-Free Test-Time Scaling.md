---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09898v1"
published: "2026-08-10T17:45:44Z"
age_days: 1
score: 26
created: 2026-08-12
concepts: ["具身智能评测与基准"]
---

# Consilience for Verifier-Free Test-Time Scaling

## 为什么重要

自动筛选分数：26

连接概念：[[具身智能评测与基准]]

## 摘要

Test-time scaling often uses an external verifier, such as compilers and test cases in
coding or trained value functions in robotics applications, to obtain high-quality
rollouts. Verifier-free test-time scaling (or VF-TTS) is gaining extensive attention as
a mechanism to enhance Large Language Model (LLM) reasoning, primarily because we do not
have access to such high-quality verifiers in many real-world applications. Among
existing VF-TTS methods, confidence-based VF-TTS methods, which compute and rank
rollouts solely by confidence, are particularly promising. Such methods introduce near-
zero overhead for sample evaluation and require minimal access to internal model states,
making the methods highly flexible across models and tasks. In this paper, we
demonstrate a critical limitation of existing confidence-based VF-TTS methods by showing
that such methods catastrophically break down on complex tasks. We observe a very
interesting phenomenon: uniformly high confidence frequently indicates a failure to
explore, favoring confidently wrong answers. To address this, our core insight is that
robust cognitive search requires a specific confidence trajectory pattern: such methods
perform exploratory branching at the beginning, as manifested by low initial confidence,
and converge to a high final confidence solution. To implement this insight, we
introduce consilience, a novel selection framework that explicitly evaluates the
temporal asymmetry of confidence in reasoning. We operationalize this via a
combinatorial metric that actively penalizes high initial confidence while strictly
demanding final certainty. Extensive experiments covering both graduate-level
mathematics problems and free-form code generation demonstrate that consilience
effectively outperforms existing baselines, validating our novel perspective on
completion confidence.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09898v1
- Authors: Lecheng Kong, Like Hui, Haitao Mao, Jun Huan
- Published: 2026-08-10T17:45:44Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
