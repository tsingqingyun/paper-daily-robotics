---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13119"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLAs-as-Tools 让高层模型负责安排长任务，让多个专门的 VLA 工具各做一段局部操作。关键是把工具选择、调用指令和执行进度接起来，使规划器能在需要时调整计划。

## 问题

长任务同时要求机器人记住整体顺序、处理失败，又要完成多种精细操作。摘要认为，让一个 VLA 同时承担持续闭环规划和多样动作执行，负担过重；拆成规划器和执行器之后，还必须解决工具是否听懂调用、规划器何时重新介入的问题。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进柜子再关门”；VLM 根据画面安排放杯、关门并调用对应工具，收到执行反馈后继续或重排，最终输出完成整段任务的动作。

## 创新点或方法

旧做法让动作策略承担较多长程决策；本文把场景分析、全局规划和恢复交给 VLM，把有明确范围的子任务交给专门 VLA。训练时，TAPT 构造与工具调用对应的训练单元，并用工具族残差适配器做专门化；单元格式和损失未说明。推理时，高层显式选择工具，工具在执行中反馈进度，以事件触发重新规划，减少持续轮询。巧处在于，拆分职责后又训练执行器适应调用方式。

### 方法如何工作

1. VLM 读取任务和场景，确定当前局部目标，使动作执行有明确范围。
2. 系统显式选择 VLA 工具并传入调用指令，把整体计划变成可执行子任务。
3. 经 TAPT 对齐的工具生成局部动作，使执行尽量符合本次调用。
4. 工具反馈执行进度，高层据事件继续或重新规划，处理长任务中的变化。具体事件条件摘要未说明。

### 必要术语

- VLA 工具：负责有限局部操作的视觉语言动作策略；本文用它承接高层调用。
- TAPT：面向工具调用的后训练；让训练内容与实际调用方式对应。
- 残差适配器：用附加参数调整原模型行为的组件；本文用于高效训练不同工具。
- 事件触发重规划：出现相关执行事件后再更新计划；本文用它减少持续查询。

## 证据

摘要报告：五个仿真基准上，相对 pi05，平均成功率提高 8.9 个百分点，衡量调用忠实度的 Non-biased Rate 提高 15.0 点；三个 Franka 真机任务中，在数据和计算匹配条件下，成功率从 16.7% 升至 58.3%。这些结果支持整套系统在所测任务上更可靠，但摘要未给出各基准结果、试验次数、指标定义及组件消融，不能把收益单独归因于 TAPT 或事件反馈。

## 局限

我会核查进度反馈是否可靠，以及错误反馈如何影响恢复。摘要未说明工具覆盖范围和新操作如何加入，因此现有结果不能直接证明工具越多，系统仍同样好用。

- **判断**：值得读到调用接口和 TAPT 数据构造细节，因为这两处决定职责拆分能否真正落地。

## 研究关联

可借鉴的是把子任务边界设计成执行器能学习、规划器能观察的接口。如果局部动作已有一定能力，而长任务经常败在调用错位或恢复不及时，这种接口值得先试。

### 下一步读哪里

下一步检查调用单元如何标注、工具何时报告事件、Non-biased Rate 如何计算，以及是否分别移除 TAPT、专门化适配器和反馈机制做对照。输入没有正文节选。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Mo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.13119v2 Announce Type: replace Abstract: Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy that distributes this burden across a high-level vision language model (VLM) agent for temporal reasoning and a family of specialized VLA tools for diverse local physical operations. The VLM handles scene analysis, global planning, and recovery, while each VLA tool executes a bounded subtask. To tightly couple agent planning with VLA tool execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes explicit tool selection and in-execution progress feedback, enabling efficient event-triggered agent replanning without continuous agent polling. To obtain diverse specialized VLA tools that faithfully follow agent invocations, we further propose Tool-Aligned Post-Training (TAPT), which constructs invocation-aligned training units for instruction following and adopts tool-family residual adapters for efficient tool specialization. Across five simulated benchmarks, VLAs-as-Tools improves the success rate of pi05 by 8.9 percentage points on average and enhances invocation fidelity by 15.0 points in Non-biased Rate. On three real-world Franka tasks, it improves success rate from 16.7% to 58.3% under matched data and compute. Code will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13119
- Authors: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
