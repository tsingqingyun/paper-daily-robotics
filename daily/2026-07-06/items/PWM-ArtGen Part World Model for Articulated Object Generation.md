---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02045v1"
published: "2026-07-02T11:12:29Z"
age_days: 3
score: 24
created: 2026-07-06
concepts: ["世界模型"]
---

# PWM-ArtGen: Part World Model for Articulated Object Generation

> [!summary] 一句话结论（基于摘要）
> Experiments demonstrate that PWM- ArtGen substantially outperforms existing baselines in the resting state and exhibits strong zero-shot generalization to out-of-distribution objects.

## 关键点

- **问题**：The key challenge in articulated 3D object generation from a single image is accurately predicting the underlying kinematic structure.
- **创新点 / 方法**：To overcome these limitations, we propose to learn the joint distribution of visual dynamics and kinematic parameters.
- **证据**：Experiments demonstrate that PWM- ArtGen substantially outperforms existing baselines in the resting state and exhibits strong zero-shot generalization to out-of-distribution objects.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/PWM-ArtGen Part World Model for Articulated Object Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The key challenge in articulated 3D object generation from a single image is accurately
predicting the underlying kinematic structure. Existing methods either infer kinematic
parameters directly from a static image that lacks dynamic part-level kinematic
relationships, or estimate parameters from visual dynamics generated from a single
image, which is prone to accumulated errors of two steps. Moreover, the limited scale
and diversity of existing annotated datasets further hinder generalization to complex,
real-world objects. To overcome these limitations, we propose to learn the joint
distribution of visual dynamics and kinematic parameters. Recognizing that articulated
objects can be formulated as dynamic systems, we propose a unified Part World Model
called PWM-ArtGen. To leverage unannotated data, this model couples action diffusion and
image diffusion with independent diffusion timesteps, which enables visual branch co-
training. We further curate a photorealistic dataset of 19.7k part-level image pairs
without kinematic annotations, to support co-training. Experiments demonstrate that PWM-
ArtGen substantially outperforms existing baselines in the resting state and exhibits
strong zero-shot generalization to out-of-distribution objects.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02045v1
- Authors: Wentao Zheng, Ancong Wu
- Published: 2026-07-02T11:12:29Z
- Age days: 3

</details>
