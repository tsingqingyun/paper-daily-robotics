---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14514v1"
published: "2026-07-16T03:11:37Z"
age_days: 1
score: 30
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# VTM-Nav: Hierarchical Visual-Topological Memory for Cross-Episode Object-Goal Navigation

> [!summary] 一句话结论（基于摘要）
> \method{} achieves the best performance across all three benchmarks, demonstrating the effectiveness and robustness of structured visual-topological experience reuse across datasets.

## 关键点

- **问题**：Object-goal navigation requires an embodied agent to locate and reach an instance of a specified object category in an indoor environment.
- **创新点 / 方法**：We introduce Cross-Episode Object-Goal Navigation, in which an agent repeatedly operates in the same scene, retains only self-acquired experience, and keeps its model parameters fixed.
- **证据**：\method{} achieves the best performance across all three benchmarks, demonstrating the effectiveness and robustness of structured visual-topological experience reuse across datasets.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object-goal navigation requires an embodied agent to locate and reach an instance of a
specified object category in an indoor environment. Recent training-free approaches
leverage vision-language models (VLMs) for open-vocabulary semantic reasoning, but are
typically evaluated under an episodic protocol that resets all scene-specific state
after each episode. We introduce Cross-Episode Object-Goal Navigation, in which an agent
repeatedly operates in the same scene, retains only self-acquired experience, and keeps
its model parameters fixed. To support experience reuse, we present \method, a training-
free VLM navigation framework with a persistent hierarchical Visual-Topological Memory
(VTM). The VTM organizes scene knowledge at room and object levels and retrieves
relevant experience through coarse-to-fine matching, providing memory as soft guidance
only when it agrees with current observations. A conservative execution guard further
mitigates oscillations, blocked motions, and premature stopping. Under a controlled
same-scene protocol, we evaluate \method{} on three benchmarks, HM3D v0.1, HM3D v0.2,
and MP3D, and compare it with a strengthened WMNav baseline augmented with cross-episode
textual memory, while keeping the VLM backbone and action pipeline identical. \method{}
achieves the best performance across all three benchmarks, demonstrating the
effectiveness and robustness of structured visual-topological experience reuse across
datasets.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14514v1
- Authors: Xiaoran Xu, Yupeng Wu, Tianyu Xue, Yifan Xu, Xuanran Dong, Xiaoshan Yang, Changsheng Xu
- Published: 2026-07-16T03:11:37Z
- Age days: 1

</details>
