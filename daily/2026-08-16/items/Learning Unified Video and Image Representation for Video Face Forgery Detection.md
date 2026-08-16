---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13064v1"
published: "2026-08-13T10:25:59Z"
age_days: 3
score: 25
created: 2026-08-16
concepts: ["具身智能评测与基准"]
---

# Learning Unified Video and Image Representation for Video Face Forgery Detection

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on benchmark datasets demonstrate the effectiveness of our framework, which outperforms state-of-theart methods in detecting partially forged videos while introducing no additional computational overhead.

## 关键点

- **问题**：Existing methods for video face forgery detection typically assume that all frames in a forged video are manipulated, while detecting partially forged videos that contain only a subset of altered frames remains challenging.
- **创新点 / 方法**：To address this issue, we propose a novel framework, UVIF, that utilizes additional annotated images to provide fine-grained supervision for detecting partial forgeries in videos.
- **证据**：Extensive experiments on benchmark datasets demonstrate the effectiveness of our framework, which outperforms state-of-theart methods in detecting partially forged videos while introducing no additional computational overhead.
- **局限**：Existing methods for video face forgery detection typically assume that all frames in a forged video are manipulated, while detecting partially forged videos that contain only a subset of altered frames remains challenging.

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/Learning Unified Video and Image Representation for Video Face Forgery Detection.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Face forgery detection is crucial for preserving the security and integrity of facial data given the rapid developments in face manipulation techniques and deep generative models. Existing methods for video face forgery detection typically assume that all frames in a forged video are manipulated, while detecting partially forged videos that contain only a subset of altered frames remains challenging. To address this issue, we propose a novel framework, UVIF, that utilizes additional annotated images to provide fine-grained supervision for detecting partial forgeries in videos. UVIF employs a unified encoder and a multi-task learning paradigm to jointly model facial videos and images for boosted video face forgery detection. A 2D backbone with temporal fusion modules is employed as the unified encoder. A pseudo labeling process is designed for video frames to bridge their representations with those of static images. A video-oriented feature alignment strategy is further introduced to reduce the distribution gap between videos and images. Extensive experiments on benchmark datasets demonstrate the effectiveness of our framework, which outperforms state-of-theart methods in detecting partially forged videos while introducing no additional computational overhead. Our code is available at https://github.com/haotianll/UVIF.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13064v1
- Authors: Haotian Liu, Yang Liu, Guoying Zhao, Xiaobai Li
- Published: 2026-08-13T10:25:59Z
- Age days: 3

</details>
