---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12910v1"
published: "2026-06-11T05:09:34Z"
age_days: 1
score: 34
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# Bounding Boxes as Goals: Language-Conditioned Grasping via Neuro-Symbolic Planning

> [!summary] 一句话结论（基于摘要）
> We achieve 73.3% overall success across 90 real-robot trials at three difficulty levels, requiring no task- specific training.

## 关键点

- **问题**：Although Vision-Language Models (VLMs) have enabled zero-shot generalization in robot task and motion planning (TAMP), current state-of-the-art approaches often remain computationally "heavyweight" or require extensive training on thousands of demonstrations.
- **创新点 / 方法**：We present GRASP (Grounded Reasoning and Symbolic Planning), a framework designed as a step toward open-vocabulary tabletop manipulation.
- **证据**：We achieve 73.3% overall success across 90 real-robot trials at three difficulty levels, requiring no task- specific training.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

For robotics to be effectively integrated into household or industrial environments,
machines must adapt to natural-language prompts in real time. Although Vision-Language
Models (VLMs) have enabled zero-shot generalization in robot task and motion planning
(TAMP), current state-of-the-art approaches often remain computationally "heavyweight"
or require extensive training on thousands of demonstrations. We present GRASP (Grounded
Reasoning and Symbolic Planning), a framework designed as a step toward open-vocabulary
tabletop manipulation. Our approach leverages a pretrained VLM to translate natural-
language queries into neuro-symbolic goal states, grounded in the physical world via a
bounding-box detection pipeline. Unlike methods that rely on fixed color lists or hard-
coded coordinates, GRASP enables robots to interpret abstract spatial concepts such as
"top shelf" and execute tasks without additional fine-tuning. We achieve 73.3% overall
success across 90 real-robot trials at three difficulty levels, requiring no task-
specific training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12910v1
- Authors: Allison Andreyev, Landon Eum, Nestor Tiglao, Romel Gomez
- Published: 2026-06-11T05:09:34Z
- Age days: 1

</details>
