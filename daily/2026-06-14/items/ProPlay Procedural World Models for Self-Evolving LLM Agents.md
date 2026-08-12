---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12780v1"
published: "2026-06-11T00:47:37Z"
age_days: 3
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ProPlay: Procedural World Models for Self-Evolving LLM Agents

> [!summary] 一句话结论（基于摘要）
> Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines.

## 关键点

- **问题**：Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience.
- **创新点 / 方法**：We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.
- **证据**：Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/ProPlay Procedural World Models for Self-Evolving LLM Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Self-evolving agents are expected to improve through interaction without external
supervision, but this remains difficult in partially observable environments where
agents must explore actively, learn from limited feedback, and decide when to trust
prior experience. Existing LLM-agent methods often rely on memory or planning modules,
yet they rarely close the loop between them to continually refine an internal
understanding of environment dynamics. We introduce ProPlay, a procedural world model
that supports procedure-level preplay, where agents can rehearse future procedural paths
using the learned world knowledge. Rather than representing experience as isolated rules
or low-level action constraints, ProPlay abstracts successful trajectories into
procedures and organizes them in a procedure graph that captures causal transitions
among task stages. Each transition is associated with a reliability record embedding to
estimate its task-specific contribution from past outcomes. Before each episode, ProPlay
simulates future procedural trajectories over known graph structures as structured soft
guidance; after execution, it refines the graph using environment feedback. Experiments
on public benchmarks show that ProPlay consistently improves environment understanding
and self-evolution capability over strong baselines. Our code has been released in
https://github.com/antman9914/proplay.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12780v1
- Authors: Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiaoguang Guo, Weixiang Sun, Chuxu Zhang, Yanfang Ye
- Published: 2026-06-11T00:47:37Z
- Age days: 3

</details>
