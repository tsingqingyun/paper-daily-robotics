---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.13245v1"
published: "2026-07-14T20:14:50Z"
age_days: 2
score: 29
created: 2026-07-17
concepts: ["智能体 Agent"]
---

# Just-In-Time Scene Graph Growth: Combating Perceptual Saturation in Long-Horizon Robotics

> [!summary] 一句话结论（基于摘要）
> To resolve this, we present JITOMA (Just-In- Time On-demand Memory Activation), a closed-loop framework that unifies task reasoning, perception, and memory into a just-in-time growth process.

## 关键点

- **问题**：While 3D Scene Graphs (3DSGs) provide crucial structured representations for embodied agents, conventional Ahead-of-Time, build-everything-then-filter pipelines conflict with the real-time, low-latency demands of edge platforms, inducing a perceptual saturation effect via severe observation redundancy.
- **创新点 / 方法**：To resolve this, we present JITOMA (Just-In- Time On-demand Memory Activation), a closed-loop framework that unifies task reasoning, perception, and memory into a just-in-time growth process.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Just-In-Time Scene Graph Growth Combating Perceptual Saturation in Long-Horizon.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While 3D Scene Graphs (3DSGs) provide crucial structured representations for embodied
agents, conventional Ahead-of-Time, build-everything-then-filter pipelines conflict with
the real-time, low-latency demands of edge platforms, inducing a perceptual saturation
effect via severe observation redundancy. To resolve this, we present JITOMA (Just-In-
Time On-demand Memory Activation), a closed-loop framework that unifies task reasoning,
perception, and memory into a just-in-time growth process. Instead of exhaustively
mapping the entire environment, JITOMA leverages a top-down task heatmap at the frontend
to filter continuous observations, routing minimal streams to maintain a global
foundation of low-cost, dormant anchors. Upon a cognitive query, the backend Large
Language Model (LLM) parses the robotic intent to dynamically awaken task-relevant
anchors, triggering resource-intensive operations -- such as dense node captioning and
functional inference -- exclusively within the activated local subgraph. To evaluate
these dynamic capabilities and study perceptual saturation trade-offs, we introduce
JITOMA-Bench, a comprehensive suite for long-horizon multi-tasking and complex multi-
step reasoning. Extensive experiments demonstrate that JITOMA substantially reduces
active graph size and captioning latency, while maintaining stable processing time under
long-horizon task switching.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.13245v1
- Authors: Yue Chang, Rufeng Chen, Yifan Tian, Dazhi Huang, Zhaofan Zhang, Yi Chen, Wenze Zhang, Li Chen, Hui Xiong, Sihong Xie
- Published: 2026-07-14T20:14:50Z
- Age days: 2

</details>
