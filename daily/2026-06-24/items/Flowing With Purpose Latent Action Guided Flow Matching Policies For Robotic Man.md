---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23420v1"
published: "2026-06-22T14:42:59Z"
age_days: 1
score: 33
created: 2026-06-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Empirically, LAFM substantially outperforms standard flow matching formulations, increasing task success rates by 23.4% in real-world robotic deployments and by 10.4% on the LIBERO-90 benchmark.

## 关键点

- **问题**：However, state-of-the-art flow matching policies suffer from a systematic structural mismatch: they rely on a globally fixed isotropic source distribution despite the strongly fragmented and heteroscedastic structure of robotic action spaces.
- **创新点 / 方法**：To address this limitation, we introduce Latent Action Guided Flow Matching (LAFM), a novel framework that replaces the monolithic Gaussian with an adaptive library of learned prior distributions.
- **证据**：Empirically, LAFM substantially outperforms standard flow matching formulations, increasing task success rates by 23.4% in real-world robotic deployments and by 10.4% on the LIBERO-90 benchmark.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow matching has recently become a new standard for behavior cloning in robotic
manipulation. However, state-of-the-art flow matching policies suffer from a systematic
structural mismatch: they rely on a globally fixed isotropic source distribution despite
the strongly fragmented and heteroscedastic structure of robotic action spaces. This
agnostic initialization forces the model to learn highly entangled vector fields,
bottlenecking training efficiency and limiting overall policy performance. To address
this limitation, we introduce Latent Action Guided Flow Matching (LAFM), a novel
framework that replaces the monolithic Gaussian with an adaptive library of learned
prior distributions. By grounding these distributions using a latent action model, LAFM
maps current observations to discrete motion primitives, selecting a specialized base
distribution that provides an informed, structurally aligned initialization for the
denoising process. This dynamic adaptivity naturally accommodates heteroscedasticity in
human demonstrations and makes transport trajectories shorter and less entangled.
Empirically, LAFM substantially outperforms standard flow matching formulations,
increasing task success rates by 23.4% in real-world robotic deployments and by 10.4% on
the LIBERO-90 benchmark. Furthermore, we demonstrate that LAFM achieves state-of-the-art
results, surpassing massively pre-trained vision-language-action models while utilizing
significantly smaller architectures.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23420v1
- Authors: Bruno Machado, Alexandre Chapin, Emmanuel Dellandrea, Liming Chen
- Published: 2026-06-22T14:42:59Z
- Age days: 1

</details>
