---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19850v1"
published: "2026-07-22T07:35:35Z"
age_days: 2
score: 24
created: 2026-07-25
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation

> [!summary] 一句话结论（基于摘要）
> Experiments on the SNEI and MUSON benchmarks demonstrate that SOPD consistently outperforms supervised fine-tuning, off-policy distillation, and standard on-policy distillation baselines in action prediction, perception consistency, and reasoning consistency.

## 关键点

- **问题**：However, large scale VLMs are difficult to deploy on resource-constrained robotic platforms, while lightweight VLMs often lack sufficient social reasoning capability.
- **创新点 / 方法**：To address this problem, we propose SOPD-SocialNav, a selective on-policy distillation (SOPD) method that transfers social navigation knowledge from a large teacher VLM to a lightweight student VLM.
- **证据**：Experiments on the SNEI and MUSON benchmarks demonstrate that SOPD consistently outperforms supervised fine-tuning, off-policy distillation, and standard on-policy distillation baselines in action prediction, perception consistency, and reasoning consistency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language models have shown strong potential for social robot navigation by
leveraging rich semantic understanding of complex environments and human behaviors.
However, large scale VLMs are difficult to deploy on resource-constrained robotic
platforms, while lightweight VLMs often lack sufficient social reasoning capability. To
address this problem, we propose SOPD-SocialNav, a selective on-policy distillation
(SOPD) method that transfers social navigation knowledge from a large teacher VLM to a
lightweight student VLM. SOPD introduces an entropy-based token selection mechanism that
uses teacher uncertainty to identify socially informative decision tokens, while
suppressing gradients from low-entropy tokens corresponding to trivial navigation
states. A temperature-controlled Jensen-Shannon divergence objective is then used to
align the student and teacher distributions on the selected tokens. Experiments on the
SNEI and MUSON benchmarks demonstrate that SOPD consistently outperforms supervised
fine-tuning, off-policy distillation, and standard on-policy distillation baselines in
action prediction, perception consistency, and reasoning consistency. Real-world
deployment on a Scout Mini robot further shows that the distilled model can generate
more socially appropriate navigation behaviors in conversational and queuing scenarios.
These results suggest that SOPD is an effective strategy for building lightweight yet
socially aware VLM-based navigation systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19850v1
- Authors: Xinyu Zhang, Zishuo Wang, Ling Xiao
- Published: 2026-07-22T07:35:35Z
- Age days: 2

</details>
