---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.05324"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 50
created: 2026-09-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?

> [!summary] 先说人话（基于摘要）
> RoboSPA 要测清 VLA 在场景变复杂、步骤变长后究竟卡在哪里。它把空间推理和流程规划分别分级，并用诊断指标补充任务成功率。

## 问题

现有操作数据集与基准主要评估预设条件下能否完成任务，难以辨别空间歧义、执行精度和长期记忆分别造成的失败。

## 创新点或方法

围绕细粒度空间推理与长时程流程规划，设置 10 类、56 个基础任务，每个任务扩展为五档难度，共 280 个变体；覆盖多种机器人形态和场景，并引入超越二元成功率的诊断指标。

## 证据

收集 527K 条轨迹。代表性 VLA 的实验显示，复杂空间关系、精确底层执行和高记忆需求规划仍然困难；摘要未给出模型得分或退化幅度。


## 局限

需核查诊断指标如何定义，以及难度递增是否能分离空间与流程因素，避免将控制失败直接解释为推理不足。

- **判断**：值得重点读任务设计与指标部分；价值在于能否定位能力短板，而非仅扩大测试规模。

## 研究关联

对 VLA 与具身评测研究者，可用于区分推理、控制和记忆瓶颈，帮助判断下一步该改模型哪一部分。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：50
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/RoboSPA Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.05324v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation. However, existing datasets and benchmarks mainly evaluate task completion under predefined settings, offering limited insight into model reasoning under increasing spatial and procedural complexity. We introduce \textbf{RoboSPA} (\textbf{Robo}t \textbf{S}patial-\textbf{P}rocedural \textbf{A}ssessment), a large-scale robotic manipulation dataset and benchmark for diagnosing embodied reasoning in VLA models. \texttt{RoboSPA} focuses on two core dimensions, Fine-Grained Spatial Reasoning and Long-Horizon Procedural Planning, covering 10 task categories and 56 base tasks. Each task is instantiated across five difficulty levels, yielding 280 variants with increasing spatial ambiguity and procedural complexity. We collect 527K trajectories across multiple embodiments and diverse scenes. Beyond binary success rate, \texttt{RoboSPA} introduces diagnostic metrics for more detailed evaluation. Experiments on representative VLA models show that current systems still struggle with complex spatial relations, precise low-level execution, and memory-intensive planning. These results establish \texttt{RoboSPA} as a challenging diagnostic benchmark for developing more capable, reliable, and generalizable embodied agents. Our data and code are available at https://github.com/fanzhenxuan/RoboSPA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.05324
- Authors: Zhenxuan Fan, Bo Zhang, Yutong Lin, Yuqian Yuan, Juekai Lin, Liang Liang, Zhuoyi Huang, Wenqiao Zhang, Juncheng Li, Siliang Tang, Jun Xiao, Yueting Zhuang
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
