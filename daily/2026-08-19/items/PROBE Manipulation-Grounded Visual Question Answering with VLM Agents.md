---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17129v1"
published: "2026-08-17T21:03:31Z"
age_days: 1
score: 34
created: 2026-08-19
concepts: ["多模态基础模型", "智能体 Agent", "Sim2Real", "具身智能评测与基准"]
---

# PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents

> [!summary] 一句话结论（基于摘要）
> We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types.

## 关键点

- **问题**：However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside.
- **创新点 / 方法**：Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes.
- **证据**：We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/PROBE Manipulation-Grounded Visual Question Answering with VLM Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes. However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside. Answering such questions in real-world cluttered environments requires reasoning in dynamic scenes: distractors must be manipulated to reveal occluded objects, and each action changes the scene the model must reason over. We formalize this setting as Manipulation-Grounded Visual Question Answering (MG-VQA) and introduce PROBE, a framework for benchmarking and finetuning VLM agents on such tasks. We first develop PROBE-Sim, a high-fidelity tabletop simulator with everyday objects and a robot manipulator equipped with grasping and pushing tools. PROBE-Sim is used to create PROBE-Bench: an evaluation suite of 150 tasks across 6 question types on cluttered tabletop scenes, where a VLM perceives, picks up or pushes objects before answering. We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types. We further design PROBE-Agent, a finetuning recipe to distill successful trajectories from a powerful teacher foundation model to a smaller open-weight model using a mixed data recipe that encourages manipulation-efficient question answering. PROBE Agent finetuned models outperform their off-the-shelf agent baseline (11.5% on average) and demonstrate positive transfer to unseen objects and a held-out task. We validate sim-to-real transfer by deploying PROBE-Agent finetuned policies in real-world tabletop environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17129v1
- Authors: Vineet Bhat, Siyi Chen, Alex Zook, Xuning Yang, Stan Birchfield, Valts Blukis, Jonathan Tremblay
- Published: 2026-08-17T21:03:31Z
- Age days: 1

</details>
