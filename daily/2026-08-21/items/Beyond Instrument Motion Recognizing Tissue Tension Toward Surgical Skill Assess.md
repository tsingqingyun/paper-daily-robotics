---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17935v2"
published: "2026-08-18T15:56:08Z"
age_days: 2
score: 25
created: 2026-08-21
concepts: ["具身智能评测与基准"]
---

# Beyond Instrument Motion: Recognizing Tissue Tension Toward Surgical Skill Assessment

> [!summary] 一句话结论（基于摘要）
> Using a compact trajectory encoder, TensionTRAC achieves competitive performance against strong pretrained video backbones.

## 关键点

- **问题**：Surgical performance assessment in minimally invasive surgery largely relies on manual expert review, making it time-consuming, subjective, and difficult to scale.
- **创新点 / 方法**：To address this gap, we introduce tissue tension recognition, a new clinically motivated video understanding task for laparoscopic and robot-assisted rectal cancer surgery.
- **证据**：Using a compact trajectory encoder, TensionTRAC achieves competitive performance against strong pretrained video backbones.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Beyond Instrument Motion Recognizing Tissue Tension Toward Surgical Skill Assess.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Surgical performance assessment in minimally invasive surgery largely relies on manual expert review, making it time-consuming, subjective, and difficult to scale. While existing surgical video understanding methods address tasks such as instrument segmentation, surgical phase recognition, and action recognition, they do not explicitly capture fine-grained tissue handling, a key indicator of surgical quality. To address this gap, we introduce tissue tension recognition, a new clinically motivated video understanding task for laparoscopic and robot-assisted rectal cancer surgery. To support this task, we construct SurgTension, the first expert-annotated tissue tension dataset, providing a benchmark for objective tissue tension recognition. We further propose TensionTRAC, a lightweight trajectory-based framework that models tissue tension from sparse point trajectories. Using a compact trajectory encoder, TensionTRAC achieves competitive performance against strong pretrained video backbones.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17935v2
- Authors: Marko Haralović, Zhiqi Miao, Alexander Machiel Bont, Jiapan Guo, Frans van Workum, Estefanía Talavera
- Published: 2026-08-18T15:56:08Z
- Age days: 2

</details>
