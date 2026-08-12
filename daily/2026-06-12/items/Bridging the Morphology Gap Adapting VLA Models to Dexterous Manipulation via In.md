---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12109v1"
published: "2026-06-10T14:03:52Z"
age_days: 1
score: 36
created: 2026-06-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

> [!summary] 一句话结论（基于摘要）
> Extensive simulation benchmarks across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate that InDex effectively masters intricate skills with minimal demonstration data, substantially outperforming monolithic baselines while preser…

## 关键点

- **问题**：Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers.
- **创新点 / 方法**：In this paper, we present InDex, a novel, data-efficient adaptation framework rooted in cross-morphology semantic inheritance.
- **证据**：Extensive simulation benchmarks across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate that InDex effectively masters intricate skills with minimal demonstration data, substantially outperforming monolithic baselines while preserving the robust spatial generalizability of the original VLA…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/Bridging the Morphology Gap Adapting VLA Models to Dexterous Manipulation via In.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot
generalization in robotic manipulation, yet the vast majority of pre-trained pipelines
remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic
priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end
joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and
acute action manifold collapse due to data scarcity. In this paper, we present InDex, a
novel, data-efficient adaptation framework rooted in cross-morphology semantic
inheritance. Rather than discarding the pre-trained 1-DoF parallel grasp output, we
repurpose it as a continuous, macroscopic virtual grasp intent proxy to sequentialize
the control topology. We implement a two-stage decoupled learning architecture: the
first stage parameter-efficiently aligns the VLA backbone to predict continuous arm
trajectories and the scalar grasp intent; the second stage freezes this spatial backbone
and leverages an intent-conditioned denoising diffusion head to decode fine-grained
joint articulations for multi-fingered end-effectors. Extensive simulation benchmarks
across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate
that InDex effectively masters intricate skills with minimal demonstration data,
substantially outperforming monolithic baselines while preserving the robust spatial
generalizability of the original VLA prior.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12109v1
- Authors: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
- Published: 2026-06-10T14:03:52Z
- Age days: 1

</details>
