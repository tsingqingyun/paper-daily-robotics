---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05695v1"
published: "2026-08-06T07:37:49Z"
age_days: 4
score: 27
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model

## 为什么重要

自动筛选分数：27

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

As large language model (LLM) agents increasingly invoke external tools and interact
with real-world systems, unsafe actions may cause irreversible consequences on external
states, user data, and downstream services. Recent runtime guardrails mitigate such
risks by checking proposed actions before execution, but many remain reactive: they
primarily assess the apparent safety of the current action, lacking an explicit model of
how risk evolves across the trajectory. This limitation creates a critical blind spot
for long-horizon risks, where individually benign-looking actions can gradually drift
the agent toward hazardous states. In response, we propose DreamGuard, a proactive
guardrail for LLM agents built around a risk-aware world model. The world model
maintains a compact recurrent latent state over the trajectory and predicts future
latent states from which DreamGuard derives immediate-hazard and prefix-risk evidence.
It then fuses these multi-horizon signals into intervention decisions before execution.
Experiments across four benchmarks and an online guardrail evaluation show that
DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves
the best safety-utility trade-off among evaluated guardrails, and maintains an average
end-to-end latency of 25 ms per call.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05695v1
- Authors: Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu
- Published: 2026-08-06T07:37:49Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
