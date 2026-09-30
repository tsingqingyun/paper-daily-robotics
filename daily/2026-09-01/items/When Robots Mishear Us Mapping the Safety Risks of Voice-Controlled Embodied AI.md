---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28518v1"
published: "2026-08-28T16:55:32Z"
age_days: 3
score: 30
created: 2026-09-01
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI

> [!summary] 先说人话（基于摘要）
> 该论文把语音识别错误注入 SafeAgentBench 和 POEX，发现机器人可能因转写歧义而接受、规划甚至执行有害指令，自动纠错只能缓解部分风险。

## 问题

语音控制具身 AI 的安全链条通常把 ASR 输出当成可靠文本，但识别错误可能保留句式却增加有害歧义，或削弱模型拒绝行为，使上层安全评测高估实际语音系统的安全性。

## 创新点或方法

输入是模拟不同 ASR 错误后的安全基准指令，作用对象是具身模型的接受、拒绝、计划和执行行为；研究比较错误类型及自动纠错影响。区别于纯文本安全测试，它显式评估语音转写噪声穿透到实体行动的风险。

## 证据

摘要明确称部分错误增加有害歧义，部分会削弱拒绝并允许不安全计划生成和执行；自动纠错有时降低风险但并非始终有效。摘要未给出风险增幅、模型数或具体错误率。


## 局限

模拟 ASR 错误能否代表真实噪声、口音和设备条件，以及“执行”处于何种环境，摘要无法确认。

- **判断**：做语音机器人安全者应精读攻击构造和失败样例；它更像重要风险地图，而不是已经完备的防御方案。

## 研究关联

对具身 Agent 和评测研究者，它说明安全边界必须覆盖语音前端到动作执行的整条管线，并把 ASR 扰动纳入红队与拒绝率测试。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/When Robots Mishear Us Mapping the Safety Risks of Voice-Controlled Embodied AI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We investigate whether automatic speech recognition (ASR) errors in user input can lead to unsafe outputs from Embodied AI (EAI) models. We find that ASR errors can lead to harmful instructions being accepted and executed by EAI models, thereby reducing safety. We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX) to evaluate how different errors affect embodied AI safety. We find that some of them preserve semantic structure but increase harmful ambiguity, while others weaken the model refusal behaviour and allow unsafe plans to be generated and executed. We show that in some cases automatic correction of ASR errors can reduce the risk, but this is not always effective. Overall, we show that ASR errors lead to significant safety risks for embodied AI.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28518v1
- Authors: Sihan Jia, Oliver Lemon
- Published: 2026-08-28T16:55:32Z
- Age days: 3

</details>
