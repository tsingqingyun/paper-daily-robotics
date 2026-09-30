---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08511v1"
published: "2026-09-08T09:57:32Z"
age_days: 1
score: 25
created: 2026-09-10
concepts: ["机器人学习"]
---

# PGMT: Perceptive General Motion Tracking for Humanoid Robots

> [!summary] 先说人话（基于摘要）
> PGMT 让人形机器人根据地形适度修改参考动作：保留动作意图，同时避开那些在当前地面上根本做不到的姿势。

## 这篇到底在做什么

- **卡在哪里**：通用全身动作跟踪在复杂地形上退化，因为不考虑地形的参考动作可能物理不可行，继续严格跟踪会与环境约束冲突。
- **关键解法**：先学习通用跟踪与恢复先验，再通过动作条件化的局部地形观测编码当前动作相关区域；地形感知的跟踪放松允许偏离参考。训练中的动作参考与地形独立选取。
- **拿什么证明**：在 Unitree G1 上零样本部署，展示对最高 37 cm 障碍地形的适应，并支持遥操作、动态动作跟踪和跌倒恢复；摘要未报告成功率。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习研究者，价值在于把通用动作先验与地形适应结合，使同一策略覆盖行走、全身动作与遥操作。
- **先别急着信**：需核查 37 cm 障碍的具体形态，以及跟踪偏差与动作意图保留如何度量。
- **判断**：值得重点读地形观测选择与跟踪放松机制，真实部署证据明确，但鲁棒范围仍需全文判断。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/PGMT Perceptive General Motion Tracking for Humanoid Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid motion trackers can reproduce diverse whole-body motions, but their performance degrades on complex terrain where terrain-agnostic references become physically infeasible. We present PGMT, a Perceptive General Motion Tracking pipeline for humanoid robots that learns terrain adaptation from independently selected motion references and terrains. PGMT first learns a general tracking and recovery prior, then incorporates terrain perception through motion-conditioned terrain glimpses that selectively encode regions relevant to the current motion. Terrain-aware tracking relaxation allows necessary deviations from the reference while preserving its motion intent. Zero-shot deployment on a Unitree G1 demonstrates robust terrain-adaptive locomotion and whole-body motion execution over real-world terrain with obstacles up to 37 cm high, while supporting teleoperation, dynamic motion tracking, and fall recovery. PGMT extends general humanoid motion tracking beyond flat ground, providing a unified policy for terrain-adaptive locomotion, diverse whole-body behaviors, and teleoperation in complex environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08511v1
- Authors: Hongyi Li, Li Peizhuo, Yucheng Tao, Ze Wang, Fangzhou Xu, Jinyi Chen, Yanyan Yuan, Dapeng Jia, Yongbin Jin, Mingfeng Fan, Guillaume Sartoretti, Hongtao Wang
- Published: 2026-09-08T09:57:32Z
- Age days: 1

</details>
