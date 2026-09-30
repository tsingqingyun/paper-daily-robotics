---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27797v1"
published: "2026-08-28T00:25:48Z"
age_days: 3
score: 22
created: 2026-08-31
concepts: ["智能体 Agent"]
---

# CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action

> [!summary] 先说人话（基于摘要）
> CEDAR 把语言技能和持续约束都编译为确定有限自动机，再通过自动机求交组合行为，使“夜间睡觉”“留在某生物群系”等约束由控制器结构保证，而不是反复提示 LLM。

## 这篇到底在做什么

- **卡在哪里**：语言任务通常含随世界变化仍需持续满足的约束；LLM 生成的自由程序虽看似合理，却缺少稳定、可验证、可组合和能根据失败轨迹修复的形式对象。
- **关键解法**：CEDAR 以环境事件轨迹为字母表，把指令落到正规语言；LLM 提供语义判断，执行反例用于纠错，技能和规范均表示为 DFA。通过自动机求交生成满足组合约束的控制器，并可复用已学习技能。
- **拿什么证明**：在 Minecraft、与程序生成基线使用相同模拟器和 API 观测的条件下，CEDAR 能保持基线无法持续满足的时间与空间约束，并通过复用技能减少累计 LLM 查询；摘要未给具体成功率或查询数。

## 值不值得读

- **和你的研究有什么关系**：对具身 Agent，这是把语言语义接到可验证执行层的轻量方案，尤其适合有限事件抽象下的长程约束组合、反例修复和技能复用。
- **先别急着信**：正规语言只能表达有限状态约束；最需核查自然语言到事件和 DFA 的落地错误，以及环境连续性被离散化后遗漏了什么。
- **判断**：值得形式方法与智能体交叉研究者精读；接口思想清晰，但保证只对正确落地且可由 DFA 表达的规范成立。

## 研究关联

- **概念**：[[智能体 Agent]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/CEDAR Automata as Verifiable Interfaces for Language-Guided Embodied Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Natural-language tasking of embodied agents is rarely just goal specification: users also impose constraints that must persist while the world changes. Code-generating LLM agents can produce plausible behaviors for such instructions, but their free-form programs provide no stable object to verify, compose with new constraints, or repair from a failing trace. We present CEDAR, a counterexample-guided framework that grounds instructions as regular languages over environment event traces. CEDAR uses a language model for semantic judgments and execution traces for correction, then represents both skills and specifications as deterministic finite automata. This turns constraints into executable finite-state objects: a learned skill can be intersected with a learned sleep at night or stay in this biome specification, yielding a controller that enforces the learned constraint by construction rather than by repeated prompting. In Minecraft, with the same simulator/API observations available to a program-generating baseline, CEDAR maintains temporal and spatial constraints that the baseline fails to preserve and amortizes reuse of learned skills, reducing cumulative LLM queries. These results suggest that regular languages offer a practical verification layer between natural-language instructions and embodied-agent policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27797v1
- Authors: Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi
- Published: 2026-08-28T00:25:48Z
- Age days: 3

</details>
