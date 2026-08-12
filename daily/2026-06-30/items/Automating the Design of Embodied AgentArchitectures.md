---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30111v1"
published: "2026-06-29T10:45:37Z"
age_days: 1
score: 29
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Automating the Design of Embodied AgentArchitectures

> [!summary] 一句话结论（基于摘要）
> We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator- aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experi…

## 关键点

- **问题**：Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules.
- **创新点 / 方法**：We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator- aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stal…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/Automating the Design of Embodied AgentArchitectures.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents are typically built as hand-designed compositions of perception, memory,
planning, and action modules. This modularity exposes a large architectural design
space, but current systems still rely on researcher intuition to choose where
information is stored, how observations are processed, and how model calls are
connected. Agent Architecture Search (AAS) automates such design for text-domain agents,
but has not been systematically evaluated on perceptual embodied agents through
simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph
runtime that hosts embodied executors as editable node-and-wire programs with simulator-
aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that
cycles through proposal, critique, experiment, and distillation, with triggered
reflection after stalls. We evaluate three AAS variants across four embodied executors
spanning vision-language navigation, embodied question answering, and language-
conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search
can produce deployable and directional success-rate gains on embodied tasks, while one
apparent high-scoring candidate is rejected as leak-bearing. At the same time, the
experiments expose constraints that are muted in text-domain AAS: optimization signals
can be masked by rollout noise, search can become trapped in local edit basins, and
episode-level credit assignment only partially emerges even when detailed logs are
available. These results characterize both the promise and the current limits of
automated architecture search for embodied agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30111v1
- Authors: Jian Zhou, Sihao Lin, Jin Li, Shuai Fu, Gengze Zhou, Qi Wu
- Published: 2026-06-29T10:45:37Z
- Age days: 1

</details>
