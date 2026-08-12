---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23617v1"
published: "2026-06-22T17:12:50Z"
age_days: 2
score: 31
created: 2026-06-25
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations.

## 关键点

- **问题**：However, we also find that fine-tuning only on actively-collected recovery data leads to catastrophic forgetting.
- **创新点 / 方法**：In this paper, we propose an active, continual learning paradigm for VLAs.
- **证据**：We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/RECALL Recovery Experience Collection for Active Lifelong Learning in Vision-Lan.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation
learning, where additional demonstrations are collected for tasks where the policy
performs poorly. This approach incurs several downsides: it requires the robot to fail
before data collection is triggered, provides little guidance about which states require
supervision, and wastes demonstrator effort on redundant parts of the task where the
policy already performs well. In this paper, we propose an active, continual learning
paradigm for VLAs. We demonstrate that active, uncertainty-guided data collection leads
to more efficient fine-tuning than when using passively-collected demonstrations.
However, we also find that fine-tuning only on actively-collected recovery data leads to
catastrophic forgetting. We evaluate techniques for continual learning, including
replay-based data mixing and elastic weight consolidation, and identify tradeoffs
between plasticity to uncertainty-guided recovery data and retention of previously
learned behaviors. Overall, our work contributes an empirical study of active continual
learning for autoregressive VLAs, establishing that uncertainty-guided recovery
demonstrations can improve adaptation efficiency while also revealing open challenges
when targeted new data is incorporated into large robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23617v1
- Authors: Ulas Berk Karli, Tesca Fitzgerald
- Published: 2026-06-22T17:12:50Z
- Age days: 2

</details>
