---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12918v1"
published: "2026-06-11T05:21:39Z"
age_days: 2
score: 26
created: 2026-06-14
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

> [!summary] 一句话结论（基于摘要）
> Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines.

## 关键点

- **问题**：Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses.
- **创新点 / 方法**：We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS.
- **证据**：Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/MAStrike Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

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

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12918v1
- Authors: Chejian Xu, Zhaorun Chen, Jingyang Zhang, Freddy Lecue, Avni Kothari, Sarah Tan, Wenbo Guo, Bo Li
- Published: 2026-06-11T05:21:39Z
- Age days: 2

</details>
