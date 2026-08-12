---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18960v1"
published: "2026-06-17T11:42:00Z"
age_days: 1
score: 29
created: 2026-06-19
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments show that Mem-World generates persistent rollouts in complex manipulation scenarios, enables more reliable policy evaluation than Ctrl-World, improving the Pearson correlation with real-world performance by 14.5\%, and supports effective…

## 关键点

- **问题**：However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames.
- **创新点 / 方法**：To address this limitation, we propose Mem-World, a memory-augmented multi-view action- conditioned world model.
- **证据**：Extensive experiments show that Mem-World generates persistent rollouts in complex manipulation scenarios, enables more reliable policy evaluation than Ctrl-World, improving the Pearson correlation with real-world performance by 14.5\%, and supports effective policy improvement through synthetic data generation, incre…
- **局限**：However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-19/Mem-World Memory-Augmented Action-Conditioned World Models for Persistent Robot.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action-conditioned world models have emerged as a promising paradigm for robot learning,
offering a scalable alternative to costly real-world experimentation by generating
action-consistent video rollouts. However, persistent world modeling remains challenging
in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the
current observation insufficient for predicting future views, causing models to forget
or hallucinate scene details seen in earlier frames. Existing memory retrieval
strategies often fail to identify informative history in dynamic manipulation scenarios.
To address this limitation, we propose Mem-World, a memory-augmented multi-view action-
conditioned world model. At its core, we present W-VMem, a 4D wrist-view-centered
surfel-indexed memory that anchors historical observations to temporally evolving
surface elements. By explicitly modeling when and where scene elements are observed,
W-VMem enables geometry-aware retrieval of relevant history frames conditioned on future
actions. During generation, relevant history frames are selected via surfel-based
rendering and scoring, providing informative and non-redundant context for prediction.
Extensive experiments show that Mem-World generates persistent rollouts in complex
manipulation scenarios, enables more reliable policy evaluation than Ctrl-World,
improving the Pearson correlation with real-world performance by 14.5\%, and supports
effective policy improvement through synthetic data generation, increasing success rates
from 58\% to 72\% on long-horizon tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18960v1
- Authors: Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, Weiming Li, Dong Wang, Huchuan Lu, Xu Jia
- Published: 2026-06-17T11:42:00Z
- Age days: 1

</details>
