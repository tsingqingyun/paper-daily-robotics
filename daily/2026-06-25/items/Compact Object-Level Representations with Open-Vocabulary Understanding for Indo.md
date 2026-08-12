---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.24767v1"
published: "2026-06-23T16:27:04Z"
age_days: 1
score: 28
created: 2026-06-25
concepts: ["多模态基础模型"]
---

# Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

> [!summary] 一句话结论（基于摘要）
> Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets.

## 关键点

- **问题**：However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability.
- **创新点 / 方法**：To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities.
- **证据**：Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Indoor visual relocalization plays a critical role in emerging spatial and embodied AI
applications. However, prior research was predominantly devoted to low-level vision
schemes, struggling to perceive scene semantics and compositions, which limits both
interpretability and applicability. In this paper, we explore the issue of how to
organize rich object information in a scene, including semantics, layout, and geometry,
into a structured map representation, thereby utilizing object units exclusively to
drive the camera relocalization task. To this end, we propose OpenReLoc, a camera
relocalization system designed to provide scene understanding and accurate pose
estimation capabilities. Leveraging recent foundation models, we first introduce a
multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective
2D-3D object matching. Additionally, we design object-oriented reference frames as
position priors, paired with a reference frame selection strategy based on the Distance-
IoU (DIOU), enabling extension to scalable scenes. Moreover, to ensure stable and
accurate pose optimization, we also propose a dual-path 2D Iterative Closest Pixel loss
guided by object shape. Experimental results demonstrate that OpenReLoc achieves
superior relocalization recall and accuracy across various datasets. Our source code
will be released upon acceptance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.24767v1
- Authors: Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
- Published: 2026-06-23T16:27:04Z
- Age days: 1

</details>
