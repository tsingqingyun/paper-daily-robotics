---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13552v1"
published: "2026-08-13T17:59:30Z"
age_days: 2
score: 25
created: 2026-08-16
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives

> [!summary] 一句话结论（基于摘要）
> Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective.

## 关键点

- **问题**：However, fairly comparing these interactive models remains challenging.
- **创新点 / 方法**：Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：However, fairly comparing these interactive models remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/PlayWorld Benchmarking World Models with Agent Players over Long-Horizon Objecti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or walk into the water and inspect whether realistic water ripples are generated. The action sequence required to achieve the same objective may vary substantially between models, making fixed action-conditioned evaluation unsuitable for cross-model comparison. To address this, we employ multi-modal Agent Players to interact with world models toward specified long-horizon objectives. Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective. To evaluate performance thoroughly, we assess models along four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution. In addition, we incorporate basic ability metrics for video quality and controllability. Experiments across nine state-of-the-art world models reveal that current models remain unreliable on long-horizon interactive objectives, particularly in maintaining spatial consistency and persistent state evolution. Code and data are available at https://github.com/kxding/PlayWorld.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13552v1
- Authors: Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang, Yuxiang Lu, Junyi Li, Shuyang Chen, Yuan Gao, Xin Tao, Pengfei Wan, Hengshuang Zhao
- Published: 2026-08-13T17:59:30Z
- Age days: 2

</details>
