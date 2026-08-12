---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.29267v1"
published: "2026-06-28T08:32:35Z"
age_days: 2
score: 31
created: 2026-06-30
concepts: ["多模态基础模型"]
---

# Enhancing Part-Level Point Grounding for Any Open-Source MLLMs

> [!summary] 一句话结论（基于摘要）
> Experiments show that our design consistently improves part-level grounding accuracy across datasets and can be seamlessly integrated into any open-source MLLMs.

## 关键点

- **问题**：While recent Multimodal Large Language Models (MLLMs) have demonstrated promising capabilities in this domain, they primarily excel at object-level grounding and often struggle with part-level grounding-an essential requirement for fine-grained tasks such as robotic manipulation.
- **创新点 / 方法**：In this work, we introduce a general approach that equips any open-source MLLMs with accurate 2D part-level point grounding, offering a more direct alternative to conventional grounding representations.
- **证据**：Experiments show that our design consistently improves part-level grounding accuracy across datasets and can be seamlessly integrated into any open-source MLLMs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/Enhancing Part-Level Point Grounding for Any Open-Source MLLMs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual grounding aims to associate free-form textual queries with specific regions in an
image. While recent Multimodal Large Language Models (MLLMs) have demonstrated promising
capabilities in this domain, they primarily excel at object-level grounding and often
struggle with part-level grounding-an essential requirement for fine-grained tasks such
as robotic manipulation. In this work, we introduce a general approach that equips any
open-source MLLMs with accurate 2D part-level point grounding, offering a more direct
alternative to conventional grounding representations. Our method leverages the
attention mechanisms inherently present in MLLMs. By synthesizing text-conditioned,
grounding-aware queries within intermediate layers via the proposed Q-Synth Module, we
capture target-relevant attention patterns and refine them with a lightweight Attention-
to-Point Decoder, which converts these patterns into a point-centric heatmap for final
prediction. Notably, all original MLLM parameters are frozen, ensuring full preservation
of their pre-trained capabilities. Experiments show that our design consistently
improves part-level grounding accuracy across datasets and can be seamlessly integrated
into any open-source MLLMs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.29267v1
- Authors: Jin-Cheng Jhang, Fu-En Wang, Xin Yang, Nan Qiao, Lu Xia, Min Sun, Cheng-Hao Kuo
- Published: 2026-06-28T08:32:35Z
- Age days: 2

</details>
