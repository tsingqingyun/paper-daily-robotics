---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19531v1"
published: "2026-06-17T19:25:28Z"
age_days: 2
score: 31
created: 2026-06-20
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?

> [!summary] 一句话结论（基于摘要）
> ImageWAM outperforms standard VLA baselines and matching competitive WAMs without additional policy pretraining across different simulator and real-world experiments.

## 关键点

- **问题**：However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction.
- **创新点 / 方法**：We propose ImageWAM, a simple WAM framework that repurposes pretrained image editing models for robot action prediction.
- **证据**：ImageWAM outperforms standard VLA baselines and matching competitive WAMs without additional policy pretraining across different simulator and real-world experiments.
- **局限**：However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/ImageWAM Do World Action Models Really Need Video Generation, or Just Image Edit.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) commonly rely on video generation to bridge visual world
modeling and robot control. However, video-based WAMs face three coupled limitations:
dense multi-frame future tokens make inference costly, full video prediction spends
capacity on action-irrelevant temporal and appearance details, and long-horizon future
imagination may introduce errors that mislead action prediction. These issues raise a
simple question: Does world action model really need video generation? We propose
ImageWAM, a simple WAM framework that repurposes pretrained image editing models for
robot action prediction. In contrast to video generation, image editing provides a
better-matched prior: it only needs to model a target-frame transformation, focuses on
action-relevant current-to-target visual differences, and grounds task instructions to
localized visual changes through edit pretraining. In practice, ImageWAM does not decode
the target frame at inference time; instead, it conditions a flow-matching action expert
on the KV caches produced by image-editing denoising, using them as a compact world-
action context. ImageWAM outperforms standard VLA baselines and matching competitive
WAMs without additional policy pretraining across different simulator and real-world
experiments. It also reduces FLOPs to 1/6 and latency to 1/4 of video-based WAMs.
Attention analysis further shows that editing caches focus on task-relevant change
regions, supporting image editing as an effective alternative to video-based world-
action modeling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19531v1
- Authors: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin
- Published: 2026-06-17T19:25:28Z
- Age days: 2

</details>
