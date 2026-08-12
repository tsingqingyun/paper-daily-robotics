---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.19282v1"
published: "2026-05-19T03:00:26Z"
age_days: 0
score: 30
created: 2026-05-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

> [!summary] 一句话结论（基于摘要）
> In VLA training on LIBERO and LIBERO-Plus, Pion consistently outperforms both baselines across l_1-regression (VLA-Adapter) and flow- matching (VLANeXt) architectures, e.g., reaching 100% success rate on LIBERO Object after 1,500 training steps with VLA-Adapt…

## 关键点

- **问题**：While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noi…
- **创新点 / 方法**：To address these challenges, we propose Pion, a drop-in replacement for Muon that preserves its computational efficiency while replacing uniform spectral whitening with a two-stage Promotion+Suppression mechanism, which we call the high-pass NS iteration.
- **证据**：In VLA training on LIBERO and LIBERO-Plus, Pion consistently outperforms both baselines across l_1-regression (VLA-Adapter) and flow- matching (VLANeXt) architectures, e.g., reaching 100% success rate on LIBERO Object after 1,500 training steps with VLA-Adapter, vs.
- **局限**：While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noi…

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/Rethinking Muon Beyond Pretraining Spectral Failures and High-Pass Remedies for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Muon is a matrix-aware optimizer that leverages Newton-Schulz (NS) iterations to enforce
spectral gradient orthogonalization by driving all singular values of the momentum
matrix toward 1. While this uniform spectral whitening enhances exploration and
outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations
beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA)
training, where inherently low-rank action-module gradients cause amplification of noisy
tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where
low-SNR gradients and the need to preserve per-head specialization from prior training
make whitening unstable. To address these challenges, we propose Pion, a drop-in
replacement for Muon that preserves its computational efficiency while replacing uniform
spectral whitening with a two-stage Promotion+Suppression mechanism, which we call the
high-pass NS iteration. This design induces a sharp spectral high-pass effect, anchoring
dominant singular values at 1 while suppressing noisy tail components toward 0, with
controllable filter strength. To preserve pretrained per-head heterogeneity, Pion also
supports a per-head mode that applies updates independently across attention heads via a
simple reshape, at no extra cost. In VLA training on LIBERO and LIBERO-Plus, Pion
consistently outperforms both baselines across l_1-regression (VLA-Adapter) and flow-
matching (VLANeXt) architectures, e.g., reaching 100% success rate on LIBERO Object
after 1,500 training steps with VLA-Adapter, vs. 97.0% for Muon and only 32.2% for
AdamW. The advantage of Pion further extends to a real Franka Research 3 robot with a
pi_0.5 backbone under the DROID setup on three grasp-and-place tasks. In RLVR post-
training on Qwen3-1.7B/4B with GRPO and GMPO, Pion also outperforms AdamW on MATH and
GSM8K while Muon collapses to zero.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.19282v1
- Authors: Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu
- Published: 2026-05-19T03:00:26Z
- Age days: 0

</details>
