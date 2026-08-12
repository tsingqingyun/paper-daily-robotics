---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.12160v1"
published: "2026-05-12T14:10:54Z"
age_days: 1
score: 31
created: 2026-05-14
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete

> [!summary] 一句话结论（基于摘要）
> On the LIBERO benchmark suite, Premover reduces mean wall-clock time from 34.0 to 29.4 seconds, a 13.6% reduction, while matching the full-prompt baseline's success rate (95.1% vs.

## 关键点

- **问题**：In real deployment, however, users take several seconds to enter a request, leaving the policy idle for a substantial fraction of the interaction.
- **创新点 / 方法**：We introduce Premover, a lightweight module that converts this idle window into useful precomputation.
- **证据**：On the LIBERO benchmark suite, Premover reduces mean wall-clock time from 34.0 to 29.4 seconds, a 13.6% reduction, while matching the full-prompt baseline's success rate (95.1% vs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/Premover Fast Vision-Language-Action Control by Acting Before Instructions Are C.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies are typically evaluated as if the user had
finished typing or speaking before the robot begins acting. In real deployment, however,
users take several seconds to enter a request, leaving the policy idle for a substantial
fraction of the interaction. We introduce Premover, a lightweight module that converts
this idle window into useful precomputation. Premover keeps the VLA backbone frozen and
attaches two small projection heads, one for image patches, one for language tokens,
that map an intermediate layer of the backbone into a shared space. The resulting focus
map is supervised by simulator-rendered target-object segmentation masks and applied as
a per-patch reweighting of the next step's image tokens. A single scalar readiness
threshold, trained jointly from streaming prefixes, decides when the policy should begin
acting. On the LIBERO benchmark suite, Premover reduces mean wall-clock time from 34.0
to 29.4 seconds, a 13.6% reduction, while matching the full-prompt baseline's success
rate (95.1% vs. 95.0%); naive premoving, by contrast, collapses to 66.4%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.12160v1
- Authors: Joonha Park, Jiseung Jeong, Taesik Gong
- Published: 2026-05-12T14:10:54Z
- Age days: 1

</details>
