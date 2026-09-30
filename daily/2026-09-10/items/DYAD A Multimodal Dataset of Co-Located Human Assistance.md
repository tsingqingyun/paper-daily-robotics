---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09023v1"
published: "2026-09-08T16:53:15Z"
age_days: 1
score: 24
created: 2026-09-10
concepts: ["多模态基础模型"]
---

# DYAD: A Multimodal Dataset of Co-Located Human Assistance

> [!summary] 先说人话（基于摘要）
> DYAD 记录人类助手什么时候出声、什么时候动手，以及这些帮助如何对应求助、任务状态和结果，让“如何帮人”成为可拆解的学习问题。

## 这篇到底在做什么

- **卡在哪里**：同处一地的具身助手需跟踪任务、识别求助并选择干预方式；既有流程或交互数据没有联合连接请求、触发原因、言语与物理帮助及其结果。
- **关键解法**：同步记录齿轮箱装配中的第一视角与工作区多模态数据，由一名受训助手遵循指导优先策略；标注完整帮助链条，并设置步骤理解、干预前模式预测和回应生成三个参考任务。
- **拿什么证明**：20 场会话包含 528 个步骤区间、611 次执行者请求和 851 条有效帮助记录。829 个可评测模式事件上，最强 RGB 模型四种子平均 macro-F1 为 0.548±0.007，因果元数据为 0.624，特权触发映射为 0.915。

## 值不值得读

- **和你的研究有什么关系**：对多模态基础模型及具身助手研究者，价值是把感知与干预选择连接起来，并揭示干预前 RGB 未恢复的信息。
- **先别急着信**：数据来自单一装配任务和一名助手，参考任务也不是端到端协作；特权信息结果不能视为可部署感知性能。
- **判断**：研究协作助手值得细读标注结构和信息可用性，贡献重点在关系完整性而非规模。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/DYAD A Multimodal Dataset of Co-Located Human Assistance.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

An embodied assistant working beside a person must track task state, recognize help seeking, choose how to intervene, and produce an appropriate response. Existing procedural datasets richly describe individual execution, while interactive datasets capture remote verbal instruction or undifferentiated co-working. They do not jointly link a co-located helper's verbal and physical interventions to performer requests, task state, assistance triggers, and outcomes. We introduce DYAD (DYadic Assistance Dataset), a synchronized multimodal record of human-human assistance during gearbox assembly. Across 20 sessions, one trained helper follows a guidance-first policy while assisting HoloLens 2 wearers. DYAD links 528 task-step intervals and 611 performer requests with 851 valid assistance records spanning verbal and physical help. DYAD's annotations span the assistance process; three reference tasks evaluate selected components rather than an end-to-end system: causal step understanding, pre-onset mode anticipation, and instructor response generation. On 829 eligible mode events, the strongest four-seed RGB mean is 0.548 +/- 0.007 macro-F1; causal metadata reaches 0.624 and a privileged trigger mapping 0.915, revealing information not recovered from pre-onset RGB. DYAD's contribution is not scale, but a linked interaction structure spanning help seeking, intervention choice, execution, and outcome under egocentric and workspace sensing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09023v1
- Authors: Akhil Ajikumar, Mahya Qorbani, Sakib Reza, Sean Andrist, Mohsen Moghaddam
- Published: 2026-09-08T16:53:15Z
- Age days: 1

</details>
