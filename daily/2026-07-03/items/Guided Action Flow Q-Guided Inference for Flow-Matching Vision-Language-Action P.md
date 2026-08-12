---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.02092v1"
published: "2026-07-02T12:30:50Z"
age_days: 0
score: 32
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies

> [!summary] 一句话结论（基于摘要）
> A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another.

## 关键点

- **问题**：The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling.
- **创新点 / 方法**：Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy.
- **证据**：A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/Guided Action Flow Q-Guided Inference for Flow-Matching Vision-Language-Action P.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-matching vision-language-action policies generate robot action chunks through an
iterative transport process, creating an opportunity for test-time guidance without
retraining the base policy. We study this opportunity in Guided Action Flow, an
inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a
learned action-chunk critic to guide its reverse-time flow sampler. The critic is
trained from real success and failure rollouts, can condition on task-description
features from the frozen SmolVLA language pathway, and is used only through action
gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A
single-task critic improves success from 68.0% to 82.0% on one seed window and from
82.0% to 86.0% on another. A multi-family task-description critic improves validation
success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest,
from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for
frozen flow-matching VLA policies, while showing that critic generalization and
uncertainty-aware guidance remain the central bottlenecks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.02092v1
- Authors: Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang
- Published: 2026-07-02T12:30:50Z
- Age days: 0

</details>
