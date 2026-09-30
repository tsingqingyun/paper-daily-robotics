---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2602.14048"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-09-05
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ProAct: Harnessing Streaming Motion Generation and Agentic Reasoning for Real-Time Embodied Social Interaction

> [!summary] 先说人话（基于摘要）
> ProAct 用快慢双系统兼顾实时动作流与主动社交推理：慢速认知系统决定何时介入，低延迟行为系统把高层意图持续转成非语言动作。

## 这篇到底在做什么

- **卡在哪里**：具身社交机器人既要连续生成流畅多模态行为，又要利用长期对话和视觉历史判断何时主动发起互动；复杂推理和严格延迟预算互相冲突，过度主动与反应迟缓都不可接受。
- **关键解法**：认知系统借助高效记忆与用户动机预测进行长程推理，输出主动意图；行为系统以意图条件的流式 flow matching 运动生成器和解耦 ControlNet 分支产生连续非语言行为，从而避免慢推理阻断动作流。
- **拿什么证明**：摘要称系统部署于实体人形机器人，并通过真实用户研究、运动生成基准及新建 ProActBench 评估主动触发与克制；未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对具身 Agent 和多模态交互研究，它展示了如何用异步快慢系统拆分实时控制与长上下文决策，ProActBench 也把“该不该主动”纳入明确评测。
- **先别急着信**：没有数字说明延迟、动作质量、触发准确性或用户偏好，双系统协调是否真正优于统一模型必须查全文。
- **判断**：概念和系统架构值得读，尤其适合社交机器人研究者；若关心效果强度，应先核查用户研究与延迟数据。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/ProAct Harnessing Streaming Motion Generation and Agentic Reasoning for Real-Tim.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2602.14048v2 Announce Type: replace Abstract: Real-time embodied social interaction places two equally demanding requirements on an agent: continuously generating fluent multimodal interaction behavior, and proactively reasoning over accumulated dialogue and visual context to decide when to take initiative. These requirements must both be satisfied under a strict latency budget, making them difficult to meet simultaneously. We present ProAct, a dual-system framework that manages these time-critical requirements by integrating a low-latency Behavioral System for streaming multimodal interaction with a slower Cognitive System that performs long-horizon social reasoning and produces high-level proactive intentions. The Cognitive System incorporates an efficient memory mechanism and a user-motivation prediction module to reason over accumulated dialogue and visual context and determine when proactive intervention is appropriate. The Behavioral System further includes an intention-conditioned streaming flow-matching motion generator with a disentangled ControlNet branch, which translates deliberative intentions into continuous non-verbal behavior without disrupting interaction fluency. We deploy ProAct on a physical humanoid robot and validate the framework through comprehensive experiments, including real-world user studies, motion-generation benchmarks, and evaluation on ProActBench, a new, targeted benchmark for evaluating proactive trigger detection and restraint in embodied interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2602.14048
- Authors: Zeyi Zhang, Zixi Kang, Ruijie Zhao, Yusen Feng, Biao Jiang, Hanyu Ji, Libin Liu
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
