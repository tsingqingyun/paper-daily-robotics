---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10724"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-09-13
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Finishing the Task Is Not Enough: Evaluating Agent Resilience and Considerate Participation under Accumulating Challenge

> [!summary] 先说人话（基于摘要）
> 这篇把Agent评测从一次任务是否完成，扩展到困难不断累积时能否保住进度、合理求助并照顾协作中的人。它通过模拟医疗工作流观察行动与自我报告如何变化。

## 问题

持续部署中，技术故障、人员依赖和流程中断会叠加。孤立任务成功率无法反映Agent恢复工作、沟通限制和遵守角色边界的能力。

## 创新点或方法

提出操作韧性与体谅式参与两个评价维度，在不同挑战强度下对照文本行动计划、提示诱导的内部评估，以及结构化工作负荷和情绪报告，分析长期适应方式。

## 证据

研究覆盖两个模型、12项利益相关者参与制定的任务和120条模拟医疗轨迹。挑战增加时，Agent更依赖人类，结构化报告中的负荷与负面情绪上升，但文本回应很少表达压力；适应范围也扩展到角色调整和更广协调。


## 局限

证据来自模拟轨迹和模型生成的报告；报告的“负荷”“情绪”不能直接视为真实内部状态，向物理具身任务迁移也需验证。

- **判断**：值得读评测维度和部署困境，适合补充长期Agent评价，不宜作为机器人执行能力证据。

## 研究关联

对Agent和具身评测研究者，它提供了持续协作场景下的评价维度，提示任务进展、升级求助和对人的影响应同时被观察。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/Finishing the Task Is Not Enough Evaluating Agent Resilience and Considerate Par.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.10724v1 Announce Type: new Abstract: Sustained deployment of generative AI agents requires more than isolated task success. Agents must remain useful across repeated interactions, changing conditions, and dependencies on people within shared workflows, especially as technical, human, and operational disruptions accumulate over time. We propose operational resilience and considerate participation as two complementary aspects of evaluating such agents: the former captures how agents recover from blocked work while preserving progress and communicating their limits, and the latter captures how their adaptation accounts for affected people, role boundaries, and the surrounding workflow. Yet both remain underexplored under accumulating challenge. We study 120 simulated healthcare trajectories across two generative AI models and twelve stakeholder-derived tasks under light, medium, and heavy challenge. We compare textual action plans, prompted internal assessments, and quantitative structured workload and affect reports to examine how agent behavior and reported state change as challenge accumulates. Regarding operational resilience, agents shift from self-directed recovery toward greater human dependence, while reporting increasing workload and negative affect in structured reports but seldom expressing strain in textual responses. Regarding considerate participation, agents broaden from task-focused adaptation toward task reframing, attention to others, role-boundary adjustment, and wider coordination, with distinct patterns across actions and internal assessments. From these findings, we derive five deployment dilemmas involving persistence, attention, role boundaries, state disclosure, and escalation that require stakeholder specification, further informing technical implications for learning, situated evaluation, and embodied adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10724
- Authors: Yuanchen Bai, Zijian Ding, Angelique Taylor
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
