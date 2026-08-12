---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18593v1"
published: "2026-05-18T16:06:29Z"
age_days: 1
score: 38
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Not What You Asked For: Typographic Attacks in Household Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> In a controlled evaluation pool of 59 attributable episodes, the attack achieves an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful episodes, under uncontrolled viewing angles and occlusion with no perceptual optimization.

## 关键点

- **问题**：However, the shared embedding space that enables this flexibility introduces a structural vulnerability to typographic attacks, where printed text in a physical scene semantically overrides visual judgment.
- **创新点 / 方法**：We introduce a decoupled perception architecture that exposes a frozen CLIP encoder to adversarial stickers while maintaining geometric grounding via DETIC.
- **证据**：In a controlled evaluation pool of 59 attributable episodes, the attack achieves an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful episodes, under uncontrolled viewing angles and occlusion with no perceptual optimization.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Open-vocabulary embodied AI agents increasingly rely on vision-language models such as
CLIP for object perception and task grounding. However, the shared embedding space that
enables this flexibility introduces a structural vulnerability to typographic attacks,
where printed text in a physical scene semantically overrides visual judgment. While
prior work has quantified this threat in static 2D benchmarks and 3D navigation tasks,
its impact on the full Sense-Plan-Act pipeline of household robot manipulation remains
unexplored. This work evaluates typographic attacks in a Habitat-based simulation using
the HomeRobot benchmark. We introduce a decoupled perception architecture that exposes a
frozen CLIP encoder to adversarial stickers while maintaining geometric grounding via
DETIC. In a controlled evaluation pool of 59 attributable episodes, the attack achieves
an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful
episodes, under uncontrolled viewing angles and occlusion with no perceptual
optimization. Critically, we find that perceptual errors propagate through the
persistent 3D semantic map to produce kinetic failures, defined here as physically
executed grasping and transport of the wrong object driven by an adversarially poisoned
semantic state. In these cases, the robot physically grasps and delivers the wrong
object to a target receptacle. These results establish typographic misclassification as
a real, measurable, and physically consequential threat to the safety of modular
manipulation pipelines that prior typographic attack research has left unexamined.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18593v1
- Authors: Ali Iranmanesh, Peng Liu
- Published: 2026-05-18T16:06:29Z
- Age days: 1

</details>
