---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12616v1"
published: "2026-06-10T19:16:31Z"
age_days: 2
score: 31
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation

> [!summary] 一句话结论（基于摘要）
> On Bench2Drive, PersonaDrive (no style) improves the driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning attains the highest driving score in every style within a roughly 2% band (its weakest style surpassing the strongest b…

## 关键点

- **问题**：Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode.
- **创新点 / 方法**：We introduce PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on retrieved demonstrations from a style-instructed human driving dataset, in which participants drive CARLA leaderboard routes under aggressive, neutral, and conservative instructions on a driver-in-the-loop rig.
- **证据**：On Bench2Drive, PersonaDrive (no style) improves the driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning attains the highest driving score in every style within a roughly 2% band (its weakest style surpassing the strongest baseline, DMW, by 5.4%), while average speed and acceleration…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Closed-loop driving simulators typically populate their environments with non-ego
traffic agents that behave largely the same way, produced either by rule-based traffic
managers or by learned models trained toward a single behavioral mode. Recent work
introduces style variation through post-hoc labels on observational data or LLM-inferred
reward weights, but these signals act as proxies for what a style should reward rather
than demonstrations of humans explicitly asked to drive in that style. We introduce
PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on
retrieved demonstrations from a style-instructed human driving dataset, in which
participants drive CARLA leaderboard routes under aggressive, neutral, and conservative
instructions on a driver-in-the-loop rig. The pipeline has three stages: (i) offline
triplet mining over per-style human driving data using a combined image-text similarity
score; (ii) training a lightweight retrieval head that fuses frozen visual features with
a small control encoder over per-style databases; and (iii) fine-tuning a single VLA
backbone to treat retrieved context points as in-context behavioral demonstrations
during waypoint prediction. At inference, the same backbone is conditioned on any style
by swapping which per-style database the retrieval head queries, so selecting a style
requires no per-style retraining while enabling human-style, style-diverse non-ego
agents for closed-loop simulation. On Bench2Drive, PersonaDrive (no style) improves the
driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning
attains the highest driving score in every style within a roughly 2% band (its weakest
style surpassing the strongest baseline, DMW, by 5.4%), while average speed and
acceleration rise by 18% and 25% from the conservative to the aggressive instruction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12616v1
- Authors: Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki
- Published: 2026-06-10T19:16:31Z
- Age days: 2

</details>
