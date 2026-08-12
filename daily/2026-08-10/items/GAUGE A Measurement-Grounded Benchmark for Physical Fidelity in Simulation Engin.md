---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
deep_read_status: processed
deep_read_note: "50_Papers/Deep Reads/GAUGE 2608.05948v1/README"
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.05948v1"
published: "2026-08-06T12:19:38Z"
age_days: 3
score: 28
created: 2026-08-10
concepts: ["世界模型", "具身智能评测与基准"]
---

# GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models

> [!summary] 一句话结论（基于摘要）
> We introduce GAUGE, a real-world-grounded diagnostic benchmark for jointly evaluating how numerical simulators and generative video world models reproduce or deviate from real-world physics.

## 关键点

- **问题**：However, existing evaluations of physical fidelity are often conducted in isolation and rely heavily on perceptual similarity or human judgments, providing limited insight into which physical principles or parameters are violated.
- **创新点 / 方法**：We introduce GAUGE, a real-world-grounded diagnostic benchmark for jointly evaluating how numerical simulators and generative video world models reproduce or deviate from real-world physics.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **L2 精读**：[[50_Papers/Deep Reads/GAUGE 2608.05948v1/README|已完成精读报告]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/GAUGE A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physics engines facilitate large-scale training and evaluation for embodied
intelligence, while generative video world models are emerging as implicit simulators of
future states and interactions. However, existing evaluations of physical fidelity are
often conducted in isolation and rely heavily on perceptual similarity or human
judgments, providing limited insight into which physical principles or parameters are
violated. We introduce GAUGE, a real-world-grounded diagnostic benchmark for jointly
evaluating how numerical simulators and generative video world models reproduce or
deviate from real-world physics. It comprises 22 controlled task families covering rigid
bodies, flexible cables, textiles, and volumetric deformable objects. Grounded in real-
world trajectories and paired with calibrated physical metadata, uncertainty
annotations, and task-specific observables, these tasks cover fundamental physical
processes including collision, friction, momentum transfer, oscillation, self-contact,
and deformation across diverse materials and conditions. We benchmark Isaac Sim,
Genesis, and Newton on 14 task families using generalized trajectory errors, and
evaluate 6 image-to-video models on 5 rigid-body tasks by testing physical-law
consistency and the temporal stability of inferred parameters. Our results reveal no
uniformly faithful physics engine, with the largest discrepancies arising in impulsive
contact, rapid textile motion, and volumetric deformation. We further find that video
world models can produce trajectories with the expected equation form while recovering
incorrect accelerations, momentum transfer, and oscillation timing. GAUGE lays the
groundwork for developing more physically faithful simulators and world models for
embodied intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.05948v1
- Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang
- Published: 2026-08-06T12:19:38Z
- Age days: 3

</details>
