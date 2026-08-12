---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Embodied AI and Robotics"
url: "https://arxiv.org/abs/2605.06311v1"
published: "2026-05-07T14:13:05Z"
age_days: 
score: 30
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "Sim2Real", "具身智能评测与基准"]
---

# Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation

> [!summary] 一句话结论（基于摘要）
> Our results show that these factors play a critical role in geometric reasoning and spatial grounding, yet are largely overlooked in existing benchmarks.

## 关键点

- **问题**：Although existing benchmarks cover a wide range of task categories, they lack visual realism, creating a large domain gap between simulation and reality.
- **创新点 / 方法**：Motivated by the analysis, we propose VISER, a visually realistic benchmark for evaluating robot manipulation in simulation.
- **证据**：Our results show that these factors play a critical role in geometric reasoning and spatial grounding, yet are largely overlooked in existing benchmarks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/Toward Visually Realistic Simulation A Benchmark for Evaluating Robot Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable simulation evaluation of robot manipulation policies serves as a high-fidelity
proxy for real-world performance. Although existing benchmarks cover a wide range of
task categories, they lack visual realism, creating a large domain gap between
simulation and reality. This undermines the reliability of simulation-based evaluation
in predicting real-world performance. To mitigate the sim-to-real visual gap, we conduct
a systematic analysis to isolate the effects of lighting and material. Our results show
that these factors play a critical role in geometric reasoning and spatial grounding,
yet are largely overlooked in existing benchmarks. Motivated by the analysis, we propose
VISER, a visually realistic benchmark for evaluating robot manipulation in simulation.
VISER features a high-fidelity dataset of over 1,000 3D assets with physically-based
rendering (PBR) materials, along with 3D scenes created from these assets through
curated layouts or generation. To this end, we propose an automated pipeline leveraging
Multi-modal Large Language Models (MLLMs) for material-aware part segmentation and
material retrieval, enabling scalable generation of physically plausible assets.
Building on the high-fidelity 3D asset dataset, we construct diverse evaluation tasks,
such as grasping, placing, and long-horizon tasks, enabling scalable and reproducible
assessment of Vision-Language-Action (VLA) models. Our benchmark shows a strong
correlation between simulation and real-world performance, achieving an average Pearson
correlation coefficient of 0.92 across different policies.

### 来源

- Source: arXiv Daily - Embodied AI and Robotics
- URL: https://arxiv.org/abs/2605.06311v1
- Authors: Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu, Jiayuan Gu, Beibei Wang
- Published: 2026-05-07T14:13:05Z
- Age days: 

</details>
