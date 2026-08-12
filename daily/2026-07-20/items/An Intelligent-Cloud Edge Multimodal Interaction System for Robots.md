---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14675v1"
published: "2026-07-16T07:39:18Z"
age_days: 3
score: 27
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# An Intelligent-Cloud Edge Multimodal Interaction System for Robots

## 为什么重要

自动筛选分数：27

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14675v1
- Authors: Zihan Guo, Xiaoqi Li
- Published: 2026-07-16T07:39:18Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
