---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12918v1"
published: "2026-06-11T05:21:39Z"
age_days: 2
score: 26
created: 2026-06-14
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

## 为什么重要

自动筛选分数：26

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes
workflows across domains such as finance and software engineering. In these systems,
safety and security are inherently distributed across role-specialized agents,
significantly expanding the attack surface, particularly under coordinated adversarial
behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming
approaches for MAS remain limited: they rely on heuristic selection of target agents and
perturb isolated message streams, leaving critical questions unanswered as which agents
are most responsible for system safety, and how compromised agents can coordinate to
bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming
in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS,
quantifying each agent's marginal contribution to system robustness under task-specific
distributions. GGuided by this attribution, MAStrike identifies vulnerable agent
coalitions and generates coordinated, role-aware adversarial manipulations. These
attacks are iteratively refined through structured causal diagnosis, attributing failure
cases to uncompromised agents that block adversarial attempts. We further build a
comprehensive MAS red-teaming benchmark and controllable environments spanning diverse
hierarchical topologies and domains, including finance, software engineering, and CRM.
Extensive experiments across MAS built on multiple frontier models show that MAStrike
substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial
Shapley value distributions and higher-order interaction structures among agents,
revealing critical vulnerabilities and coordination patterns that are overlooked by
prior single-agent or template-based methods.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12918v1
- Authors: Chejian Xu, Zhaorun Chen, Jingyang Zhang, Freddy Lecue, Avni Kothari, Sarah Tan, Wenbo Guo, Bo Li
- Published: 2026-06-11T05:21:39Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
