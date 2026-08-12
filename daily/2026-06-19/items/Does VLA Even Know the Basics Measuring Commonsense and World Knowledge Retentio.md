---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19297v1"
published: "2026-06-17T17:20:46Z"
age_days: 1
score: 42
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds.

## 关键点

- **问题**：Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control.
- **创新点 / 方法**：We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action.
- **证据**：Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-19/Does VLA Even Know the Basics Measuring Commonsense and World Knowledge Retentio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning
powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and
factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks
are ambiguous, conflating missing knowledge with poor generalization of low-level
control. We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge
benchmarks to VLA evaluation by requiring agents to answer through action. Each question
becomes a short tabletop episode where the agent performs a single object-placement
action to select among candidate answers, yielding an action-grounded success rate with
reduced control confounds. We curate a test suite of such environments across diverse
commonsense and world-knowledge categories and introduce layerwise intent probing to
localize answer-relevant information across the VLM backbone and action head. In a
large-scale study of 7 VLA models and 9 VLM baselines, we systematically rank models
across categories, finding that VLAs show solid performance on simple concepts while
exhibiting larger gaps on richer semantic categories relative to their source VLMs, that
VQA co-training is associated with better knowledge retention, and that answer-relevant
signals peak in middle VLA layers but attenuate in upper layers. Act2Answer is available
at https://tttonyalpha.github.io/act2answer/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19297v1
- Authors: Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin, Nikita Kurlaev, Daria Pugacheva, Albina Burlova, Mikhail Kolosov, Denis Shepelev, Andrey Kuznetsov, Elena Tutubalina, Aleksandr I. Panov, Alexey K. Kovalev, Vlad Shakhuro
- Published: 2026-06-17T17:20:46Z
- Age days: 1

</details>
