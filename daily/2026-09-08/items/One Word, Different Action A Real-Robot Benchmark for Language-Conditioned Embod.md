---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.05260"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-09-08
concepts: ["具身智能评测与基准"]
---

# One Word, Different Action: A Real-Robot Benchmark for Language-Conditioned Embodied Reasoning

> [!summary] 先说人话（基于摘要）
> One Word, Different Action 同时测试机器人是否会被无关措辞带偏，以及任务真正变化时能否改对动作。结果指向更难的问题：把多个约束合成一个可执行决定。

## 这篇到底在做什么

- **卡在哪里**：可靠语言控制既要求任务不变时决策稳定，也要求任务变化时正确响应；孤立的单约束变化不足以检验多条件决策。
- **关键解法**：基于真实机器人的物理决策状态和可执行动作，构造保持任务与改变任务的指令对，联合测量决策不变性、敏感性，并加入多约束推理与真实 RGB 定位。
- **拿什么证明**：现代模型在单约束指令变化上接近饱和，若干模型在多约束组合时明显退化；摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：可帮助具身评测区分语言鲁棒性和真正的任务条件组合能力，避免把简单指令辨别当作成熟操作推理。
- **先别急着信**：需核查决策正确与完整物理执行成功如何关联，以及多约束样本覆盖哪些冲突类型。
- **判断**：值得读指令对构造和错误案例，适合补充现有 VLA 语言条件评测。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/One Word, Different Action A Real-Robot Benchmark for Language-Conditioned Embod.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.05260v1 Announce Type: new Abstract: Natural-language instruction changes can directly alter robot behavior. A reliable embodied system should preserve its action when the task is unchanged and update it correctly when the task itself changes. We introduce One Word, Different Action, a real-robot benchmark built on physical decision states and executable actions, using task-preserving and task-changing instruction pairs to jointly evaluate Decision Invariance and Decision Sensitivity, with further evaluation under multi-constraint reasoning and real-RGB grounding. Experiments show that modern models are near saturation on single-constraint instruction changes, yet several models degrade noticeably when multiple task constraints must be integrated into one executable decision. These results suggest that the more salient remaining challenge is no longer recognizing an isolated instruction change, but reliably composing multiple task requirements into a correct robot action decision.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.05260
- Authors: Yiwei Liu, Luwei Yang, Shunbo Lei
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
