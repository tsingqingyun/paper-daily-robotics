---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08511v2"
published: "2026-09-08T09:57:32Z"
age_days: 2
score: 25
created: 2026-09-11
concepts: ["机器人学习"]
---

# PGMT: Perceptive General Motion Tracking for Humanoid Robots

> [!summary] 先说人话（基于摘要）
> We present PGMT, a Perceptive General Motion Tracking pipeline for humanoid robots that learns terrain adaptation from independently selected motion references and terrains.

## 这篇到底在做什么

- **卡在哪里**：Humanoid motion trackers can reproduce diverse whole-body motions, but their performance degrades on complex terrain where terrain-agnostic references become physically infeasible.
- **关键解法**：We present PGMT, a Perceptive General Motion Tracking pipeline for humanoid robots that learns terrain adaptation from independently selected motion references and terrains.
- **拿什么证明**：摘要未报告明确实验结论；需阅读全文核查。

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/PGMT Perceptive General Motion Tracking for Humanoid Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid motion trackers can reproduce diverse whole-body motions, but their performance degrades on complex terrain where terrain-agnostic references become physically infeasible. We present PGMT, a Perceptive General Motion Tracking pipeline for humanoid robots that learns terrain adaptation from independently selected motion references and terrains. PGMT first learns a general tracking and recovery prior, then incorporates terrain perception through motion-conditioned terrain glimpses that selectively encode regions relevant to the current motion. Terrain-aware tracking relaxation allows necessary deviations from the reference while preserving its motion intent. Zero-shot deployment on a Unitree G1 demonstrates robust terrain-adaptive locomotion and whole-body motion execution over real-world terrain with obstacles up to 37 cm high, while supporting teleoperation, dynamic motion tracking, and fall recovery. PGMT extends general humanoid motion tracking beyond flat ground, providing a unified policy for terrain-adaptive locomotion, diverse whole-body behaviors, and teleoperation in complex environments. Project homepage: https://luyili.github.io/pgmt/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08511v2
- Authors: Hongyi Li, Li Peizhuo, Yucheng Tao, Ze Wang, Fangzhou Xu, Jinyi Chen, Yanyan Yuan, Dapeng Jia, Yongbin Jin, Mingfeng Fan, Guillaume Sartoretti, Hongtao Wang
- Published: 2026-09-08T09:57:32Z
- Age days: 2

</details>
