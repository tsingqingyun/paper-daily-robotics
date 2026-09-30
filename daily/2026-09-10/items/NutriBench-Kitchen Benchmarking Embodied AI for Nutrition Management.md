---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07135v1"
published: "2026-09-07T07:34:33Z"
age_days: 2
score: 27
created: 2026-09-10
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# NutriBench-Kitchen: Benchmarking Embodied AI for Nutrition Management

> [!summary] 先说人话（基于摘要）
> 厨房助手不仅要认出食材，还要记住食材何时加入、状态如何变化，并据此回答和规划。NutriBench-Kitchen 测试这条能力链，Nutri-Vgent 用分工明确的记忆帮助模型跟踪过程。

## 问题

动态厨房中的营养管理需要持续更新食物状态并结合菜谱知识决策；静态食物理解和烹饪动作基准没有测量这种持续状态使用能力。

## 创新点或方法

从烹饪视频构建五类问答任务，覆盖食材进入、记忆管理、菜谱查询及长短期规划；Nutri-Vgent 分设情节、食物状态和菜谱记忆。

## 证据

基准含 160 段视频、1,500 个人工核验问答。闭源与开源 VLM 均明显落后于人类，尤其在数量估计、长期跟踪和多约束推理上；Nutri-Vgent 持续改善表现，但摘要未报告增益数字。


## 局限

证据来自视频问答，不能直接推出机器人闭环操作能力；需核查规划题如何验证状态依赖。

- **判断**：值得细读任务标注与记忆设计，尤其适合做长视频智能体；应保留视频推理与实际执行之间的界限。

## 研究关联

适合多模态智能体研究者检验结构化记忆是否帮助长期状态推理，也为具身评测提供超越动作完成率的任务维度。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/NutriBench-Kitchen Benchmarking Embodied AI for Nutrition Management.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

An embodied kitchen assistant must do more than recognize food in isolated frames. It must track ingredient states over time and integrate visual observations with recipe and nutritional knowledge to support constraint-aware decision-making. We formalize this capability as \emph{Embodied Nutrition Management}: perceiving nutrition-relevant events, maintaining a persistent food state, and using it for knowledge-grounded planning. Existing benchmarks evaluate static food understanding or embodied cooking actions, but do not measure whether an agent can continuously update and use nutrition-relevant states in dynamic kitchens. To fill this gap, we introduce \textbf{NutriBench-Kitchen}, a benchmark containing 1,500 manually verified question--answer pairs from 160 cooking videos. It covers five task families: Ingredient Entry, Memory Management, Recipe Query, Long-Term Planning, and Short-Term Planning, spanning food-state construction, maintenance, knowledge retrieval, and decision-making across different planning horizons. Evaluations of proprietary and open-source large vision-language models reveal a substantial gap from human performance, particularly in quantitative ingredient estimation, long-term state tracking, and reasoning under interacting constraints. We further introduce \textbf{Nutri-Vgent}, a diagnostic long-video agent with separate episodic, food-state, and recipe memories. Its consistent improvements demonstrate the value of explicit state representations and structured memory for nutrition management. Together, NutriBench-Kitchen and Nutri-Vgent provide a testbed for studying persistent state tracking and knowledge-grounded reasoning in dynamic kitchens. Code is available at https://github.com/V1ol1n/NutriBench-Kitchen.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07135v1
- Authors: Yulin Wei, Xiangchen Wang, Jianhui Pan, Jinyu Xiao, Zheng Tan, Ruozai Tian, Guanhua Chen, Feng Zheng
- Published: 2026-09-07T07:34:33Z
- Age days: 2

</details>
