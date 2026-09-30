---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21290"
published: "Mon, 24 Aug 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-08-25
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation

> [!summary] 一句话结论（基于摘要）
> On the simulation benchmark, VT-MUSE outperforms the strongest baseline evaluated on all tasks by 11 percentage points and also achieves substantial improvements in real-world experiments.

## 问题

VT-MUSE addresses both limitations through a two-stage representation learning framework.

## 创新点或方法

arXiv:2608.21290v1 Announce Type: new Abstract: We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation.

## 证据

On the simulation benchmark, VT-MUSE outperforms the strongest baseline evaluated on all tasks by 11 percentage points and also achieves substantial improvements in real-world experiments.

## 局限

VT-MUSE addresses both limitations through a two-stage representation learning framework.


## 研究关联

- **概念**：多模态基础模型 世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-25/VT-MUSE Multimodal Unified Sequential Visuotactile Representation Learning for M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.21290v1 Announce Type: new Abstract: We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation. Existing approaches often encode visual and tactile observations independently before fusion, limiting their ability to capture fine-grained cross-modal dependencies. Moreover, most methods focus on observations at the current time step and overlook the temporal evolution of contact. VT-MUSE addresses both limitations through a two-stage representation learning framework. In Stage I, modality specific encoders are jointly adapted via cross-modal temporal alignment and masked-view consistency. In Stage II, a conditional variational latent model processes masked visual sequences together with full tactile histories. Auxiliary decoders reconstruct the masked recent visual observations and predict tactile depth changes, encouraging the latent representation to retain both global visual context and local contact dynamics. The learned representation is subsequently integrated into a lightweight Transformer policy through gated cross-attention. On the simulation benchmark, VT-MUSE outperforms the strongest baseline evaluated on all tasks by 11 percentage points and also achieves substantial improvements in real-world experiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21290
- Authors: Congsheng Xu, Qiaochu Yang, Fangyuan Shi, Yifan Han, Baijun Chen, Yiming Wang, Haonan Zhao, Daolin Ma, Xiaokang Yang, Hesheng Wang
- Published: Mon, 24 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
