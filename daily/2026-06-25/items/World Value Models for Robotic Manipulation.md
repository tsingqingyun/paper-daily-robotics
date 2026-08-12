---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24742v1"
published: "2026-06-23T16:07:48Z"
age_days: 1
score: 38
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# World Value Models for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> When deployed for policy learning, WVM improves manipulation performance across various policy extraction approaches in both simulated and real-world deployment, providing robust guidance for learning from mixed-quality data.

## 关键点

- **问题**：However, most existing robotic value models are built on Vision-Language Model (VLM) backbones that are pretrained primarily on static or temporally sparse visual observations, lacking the requisite temporal modeling capabilities for value estimation.
- **创新点 / 方法**：Generalist value models play a pivotal role in scaling robotic policy learning from large-scale, mixed-quality data.
- **证据**：When deployed for policy learning, WVM improves manipulation performance across various policy extraction approaches in both simulated and real-world deployment, providing robust guidance for learning from mixed-quality data.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist value models play a pivotal role in scaling robotic policy learning from
large-scale, mixed-quality data. Mathematically, accurate value estimation demands deep
temporal understanding, requiring models to both ground the current belief using
historical context and plan over future outcomes. However, most existing robotic value
models are built on Vision-Language Model (VLM) backbones that are pretrained primarily
on static or temporally sparse visual observations, lacking the requisite temporal
modeling capabilities for value estimation. Unlike VLMs, world models naturally excel at
temporal modeling and future planning, making them ideal foundations for learning
generalizable value functions. Driven by this insight, we marry world models with value
estimation to construct a new generalist robotic value model, World Value Model (WVM),
that offers accurate task progressions to assess data quality. On standard benchmarks,
WVM delivers state-of-the-art (SOTA) Value-Order Correlation (VOC) results.
Complementing standard evaluation suites that contains only expert data, we further
introduce Suboptimal-Value-Bench, a multi-embodiment benchmark consisting of 800
suboptimal trajectories with high-fidelity, human-labeled frame annotations. Our
evaluations show that WVM maintains its SOTA performance on Suboptimal-Value-Bench,
establishing its robustness in handling both expert and suboptimal data. When deployed
for policy learning, WVM improves manipulation performance across various policy
extraction approaches in both simulated and real-world deployment, providing robust
guidance for learning from mixed-quality data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24742v1
- Authors: Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan, Junzhi Yu, Xiao Ma
- Published: 2026-06-23T16:07:48Z
- Age days: 1

</details>
