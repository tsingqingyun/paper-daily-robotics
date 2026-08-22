---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20308v1"
published: "2026-08-20T17:46:24Z"
age_days: 1
score: 30
created: 2026-08-22
concepts: ["具身智能评测与基准"]
---

# DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery

> [!summary] 一句话结论（基于摘要）
> We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder.

## 关键点

- **问题**：Egocentric video offers scalable manipulation data for embodied AI, yet recovering metric 3D hand trajectories remains challenging due to severe object occlusion and frequent out-of-sight gaps.
- **创新点 / 方法**：We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Egocentric video offers scalable manipulation data for embodied AI, yet recovering metric 3D hand trajectories remains challenging due to severe object occlusion and frequent out-of-sight gaps.

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/DreamHand Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric video offers scalable manipulation data for embodied AI, yet recovering metric 3D hand trajectories remains challenging due to severe object occlusion and frequent out-of-sight gaps. Existing single-frame and windowed temporal regressors fail when hand shortly leaves the frame, while recent video diffusion models (VDMs) rely on heavy, stochastic multi-step sampling as pixel-space renderers. We instead repurpose VDM into a deterministic geometry encoder. A single forward pass over the clean latent exposes scene content beyond current observations, including occluded and out-of-sight hands. We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder. DreamHand recovers continuous bimanual trajectories with metric placement and no external detector, while a Ray-Based Camera Solver supports a second configuration that needs no test-time camera intrinsics. Across five egocentric benchmarks, DreamHand sets a new state of the art, cutting MPJPE-p by 30% on occlusion-heavy ARCTIC and 40% on HOT3D. These gains reach 46%-61% once out-of-sight hands are included in the evaluation, offering a scalable path from everyday human video to robot manipulation data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20308v1
- Authors: Yufei Liu, Xixi Wang, Hao Li, Ganlong Zhao, Kaitong Cai, Chengkai Jin, Chunxiao Liu, Jianbo Liu, Siyuan Huang, Xingang Pan, Hongsheng Li
- Published: 2026-08-20T17:46:24Z
- Age days: 1

</details>
