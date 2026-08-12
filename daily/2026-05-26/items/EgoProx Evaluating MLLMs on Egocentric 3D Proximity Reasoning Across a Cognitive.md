---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.24456v1"
published: "2026-05-23T08:07:45Z"
age_days: 2
score: 30
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# EgoProx: Evaluating MLLMs on Egocentric 3D Proximity Reasoning Across a Cognitive Hierarchy

> [!summary] 一句话结论（基于摘要）
> To this end, we introduce EgoProx, a benchmark for egocentric 3D proximity reasoning.

## 关键点

- **问题**：Whether multimodal large language models (MLLMs) can perform such embodied 3D reasoning remains unclear.
- **创新点 / 方法**：To this end, we introduce EgoProx, a benchmark for egocentric 3D proximity reasoning.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/EgoProx Evaluating MLLMs on Egocentric 3D Proximity Reasoning Across a Cognitive.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humans constantly reason about 3D proximity, the relations between their body and
surrounding objects, to guide perception and action in daily life. Whether multimodal
large language models (MLLMs) can perform such embodied 3D reasoning remains unclear. To
this end, we introduce EgoProx, a benchmark for egocentric 3D proximity reasoning. We
organize our tasks along a cognitive chain, covering intention, exploration,
exploitation, and chain-of-actions reasoning. We also design an agent based data engine
that produces diverse and consistent QA pairs at scale. We benchmark prevailing MLLMs on
EgoProx and conduct additional analyses with dataset specific and task specific
instruction tuning. We observe large cross-domain gains, indicating that current MLLMs
contain some spatial knowledge; however, they still struggle to effectively leverage it
for spatial reasoning VQA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.24456v1
- Authors: Jinzhao Li, Yinuo Chen, Dongxu Piao, Panwang Pan, Yifan Yu, Dong Wang, Honglei Yan, Liang Yue, Shaofei Wang, Yixin Chen, Siyuan Huang, Miao Liu
- Published: 2026-05-23T08:07:45Z
- Age days: 2

</details>
