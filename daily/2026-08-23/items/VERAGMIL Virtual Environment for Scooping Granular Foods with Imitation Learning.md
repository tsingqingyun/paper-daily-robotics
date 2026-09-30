---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18258v1"
published: "2026-08-18T19:18:38Z"
age_days: 4
score: 20
created: 2026-08-23
concepts: ["机器人学习", "具身智能评测与基准"]
---

# VERAGMIL: Virtual Environment for Scooping Granular Foods with Imitation Learning Models

> [!summary] 一句话结论（基于摘要）
> Results show that VR-based demonstrations significantly outperform 3D space mouse data, with BCQ achieving the best overall performance, particularly in reducing spillage and approaching human performance.

## 问题

Manipulating granular food items, such as rice and beans, poses significant challenges due to their dynamic physical properties.

## 创新点或方法

To address this, we present VERAGMIL, a framework that combines a high-fidelity simulator with an intuitive Virtual Reality (VR) interface for recording demonstrations and supporting different imitation learning methods.

## 证据

Results show that VR-based demonstrations significantly outperform 3D space mouse data, with BCQ achieving the best overall performance, particularly in reducing spillage and approaching human performance.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：20
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/VERAGMIL Virtual Environment for Scooping Granular Foods with Imitation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot-Assisted Feeding (RAF) systems are essential for assisting individuals with disabilities or motor impairments in eating tasks. Manipulating granular food items, such as rice and beans, poses significant challenges due to their dynamic physical properties. Learning from human demonstrations offers a promising solution, but acquiring high-quality demonstrations is complex. To address this, we present VERAGMIL, a framework that combines a high-fidelity simulator with an intuitive Virtual Reality (VR) interface for recording demonstrations and supporting different imitation learning methods. VERAGMIL provides a realistic environment for training RAF systems to handle granular materials, including robots, sensors, and various food items with distinct physical characteristics. We evaluate VERAGMIL by training three imitation learning models, BC, BC-RNN, and BCQ, on granular scooping and transporting tasks using both VR interface and 3D space mouse demonstrations, comparing them with a human-expert baseline. The models are assessed on success rate, spillage, generalization to unseen food items, and task completion time. Results show that VR-based demonstrations significantly outperform 3D space mouse data, with BCQ achieving the best overall performance, particularly in reducing spillage and approaching human performance. These findings underscore the effectiveness of our framework for training RAF systems in granular material handling. The code for our framework is publicly available at: https://github.com/AmanuelErgogo/VERAGMIL.git.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18258v1
- Authors: Amanuel Ergogo, Diego Dall'Alba, Przemyslaw Korzeniowski
- Published: 2026-08-18T19:18:38Z
- Age days: 4

</details>
