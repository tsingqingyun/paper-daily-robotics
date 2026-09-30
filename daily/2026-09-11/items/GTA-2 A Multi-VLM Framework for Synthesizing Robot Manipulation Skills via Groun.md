---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09808v1"
published: "2026-09-09T07:04:35Z"
age_days: 1
score: 31
created: 2026-09-11
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes

> [!summary] 先说人话（基于摘要）
> GTA-2 achieves an average zero-shot success rate of 73.9%, exceeding the strongest baseline by 31.4 percentage points, while targeted refinement raises GTA-2's average success rate to 90.7%.

## 问题

However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills.

## 创新点或方法

We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable object-centric task-axis components.

## 证据

GTA-2 achieves an average zero-shot success rate of 73.9%, exceeding the strongest baseline by 31.4 percentage points, while targeted refinement raises GTA-2's average success rate to 90.7%.


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/GTA-2 A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Groun.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation tasks are often decomposed into behaviors or skills. However, one often needs to predefine these behaviors for specific tasks or try to cover a wide range of tasks using generic skills. As a result, these behaviors can remain too coarse to expose the geometric, control, and scene-dependent decisions required for execution. We introduce Grounded Task Axes v2 (GTA-2), a modular multi-VLM framework that constructs executable, task-bespoke manipulation skills from reusable object-centric task-axis components. Rather than predicting actions end-to-end or composing fixed task-level primitives, GTA-2 represents each skill as semantic subtasks comprising task-relevant keypoints and axes, controller compositions, and scene-dependent parameters. Four specialized VLM agents separately decompose the task, construct an abstract task-axis skill, assign controller parameters, and ground the required visual features from RGB-D observations. This abstraction-to-grounding factorization enables zero-shot skill generation without task-specific robot demonstrations, policy training, or fine-tuning. It also keeps intermediate decisions explicit, allowing targeted human feedback to refine an incorrect stage while preserving correct components. We evaluate GTA-2 on 14 real-robot manipulation tasks against a VLA policy pi_{0.5} and two Code-as-Policies baselines using task-axis controllers or conventional robot primitives. GTA-2 achieves an average zero-shot success rate of 73.9%, exceeding the strongest baseline by 31.4 percentage points, while targeted refinement raises GTA-2's average success rate to 90.7%. Project page: https://gta2-project.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09808v1
- Authors: M. Yunus Seker, Shobhit Aggarwal, Ruwan Wickramarachchi, Jonathan Francis, Oliver Kroemer
- Published: 2026-09-09T07:04:35Z
- Age days: 1

</details>
