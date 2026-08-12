---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15982v1"
published: "2026-07-17T14:18:20Z"
age_days: 2
score: 26
created: 2026-07-20
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Data and Learning Where it Matters for Contact-Rich Manipulation

> [!summary] 一句话结论（基于摘要）
> Across four challenging real-world tasks, using only 2 to 2.5 hours of autonomous data collection, we achieve an average success rate of 96%, compared to the strongest baseline at 55%.

## 关键点

- **问题**：Learned policies trained end-to-end on large datasets often remain brittle in high- precision tasks and struggle with generalization.
- **创新点 / 方法**：We propose an automated data-collection scheme in combination with offline deep reinforcement learning for the critical segment of the task, eliminating reliance on a teleoperator's skill and on online policy updates.
- **证据**：Across four challenging real-world tasks, using only 2 to 2.5 hours of autonomous data collection, we achieve an average success rate of 96%, compared to the strongest baseline at 55%.
- **局限**：We find that these limitations largely stem from a lack of structure and focus in data collection.

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/Data and Learning Where it Matters for Contact-Rich Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learned policies trained end-to-end on large datasets often remain brittle in high-
precision tasks and struggle with generalization. We find that these limitations largely
stem from a lack of structure and focus in data collection. Our key insight is to
leverage dense data collection only for the critical segment of contact-rich tasks and
to rely on traditional planning during simple free-space motion. We propose an automated
data-collection scheme in combination with offline deep reinforcement learning for the
critical segment of the task, eliminating reliance on a teleoperator's skill and on
online policy updates. Across four challenging real-world tasks, using only 2 to 2.5
hours of autonomous data collection, we achieve an average success rate of 96%, compared
to the strongest baseline at 55%. Notably, performance remains high in out-of-
distribution scenarios where end-to-end approaches struggle. Our results pave the way
for targeted data collection for contact-rich tasks and for high success rates in
precision applications.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15982v1
- Authors: Oliver Hausdörfer, Linus Schwarz, Gabor Marko, Christian Dietz, Timo Class, Luka Hofer, Jim Yun-Jin Li, Johannes Hechtl, Ralf Römer, Angela P. Schoellig
- Published: 2026-07-17T14:18:20Z
- Age days: 2

</details>
