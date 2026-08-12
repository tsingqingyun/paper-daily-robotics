---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09853v1"
published: "2026-08-10T17:09:37Z"
age_days: 0
score: 35
created: 2026-08-11
concepts: ["多模态基础模型", "机器人学习"]
---

# RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

> [!summary] 一句话结论（基于摘要）
> We introduce RynnValue, an open-source value foundation model for robotic manipulation that replaces these anchors with temporal distance, the directed cost-to-go from an observation to the language-specified goal.

## 关键点

- **问题**：General-purpose reward models are increasingly the bottleneck for scaling robot learning, yet the recipe for learning value-related capabilities from large-scale heterogeneous corpora remains underexplored.
- **创新点 / 方法**：We introduce RynnValue, an open-source value foundation model for robotic manipulation that replaces these anchors with temporal distance, the directed cost-to-go from an observation to the language-specified goal.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/RynnValue Scaling Robotic Value Foundation Models with Temporal Distance.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose reward models are increasingly the bottleneck for scaling robot
learning, yet the recipe for learning value-related capabilities from large-scale
heterogeneous corpora remains underexplored. Existing approaches tie supervision to
task-internal anchors such as preferences or normalized progress, none of which transfer
cleanly across embodiments and data sources. We introduce RynnValue, an open-source
value foundation model for robotic manipulation that replaces these anchors with
temporal distance, the directed cost-to-go from an observation to the language-specified
goal. Because temporal-distance labels can be derived directly from timestamps,
RynnValue scales to over 7,000 hours and roughly 3M instruction-conditioned clips
without preference or progress annotations. To make temporal-value learning reliable at
scale, we combine random temporal sampling, temporal-order shuffling, and value-
isolation attention, suppressing shortcuts that would leave predictions insensitive to
failures and regressions. Trained without preference labels, RynnValue attains an
average Kendall's tau_a of 0.675 on RBM-EVAL-OOD, surpassing the fully preference-
supervised state of the art (0.655) and more than doubling a progress-only counterpart
(0.292), while generalizing zero-shot to unseen tasks, embodiments, and viewpoints.
Converted into dense rewards via potential-based shaping, it raises real-world policy
success from 52.5% to 72.5% online and from 63.8% to 82.5% offline. These results
establish temporal distance as a scalable supervision target and practical reward
interface for generalist robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09853v1
- Authors: Dongchi Huang, Hongyin Zhang, Bohan Hou, Siteng Huang, Zhian Su, Hang Guo, Tong Lu, Zhaofeng Xu, Jiahao Tang, Jianfei Yang, Donglin Wang, Peixi Peng, Mingxiu Chen, Deli Zhao, Xin Li
- Published: 2026-08-10T17:09:37Z
- Age days: 0

</details>
