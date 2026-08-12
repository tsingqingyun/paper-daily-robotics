---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17256v1"
published: "2026-06-15T20:00:20Z"
age_days: 2
score: 33
created: 2026-06-18
concepts: ["AI 核心知识地图"]
---

# Contrastive Action-Image Pre-training for Visuomotor Control

> [!summary] 一句话结论（基于摘要）
> Leveraging 32,041 hours of egocentric human video and only 88 hours of robotic manipulation data, CAIP outperforms state-of-the-art vision encoders including DINOv2, SigLIP, MVP, and R3M.

## 关键点

- **问题**：Existing vision encoders for robotics face a fundamental bottleneck: robotic datasets lack the scale necessary for large-scale pre-training.
- **创新点 / 方法**：To this end, we introduce CAIP (Contrastive Action-Image Pre-training), a vision encoder that treats human hand poses from large-scale egocentric video as a proxy for end-effector actions.
- **证据**：Leveraging 32,041 hours of egocentric human video and only 88 hours of robotic manipulation data, CAIP outperforms state-of-the-art vision encoders including DINOv2, SigLIP, MVP, and R3M.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing vision encoders for robotics face a fundamental bottleneck: robotic datasets
lack the scale necessary for large-scale pre-training. Prior work circumvents this data
scarcity by turning to internet-scale image and language data or egocentric human video.
While these models show promise, neither paradigm learns from paired vision and action
data, which downstream visuomotor control policies require. However, robot trajectories,
the most direct source of this paired signal, are not available at pre-training scale,
motivating us to extract action signals from abundant human video instead. To this end,
we introduce CAIP (Contrastive Action-Image Pre-training), a vision encoder that treats
human hand poses from large-scale egocentric video as a proxy for end-effector actions.
By extracting 3D hand keypoints, a representation that aligns naturally with downstream
robot action spaces, CAIP learns a unified action-image representation through a
contrastive objective. Leveraging 32,041 hours of egocentric human video and only 88
hours of robotic manipulation data, CAIP outperforms state-of-the-art vision encoders
including DINOv2, SigLIP, MVP, and R3M. Evaluated on a challenging real-world dexterous
manipulation setup using Dexmate Vega and Sharpa Wave hands, CAIP yields performance
gains of more than 30% on tasks involving folding, pouring, and fine-grained
manipulation. Our results show that our method of contrastive action-centric pre-
training yields a scalable path to achieving robust visual representations better suited
for physical interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17256v1
- Authors: Yuvan Sharma, Dantong Niu, Anirudh Pai, Zekai Wang, Zhuoyang Liu, Baifeng Shi, Stefano Saravalle, Boning Shao, Ruijie Zheng, Jing Wang, Konstantinos Kallidromitis, Yusuke Kato, Fabio Galasso, Yuke Zhu, Danfei Xu, Linxi "Jim" Fan, Jitendra Malik, Trevor Darrell, Roei Herzig
- Published: 2026-06-15T20:00:20Z
- Age days: 2

</details>
