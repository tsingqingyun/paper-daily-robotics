---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20975v1"
published: "2026-08-21T10:55:14Z"
age_days: 3
score: 27
created: 2026-08-24
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models

> [!summary] 一句话结论（基于摘要）
> We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact across cooperative and competitive scenarios requiring integration of verbal statements, spatial trajec…

## 关键点

- **问题**：Signal-level analysis reveals two sequential bottlenecks: most models cannot produce directionally coherent nonverbal signals, and even when signals are present, VLM agents fail to interpret others behaviors and react to them.
- **创新点 / 方法**：We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact across cooperative and competitive scenarios requiring integration of verbal statements, spatial trajectories, gaze direction, and facial expression under systemat…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Signal-level analysis reveals two sequential bottlenecks: most models cannot produce directionally coherent nonverbal signals, and even when signals are present, VLM agents fail to interpret others behaviors and react to them.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/Belief Without Behavior Measuring the Translation of Theory of Mind into Coordin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap between social inference and social action. We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact across cooperative and competitive scenarios requiring integration of verbal statements, spatial trajectories, gaze direction, and facial expression under systematically varied ToM constraints. Evaluating 13 models, including 11 VLMs, across 200 trials per model, we find that VLMs fail to produce behaviors consistent with the expected outcomes under ToM-order constraints, and that imposing explicit ToM-order constraints produces no reliable behavioral change aligned with the specified reasoning level. Signal-level analysis reveals two sequential bottlenecks: most models cannot produce directionally coherent nonverbal signals, and even when signals are present, VLM agents fail to interpret others behaviors and react to them. PCM-LLM, included as a structured architectural reference point with an explicit ToM module, succeeds across all conditions, suggesting that explicit belief-action coupling is a sufficient ingredient for this class of tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20975v1
- Authors: Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf
- Published: 2026-08-21T10:55:14Z
- Age days: 3

</details>
