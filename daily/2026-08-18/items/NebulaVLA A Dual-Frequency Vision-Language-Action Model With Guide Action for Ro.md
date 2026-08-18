---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16503v1"
published: "2026-08-17T12:40:23Z"
age_days: 0
score: 44
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Comprehensive evaluations demonstrate that NebulaVLA significantly outperforms synchronous baselines, achieving an 85.5\% average success rate on LIBERO-Plus and accelerating action generation by \textasciitilde 2.7$\times$.

## 关键点

- **问题**：Real-world deployment of Vision-Language-Action (VLA) models is often bottlenecked by efficiency-performance trade-offs, cross-embodiment generalization, and execution smoothness.
- **创新点 / 方法**：We present NebulaVLA, an asynchronous dual-frequency architecture that decouples high-level semantic reasoning from low-level action control, optimizing computational resources and modularity.
- **证据**：Comprehensive evaluations demonstrate that NebulaVLA significantly outperforms synchronous baselines, achieving an 85.5\% average success rate on LIBERO-Plus and accelerating action generation by \textasciitilde 2.7$\times$.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：44
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/NebulaVLA A Dual-Frequency Vision-Language-Action Model With Guide Action for Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-world deployment of Vision-Language-Action (VLA) models is often bottlenecked by efficiency-performance trade-offs, cross-embodiment generalization, and execution smoothness. We present NebulaVLA, an asynchronous dual-frequency architecture that decouples high-level semantic reasoning from low-level action control, optimizing computational resources and modularity. To bridge semantic gaps across heterogeneous robots, we introduce GESTURE-7, a unified language-grounded action representation. Furthermore, our Guide Action algorithm enforces kinematic continuity via mask-based smoothness constraints. Comprehensive evaluations demonstrate that NebulaVLA significantly outperforms synchronous baselines, achieving an 85.5\% average success rate on LIBERO-Plus and accelerating action generation by \textasciitilde 2.7$\times$. This asynchronous design enables highly efficient and responsive control for practical robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16503v1
- Authors: Cong Zhao, Shuai Tian, Xu Zhang, Baocheng Ni, Xinguo Song, Xueying Sun, Shu Jiang, Shouchang Yang, Bo Tang, Jin Deng, Ge Zhu, YongCheng Wang, Jin Xu, Ri Yang
- Published: 2026-08-17T12:40:23Z
- Age days: 0

</details>
