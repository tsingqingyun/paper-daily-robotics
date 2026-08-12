---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24051v1"
published: "2026-06-23T01:40:54Z"
age_days: 1
score: 30
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model

> [!summary] 一句话结论（基于摘要）
> DriveStack-VLA achieves 91.6 PDMS on NAVSIMv1, 91.0 EPDMS on NAVSIMv2 (with the human penalty filter enabled), and a driving score of 79.49 with a success rate of 56.36\% on the closed-loop Bench2Drive.

## 关键点

- **问题**：However, existing VLA driving models still lack driving-oriented spatial intelligence: their policies are mainly grounded on perspective image tokens and language priors, while precise motion planning requires metric geometry, top-down scene structure, and attention to safety-critical perceptual cues.
- **创新点 / 方法**：In this paper, we present DriveStack-VLA, a framework built upon a large VLM backbone.
- **证据**：DriveStack-VLA achieves 91.6 PDMS on NAVSIMv1, 91.0 EPDMS on NAVSIMv2 (with the human penalty filter enabled), and a driving score of 79.49 with a success rate of 56.36\% on the closed-loop Bench2Drive.
- **局限**：This limitation makes current models vulnerable to weak visual geometry modeling and perceptual coverage in expert demonstrations.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/DriveStack-VLA Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action driving models convert a pretrained Vision-Language Model into a
driving policy, allowing them to use world knowledge and follow language guidances.
However, existing VLA driving models still lack driving-oriented spatial intelligence:
their policies are mainly grounded on perspective image tokens and language priors,
while precise motion planning requires metric geometry, top-down scene structure, and
attention to safety-critical perceptual cues. This limitation makes current models
vulnerable to weak visual geometry modeling and perceptual coverage in expert
demonstrations. In this paper, we present DriveStack-VLA, a framework built upon a large
VLM backbone. To strengthen the spatial grounding of VLA driving, we develop dual visual
modeling components. We inject a Bird-Eye-View representation into the Large Language
Model decoder through a DeepStack-style connection, and propose Render-Teacher Alignment
to align the perceptual focus of real images with that of rasterized images.
Furthermore, to bridge the gap in multimodal trajectory selection, we introduce a head-
based self-critique module that ranks sampled trajectories and conditionally refines the
best one. DriveStack-VLA achieves 91.6 PDMS on NAVSIMv1, 91.0 EPDMS on NAVSIMv2 (with
the human penalty filter enabled), and a driving score of 79.49 with a success rate of
56.36\% on the closed-loop Bench2Drive. More visualizations are available on our project
page: https://anonymous.4open.science/w/drivestack-vla/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24051v1
- Authors: Jingke Wang, Zhenru Zhao, Shuangming Lei, Hao Su, Yuehao Huang, Yijia Xie, Kai Tang, Guanglin Xu, AiXue Ye, Yukai Ma, Yong Liu
- Published: 2026-06-23T01:40:54Z
- Age days: 1

</details>
