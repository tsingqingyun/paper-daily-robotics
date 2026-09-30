---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11561v1"
published: "2026-09-10T13:52:51Z"
age_days: 1
score: 28
created: 2026-09-12
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Memory as Plans: World-Action Modeling with Memory-Grounded Planning

> [!summary] 先说人话（基于摘要）
> MaP-WAM把历史记忆先压成当前执行计划，避免动作模型每一步都重读全部过去。执行器同时预测动作和进度，以决定何时切换子任务。

## 问题

长程任务依赖当前画面之外的信息；语言摘要可能丢失视觉细节，持续扩大的视觉历史窗口又会拖累执行效率。

## 创新点或方法

把已完成片段保存为语言指令与稀疏视觉记录，规划器据此生成下一片段的语言计划和视觉引导；WAP模型联合预测动作块与执行进度，通过计划—观测对齐校准切换时机，并更新闭环上下文。

## 证据

摘要报告RMBench成功率83.3%、达到最先进表现，真实机器人任务成功率78.0%；随着历史增长，执行器推理延迟保持近似恒定。


## 局限

恒定延迟针对执行器；需核查规划阶段开销、片段边界错误和视觉记忆压缩对完整闭环的影响。

- **判断**：值得精读记忆表示、进度校准和延迟测量，与2AM对照尤其有助于理解记忆接口设计。

## 研究关联

为Agent、VLA和世界—动作模型研究者提供了长期记忆与固定执行上下文兼容的方案，进度预测也连接了规划与实际完成状态。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Memory as Plans World-Action Modeling with Memory-Grounded Planning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Mainstream robotic policies often adopt a Markovian formulation, but many complex real-world manipulation tasks are inherently non-Markovian, requiring long-horizon memory beyond the current observation. Existing memory mechanisms often rely on language summaries, growing visual windows, or their combinations, and may therefore lose fine-grained visual evidence or face a trade-off between history coverage and execution efficiency. We introduce MaP-WAM, a Memory-as-Plans framework that decomposes memory-dependent world-action modeling into memory-grounded planning and plan-conditioned execution, and uses long-term multimodal episodic context as planning-time evidence rather than repeatedly conditioning the executor on the full history. MaP-WAM represents memory as completed segment records containing language instructions and sparse visual context, and converts this episodic memory into compact plans comprising the next segment-level language plan and corresponding visual guidance. A World-Action-Progress (WAP) model executes each plan over an unknown duration by jointly predicting action chunks and corresponding execution progress at inference time, calibrating predicted progress through plan-observation alignment for adaptive segment transitions and closed-loop context updates. MaP-WAM keeps the executor context length fixed, while structured attention further enables key-value caching in both planning and execution. MaP-WAM achieves state-of-the-art performance on RMBench with an 83.3% success rate and attains 78.0% success on real-robot tasks, while maintaining approximately constant executor inference latency as task history grows.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11561v1
- Authors: Sizhe Zhao, Haozhe Xie, Weiyu Zhao, Chenchu Zhang, Huan Wang, Chenyang Wang, Qinglin Liu, Shengping Zhang
- Published: 2026-09-10T13:52:51Z
- Age days: 1

</details>
