---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21017v1"
published: "2026-07-23T08:02:53Z"
age_days: 0
score: 28
created: 2026-07-24
concepts: ["世界模型", "机器人学习"]
---

# TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation

> [!summary] 一句话结论（基于摘要）
> In this paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the paradigm from imaginative layout generation to deterministic reconstruction from unstructured, in-the-wild image data.

## 关键点

- **问题**：The development of generalizable robotic manipulation policies is inherently bounded by the availability of large-scale, high-fidelity scene data.
- **创新点 / 方法**：In this paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the paradigm from imaginative layout generation to deterministic reconstruction from unstructured, in-the-wild image data.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-24/TableVerse A Large-scale Tabletop Dataset with Real-world Grounded Layouts for G.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The development of generalizable robotic manipulation policies is inherently bounded by
the availability of large-scale, high-fidelity scene data. While recent automated
synthesis methods attempt to bridge this gap via text-to-layout hallucination or
simplified procedural generation, they frequently suffer from physical implausibility
and fail to capture the complex, dense clutter of actual human environments. In this
paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the
paradigm from imaginative layout generation to deterministic reconstruction from
unstructured, in-the-wild image data. Our framework seamlessly processes unscripted
internet media into high-fidelity, simulation-ready tabletop environments with accurate
metric scales, authentic topologies, and verified mechanical stability. Furthermore, an
automated task-conditioned trajectory generation framework is integrated to synthesize
high-quality, collision-free pick-and-place demonstrations. Leveraging this complete
pipeline, we construct the TableVerse-100K Dataset, a large-scale corpus comprising
100,000 unique, physically consistent environments paired with interactive manipulation
trajectories. By capturing diverse asset compositions, realistic spatial distributions,
and high-quality demonstrations, TableVerse-100K establishes a highly scalable and high-
fidelity data foundation, providing significant value to facilitate future research in
generalizable robotic manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21017v1
- Authors: Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
- Published: 2026-07-23T08:02:53Z
- Age days: 0

</details>
