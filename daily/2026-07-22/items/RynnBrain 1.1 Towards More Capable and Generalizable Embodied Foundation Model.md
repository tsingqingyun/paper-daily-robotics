---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.17977v1"
published: "2026-07-20T14:13:27Z"
age_days: 1
score: 41
created: 2026-07-22
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model

> [!summary] 一句话结论（基于摘要）
> RynnBrain 1.1 achieves strong results on embodied cognition, localization, and 3D grounding, with the 122B-A10B model outperforming all evaluated proprietary and open- source models on VSI-Bench, MMSI, and RefSpatial-Bench.

## 关键点

- **问题**：We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales.
- **创新点 / 方法**：We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales.
- **证据**：RynnBrain 1.1 achieves strong results on embodied cognition, localization, and 3D grounding, with the 122B-A10B model outperforming all evaluated proprietary and open- source models on VSI-Bench, MMSI, and RefSpatial-Bench.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and
122B-A10B scales. Trained with a unified spatio-temporal and physically grounded
framework, RynnBrain 1.1 supports embodied perception, spatial reasoning, localization,
and planning. Compared with RynnBrain 1.0, it further introduces contact-point
prediction across the model family and native 3D grounding for the 2B and 9B models,
yielding representations and outputs that are more directly aligned with robot
manipulation. We also develop RynnBrain-VLA with a unified cross-embodiment action space
and embodiment-specific masking, and deploy it on Unitree G1, Astribot-S1, and Tianji-
Wuji. RynnBrain 1.1 achieves strong results on embodied cognition, localization, and 3D
grounding, with the 122B-A10B model outperforming all evaluated proprietary and open-
source models on VSI-Bench, MMSI, and RefSpatial-Bench. Real-robot experiments show that
RynnBrain-initialized policies outperform Qwen-based and representative generalist VLAs,
while joint multi-task and multi-embodiment training improves process scores and success
rates over per-task training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.17977v1
- Authors: Kehan Li, Bohan Hou, Minghao Zhu, Tianyi Zhang, Zesen Cheng, Zhikai Wang, Sicong Leng, Xin Li, Xiao Lin, Biying Yao, Minghua Zeng, Jiangpin Liu, Ronghao Dang, Jiayan Guo, Siteng Huang, Haoyu Zhao, Heng Ping, Yaxi Zhao, Kexiang Wang, Tong Lu, Shengke Xue, Jiahao Tang, Yulei Wang, Zejing Wang, Jianwei Gao, Shijian Lu, Chengju Liu, Jianfei Yang, Mingxiu Chen, Deli Zhao
- Published: 2026-07-20T14:13:27Z
- Age days: 1

</details>
