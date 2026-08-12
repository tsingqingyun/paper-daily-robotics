---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19695v1"
published: "2026-07-22T02:53:46Z"
age_days: 2
score: 35
created: 2026-07-24
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation

> [!summary] 一句话结论（基于摘要）
> We introduce NavVerse, a physics-enabled benchmark for indoor-to-outdoor embodied navigation.

## 关键点

- **问题**：Existing benchmarks usually evaluate indoor and outdoor navigation separately, and many abstract away robot execution, leaving exit finding, boundary traversal, adaptation, and kinodynamic failures underexplored.
- **创新点 / 方法**：We introduce NavVerse, a physics-enabled benchmark for indoor-to-outdoor embodied navigation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots deployed in delivery, campus, and emergency-response settings often need to
navigate from buildings to streets within a single continuous episode. Existing
benchmarks usually evaluate indoor and outdoor navigation separately, and many abstract
away robot execution, leaving exit finding, boundary traversal, adaptation, and
kinodynamic failures underexplored. We introduce NavVerse, a physics-enabled benchmark
for indoor-to-outdoor embodied navigation. NavVerse contains 100 indoor scenes, 50 urban
outdoor scenes, and 50 indoor-to-outdoor scenes, and 10,000 episodes spanning Object
Navigation, Vision-and-Language Navigation, and Place Navigation tasks, where agents
search for semantic points of interest such as restaurants or banks. Agents are
evaluated through executable robot interfaces using task-success, path-efficiency, and
safety metrics. Zero-shot experiments with RL, VLA, and modular baselines show that
current agents remain far from solving cross-context navigation: end-to-end VLAs obtain
the highest zero-shot success, while the modular method provides the strongest safety
profile. PlaceNav further reveals a clear drop from outdoor to indoor-to-outdoor scenes,
indicating that adaptation remains major bottleneck.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19695v1
- Authors: Junzhe Wu, Yue Hu, Zeyu Han, Po-Hsun Chang, Yinan Dong, Behrad Rabiei, Maani Ghaffari
- Published: 2026-07-22T02:53:46Z
- Age days: 2

</details>
