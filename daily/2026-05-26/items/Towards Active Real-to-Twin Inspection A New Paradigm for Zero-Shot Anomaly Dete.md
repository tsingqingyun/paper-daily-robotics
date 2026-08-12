---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25407v1"
published: "2026-05-25T04:05:25Z"
age_days: 1
score: 29
created: 2026-05-26
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Towards Active Real-to-Twin Inspection: A New Paradigm for Zero-Shot Anomaly Detection

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that AVATAR substantially outperforms adapted state-of-the-art baselines, exhibiting exceptional robustness to severe viewpoint variations.

## 关键点

- **问题**：The deployment of zero-shot anomaly detection (AD) in embodied industrial inspection is severely bottlenecked by its reliance on passive, fixed-viewpoint 2D imagery.
- **创新点 / 方法**：To break this limitation, we introduce Real-to-Twin Anomaly Detection, a novel task that evaluates physical observations directly against geometrically matched CAD Digital Twins.
- **证据**：Extensive experiments demonstrate that AVATAR substantially outperforms adapted state-of-the-art baselines, exhibiting exceptional robustness to severe viewpoint variations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-26/Towards Active Real-to-Twin Inspection A New Paradigm for Zero-Shot Anomaly Dete.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The deployment of zero-shot anomaly detection (AD) in embodied industrial inspection is
severely bottlenecked by its reliance on passive, fixed-viewpoint 2D imagery. Such
formulations inherently fail to accommodate the active, dynamic observations required in
real-world environments. To break this limitation, we introduce Real-to-Twin Anomaly
Detection, a novel task that evaluates physical observations directly against
geometrically matched CAD Digital Twins. To tackle this new task, we propose AVATAR, a
framework designed to learn robust semantic alignment between Real and Digital Twins. By
bridging benign Sim2Real domain gaps using only defect-free pairs, AVATAR effectively
transforms CAD priors into dynamic, anomaly-free references. This elegant formulation
enables the model to localize diverse anomalies in a zero-shot manner as unalignable
deviations, eliminating the need for defect annotations. Extensive experiments
demonstrate that AVATAR substantially outperforms adapted state-of-the-art baselines,
exhibiting exceptional robustness to severe viewpoint variations. The code and dataset
will be made publicly available.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25407v1
- Authors: Jiaxuan Liu, Yunkang Cao, Yufeng Chen, Chunyang Li, Yuhuan Du, Hui Zhang
- Published: 2026-05-25T04:05:25Z
- Age days: 1

</details>
