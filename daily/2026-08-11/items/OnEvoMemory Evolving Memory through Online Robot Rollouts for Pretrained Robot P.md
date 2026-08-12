---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.08749v1"
published: "2026-08-09T14:53:19Z"
age_days: 1
score: 30
created: 2026-08-11
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies

> [!summary] 一句话结论（基于摘要）
> Experiments on long-horizon manipulation benchmarks show that OnEvoMemory improves the performance of the base VLA policy through both offline initialization and online memory evolution.

## 关键点

- **问题**：However, existing memory mechanisms heavily rely on external models or predefined update rules.
- **创新点 / 方法**：To address this, we propose OnEvoMemory, a value-guided memory module for pretrained robot policies.
- **证据**：Experiments on long-horizon manipulation benchmarks show that OnEvoMemory improves the performance of the base VLA policy through both offline initialization and online memory evolution.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/OnEvoMemory Evolving Memory through Online Robot Rollouts for Pretrained Robot P.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robot manipulation requires policies to track completed subtasks and
critical interaction events. However, existing memory mechanisms heavily rely on
external models or predefined update rules. To address this, we propose OnEvoMemory, a
value-guided memory module for pretrained robot policies. It maintains recent context,
high-value experiences, and salient transitions, while learning which experiences should
be retained from trajectory outcomes. Offline demonstrations initialize the memory
prior, whereas successful and unsuccessful online rollouts refine memory selection,
helping the policy recognize task-stage transitions and avoid repeating completed
subtasks. Experiments on long-horizon manipulation benchmarks show that OnEvoMemory
improves the performance of the base VLA policy through both offline initialization and
online memory evolution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.08749v1
- Authors: Zhongxi Chen, Shenqi Zong
- Published: 2026-08-09T14:53:19Z
- Age days: 1

</details>
