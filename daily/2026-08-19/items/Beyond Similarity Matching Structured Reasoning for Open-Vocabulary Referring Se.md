---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16103v1"
published: "2026-08-17T04:48:02Z"
age_days: 1
score: 28
created: 2026-08-19
concepts: ["具身智能评测与基准"]
---

# Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS

> [!summary] 一句话结论（基于摘要）
> It achieves 47.2 Avg.

## 关键点

- **问题**：Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions.
- **创新点 / 方法**：We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection.
- **证据**：It achieves 47.2 Avg.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/Beyond Similarity Matching Structured Reasoning for Open-Vocabulary Referring Se.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection. QAGaussian first learns query-conditioned multi-scale Gaussian slots as differentiable candidates whose receptive fields are shaped by the input expression. It then builds a relation-aware slot graph with language-conditioned edge weighting to propagate target-reference, attribute, part-whole, and contextual evidence. A granularity-adaptive router softly combines region-level, object-level, part-level, attribute-aware, and relation-aware mask branches, followed by relation-constrained refinement for spatial, part-whole, attribute, and geometric consistency. QAGaussian is pretrained only on Mosaic3D-5.6M for Gaussian-text alignment and evaluated on independent benchmarks without target-dataset fine-tuning. It achieves 47.2 Avg. mIoU and 63.2 Avg. F1, outperforming the strongest 3DGS referring baseline by 2.7 mIoU points and 2.9 F1 points. It also improves Part-mIoU from 38.6 to 43.4, Rel-mIoU from 44.4 to 50.8, and reduces target-reference confusion from 10.8 to 7.4. These results demonstrate that query-conditioned slot learning, relation-aware graph reasoning, and adaptive routing provide an effective neural modeling strategy for open-vocabulary referring segmentation in 3DGS. The code is available at https://github.com/zqeslwyz/QAGaussian.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16103v1
- Authors: Yizhao Wang, Xinfa Wang, Jingbo Wang, Jingbo Wang, Guantao Zhang, Yafeng Han, Guohong Gao, Yuhe Xia
- Published: 2026-08-17T04:48:02Z
- Age days: 1

</details>
