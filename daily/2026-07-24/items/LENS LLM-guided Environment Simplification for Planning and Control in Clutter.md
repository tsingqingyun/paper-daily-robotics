---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.19633v1"
published: "2026-07-22T00:05:00Z"
age_days: 2
score: 30
created: 2026-07-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# LENS: LLM-guided Environment Simplification for Planning and Control in Clutter

> [!summary] 一句话结论（基于摘要）
> In our experiments, we show that LENS improves classical planning, model-based control, and a vision-language-action model, across a diverse set of highly cluttered manipulation scenes.

## 关键点

- **问题**：Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging to handle for today's prevalent approaches.
- **创新点 / 方法**：The problem scales in complexity due to more objects and collisions, more unpredictable contact physics, distractors, and task ambiguity.
- **证据**：In our experiments, we show that LENS improves classical planning, model-based control, and a vision-language-action model, across a diverse set of highly cluttered manipulation scenes.
- **局限**：Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging to handle for today's prevalent approaches.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite recent advances in general-purpose robotic manipulation, real-world multi-object
clutter remains challenging to handle for today's prevalent approaches. The problem
scales in complexity due to more objects and collisions, more unpredictable contact
physics, distractors, and task ambiguity. Bridging this gap to real-world deployment
requires effective scene abstractions; yet today, producing such abstractions requires
extensive task-specific manual engineering, which does not scale. These abstractions are
costly to generate and difficult to adjust or fine-tune. We instead propose a plug-and-
play fix to automatically generate scene-specific, task-specific, adaptively updating
abstractions on top of existing planning and control stacks. LLM-guided Environment
Simplification (LENS) produces a de-cluttered abstracted scene representation by merging
(e.g., stacked objects) or pruning (e.g., distant objects) scene entities in a closed
loop in response to task progress. These dynamic, task-relevant abstractions are
versatile and easy to use. In our experiments, we show that LENS improves classical
planning, model-based control, and a vision-language-action model, across a diverse set
of highly cluttered manipulation scenes. Project website: https://lens-2026.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.19633v1
- Authors: Aileen Liao, Rachel Holladay, Dinesh Jayaraman, Michael Posa
- Published: 2026-07-22T00:05:00Z
- Age days: 2

</details>
