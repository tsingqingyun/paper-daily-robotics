---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09298v1"
published: "2026-08-10T08:48:06Z"
age_days: 0
score: 38
created: 2026-08-11
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation

> [!summary] 一句话结论（基于摘要）
> To operationalize this contract, we introduce WorldSimProbe, comprising five controlled suites spanning local control sensitivity, global trajectory variation, source-diverse actions, interaction grounding, and dynamics.

## 关键点

- **问题**：Yet their applicability remains difficult to establish because prevailing evaluations emphasize visual quality, task outcomes, or coarse rollout-level responsiveness without directly testing simulator fidelity.
- **创新点 / 方法**：To operationalize this contract, we introduce WorldSimProbe, comprising five controlled suites spanning local control sensitivity, global trajectory variation, source-diverse actions, interaction grounding, and dynamics.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action-conditioned world models (ACWMs) promise to provide embodied AI with scalable
predictive simulators for planning, policy evaluation, and data generation. Realizing
this promise requires precise action-conditioned transitions rather than merely
plausible outputs. Yet their applicability remains difficult to establish because
prevailing evaluations emphasize visual quality, task outcomes, or coarse rollout-level
responsiveness without directly testing simulator fidelity. To address this gap, we
evaluate ACWMs through the observable capabilities expected of physical simulators.
Accordingly, we formalize Observable Simulator Contract, a minimal contract that any
action-conditioned physical simulator should satisfy: supplied actions must induce
corresponding agent motion, and environment responses must be grounded in that realized
motion. To operationalize this contract, we introduce WorldSimProbe, comprising five
controlled suites spanning local control sensitivity, global trajectory variation,
source-diverse actions, interaction grounding, and dynamics. Suite-specific evaluators
assess simulator-relative calibration, dense action-to-motion correspondence, false-
interaction grounding, and primitive-level dynamics. We evaluate six open-source ACWMs
on more than 18,000 instances across RoboTwin, ManiSkill, and LIBERO. World-SimProbe
reveals systematic action-realization degradation across control variation, structured
failures in interaction grounding and dynamics, and benchmark signals consistent with
human judgments and downstream outcomes. Together, this capability-based framework
provides a transparent, and standardized paradigm for diagnosing ACWM simulator fidelity
beyond coarse, task-directed evaluation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09298v1
- Authors: Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo, Yijie Xu, Sixiang Chen, Zhongxia Zhao, Zihao Wang, DaFeng Chi, Peidong Liu, YuTong Chen, Henghua Liu, Zhihao Yuan, Huizhu Jia, Yuzheng Zhuang, Tianle Zhang, Liang Lin, Huajie Tan, Shanghang Zhang
- Published: 2026-08-10T08:48:06Z
- Age days: 0

</details>
