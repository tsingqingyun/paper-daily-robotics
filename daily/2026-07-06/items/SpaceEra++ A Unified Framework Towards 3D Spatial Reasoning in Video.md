---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01784v1"
published: "2026-07-02T06:56:29Z"
age_days: 4
score: 23
created: 2026-07-06
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SpaceEra++: A Unified Framework Towards 3D Spatial Reasoning in Video

> [!summary] 一句话结论（基于摘要）
> In addition, to enhance spatial reasoning, we develop SpaceAlign, which enforces pairwise object constraints by jointly exploiting absolute coordinates and relative spatial relations, thereby aligning optimization with spatial accuracy.

## 关键点

- **问题**：However, pre-trained vision-language models (VLMs) remain constrained by spatial uncertainty stemming from inherently 2D observations and by the scarcity of data for 3D spatial understanding.
- **创新点 / 方法**：To address these limitations, we proposed a novel framework, SpaceEra, in the NeurIPS 2025 Spotlight paper.
- **证据**：In addition, to enhance spatial reasoning, we develop SpaceAlign, which enforces pairwise object constraints by jointly exploiting absolute coordinates and relative spatial relations, thereby aligning optimization with spatial accuracy.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-06/SpaceEra++ A Unified Framework Towards 3D Spatial Reasoning in Video.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual-spatial understanding, defined as the ability to infer object relationships and
scene layouts from visual inputs, is fundamental to downstream tasks such as robotic
navigation and embodied interaction. However, pre-trained vision-language models (VLMs)
remain constrained by spatial uncertainty stemming from inherently 2D observations and
by the scarcity of data for 3D spatial understanding. To address these limitations, we
proposed a novel framework, SpaceEra, in the NeurIPS 2025 Spotlight paper. Although it
achieved significant performance gains, we further observed that its effectiveness is
hindered by insufficient input from scanning videos and weak reasoning constraints. To
tackle these newly emerged challenges, we extend the original framework into a
comprehensive system, termed SpaceEra++, which spans data construction, model design,
training optimization, and prompting inference. Specifically, to alleviate input
insufficiency, we introduce ScenePick, a frame sampling strategy that balances spatial
coverage with object semantics to produce compact yet comprehensive scene
representations. In addition, to enhance spatial reasoning, we develop SpaceAlign, which
enforces pairwise object constraints by jointly exploiting absolute coordinates and
relative spatial relations, thereby aligning optimization with spatial accuracy.
Extensive experiments across multiple benchmarks demonstrate consistent improvements
over strong baselines, while ablation studies validate both the individual and joint
contributions of each component, and further analyses provide guidance for future
research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01784v1
- Authors: Weili Guan, Haoyu Zhang, Meng Liu, Qianlong Xiang, Yaowei Wang, Liqiang Nie
- Published: 2026-07-02T06:56:29Z
- Age days: 4

</details>
