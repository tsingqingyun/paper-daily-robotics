---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18077v1"
published: "2026-08-18T17:59:30Z"
age_days: 2
score: 25
created: 2026-08-21
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Hydra-0: Action Flow for Generalist World Modeling and Control

> [!summary] 一句话结论（基于摘要）
> Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient adaptation.

## 关键点

- **问题**：We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion.
- **创新点 / 方法**：We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion.
- **证据**：Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient adaptation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Hydra-0 Action Flow for Generalist World Modeling and Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion. This shared visual interface enables generalist world modeling and control by learning action consequences across embodiments, tasks, environments, and video-generation backbones. Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient adaptation. On the RoboLab benchmark, Hydra-0 achieves a Pearson correlation of r=0.96 between replayed and reference success rates. Finally, we uncover an emergent inverse mode of this interface: a world action model that predicts compatible robot motion from desired object flow transferred from a human demonstration. A trained action head maps the resulting latent features to executable actions without requiring task-specific expert robot demonstrations. Together, these results demonstrate the potential of action flow as a shared control interface connecting heterogeneous training data, open-loop policy evaluation, and robot control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18077v1
- Authors: Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- Published: 2026-08-18T17:59:30Z
- Age days: 2

</details>
