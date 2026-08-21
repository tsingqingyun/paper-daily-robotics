---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18948v1"
published: "2026-08-19T14:15:36Z"
age_days: 1
score: 34
created: 2026-08-21
concepts: ["机器人学习"]
---

# RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience

> [!summary] 一句话结论（基于摘要）
> Experiments show that RoboEdit achieves state-of-the-art editing quality and supports downstream robot control policies in real-world manipulation tasks.

## 关键点

- **问题**：Collecting robot hand-object interaction data is costly and embodiment-specific, yet abundant human-object videos remain unusable for robot training.
- **创新点 / 方法**：We present RoboEdit, a human-to-robot video editing suite that transforms human manipulation videos into action-consistent, physically plausible robot videos with aligned 3D hand states.
- **证据**：Experiments show that RoboEdit achieves state-of-the-art editing quality and supports downstream robot control policies in real-world manipulation tasks.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/RoboEdit Turning Human Manipulation Videos into Scalable Robot Experience.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Collecting robot hand-object interaction data is costly and embodiment-specific, yet abundant human-object videos remain unusable for robot training. We present RoboEdit, a human-to-robot video editing suite that transforms human manipulation videos into action-consistent, physically plausible robot videos with aligned 3D hand states. To enable scalable supervision, we introduce RoboEdit-ADC, an automatic pipeline that reconstructs and retargets 3D interactions from RGB videos across embodiments. This pipeline generates RoboEdit-14M, a large-scale dataset of 174K aligned video pairs (14M frames) spanning seven robot embodiments, diverse scenes, and interaction types. The core editing engine, RoboEdit-Trans, employs cross-embodiment adaptation modules to preserve temporal coherence while adapting appearance and motion. It further integrates a 3D Robot-State Decoder to recover per-frame hand states for structured motion supervision. Experiments show that RoboEdit achieves state-of-the-art editing quality and supports downstream robot control policies in real-world manipulation tasks. Ultimately, the RoboEdit suite unlocks the vast potential of unlabeled human videos, providing scalable, high-fidelity visual and 3D motion supervision for generalizable robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18948v1
- Authors: Yaowei Guo, Zeng Tao, Yuxin Jiang, Yunuo Chen, Zhiyang Dou, Yuxiang Ma, Yin Yang, Demetri Terzopoulos, Ying Jiang, Chenfanfu Jiang
- Published: 2026-08-19T14:15:36Z
- Age days: 1

</details>
