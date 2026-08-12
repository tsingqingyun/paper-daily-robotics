---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01925v1"
published: "2026-07-02T09:21:17Z"
age_days: 3
score: 24
created: 2026-07-06
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# SPLC: Social Preference Learning for Crowd Robot Navigation

> [!summary] 一句话结论（基于摘要）
> This paper proposes a Social Preference Learning for Crowd Robot Navigation (SPLC) algorithm to eliminate the need for detailed reward design.

## 关键点

- **问题**：However, the inherent complexity of pedestrian motion renders the design of effective reward functions for promoting socially compliant robot behaviors a persistent challenge.
- **创新点 / 方法**：This paper proposes a Social Preference Learning for Crowd Robot Navigation (SPLC) algorithm to eliminate the need for detailed reward design.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/SPLC Social Preference Learning for Crowd Robot Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Offline reinforcement learning (RL) holds significant potential for crowd robot
navigation in human-robot coexistence applications. However, the inherent complexity of
pedestrian motion renders the design of effective reward functions for promoting
socially compliant robot behaviors a persistent challenge. This paper proposes a Social
Preference Learning for Crowd Robot Navigation (SPLC) algorithm to eliminate the need
for detailed reward design. Its core innovation lies in the introduction of a social
preference feedback mechanism to automatically generate preference data through
principled preference evaluation criteria. By explicitly accounting for the intricacies
of pedestrian dynamics, the pipeline mitigates the reward bias and facilitates the
systematic quantification of broad social norms, thereby fostering socially compliant
behaviors. Extensive experiments integrating SPLC with offline RL methods demonstrate
consistent improvements over state-of-the-art baselines across standard performance
metrics. Furthermore, real-world experiments on the TurtleBot4 further validate the
effectiveness of SPLC in practical human-robot coexistence settings. Our code and video
demos are available at https://github.com/sklus949/SPLC.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01925v1
- Authors: Zixuan Chen, Hao Fu, Haiwen Hu, Shiquan Zheng
- Published: 2026-07-02T09:21:17Z
- Age days: 3

</details>
