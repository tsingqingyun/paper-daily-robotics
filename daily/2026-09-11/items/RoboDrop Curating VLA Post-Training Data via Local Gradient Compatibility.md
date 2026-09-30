---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10021v1"
published: "2026-09-09T10:55:10Z"
age_days: 1
score: 26
created: 2026-09-11
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility

> [!summary] 先说人话（基于摘要）
> To address these challenges, we introduce \textsc{RoboDrop}, a data-curation framework that audits supervision using local gradient compatibility measured along the training trajectory as a proxy for its effect on post-training performance.

## 这篇到底在做什么

- **卡在哪里**：Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data.
- **关键解法**：To address these challenges, we introduce \textsc{RoboDrop}, a data-curation framework that audits supervision using local gradient compatibility measured along the training trajectory as a proxy for its effect on post-training performance.
- **拿什么证明**：摘要未报告明确实验结论；需阅读全文核查。

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/RoboDrop Curating VLA Post-Training Data via Local Gradient Compatibility.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision--language--action (VLA) models acquire broad generalization through large-scale pretraining, yet adapting them to a new task and robot embodiment still requires post-training on newly collected data. Unlike pretraining, post-training targets task- and embodiment-specific adaptation, making it particularly sensitive to data quality. In practice, collected robot datasets often contain heterogeneous errors, including execution mistakes, sensor drift, and timestamp misalignment, which can impair post-training and policy performance. Manual inspection is costly, while existing data-cleaning methods are typically tailored to particular corruption types. To address these challenges, we introduce \textsc{RoboDrop}, a data-curation framework that audits supervision using local gradient compatibility measured along the training trajectory as a proxy for its effect on post-training performance. During a one-epoch warm-up run, RoboDrop scores each candidate sample online by comparing its gradient with those of task-semantic and visually matched validation samples. The resulting sample scores are aggregated at the episode level, and a simple automatic post-processing rule converts them into filtering decisions. We evaluate RoboDrop on controlled observation--action corruptions, naturally suboptimal demonstrations in simulation, and real-robot datasets containing non-expert collection errors. Across these settings, RoboDrop more accurately distinguishes unreliable demonstrations than prior methods, while post-training on the curated data consistently yields stronger downstream policies, with average real-robot rollout success rising from $35.0\%$ to $67.5\%$. These results establish training-trajectory-aware, context-conditioned supervision auditing as an effective approach to robust VLA post-training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10021v1
- Authors: Runze Xu, Yuanfan Xu, Cuijie Xu, Shuang Dai, Yining Li, Yu Wang, Jincheng Yu
- Published: 2026-09-09T10:55:10Z
- Age days: 1

</details>
