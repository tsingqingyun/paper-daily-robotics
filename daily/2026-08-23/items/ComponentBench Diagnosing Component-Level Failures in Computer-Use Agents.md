---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18307v1"
published: "2026-08-18T20:38:26Z"
age_days: 4
score: 22
created: 2026-08-23
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents

> [!summary] 一句话结论（基于摘要）
> Evaluating seven models -- GPT-5.4, Gemini 3 Flash, GPT-5.4 mini, GPT-5 mini, Gemini 3.1 Flash-Lite, Qwen3-VL-235B, and UI-TARS-1.5-7B -- across four observation and action spaces, we show that these design choices critically impact performance.

## 问题

Beyond task collection, we introduce a scalable pipeline for auditing realized structural difficulty after implementation and synthesizing structured failure analyses across tasks and component families.

## 创新点或方法

We present ComponentBench, a benchmark and diagnostic pipeline for component-level evaluation of computer-use agents on modern web UIs.

## 证据

Evaluating seven models -- GPT-5.4, Gemini 3 Flash, GPT-5.4 mini, GPT-5 mini, Gemini 3.1 Flash-Lite, Qwen3-VL-235B, and UI-TARS-1.5-7B -- across four observation and action spaces, we show that these design choices critically impact performance.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/ComponentBench Diagnosing Component-Level Failures in Computer-Use Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Current evaluation of computer-use agents is split between long-horizon workflow benchmarks and atomic GUI-grounding tests. This leaves an under-instrumented middle layer: realistic component-centered interactions (e.g., toggle a button set) that are short enough to diagnose and rich enough to capture the burdens of modern interfaces. We present ComponentBench, a benchmark and diagnostic pipeline for component-level evaluation of computer-use agents on modern web UIs. ComponentBench is organized around a library-agnostic ontology of 97 canonical UI components instantiated as 2,910 programmatically verified tasks across widely used component libraries, paired with cleaned human reference trajectories that enable evaluation of both task success and interaction efficiency. Beyond task collection, we introduce a scalable pipeline for auditing realized structural difficulty after implementation and synthesizing structured failure analyses across tasks and component families. Evaluating seven models -- GPT-5.4, Gemini 3 Flash, GPT-5.4 mini, GPT-5 mini, Gemini 3.1 Flash-Lite, Qwen3-VL-235B, and UI-TARS-1.5-7B -- across four observation and action spaces, we show that these design choices critically impact performance. Within a single shared harness, changing only the observation and action space shifts task success by more than 30% for the same model: GPT-5 mini falls from 83.1% with accessibility-tree observations to 48.9% with coordinate-only Pixel control. Moreover, even the fastest configuration takes 3.7x as long as the matched human reference, and spatial manipulations that are trivial for humans continue to challenge current agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18307v1
- Authors: Tianchen Guan, Xinlei Lin, Royce Cheng-Yue, Xiangjun Wang, Shuyan Zhou
- Published: 2026-08-18T20:38:26Z
- Age days: 4

</details>
