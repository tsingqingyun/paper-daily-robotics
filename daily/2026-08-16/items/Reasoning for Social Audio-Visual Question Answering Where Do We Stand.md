---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13239v1"
published: "2026-08-13T13:44:35Z"
age_days: 2
score: 25
created: 2026-08-16
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Reasoning for Social Audio-Visual Question Answering: Where Do We Stand?

> [!summary] 一句话结论（基于摘要）
> A simple Vanilla SFT baseline matches or outperforms existing reasoning methods across three benchmarks at a fraction of the cost, establishing it as an essential baseline for evaluating novel fine-tuning techniques.

## 关键点

- **问题**：These surprising findings reveal the limitations of current MLLMs when it comes to social understanding.
- **创新点 / 方法**：Training Multimodal Large Language Models for audio-visual social understanding is a crucial step toward embodied social intelligence.
- **证据**：A simple Vanilla SFT baseline matches or outperforms existing reasoning methods across three benchmarks at a fraction of the cost, establishing it as an essential baseline for evaluating novel fine-tuning techniques.
- **局限**：These surprising findings reveal the limitations of current MLLMs when it comes to social understanding.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Reasoning for Social Audio-Visual Question Answering Where Do We Stand.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training Multimodal Large Language Models for audio-visual social understanding is a crucial step toward embodied social intelligence. Chain-of-thought (CoT) reasoning has become the dominant approach, with HumanOmniV2 and its IntentBench benchmark as a prominent reference point. In this context, we report three findings. First, IntentBench is highly noisy: $\sim$7% of questions are broken and $\sim$23% are trivially answerable without the video input. We remove the affected questions and release Intentbench-Prime. Second, current reasoning approaches are expensive and surprisingly ineffective. A simple Vanilla SFT baseline matches or outperforms existing reasoning methods across three benchmarks at a fraction of the cost, establishing it as an essential baseline for evaluating novel fine-tuning techniques. Third, our analysis reveals that substantial priors can be learned solely from the text modality and that using a textual caption instead of the video yields performance on par with Vanilla SFT. These surprising findings reveal the limitations of current MLLMs when it comes to social understanding. IntentBench-Prime, Vanilla SFT model, and code are publicly available.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13239v1
- Authors: Koen P. de Vries, Xavier Alameda-Pineda, Estefanía Talavera, Stéphane Lathuilière
- Published: 2026-08-13T13:44:35Z
- Age days: 2

</details>
