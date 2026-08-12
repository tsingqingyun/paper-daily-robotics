---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12396v1"
published: "2026-06-10T17:57:06Z"
age_days: 1
score: 30
created: 2026-06-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving

> [!summary] 一句话结论（基于摘要）
> We introduce VLGA, the first vision- language-action model supervised to reconstruct the dense 3D world it drives through.

## 关键点

- **问题**：Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them.
- **创新点 / 方法**：We introduce VLGA, the first vision- language-action model supervised to reconstruct the dense 3D world it drives through.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/VLGA Vision-Language-Geometry-Action Models for Autonomous Driving.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models can describe scenes and reason about them in
language, yet still struggle to ground their actions in the dense 3D world around them.
Existing approaches either inject features from a frozen 3D foundation model without an
objective that ensures the policy uses them, or constrain geometry with sparse box and
map losses that provide no dense spatial signal. We introduce VLGA, the first vision-
language-action model supervised to reconstruct the dense 3D world it drives through.
VLGA introduces geometry as a fourth modality alongside vision, language, and action
through a dedicated expert supervised by a per-pixel pointmap regression loss against
LiDAR. Extensive experiments conducted on challenging nuScenes and Bench2Drive datasets
for open-loop and closed-loop evaluations, respectively, show the superiority of VLGA
over counterpart VLA methods. In particular, on open-loop nuScenes, VLGA sets a new
state of the art among VLA methods without ego status, with the lowest L2 (0.50\,m
average) and 3-second collision rate (0.18\%). On closed-loop Bench2Drive, VLGA attains
the state-of-the-art driving score of 79.08, +0.71 over the strongest prior VLA, at
comparable efficiency and comfort.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12396v1
- Authors: Jin Yao, Dhruva Dixith Kurra, Tom Lampo, Zezhou Cheng, Danhua Guo, Burhan Yaman
- Published: 2026-06-10T17:57:06Z
- Age days: 1

</details>
