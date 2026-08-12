---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14574v1"
published: "2026-06-12T15:53:16Z"
age_days: 2
score: 27
created: 2026-06-15
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

Large language models (LLMs) are increasingly deployed as planners for autonomous agents
in household environments. While existing benchmarks evaluate whether LLM-generated
plans execute successfully, they overlook a critical type of failure: latent failures.
Unlike immediate failures that trigger instant feedback at execution time and enable
timely correction, latent failures do not immediately halt plan execution but silently
compromise goal achievement. In severe cases, they cause irreversible harm. To address
this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM
planning through a human-curated symbolic world model grounded in the kitchen domain.
SIMMER defines a world model comprising 77 actions, 262 unique objects, and
approximately 46,800 possible interactions that are semantically realistic, derived from
real-world cooking scripts. It then leverages a state machine executor that validates
plans against the world model and detects immediate precondition violations, latent
hazards, and irreversible failures. Experiments across six LLMs show that even frontier
models achieve at most 17% error-free plans. Moreover, up to 56% of plans contain latent
failures, the majority of which lead to irreversible consequences. We further
demonstrate that explicit state reasoning via counterfactual foresight simulation can
reduce latent failures by up to 72% and irreversible cases by up to 75%, suggesting a
promising direction for more robust LLM planners.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14574v1
- Authors: Xiaoxin Lu, Ranran Haoran Zhang, Rui Zhang
- Published: 2026-06-12T15:53:16Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
