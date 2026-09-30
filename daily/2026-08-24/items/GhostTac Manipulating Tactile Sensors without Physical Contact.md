---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20817v1"
published: "2026-08-21T07:39:19Z"
age_days: 3
score: 27
created: 2026-08-24
concepts: ["具身智能评测与基准"]
---

# GhostTac: Manipulating Tactile Sensors without Physical Contact

> [!summary] 一句话结论（基于摘要）
> We present GhostTac, the first contactless attack, to the best of our knowledge, that manipulates tactile sensing through electromagnetic interference (EMI).

## 问题

However, the physical-layer security of tactile sensors has received little attention.

## 创新点或方法

We present GhostTac, the first contactless attack, to the best of our knowledge, that manipulates tactile sensing through electromagnetic interference (EMI).

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/GhostTac Manipulating Tactile Sensors without Physical Contact.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tactile sensors are integral to modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. However, the physical-layer security of tactile sensors has received little attention. We present GhostTac, the first contactless attack, to the best of our knowledge, that manipulates tactile sensing through electromagnetic interference (EMI). GhostTac exploits nonlinear rectification and limited-bandwidth amplification, converting carefully crafted EMI signals into persistent DC offsets that bypass onboard filtering and induce stable measurement deviations. It enables fine-grained, controllable manipulation of sensor outputs by shaping the spatial distribution and magnitude of interference at targeted locations. Such manipulation can induce harmful robot behaviors, including excessive force that may damage objects or injure people. We evaluate GhostTac on 10 sensor modules and two dexterous hands, covering 15 tactile sensors of different types, and demonstrate consistent effectiveness across all tested devices. Three case studies involving tactile grasping, slip detection, and material classification further illustrate its practical impact on real robotic tasks. These findings reveal a new physical attack vector against tactile sensing in robotic systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20817v1
- Authors: Kun Wang, Xuancun Lu, Ruochen Zhou, Kai Wang, Tongjun Ye, Yihao Shao, Chen Yan, Xiaoyu Ji, Wenyuan Xu
- Published: 2026-08-21T07:39:19Z
- Age days: 3

</details>
