---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17633v2"
published: "2026-08-18T10:53:50Z"
age_days: 2
score: 28
created: 2026-08-21
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects

> [!summary] 一句话结论（基于摘要）
> Under a unified evaluation protocol on Replica, OVIP-SG outperforms ConceptGraphs by 6.31 points in class-mean accuracy (mAcc) and 5.15 points in frequency-weighted mIoU (F-mIoU) while achieving a class-agnostic native-instance Panoptic Quality (PQ) of 0.398.

## 关键点

- **问题**：Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a queried object is absent, hindering robust embodied open-world navigation and exploration.
- **创新点 / 方法**：We present OVIP-SG, a unified framework for instance-preserving semantic mapping, functional scene partitioning, and language-guided small, fine-grained object retrieval.
- **证据**：Under a unified evaluation protocol on Replica, OVIP-SG outperforms ConceptGraphs by 6.31 points in class-mean accuracy (mAcc) and 5.15 points in frequency-weighted mIoU (F-mIoU) while achieving a class-agnostic native-instance Panoptic Quality (PQ) of 0.398.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/OVIP-SG Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retriev.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a queried object is absent, hindering robust embodied open-world navigation and exploration. We present OVIP-SG, a unified framework for instance-preserving semantic mapping, functional scene partitioning, and language-guided small, fine-grained object retrieval. OVIP-SG uses a vision-language model (VLM) to enumerate scene-specific categories for robust open-world detection. Symmetric 3D Intersection over Union (IoU) association and area-weighted feature fusion preserve small independent instances, while VLM-inferred object functions partition scenes into compact functional search regions. A four-stage cascaded retrieval pipeline further incorporates voxel voting and determines target absence from exploration coverage. Under a unified evaluation protocol on Replica, OVIP-SG outperforms ConceptGraphs by 6.31 points in class-mean accuracy (mAcc) and 5.15 points in frequency-weighted mIoU (F-mIoU) while achieving a class-agnostic native-instance Panoptic Quality (PQ) of 0.398. It reduces the search area to 21.8% of the indoor floor space and reaches 0.773 balanced accuracy for object-presence classification. Real-world robotic experiments further demonstrate its practical effectiveness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17633v2
- Authors: Tianjing Hao, Haiyu Lan, Angsong Li, Cheng Chen, Enyu Li, Jiarui Yang, Yuning Su, Peiwen Lin, Wang Chuang
- Published: 2026-08-18T10:53:50Z
- Age days: 2

</details>
