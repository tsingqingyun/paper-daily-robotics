---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15060v1"
published: "2026-08-15T06:18:13Z"
age_days: 2
score: 31
created: 2026-08-18
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# EgoTac: In-the-wild Tactile Prediction from Egocentric Vision

> [!summary] 一句话结论（基于摘要）
> Experiments demonstrate strong performance: in-domain prediction achieves an average force error below 0.06N.

## 关键点

- **问题**：Directly collecting large-scale tactile data is challenging due to sensor limitations, while human video data is abundant, contact-rich, and easily scalable.
- **创新点 / 方法**：To address this, we introduce EgoTac, a generalizable model that predicts rich tactile information directly from egocentric human videos.
- **证据**：Experiments demonstrate strong performance: in-domain prediction achieves an average force error below 0.06N.
- **局限**：Directly collecting large-scale tactile data is challenging due to sensor limitations, while human video data is abundant, contact-rich, and easily scalable.

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/EgoTac In-the-wild Tactile Prediction from Egocentric Vision.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Touch is fundamental to dexterous manipulation, yet most egocentric human data increasingly used for robot learning lacks tactile information. Directly collecting large-scale tactile data is challenging due to sensor limitations, while human video data is abundant, contact-rich, and easily scalable. This motivates a natural question: can tactile signals be inferred purely from vision? To address this, we introduce EgoTac, a generalizable model that predicts rich tactile information directly from egocentric human videos. EgoTac is trained on a unified corpus of over 5.7M image-tactile pairs, covering both continuous force measurements and binary contacts. By learning from this diverse dataset, EgoTac captures nuanced touch dynamics across varied interactions. Experiments demonstrate strong performance: in-domain prediction achieves an average force error below 0.06N. On out-of-domain contact prediction benchmarks, EgoTac consistently outperforms the state-of-the-art contact estimator. It also captures the rise and fall patterns of real tactile data and enables zero-shot predictions on unconstrained real-world videos. Scaling analyses further reveal that both data diversity and volume improve performance steadily. Overall, EgoTac provides a scalable pathway to extract tactile priors from egocentric human videos, enabling broadly applicable tactile-aware robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15060v1
- Authors: Wenkang Zhang, Chengbo Yuan, Zicheng Zhang, Zhengxue Cheng, Yang Gao
- Published: 2026-08-15T06:18:13Z
- Age days: 2

</details>
