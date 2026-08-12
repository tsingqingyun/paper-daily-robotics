---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.25371v1"
published: "2026-05-25T02:52:34Z"
age_days: 1
score: 32
created: 2026-05-26
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# FOUND-IT: Foundation-model-first Task-driven 3D Scene Graphs with Granularity on Demand

> [!summary] 一句话结论（基于摘要）
> In addition to achieving 79% higher accuracy on the ASHiTA SG3D task grounding benchmark, we demonstrate FOUND-IT runs in real-time on a ground robot using a Jetson Thor.

## 关键点

- **问题**：However, in a major departure from related work, we consider the realistic case where the list of tasks is not predefined and fixed, but evolves as the robot operates.
- **创新点 / 方法**：We present the first approach to build hierarchical task-driven 3D scene graphs of arbitrary indoor or outdoor environments using an uncalibrated monocular camera in real- time.
- **证据**：In addition to achieving 79% higher accuracy on the ASHiTA SG3D task grounding benchmark, we demonstrate FOUND-IT runs in real-time on a ground robot using a Jetson Thor.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present the first approach to build hierarchical task-driven 3D scene graphs of
arbitrary indoor or outdoor environments using an uncalibrated monocular camera in real-
time. We leverage geometric foundation models to estimate geometric attributes of the
scene graph (e.g., object bounding boxes), but we also observe that traversability
information (the "places" layer of a scene graph) can be directly reconstructed by
adding an extra head to existing geometric foundation models, like VGGT. Our approach is
task-driven in the sense that we adjust the granularity of the objects and regions in
the map depending on the task; for instance, during a manipulation task, our approach is
able to resolve small knobs on a stove, while during a navigation task it can focus on
large objects (e.g., the entire stove). However, in a major departure from related work,
we consider the realistic case where the list of tasks is not predefined and fixed, but
evolves as the robot operates. This naturally allows dealing with complex loco-
manipulation tasks, where the robot can dynamically adjust its representation as the
task unfolds. We dub the resulting approach FOUND-IT. FOUND-IT also includes an agentic
approach to query information in the scene graph. In addition to achieving 79% higher
accuracy on the ASHiTA SG3D task grounding benchmark, we demonstrate FOUND-IT runs in
real-time on a ground robot using a Jetson Thor. Furthermore, to highlight the
robustness of our method, we demonstrate constructing 3D scene graphs on casually
captured realtor apartment tours from YouTube. Code will be made available upon
publication.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.25371v1
- Authors: Dominic Maggio, Nicolas Gorlo, Luca Carlone
- Published: 2026-05-25T02:52:34Z
- Age days: 1

</details>
