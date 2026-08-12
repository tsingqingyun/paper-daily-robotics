---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13040v1"
published: "2026-06-11T08:20:42Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> To address this gap, we present RoboProcessBench, a benchmark for process-aware understanding in vision-language robotic manipulation.

## 关键点

- **问题**：Vision-language models (VLMs) are increasingly explored as visual critics, reward generators, and failure detectors in robotic manipulation.
- **创新点 / 方法**：To address this gap, we present RoboProcessBench, a benchmark for process-aware understanding in vision-language robotic manipulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Extensive evaluation of various VLMs on ProcessData-Eval reveals broad limitations across 12 diagnostic task families, suggesting current models still lack robust process-aware understanding of manipulation executions.

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/RoboProcessBench Benchmarking Process-Aware Understanding in Vision-Language Rob.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language models (VLMs) are increasingly explored as visual critics, reward
generators, and failure detectors in robotic manipulation. These roles implicitly
require models to judge not only final task success, but also how a manipulation
execution is physically and temporally progressing. However, existing evaluations fail
to test whether VLMs possess fine-grained process understanding. To address this gap, we
present RoboProcessBench, a benchmark for process-aware understanding in vision-language
robotic manipulation. RoboProcessBench decomposes such capability into two complementary
dimensions, \emph{static monitoring} and \emph{dynamic reasoning}, instantiated as 12
diagnostic question families covering phase, contact, motion, coordination, primitive-
local progress, temporal order, outcome, and primitive-level transitions. Built from
physically grounded execution traces, the curated benchmark corpus ProcessData contains
\textasciitilde 58k question-answer pairs across 260 manipulation tasks, which is
further split into ProcessData-SFT and ProcessData-Eval for post-training and evaluation
purposes. Extensive evaluation of various VLMs on ProcessData-Eval reveals broad
limitations across 12 diagnostic task families, suggesting current models still lack
robust process-aware understanding of manipulation executions. But with ProcessData-SFT,
the post-trained \textit{Qwen2.5-VL-7B} and \textit{InternVL-3-8B} exhibit consistent
gains on local state, motion, progress, and primitive-aware cues. These results
demonstrate that RoboProcessBench serves as both an evaluation benchmark and a learnable
supervision source for developing VLMs capable of monitoring and evaluating robotic
manipulation processes. Project webpage:
\href{https://processbench-2026.github.io/RoboProcessBench-
Web/}{https://processbench-2026.github.io}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13040v1
- Authors: Dayu Xia, Yue Shi, Yao Mu, Huiting Ji, Chaofan Ma, Yingjie Zhou, Hua Chen, Yang Liu, Jiezhang Cao, Guangtao Zhai
- Published: 2026-06-11T08:20:42Z
- Age days: 2

</details>
