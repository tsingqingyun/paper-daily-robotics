---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13877v1"
published: "2026-06-11T20:01:49Z"
age_days: 3
score: 32
created: 2026-06-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation

> [!summary] 一句话结论（基于摘要）
> In particular, point-cloud observations improve average planning success rates from 20.7% with wrist-view observations and 22.0% with front-view observations to 32.1%.

## 关键点

- **问题**：However, it remains unclear which representation properties fundamentally support stable long-horizon planning in contact-rich settings.
- **创新点 / 方法**：In this paper, we present ContactWorld, a benchmark and systematic empirical study of vision-tactile world models spanning 12 contact-rich manipulation tasks, including insertion, disassembly, screwing, and exploratory interaction.
- **证据**：In particular, point-cloud observations improve average planning success rates from 20.7% with wrist-view observations and 22.0% with front-view observations to 32.1%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich manipulation requires world models to reason over complex contact dynamics
from multimodal sensory observations. However, it remains unclear which representation
properties fundamentally support stable long-horizon planning in contact-rich settings.
In this paper, we present ContactWorld, a benchmark and systematic empirical study of
vision-tactile world models spanning 12 contact-rich manipulation tasks, including
insertion, disassembly, screwing, and exploratory interaction. Across extensive
experiments, we find that representations that are both spatially structured and
temporally continuous consistently achieve the strongest planning performance. In
particular, point-cloud observations improve average planning success rates from 20.7%
with wrist-view observations and 22.0% with front-view observations to 32.1%. We further
find that the effectiveness of tactile sensing depends critically on cross-modal
representation compatibility rather than modality scaling alone. Combining point-cloud
observations with tactile force-field representations, which preserve richer spatial
structure and interaction dynamics, further improves performance to 36.1%, yielding the
strongest overall planning performance across all evaluated tasks. Moreover, tactile
sensing becomes increasingly important under long-horizon planning objectives, where
compounding prediction errors and contact uncertainty accumulate over time. Together,
these findings highlight the importance of representation structure, multimodal
compatibility, and long-horizon robustness in vision-tactile world models for contact-
rich robotic manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13877v1
- Authors: Zhiyuan Zhang, Pokuang Zhou, Kaidi Zhang, Adeesh Desai, Temitope Amosa, Davood Soleymanzadeh, Jiuzhou Lei, Minghui Zheng, Yu She
- Published: 2026-06-11T20:01:49Z
- Age days: 3

</details>
