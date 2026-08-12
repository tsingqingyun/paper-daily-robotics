---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18950v1"
published: "2026-07-21T10:37:18Z"
age_days: 3
score: 26
created: 2026-07-25
concepts: ["具身智能评测与基准"]
---

# Design and stability analysis of an underactuated hand with passively rotating fingers

> [!summary] 一句话结论（基于摘要）
> With only two phalanges per finger, the design simplifies kinematic complexity while supporting precision and enveloping grasps.

## 关键点

- **问题**：This paper presents an innovative design and stability analysis of an underactuated robotic finger with spatial mobility, designed to enhance gripping dexterity in robotic hands.
- **创新点 / 方法**：The finger architecture incorporates a revolute joint at its base, enabling passive spatial rotation that facilitates both cylindrical and spherical grasping.
- **证据**：With only two phalanges per finger, the design simplifies kinematic complexity while supporting precision and enveloping grasps.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/Design and stability analysis of an underactuated hand with passively rotating f.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper presents an innovative design and stability analysis of an underactuated
robotic finger with spatial mobility, designed to enhance gripping dexterity in robotic
hands. The finger architecture incorporates a revolute joint at its base, enabling
passive spatial rotation that facilitates both cylindrical and spherical grasping. With
only two phalanges per finger, the design simplifies kinematic complexity while
supporting precision and enveloping grasps. Stability criteria, based on the moment at
the finger base joint induced by contact forces, are introduced to ensure reliable
object gripping and prevent ejection during manipulation. The study also examines a
differential mechanism that distributes a single actuation torque across multiple
fingers, allowing adaptive and coordinated motion. This mechanism enhances the hand's
ability to grasp diverse object shapes with minimal pre-grasp adjustments, leveraging
passivity for autonomous adaptation. Theoretical findings are experimentally validated
using a fully mechanical prototype, demonstrating versatility in performing cylindrical,
spherical, parallel, and enveloping grasps. The integration of underactuation-both
within individual fingers and among multiple fingers-reduces mechanical complexity,
cost, and control demands while preserving functional adaptability. This work advances
the development of compliant robotic hands suitable for applications requiring dexterity
and robustness, such as agricultural robotics, logistics, assistive technologies, and
waste sorting. Future research will focus on automating actuation and refining control
strategies to further improve grasp stability and precision, paving the way for
autonomous manipulation in unstructured environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18950v1
- Authors: Léonie Plancoulaine, Sylvain Guégan, Franck Plestan, Damien Chablat
- Published: 2026-07-21T10:37:18Z
- Age days: 3

</details>
