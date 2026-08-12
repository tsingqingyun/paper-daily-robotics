---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17463v1"
published: "2026-06-16T03:25:34Z"
age_days: 1
score: 32
created: 2026-06-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal even…

## 关键点

- **问题**：Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed.
- **创新点 / 方法**：The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation,
yet they remain brittle precisely where each stage depends on what was just completed.
The core issue is structural: short-window VLAs lack an explicit channel for rouxting
information across sub-task boundaries, and existing memory-augmented variants either
write at every frame, retrieve from demonstration-time stages, or fire at sub-goal
events without performing an explicit sub-task-to-sub-task hand-off into the action
expert. We identify the sub-goal completion event as the natural temporal unit for
cross-subtask memory hand-off, and present WeaveLA (Weave Latent memory for Vision-
Language-Action policies), a cross-subtask memory interface that, on top of a frozen VLA
backbone, compresses each completed segment into latent tokens via query-driven
attention pooling and routes them directly into the action-generation path of the next
sub-task. This event-triggered, action-side design preserves the base policy's short-
window interface while adding a lightweight cross-subtask channel. Through stratified
evaluation on RoboMME with a $π_{0.5}$ backbone, WeaveLA's gains land exactly where the
channel is needed: on the hardest repetition slice (SwingXtimes, $N{=}3$), success rises
from $0\%$ to $47.8\%$, while single-execution episodes remain unchanged. Per-episode
paired analysis confirms the gains are confined to tasks whose causal structure requires
cross-subtask information.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17463v1
- Authors: Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue, Guiliang Liu, Simo Wu, Xiangyang Xue, Taiping Zeng
- Published: 2026-06-16T03:25:34Z
- Age days: 1

</details>
