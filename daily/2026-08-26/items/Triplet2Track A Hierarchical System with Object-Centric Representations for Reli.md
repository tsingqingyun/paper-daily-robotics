---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.22800v1"
published: "2026-08-24T04:46:25Z"
age_days: 1
score: 33
created: 2026-08-26
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation

> [!summary] 一句话结论（基于摘要）
> Across diverse real-world long-horizon tasks, TTS achieves a 74.8\% average success rate and supports object-level and compositional generalization.

## 关键点

- **问题**：Ensuring reliability in uncertain environments remains difficult for long-horizon robotic manipulation.
- **创新点 / 方法**：To address these issues, we introduce the Triplet-to-Track System (TTS), a closed-loop long-horizon imitation learning system that uses human videos to reduce reliance on robot-collected data.
- **证据**：Across diverse real-world long-horizon tasks, TTS achieves a 74.8\% average success rate and supports object-level and compositional generalization.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Triplet2Track A Hierarchical System with Object-Centric Representations for Reli.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Ensuring reliability in uncertain environments remains difficult for long-horizon robotic manipulation. End-to-end VLA models are data-heavy and opaque, making diagnosis and verification difficult. Hierarchical pipelines are more interpretable, but their plans are often weakly grounded in observations, weakly aligned with low-level actions, and computed without online feedback, leading to open-loop behavior and hallucinations. To address these issues, we introduce the Triplet-to-Track System (TTS), a closed-loop long-horizon imitation learning system that uses human videos to reduce reliance on robot-collected data. TTS represents high-level subgoals as instance-grounded triplets, translates them into continuous track priors for execution, and monitors task progress from observations for online replanning. Across diverse real-world long-horizon tasks, TTS achieves a 74.8\% average success rate and supports object-level and compositional generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.22800v1
- Authors: Jianxiang Liu, Gaojing Zhang, Chuan Wen, Qipeng Liu, Yuxuan Zhao, Ning Guo, Wenzhao Lian
- Published: 2026-08-24T04:46:25Z
- Age days: 1

</details>
