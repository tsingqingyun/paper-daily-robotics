---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11901v1"
published: "2026-06-10T10:28:04Z"
age_days: 1
score: 37
created: 2026-06-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World

> [!summary] 一句话结论（基于摘要）
> Our results show that current policies remain challenged by bimanual manipulation, particularly in early interaction stages, parallel arm execution, and transfer between simulation and real-world settings.

## 关键点

- **问题**：Bimanual robot systems substantially expand manipulation capabilities, but coordinating two arms introduces additional control complexity and failure modes that are not well captured by existing benchmarks.
- **创新点 / 方法**：We introduce DuoBench, an extensible benchmarking framework for bimanual manipulation policies on the FR3 Duo platform.
- **证据**：Our results show that current policies remain challenged by bimanual manipulation, particularly in early interaction stages, parallel arm execution, and transfer between simulation and real-world settings.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Bimanual robot systems substantially expand manipulation capabilities, but coordinating
two arms introduces additional control complexity and failure modes that are not well
captured by existing benchmarks. We introduce DuoBench, an extensible benchmarking
framework for bimanual manipulation policies on the FR3 Duo platform. DuoBench comprises
eleven tasks spanning four coordination categories, implemented in simulation and
partially reproduced in the real world through reproducible task recipes with
3D-printable assets. In addition, we propose a stage-based evaluation scheme that
supports fine-grained semantic failure analysis beyond binary success and provide human-
teleoperated datasets for all benchmark tasks. We benchmark several dual-arm imitation-
learning and vision-language-action policies in simulation and on real hardware. Our
results show that current policies remain challenged by bimanual manipulation,
particularly in early interaction stages, parallel arm execution, and transfer between
simulation and real-world settings. DuoBench provides a reproducible testbed for
diagnosing these failure modes and studying future methods for dual-arm policy learning.
Code, datasets, and videos are available at https://duobench.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11901v1
- Authors: Tobias Jülg, Seongjin Bien, Simon Hilber, Yannik Blei, Pierre Krack, Maximilian Li, Sven Parusel, Rudolf Lioutikov, Florian Walter, Wolfram Burgard
- Published: 2026-06-10T10:28:04Z
- Age days: 1

</details>
