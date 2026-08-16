---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13028v1"
published: "2026-08-13T09:55:59Z"
age_days: 3
score: 25
created: 2026-08-16
concepts: ["Sim2Real", "具身智能评测与基准"]
---

# RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction

> [!summary] 一句话结论（基于摘要）
> Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform.

## 关键点

- **问题**：Human-to-robot (H2R) object handover is a fundamental capability for human-robot collaboration, yet progress is hindered by the scarcity of large-scale, human-centric datasets and the significant sim-to-real gap.
- **创新点 / 方法**：To address these challenges, we introduce Hand2Bot, an RGB-D video dataset that provides rich contextual information such as body posture and facial expressions, specifically collected for handover scenarios with real-world noise patterns.
- **证据**：Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human-to-robot (H2R) object handover is a fundamental capability for human-robot collaboration, yet progress is hindered by the scarcity of large-scale, human-centric datasets and the significant sim-to-real gap. To address these challenges, we introduce Hand2Bot, an RGB-D video dataset that provides rich contextual information such as body posture and facial expressions, specifically collected for handover scenarios with real-world noise patterns. We further propose PassGen, a generative pipeline that leverages stable video diffusion and an Intention-Aware Temporal Face Encoder to synthesize realistic handover sequences while ensuring hand-object consistency. To bridge the sim-to-real gap, we implement a morphology-based depth editing strategy that replicates realistic sensor noise found in physical depth maps. Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform. Our results confirm that training on PassGen allows for robust zero-shot transfer and earlier intention anticipation compared to traditional hand-centric baselines, effectively enabling socially aware robotic behavior in shared workspaces.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13028v1
- Authors: Tianyu Sun, Zhoujie Fu, Zihui Gao, Bang Zhang, Guosheng Lin
- Published: 2026-08-13T09:55:59Z
- Age days: 3

</details>
