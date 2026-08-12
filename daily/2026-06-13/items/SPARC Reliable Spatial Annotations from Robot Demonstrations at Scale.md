---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13497v1"
published: "2026-06-11T15:46:28Z"
age_days: 1
score: 40
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale

> [!summary] 一句话结论（基于摘要）
> On 1.7k human- annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly outperforms detection-only baselines in localization accuracy while retaining three times more samples at high-precision operating points.

## 关键点

- **问题**：Our experiments demonstrate that models finetuned on our annotations achieve state-of-the-art results on object-grounding and pointing benchmarks among similarly sized models, while remaining competitive on broader spatial-reasoning suites without manually verified or annotated training data.
- **创新点 / 方法**：This work introduces Spatial Annotations from Robot Demonstrations with Reliability Calibration (SPARC), a risk-aware framework that automatically labels robot demonstrations with structured spatial annotations and assigns each annotation a reliability score.
- **证据**：On 1.7k human- annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly outperforms detection-only baselines in localization accuracy while retaining three times more samples at high-precision operating points.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/SPARC Reliable Spatial Annotations from Robot Demonstrations at Scale.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This work introduces Spatial Annotations from Robot Demonstrations with Reliability
Calibration (SPARC), a risk-aware framework that automatically labels robot
demonstrations with structured spatial annotations and assigns each annotation a
reliability score. Structured spatial annotations, such as bounding boxes, object
trajectories, and manipulation phase labels, benefit a broad range of robotics
applications from training grounded robot policies and embodied foundation models to
motion planning and hierarchical task composition. Existing automated pipelines generate
such annotations at scale but provide no reliable quality signal: detector confidence is
poorly calibrated for annotation correctness, forcing a choice between accepting noisy
labels or discarding useful samples. In contrast to existing automated pipelines, SPARC
leverages the spatio-temporal structure inherent to robot tasks to generate a
reliability signal, reducing noisy labels and retaining more useful samples. We further
introduce Interaction-Aware Bench (IA-Bench), a benchmark that measures model accuracy
in grounding the locations of interacted objects in robot demonstrations. On 1.7k human-
annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly
outperforms detection-only baselines in localization accuracy while retaining three
times more samples at high-precision operating points. Our experiments demonstrate that
models finetuned on our annotations achieve state-of-the-art results on object-grounding
and pointing benchmarks among similarly sized models, while remaining competitive on
broader spatial-reasoning suites without manually verified or annotated training data.
Furthermore, policies trained on SPARC-generated annotations outperform baselines in
cluttered, visually ambiguous real-world scenes. Code, data, and models are available at
intuitive-robots.github.io/sparc-labeling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13497v1
- Authors: Nils Blank, Paul Mattes, Maximilian Xiling Li, Jakub Suliga, Thomas Roth, Moritz Reuss, Pankhuri Vanjani, Rudolf Lioutikov
- Published: 2026-06-11T15:46:28Z
- Age days: 1

</details>
