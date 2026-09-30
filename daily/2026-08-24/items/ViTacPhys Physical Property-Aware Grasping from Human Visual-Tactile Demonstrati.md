---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21355v1"
published: "2026-08-21T17:58:10Z"
age_days: 2
score: 28
created: 2026-08-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations

> [!summary] 一句话结论（基于摘要）
> On seen objects, it achieves 97.2% mass classification accuracy, 98.8% friction-coefficient classification accuracy, and a stiffness mean absolute percentage error (MAPE) of 5.51%.

## 问题

We transfer ViTacPhys from the human domain to the robot domain using limited robot teleoperation data, robot-style video augmentation, and human demonstrations with matched actions, and deploy it as an online module for adaptive grasping.

## 创新点或方法

We introduce ViTacPhys, a visual-tactile framework and data acquisition system that estimates object mass and friction-coefficient classes, together with continuous stiffness, from human manipulation demonstrations.

## 证据

On seen objects, it achieves 97.2% mass classification accuracy, 98.8% friction-coefficient classification accuracy, and a stiffness mean absolute percentage error (MAPE) of 5.51%.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/ViTacPhys Physical Property-Aware Grasping from Human Visual-Tactile Demonstrati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent vision-based action models have demonstrated strong capabilities in complex manipulation, but they rarely leverage explicit object physical properties to adapt their policies. We introduce ViTacPhys, a visual-tactile framework and data acquisition system that estimates object mass and friction-coefficient classes, together with continuous stiffness, from human manipulation demonstrations. Trained on data from 60 rigid and deformable objects, ViTacPhys combines temporal visual-tactile modeling, cross-attention multimodal fusion, and a semantic prior derived from a vision-language model. On seen objects, it achieves 97.2% mass classification accuracy, 98.8% friction-coefficient classification accuracy, and a stiffness mean absolute percentage error (MAPE) of 5.51%. On held-out objects from known categories, it achieves 87.5% mass accuracy, 97.5% friction-coefficient accuracy, and a stiffness MAPE of 9.08%. We transfer ViTacPhys from the human domain to the robot domain using limited robot teleoperation data, robot-style video augmentation, and human demonstrations with matched actions, and deploy it as an online module for adaptive grasping. The resulting physical-property-conditioned policy achieves total grasping success rates of 95.0% on in-distribution objects and 83.4% on out-of-distribution objects. For out-of-distribution objects successfully grasped by both methods, its force profiles are more consistent with human teleoperation than those produced by ACT. These results demonstrate the feasibility of explicitly estimating and conditioning on object physical properties for real-world adaptive grasping.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21355v1
- Authors: Yiwen Liu, Yujun Zhu, Kui Jia, Zhao Liao, Yangwei You, Shuaijun Wang
- Published: 2026-08-21T17:58:10Z
- Age days: 2

</details>
