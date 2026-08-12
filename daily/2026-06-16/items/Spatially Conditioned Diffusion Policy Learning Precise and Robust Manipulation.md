---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14535v1"
published: "2026-06-12T15:12:03Z"
age_days: 3
score: 25
created: 2026-06-16
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera

> [!summary] 一句话结论（基于摘要）
> Extensive simulation experiments show that SCDP consistently outperforms strong single-view baselines and achieves performance comparable to multi- camera baselines.

## 关键点

- **问题**：However, manipulation from a single global view remains challenging, as the policy should capture fine-grained interaction details and identify task-relevant regions without local wrist views.
- **创新点 / 方法**：To address this challenge, we present Spatially Conditioned Diffusion Policy (SCDP), a diffusion-based visuomotor policy that achieves precise and robust manipulation in a single-camera setting.
- **证据**：Extensive simulation experiments show that SCDP consistently outperforms strong single-view baselines and achieves performance comparable to multi- camera baselines.
- **局限**：However, manipulation from a single global view remains challenging, as the policy should capture fine-grained interaction details and identify task-relevant regions without local wrist views.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/Spatially Conditioned Diffusion Policy Learning Precise and Robust Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent visual imitation learning systems have widely adopted multi-camera setups with
wrist-mounted cameras as the de facto standard. However, manipulation from a single
global view remains challenging, as the policy should capture fine-grained interaction
details and identify task-relevant regions without local wrist views. To address this
challenge, we present Spatially Conditioned Diffusion Policy (SCDP), a diffusion-based
visuomotor policy that achieves precise and robust manipulation in a single-camera
setting. Our key idea is that end-effector trajectories can serve as visual attention
anchors that reflect task-relevant regions. Building on this idea, SCDP consists of two
key components: (i) a visual encoder that produces multi-scale feature maps to capture
both broader context and fine-grained visual features, and (ii) a spatial conditioning
module that samples point-wise features along intermediate end-effector trajectories in
the diffusion loop. Extensive simulation experiments show that SCDP consistently
outperforms strong single-view baselines and achieves performance comparable to multi-
camera baselines. Real-world experiments further demonstrate precise manipulation and
robustness to visual distractors, highlighting the potential of single-camera imitation
learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14535v1
- Authors: Seoyoon Kim, Kanghyun Kim, Dongwoo Ko, Yeong Jin Heo, Min Jun Kim
- Published: 2026-06-12T15:12:03Z
- Age days: 3

</details>
