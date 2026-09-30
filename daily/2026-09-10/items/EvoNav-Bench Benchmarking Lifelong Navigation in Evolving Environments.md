---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08292v1"
published: "2026-09-08T06:05:05Z"
age_days: 1
score: 27
created: 2026-09-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# EvoNav-Bench: Benchmarking Lifelong Navigation in Evolving Environments

> [!summary] 先说人话（基于摘要）
> 机器人记住的地图会过时，复用经验反而可能带错路。EvoNav-Bench 在连续导航任务之间改变环境，专门测试智能体能否识别并处理失效记忆。

## 问题

终身导航需要复用此前探索结果以节省重复搜索，但现有方法通常假定环境静止，可能把旧观测与新观测错误融合；现有基准难以暴露这一问题。

## 创新点或方法

基于 ProcTHOR 扩展 GOAT-Bench 式连续导航，在子任务之间修改环境，让历史场景表示部分有效、部分过期，并比较 Frontier-Update、Fail-then-Update 和 Stage-Reset 三种启发式处理策略。

## 证据

评测了三种近期场景表示复用方法及三种启发式策略，报告现有方法在环境变化下表现脆弱。摘要未给出可核查的结果数字。


## 局限

需核查环境修改的类型、幅度及发生频率；这些设定决定基准能代表哪些真实变化。

- **判断**：做长期导航或场景记忆的研究者值得细读任务协议与失败案例，核心价值是补上静态基准遗漏的失效模式。

## 研究关联

对具身智能体和导航评测研究者，价值在于把“记得住”与“知道何时更新”分开检验，可用于测试持久记忆的实际可靠性。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/EvoNav-Bench Benchmarking Lifelong Navigation in Evolving Environments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Lifelong navigation (LN) requires an embodied agent to solve a sequence of navigation subtasks in the same environment. Since solving each subtask from scratch incurs redundant exploration, an LN agent must consolidate experience from earlier stages and reuse it in later stages, often through persistent scene representations such as scene graphs or visual snapshots. However, existing approaches typically assume a stationary environment, whereas in real-world LN settings, human activities can cause the environment to evolve. With the stationary assumption violated, existing methods may fuse outdated prior observations with new observations, yet current benchmarks cannot reveal this failure mode. In this paper, we present EvoNav-Bench, which extends the GOAT-Bench style LN formulation in the context of evolving environments. Built on the ProcTHOR framework, EvoNav-Bench introduces environment modifications between navigation tasks, making prior experience useful but not fully reliable. This design enables controlled evaluation of how environment evolution affects LN agents that reuse prior scene observations. Using EvoNav-Bench, we benchmark three recent methods that build and reuse scene representations for navigation. We also compare three simple heuristic strategies for handling environment evolution: Frontier-Update, Fail-then-Update, and Stage-Reset. Our results show that existing methods are brittle under environment evolution, while the heuristic strategies enable a controlled analysis of how agents can adapt to scene changes and mitigate their impact.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08292v1
- Authors: Xilin Wang, Guoxi Zhang, Hongming Xu, Zhuofan Zhang, Tianxu Wang, Lifeng Fan
- Published: 2026-09-08T06:05:05Z
- Age days: 1

</details>
