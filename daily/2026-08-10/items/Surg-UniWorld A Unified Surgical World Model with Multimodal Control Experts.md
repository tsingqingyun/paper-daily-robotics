---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06770v1"
published: "2026-08-07T03:43:37Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that Surg-UniWorld consistently outperforms existing controllable video generation methods and surgical world-model baselines in generation quality, temporal consistency, and multimodal controllability.

## 关键点

- **问题**：However, existing methods lack a unified multimodal control paradigm, while direct fusion of heterogeneous visual conditions often causes anatomical distortion, instrument appearance drift, and temporally inconsistent interactions.
- **创新点 / 方法**：In this work, we propose {Surg-UniWorld}, a unified surgical world model with multimodal control experts.
- **证据**：Extensive experiments demonstrate that Surg-UniWorld consistently outperforms existing controllable video generation methods and surgical world-model baselines in generation quality, temporal consistency, and multimodal controllability.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Controllable surgical world models can provide a generative foundation for surgical
artificial intelligence and simulation by synthesizing realistic instrument--tissue
interactions. However, existing methods lack a unified multimodal control paradigm,
while direct fusion of heterogeneous visual conditions often causes anatomical
distortion, instrument appearance drift, and temporally inconsistent interactions. In
this work, we propose {Surg-UniWorld}, a unified surgical world model with multimodal
control experts. Surg-UniWorld first constructs a {Hierarchical Surgical Anchor} from
first-frame appearance and hierarchical semantic masks to preserve persistent scene
identity, anatomical organization, and interaction boundaries. {Anchor-Relative Modality
Experts} then interpret edge, depth, and optical-flow evidence relative to the shared
anchor, capturing complementary boundary, geometric, and motion information. A
{Multimodal Control Expert} further performs contribution-preserving stage-wise
composition of the activated modality increments and generates control hints for the
Wan2.2 video diffusion backbone. To support multimodal surgical world modeling, we
further construct Cholec80-SurgWAM, a benchmark for controllable surgical video
generation. Extensive experiments demonstrate that Surg-UniWorld consistently
outperforms existing controllable video generation methods and surgical world-model
baselines in generation quality, temporal consistency, and multimodal controllability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06770v1
- Authors: Rulin Zhou, Wanhao Liu, Guoheng Ma, Liangjin Shao, Qiujie Song, Yidu Wang, Guankun Wang, Tong Chen, Long Bai, Luping Zhou, Hongliang Ren
- Published: 2026-08-07T03:43:37Z
- Age days: 3

</details>
