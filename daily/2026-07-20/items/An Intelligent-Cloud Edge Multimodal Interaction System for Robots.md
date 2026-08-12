---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14675v1"
published: "2026-07-16T07:39:18Z"
age_days: 3
score: 27
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# An Intelligent-Cloud Edge Multimodal Interaction System for Robots

> [!summary] 一句话结论（基于摘要）
> Experiments on a public gesture dataset and a custom dataset show that YOLO-DC achieves precision values of 98.9% and 95.0%, with mAP@0.5 values of 90.7% and 92.7%, respectively.

## 关键点

- **问题**：Robust human-robot interaction in complex environments requires accurate gesture perception, semantic scene understanding, and reliable task planning under limited onboard computing resources.
- **创新点 / 方法**：This paper presents a cloud-edge multimodal interaction framework that integrates an enhanced YOLO-based gesture detector with coordinated large language model (LLM) and vision-language model (VLM) agents.
- **证据**：Experiments on a public gesture dataset and a custom dataset show that YOLO-DC achieves precision values of 98.9% and 95.0%, with mAP@0.5 values of 90.7% and 92.7%, respectively.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/An Intelligent-Cloud Edge Multimodal Interaction System for Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust human-robot interaction in complex environments requires accurate gesture
perception, semantic scene understanding, and reliable task planning under limited
onboard computing resources. This paper presents a cloud-edge multimodal interaction
framework that integrates an enhanced YOLO-based gesture detector with coordinated large
language model (LLM) and vision-language model (VLM) agents. The proposed detector,
incorporates the Convolutional Block Attention Module (CBAM) into the neck and replaces
the baseline bounding-box regression objective with Distance-IoU (DIoU) loss. These
modifications improve feature discrimination and localization for small or partially
occluded gestures in complex backgrounds. The cloud layer performs gesture detection,
scene understanding, multimodal fusion, and action planning, whereas the TonyPi robot
locally handles data acquisition, communication, action execution, and feedback.
Experiments on a public gesture dataset and a custom dataset show that YOLO-DC achieves
precision values of 98.9% and 95.0%, with mAP@0.5 values of 90.7% and 92.7%,
respectively. System-level evaluation yields success rates of 95%, 88%, and 82% for
single-action, composite-action, and vision-dependent tasks. A 30 participant evaluation
yields an overall mean satisfaction score of 3.69 out of 5. These results demonstrate
the feasibility of combining refined gesture detection with multimodal agents for
resource-constrained robotic interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14675v1
- Authors: Zihan Guo, Xiaoqi Li
- Published: 2026-07-16T07:39:18Z
- Age days: 3

</details>
