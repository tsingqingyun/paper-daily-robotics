---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19876v1"
published: "2026-07-22T08:04:17Z"
age_days: 1
score: 36
created: 2026-07-24
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding

> [!summary] 一句话结论（基于摘要）
> To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline.

## 关键点

- **问题**：Evaluating the physical consistency of embodied world models(EWMs) is a critical open challenge.
- **创新点 / 方法**：To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/KineBench Benchmarking Embodied World Models via IDM-Free Kinematic Grounding.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Evaluating the physical consistency of embodied world models(EWMs) is a critical open
challenge. While closed-loop evaluation via simulator rollouts offers a more faithful
assessment of physical plausibility than open-loop alternatives, existing frameworks
almost exclusively rely on Inverse Dynamics Models(IDMs) for action extraction. Due to
the intricate mapping from 2D pixel space to 3D kinematic space, the learned IDMs can be
brittle to data outside their training distribution, resulting in unreliable action
extraction from the generated videos with novel objects and scenarios. This creates an
unavoidable attribution ambiguity between world model inaccuracies and extractor errors.
To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for
EWMs, built upon an explicit kinematic grounding pipeline. Given a generated video,
KineBench employs cascaded visual foundation models to directly extract 6D end-effector
poses from individual frames, which are then executed in a physics simulator for closed-
loop validation. Beyond execution-based task success, KineBench incorporates two
classical 3D kinematic metrics--Spectral Arc Length (SPARC) and the Maruyama
Manipulability Index--to characterize trajectory smoothness and kinematic feasibility
from a robot-centric perspective. Built on 20 diverse manipulation tasks in ManiSkill3,
KineBench evaluates EWMs across four progressive suites: basic execution, task transfer,
visual out-of-distribution generalization, and complexity-conditioned scaling.
Evaluation across frontier models reveals task-complexity-bounded nonlinear scaling in
embodied video generation, providing empirical guidance for future data-scaling
strategies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19876v1
- Authors: Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li
- Published: 2026-07-22T08:04:17Z
- Age days: 1

</details>
