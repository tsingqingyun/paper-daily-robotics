---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19684v1"
published: "2026-08-20T06:20:03Z"
age_days: 3
score: 23
created: 2026-08-23
concepts: ["机器人学习"]
---

# Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy.

## 关键点

- **问题**：However, a limitation of this approach is that the quality of the low-level policy highly depends on the quality of the dataset.
- **创新点 / 方法**：To address this issue, we introduce QDOS (Quality-Diversity Offline Skill learning), a unified pipeline for robust offline-to-online learning.
- **证据**：By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy.
- **局限**：However, a limitation of this approach is that the quality of the low-level policy highly depends on the quality of the dataset.

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcemen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach to achieve this goal is to employ a two-stage strategy: In the first stage, diverse skills are extracted as a low-level policy from a given dataset, and a high-level policy is trained to solve a specific task in the second stage. Typically, extraction of the low-level policy is performed based on unsupervised learning such as trajectory VAE. However, a limitation of this approach is that the quality of the low-level policy highly depends on the quality of the dataset. To address this issue, we introduce QDOS (Quality-Diversity Offline Skill learning), a unified pipeline for robust offline-to-online learning. Our approach incorporates an Advantage-Weighted Quality-Diversity pretraining objective, which weights the skill extraction and diversity objectives by the estimated advantage of each trajectory segment. This approach allows the model to extract diverse and high-value skills. By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy. We further integrate this with a dual dataset reuse strategy, where offline data is used both for skill pretraining and for populating the online replay buffer via pseudo-labeling. Experiments demonstrate that QDOS significantly outperforms strong baselines in structured manipulation tasks and unstructured locomotion tasks, confirming its ability to accelerate exploration and improve final returns in challenging sparse-reward domains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19684v1
- Authors: Tanachai Anakewat, Takayuki Osa, Tatsuya Harada
- Published: 2026-08-20T06:20:03Z
- Age days: 3

</details>
