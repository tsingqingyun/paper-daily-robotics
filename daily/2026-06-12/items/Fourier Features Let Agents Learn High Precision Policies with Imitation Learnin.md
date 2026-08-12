---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12334v1"
published: "2026-06-10T17:05:50Z"
age_days: 1
score: 37
created: 2026-06-12
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Fourier Features Let Agents Learn High Precision Policies with Imitation Learning

> [!summary] 一句话结论（基于摘要）
> High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues.

## 关键点

- **问题**：High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues.
- **创新点 / 方法**：Policies that leverage 3D information directly, such as those based on point clouds, offer a stronger geometric prior over purely image-based ones, yet their performance remains highly task-dependent.
- **证据**：High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/Fourier Features Let Agents Learn High Precision Policies with Imitation Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

High-precision robotic manipulation requires fine-grained spatial reasoning that is
often difficult to achieve with RGB-only policies due to depth ambiguity and perspective
scale issues. Policies that leverage 3D information directly, such as those based on
point clouds, offer a stronger geometric prior over purely image-based ones, yet their
performance remains highly task-dependent. We hypothesize that this discrepancy may be
due to the spectral bias of neural networks towards learning low frequency functions,
which especially affects architectures conditioned on slow-moving Cartesian features. We
thus propose to map point clouds from Cartesian space into high-dimensional Fourier
space, effectively equipping the point cloud encoder with direct access to high-
frequency features. We experimentally validate the use of Fourier features on
challenging manipulation tasks from the RoboCasa and ManiSkill3 benchmarks and on a real
robot setup. Despite their simplicity, we find that Fourier features provide significant
benefits across diverse encoder architectures and benchmarks and are robust across
hyperparameters. Our results indicate that Fourier features let policies leverage
geometric details more effectively than Cartesian features, showing their potential as a
general-purpose tool for point cloud-based imitation learning. We provide source code
and videos on our project page: https://fourier-il.github.io/fourier-il

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12334v1
- Authors: Balázs Gyenes, Emiliyan Gospodinov, Jan Frieling, Enrico Krohmer, Nicolas Schreiber, Xiaogang Jia, Niklas Freymuth, Gerhard Neumann
- Published: 2026-06-10T17:05:50Z
- Age days: 1

</details>
