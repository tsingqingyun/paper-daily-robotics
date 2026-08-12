---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13097v1"
published: "2026-06-11T09:25:27Z"
age_days: 4
score: 22
created: 2026-06-16
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents

## 为什么重要

自动筛选分数：22

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Code-writing large language models (CodeLLMs) generate executable code policies for
embodied agents by translating natural language goals and environmental constraints into
structured control programs. However, policy generation in open-domain embodied
environments suffers from two fundamental limitations: (i) delayed decoding caused by
repetitive prefill computation over long prompts, and (ii) limited robustness due to
fully generative decoding, which often produces API mismatches, missing safety guards,
and unstable control logic. To address these limitations, we present FCGraft, a
Functional Cache Grafting framework. FCGraft maintains a library of function-level
validated code skeletons and their associated prompt-level Transformer key-value (KV)
caches, and synthesizes new policies by retrieving relevant functions and grafting their
KV caches when a new task is provided. Given retrieved function caches, FCGraft performs
cache grafting via stitching, which composes cached function segments into a composite
policy, and patching, which locally adapts only the necessary code regions to satisfy
task-specific parameters and constraints with minimal additional decoding. By
eliminating redundant prefill computation, this approach reduces generation latency,
while reusing validated control structures improves robustness over prompt-level caching
methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy
synthesis.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13097v1
- Authors: Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo
- Published: 2026-06-11T09:25:27Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
