---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12145v1"
published: "2026-08-12T15:06:51Z"
age_days: 2
score: 28
created: 2026-08-15
concepts: ["具身智能评测与基准"]
---

# Autonomous Telerehabilitation via Skeletal Motion Prediction and Joint-Level Performance Assessment

> [!summary] 一句话结论（基于摘要）
> Each module is evaluated independently on established benchmarks: the classifier achieves 96.45% mean-class accuracy on squat sequences from the PROZIS dataset, and the adopted STARS predictor achieves a mean MPJPE of 75.8 mm at 560 ms on Human3.6M, outperfor…

## 关键点

- **问题**：Autonomous rehabilitation systems must not only recognize human motion but also provide structured feedback to support users without continuous therapist supervision.
- **创新点 / 方法**：This paper presents a telerehabilitation pipeline that integrates skeleton-based exercise quality assessment and short-term motion prediction into a two-module system operating on marker-free RGB video.
- **证据**：Each module is evaluated independently on established benchmarks: the classifier achieves 96.45% mean-class accuracy on squat sequences from the PROZIS dataset, and the adopted STARS predictor achieves a mean MPJPE of 75.8 mm at 560 ms on Human3.6M, outperforming graph and recurrent baselines across all prediction hor…
- **局限**：The framework is designed for eventual deployment in assistive robotics and home-based rehabilitation contexts; end-to-end integration and clinical validation are important directions for future work.

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/Autonomous Telerehabilitation via Skeletal Motion Prediction and Joint-Level Per.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous rehabilitation systems must not only recognize human motion but also provide structured feedback to support users without continuous therapist supervision. This paper presents a telerehabilitation pipeline that integrates skeleton-based exercise quality assessment and short-term motion prediction into a two-module system operating on marker-free RGB video. A self-attentive Bidirectional LSTM performs exercise quality classification using MMD-NCA metric learning, while a graph-based motion prediction module computes per-joint position errors between predicted and observed poses, generating spatially localized deviation signals. Each module is evaluated independently on established benchmarks: the classifier achieves 96.45% mean-class accuracy on squat sequences from the PROZIS dataset, and the adopted STARS predictor achieves a mean MPJPE of 75.8 mm at 560 ms on Human3.6M, outperforming graph and recurrent baselines across all prediction horizons. The framework is designed for eventual deployment in assistive robotics and home-based rehabilitation contexts; end-to-end integration and clinical validation are important directions for future work. By combining motion recognition and prediction in a single system, this work contributes a step toward autonomous, feedback-driven telerehabilitation, for more accessible and scalable rehabilitation solutions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12145v1
- Authors: Lara Pereira, João Ruivo Paulo, Pedro Santos, Paulo Peixoto
- Published: 2026-08-12T15:06:51Z
- Age days: 2

</details>
