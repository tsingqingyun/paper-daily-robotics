---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16476v1"
published: "2026-08-17T12:15:59Z"
age_days: 1
score: 28
created: 2026-08-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Exposing the Long-tail in Embodied Urban Navigation via Scalable Learning from In-the-Wild Videos

> [!summary] 一句话结论（基于摘要）
> To address these challenges, we present a scalable framework for learning point-goal urban navigation from web-scale in-the-wild egocentric videos while systematically exposing its long tail.

## 关键点

- **问题**：Learning embodied urban navigation policies from real-world data is constrained by the cost of task-specific data collection and the limited coverage of rare yet safety-critical scenarios.
- **创新点 / 方法**：To address these challenges, we present a scalable framework for learning point-goal urban navigation from web-scale in-the-wild egocentric videos while systematically exposing its long tail.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Exposing the Long-tail in Embodied Urban Navigation via Scalable Learning from I.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning embodied urban navigation policies from real-world data is constrained by the cost of task-specific data collection and the limited coverage of rare yet safety-critical scenarios. To address these challenges, we present a scalable framework for learning point-goal urban navigation from web-scale in-the-wild egocentric videos while systematically exposing its long tail. The framework automatically annotates uncurated web videos with metric trajectories and structured navigation semantics, which are then used to train a vision-language-action policy for interpretable navigation planning. We characterize the long tail based on model performance and the distribution of perception-motion patterns, and employ reflection-based analysis to diagnose recurring failure modes. Experiments on web-video data and real-world urban navigation tasks demonstrate effective knowledge transfer from unconstrained videos and reveal coherent long-tail structures beyond aggregate navigation performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16476v1
- Authors: Bingyi Xia, Han Bao, Zhewei Chen, Hanjing Ye, Jingwen Yu, Yuhan Pang, Wenjun Xu, Jiankun Wang
- Published: 2026-08-17T12:15:59Z
- Age days: 1

</details>
