---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19060v1"
published: "2026-07-21T12:48:48Z"
age_days: 3
score: 26
created: 2026-07-25
concepts: ["世界模型", "具身智能评测与基准"]
---

# Deep learning-based prediction of time-resolved adhesive forces in viscoelastic Hertzian contacts

> [!summary] 一句话结论（基于摘要）
> We found that the best-performing model has an LSTM architecture with concatenated conditioning, which achieves a held-out mean-squared error of $5.0\times10^{-4}$, a median pull-off-force error of $\approx2.2\%$, and a median hysteresis error of $\approx1.1\…

## 关键点

- **问题**：Fast prediction of the response of adhesive soft viscoelastic contacts represents a current challenge in soft robotics and for gripping and manipulation tasks.
- **创新点 / 方法**：To enable learning across these heterogeneous time scales, we introduce a fixed-measurement-step (FMS) representation that converts variable-length trajectories into fixed-length sequences while preserving their physical-time information.
- **证据**：We found that the best-performing model has an LSTM architecture with concatenated conditioning, which achieves a held-out mean-squared error of $5.0\times10^{-4}$, a median pull-off-force error of $\approx2.2\%$, and a median hysteresis error of $\approx1.1\%$.
- **局限**：In this work, we overcome this limitation by training a scalar-conditioned, stateful, sequence-to-sequence deep learning model to predict the full force evolution from a prescribed displacement history for both short- and long-range adhesion regimes.

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Deep learning-based prediction of time-resolved adhesive forces in viscoelastic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Fast prediction of the response of adhesive soft viscoelastic contacts represents a
current challenge in soft robotics and for gripping and manipulation tasks. Determining
the complete time-resolved force trajectory requires full numerical simulations, whose
computational cost is strongly parameter-dependent, making them impractical for real-
time application or design-optimization loops. In this work, we overcome this limitation
by training a scalar-conditioned, stateful, sequence-to-sequence deep learning model to
predict the full force evolution from a prescribed displacement history for both short-
and long-range adhesion regimes. The data set spans four orders of magnitude in loading
and unloading rates and includes varied dwell times, with the Tabor parameter ranging
from $0.2$ to $3.2$. To enable learning across these heterogeneous time scales, we
introduce a fixed-measurement-step (FMS) representation that converts variable-length
trajectories into fixed-length sequences while preserving their physical-time
information. Different architectures were trained, including long short-term memory
(LSTM) networks, temporal convolutional neural (TCN) networks, and time-distributed
dense layers with three different Tabor-conditioning mechanisms. The models were
compared using global waveform and error metrics. We found that the best-performing
model has an LSTM architecture with concatenated conditioning, which achieves a held-out
mean-squared error of $5.0\times10^{-4}$, a median pull-off-force error of
$\approx2.2\%$, and a median hysteresis error of $\approx1.1\%$. For the held-out
protocols, the model predicts a complete force trajectory with a median inference time
of $0.16$ s. The model is tested across unseen parameter combinations and against
analytical limiting cases, providing a rapid surrogate for repeated numerical
evaluations with potential use in control-oriented applications.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19060v1
- Authors: Ali Maghami, Merten Stender, Michele Ciavarella, Antonio Papangelo
- Published: 2026-07-21T12:48:48Z
- Age days: 3

</details>
