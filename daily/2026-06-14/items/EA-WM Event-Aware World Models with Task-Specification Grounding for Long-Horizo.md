---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13053v1"
published: "2026-06-11T08:35:37Z"
age_days: 2
score: 27
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型"]
---

# EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation

> [!summary] 一句话结论（基于摘要）
> We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification.

## 关键点

- **问题**：Pretrained-feature world models provide a useful substrate for robot imagination, but visual or latent prediction alone does not determine whether an imagined future satisfies task-relevant events.
- **创新点 / 方法**：We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Pretrained-feature world models provide a useful substrate for robot imagination, but visual or latent prediction alone does not determine whether an imagined future satisfies task-relevant events.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/EA-WM Event-Aware World Models with Task-Specification Grounding for Long-Horizo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained-feature world models provide a useful substrate for robot imagination, but
visual or latent prediction alone does not determine whether an imagined future
satisfies task-relevant events. Long-horizon manipulation requires progress signals that
are relational, predicate-level, and physically grounded: whether an object has moved,
whether a drawer or contact state has changed, whether a placement predicate is
satisfied, and whether a candidate future is reliable enough for execution. We introduce
EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics
with task-specification-grounded event prediction and verification. EA-WM rolls out
candidate futures in pretrained visual-feature space, decodes them into structured event
states, and scores them using task-progress, semantic-consistency, physical-feasibility,
and uncertainty terms. The verifier guides sampling-based planning, gates candidate
actions, and, in the contact-sensitive LIBERO wine-rack setting, selects among
PPOgenerated proposals. Across navigation, deformable-object, wall-constrained, and
languagedescribed manipulation studies, EA-WM shows that event-aware verification can
make featurespace world models more interpretable and better aligned with task progress.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13053v1
- Authors: Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng
- Published: 2026-06-11T08:35:37Z
- Age days: 2

</details>
