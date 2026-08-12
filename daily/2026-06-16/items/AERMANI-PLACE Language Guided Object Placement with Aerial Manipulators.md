---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14531v1"
published: "2026-06-12T15:07:55Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["具身智能评测与基准"]
---

# AERMANI-PLACE: Language Guided Object Placement with Aerial Manipulators

> [!summary] 一句话结论（基于摘要）
> Experimental results show that the proposed method reliably infers placement locations from language instructions with an average success rate of 87\% on the test-set and transfers effectively to real-world aerial manipulation with an average success rate of…

## 关键点

- **问题**：Such interfaces are not intuitive and require users to reason about coordinate frames and scene geometry, making them difficult to use in practical deployments.
- **创新点 / 方法**：Inspired by this observation, we present AERMANI- PLACE, a framework for language-guided object placement with aerial manipulators.
- **证据**：Experimental results show that the proposed method reliably infers placement locations from language instructions with an average success rate of 87\% on the test-set and transfers effectively to real-world aerial manipulation with an average success rate of 72\%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object placement is a fundamental component of aerial manipulation tasks, yet existing
systems typically require the desired placement position to be specified explicitly in
metric coordinates. Such interfaces are not intuitive and require users to reason about
coordinate frames and scene geometry, making them difficult to use in practical
deployments. In contrast, humans often communicate spatial goals through a combination
of language and pointing gestures. Inspired by this observation, we present AERMANI-
PLACE, a framework for language-guided object placement with aerial manipulators. Given
a scene image and a natural language instruction, an image editing model generates a
modified version of the scene containing a visual marker that indicates where the object
should be placed. This marker is then grounded into the physical environment using depth
observations to recover a metric place point, after which a placement trajectory is
generated and executed by the aerial manipulator. We evaluate the proposed approach on a
test set of 100 language-guided placement tasks and demonstrate successful execution on
a real aerial manipulation platform. Experimental results show that the proposed method
reliably infers placement locations from language instructions with an average success
rate of 87\% on the test-set and transfers effectively to real-world aerial manipulation
with an average success rate of 72\%. Video: https://youtu.be/SgwwgLBsv0g

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14531v1
- Authors: Sarthak Mishra, Ritama Sanyal, Rishabh Dev Yadav, Wei Pan, Spandan Roy
- Published: 2026-06-12T15:07:55Z
- Age days: 3

</details>
