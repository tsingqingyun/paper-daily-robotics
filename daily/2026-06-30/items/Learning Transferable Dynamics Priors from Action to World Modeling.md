---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29501v1"
published: "2026-06-28T17:01:55Z"
age_days: 1
score: 32
created: 2026-06-30
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning Transferable Dynamics Priors from Action to World Modeling

> [!summary] 一句话结论（基于摘要）
> By pretraining a model to predict how actions drive visual scene evolution, the resulting world model captures reusable interaction dynamics beyond appearance-level video generation.

## 关键点

- **问题**：We study action-conditioned world modeling as a scalable way to learn transferable dynamics priors for robot learning.
- **创新点 / 方法**：By pretraining a model to predict how actions drive visual scene evolution, the resulting world model captures reusable interaction dynamics beyond appearance-level video generation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/Learning Transferable Dynamics Priors from Action to World Modeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We study action-conditioned world modeling as a scalable way to learn transferable
dynamics priors for robot learning. By pretraining a model to predict how actions drive
visual scene evolution, the resulting world model captures reusable interaction dynamics
beyond appearance-level video generation. Concretely, we pretrain a multi-view
interactive base diffusion world model, A2World, on large-scale robot manipulation data
with real action annotations. We validate the learned dynamics priors from two
complementary perspectives. First, we adapt A2World into a task- or scene-specialized
real-world simulator, A2World-sim, whose long-horizon rollouts support simulator-based
policy evaluation and scalable what-if analysis by replacing real-robot rollouts with
world model rollouts. Second, starting from the same pretrained weights, we adapt
A2World into a video-action joint prediction model, A2World-policy, that predicts
actions under visual and instruction conditioning. Experiments across simulation
benchmarks and real-robot settings demonstrate that action-conditioned world model
pretraining yields transferable dynamics priors that benefit both simulator-centric and
policy-centric robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29501v1
- Authors: Ze Huang, Jiahui Zhang, Hairuo Liu, Chenxi Zhang, Ran Cheng, Li Zhang
- Published: 2026-06-28T17:01:55Z
- Age days: 1

</details>
