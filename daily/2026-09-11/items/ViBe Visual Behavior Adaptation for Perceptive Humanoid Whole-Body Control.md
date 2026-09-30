---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09918v1"
published: "2026-09-09T09:11:26Z"
age_days: 1
score: 25
created: 2026-09-11
concepts: ["Sim2Real"]
---

# ViBe: Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control

> [!summary] 先说人话（基于摘要）
> We present ViBe, a post-training framework for adapting motion trackers to perceptive control tasks.

## 问题

By design, the resulting trackers lack exteroceptive feedback hence reacting to the environment remains the responsibility of a higher-level planner.

## 创新点或方法

We present ViBe, a post-training framework for adapting motion trackers to perceptive control tasks.

## 证据

摘要未报告明确实验结论；需阅读全文核查。


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：Sim2Real
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/ViBe Visual Behavior Adaptation for Perceptive Humanoid Whole-Body Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Motion tracking provides a scalable recipe for humanoid whole-body control. By design, the resulting trackers lack exteroceptive feedback hence reacting to the environment remains the responsibility of a higher-level planner. Existing perceptive controllers train geometry-only encoders from scratch, trading semantics for sim-to-real ease, and typically rely on teacher-student distillation for a task of interest. We present ViBe, a post-training framework for adapting motion trackers to perceptive control tasks. We leverage pre-trained visual encoders with a multi-query extractor module to learn task-relevant perceptive feedback. This feedback is grafted onto the tracker's input via low-rank adapters, enabling parameter-efficient fine-tuning. Given a task reward and a reference dataset, this modular controller can be adapted directly via policy optimization. Across four tasks, ViBe shows zero-shot sim-to-real transfer spanning perceptive walking on curbs and parkour, Repose Cube, omni-object loco-manipulation, and dodgeball, with visually robust performance across outdoor, low-light, and RGB distractor conditions. Finally, we solve a goal-oriented Repose Cube task with a deliberately simple planner, demonstrating the efficacy of perceptive controllers, adapted by our approach.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09918v1
- Authors: Lokesh Krishna, Sarvesh Venkatesan, An Zhang, Quan Nguyen
- Published: 2026-09-09T09:11:26Z
- Age days: 1

</details>
