---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22136v1"
published: "2026-06-20T16:31:40Z"
age_days: 3
score: 45
created: 2026-06-24
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data

> [!summary] 一句话结论（基于摘要）
> Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%.

## 关键点

- **问题**：Scaling dexterous manipulation requires generalization across objects, scenes, and tasks, yet existing data sources face a trade-off between scale and scene/embodiment alignment: teleoperation data is well aligned with robot deployment but expensive to collect; simulation is scalable but limited by the sim-to-real gap…
- **创新点 / 方法**：We propose Wh0, a framework that uses generative video world models as scalable and controllable sources of egocentric human-hand manipulation data to unlock the manipulation capabilities of pretrained dexterous VLA models.
- **证据**：Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling dexterous manipulation requires generalization across objects, scenes, and
tasks, yet existing data sources face a trade-off between scale and scene/embodiment
alignment: teleoperation data is well aligned with robot deployment but expensive to
collect; simulation is scalable but limited by the sim-to-real gap; and real egocentric
videos scale effectively but remain misaligned with robot deployment. We propose Wh0, a
framework that uses generative video world models as scalable and controllable sources
of egocentric human-hand manipulation data to unlock the manipulation capabilities of
pretrained dexterous VLA models. Conditioned on language, objects, and scenes, Wh0 uses
a generative world model to produce WM-H, a 50k-episode dataset of egocentric human-
object interaction videos. Wh0 then converts the generated videos into robot-trainable
supervision through hand motion reconstruction and visual editing. Co-trained with a
limited amount of real robot data, WM-H adapts pretrained VLA models to dexterous
manipulation deployment. Across 18 real-world dexterous manipulation tasks, compared
with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen
tasks from 8.3% to 38.9%. Ablation studies further show that scalable generation and
scene/embodiment alignment are key drivers of performance gains. Videos and open-source
code can be found on our project website: https://chenyt31.github.io/wh0.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22136v1
- Authors: Yangtao Chen, Zixuan Chen, Peiyang Wang, Yong-Lu Li, Jing Huo, Jieqi Shi, Yang Gao
- Published: 2026-06-20T16:31:40Z
- Age days: 3

</details>
