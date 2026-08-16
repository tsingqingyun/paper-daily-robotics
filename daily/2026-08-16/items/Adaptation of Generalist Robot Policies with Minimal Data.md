---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11363v1"
published: "2026-08-11T19:15:26Z"
age_days: 4
score: 26
created: 2026-08-16
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Adaptation of Generalist Robot Policies with Minimal Data

> [!summary] 一句话结论（基于摘要）
> Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction.

## 关键点

- **问题**：Yet fully autonomous learning remains difficult with current policies: sparse rewards and weak zero-shot exploration make it unlikely that a robot will discover successful behavior from scratch.
- **创新点 / 方法**：We build MiDAS, a simple offline-to-online RL recipe that first anchors a pre-trained VLA to the target task with behavior cloning on single/few demonstrations, then improves it through value-based online RL on a residual policy parameterization.
- **证据**：Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Adaptation of Generalist Robot Policies with Minimal Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A central goal in robot learning is to move beyond task-specific human data collection toward robots that improve through autonomous interaction. Yet fully autonomous learning remains difficult with current policies: sparse rewards and weak zero-shot exploration make it unlikely that a robot will discover successful behavior from scratch. We study minimal-data adaptation, a regime in which a pre-trained robot policy must learn a new task from as little as one demonstration followed by autonomous online interaction. This setting serves as the closest tractable proxy for fully autonomous improvement, allowing us to study whether minimal human guidance can bootstrap autonomous learning and what algorithmic ingredients make it feasible. We build MiDAS, a simple offline-to-online RL recipe that first anchors a pre-trained VLA to the target task with behavior cloning on single/few demonstrations, then improves it through value-based online RL on a residual policy parameterization. Across LIBERO and RoboCasa, MiDAS recovers strong task performance from as little as one demonstration, substantially outperforming baselines and generalizing beyond demonstrated conditions. We further evaluate MiDAS on a bimanual YAM platform. Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction. To the best of our knowledge, this is the first demonstration of reliable robot policy adaptation from a single task demonstration.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11363v1
- Authors: Shreyas Kowshik, Sreyas Venkataraman, Leo Wang, Niharika Pant, Max Simchowitz, Aviral Kumar
- Published: 2026-08-11T19:15:26Z
- Age days: 4

</details>
