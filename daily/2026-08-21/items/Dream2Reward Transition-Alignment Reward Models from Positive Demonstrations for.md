---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18787v1"
published: "2026-08-19T10:44:20Z"
age_days: 1
score: 26
created: 2026-08-21
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> These results show that comparing realized motion with predicted successful change provides an effective way to convert positive demonstrations into dense rewards for robot learning.

## 关键点

- **问题**：Learning robotic policies requires dense rewards that remain informative when behavior departs from successful demonstrations.
- **创新点 / 方法**：We introduce Dream2Reward, which learns a language-conditioned successful latent transition field from positive demonstrations.
- **证据**：These results show that comparing realized motion with predicted successful change provides an effective way to convert positive demonstrations into dense rewards for robot learning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Dream2Reward Transition-Alignment Reward Models from Positive Demonstrations for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning robotic policies requires dense rewards that remain informative when behavior departs from successful demonstrations. Progress-based rewards estimate how far an observation has advanced along a nominal successful trajectory, but may remain high after an incorrect transition. We introduce Dream2Reward, which learns a language-conditioned successful latent transition field from positive demonstrations. Given the visual history up to a transition start, the model predicts the latent displacement associated with successful execution and scores the observed displacement through signed directional and symmetric magnitude agreement. This transition-level comparison penalizes wrong-direction, overshooting, and stagnant motion even when the resulting observation appears to show progress. Dream2Reward requires no failure annotations, progress labels, or synthetic negatives, and produces a dense causal reward. Across mechanism diagnostics and shared-trajectory evaluations, it provides stronger success-failure separation and more informative feedback on low-quality behavior than progress-based alternatives. Across online and offline policy learning, the same frozen reward model reduces reward hacking and supports stronger downstream performance, including in real-robot manipulation. These results show that comparing realized motion with predicted successful change provides an effective way to convert positive demonstrations into dense rewards for robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18787v1
- Authors: Haoyu Zhang, Zecui Zeng, Bin Wang, Lusong Li, Liang Lin, Long Cheng
- Published: 2026-08-19T10:44:20Z
- Age days: 1

</details>
