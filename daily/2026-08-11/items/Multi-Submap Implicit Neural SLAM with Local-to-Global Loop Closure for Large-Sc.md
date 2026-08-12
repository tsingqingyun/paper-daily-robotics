---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09146v1"
published: "2026-08-10T05:49:55Z"
age_days: 1
score: 31
created: 2026-08-11
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

> [!summary] 一句话结论（基于摘要）
> To address global consistency, we introduce a local-to-global loop closure framework leveraging the foundation model for high-performance global descriptor extraction, significantly enhancing relocalization accuracy under varying viewpoints.

## 关键点

- **问题**：Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small- scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift.
- **创新点 / 方法**：Specifically, we propose a progressive mapping strategy that dynamically allocates neural submaps to maintain high- fidelity representations without memory explosion.
- **证据**：To address global consistency, we introduce a local-to-global loop closure framework leveraging the foundation model for high-performance global descriptor extraction, significantly enhancing relocalization accuracy under varying viewpoints.
- **局限**：Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small- scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-
scale scene reconstruction, yet scaling these methods to extensive, complex environments
remains challenging due to catastrophic forgetting and accumulated trajectory drift.
This paper presents a robust, large-scale neural SLAM system featuring a multi-submap
architecture and a dual-tier loop closure mechanism. Specifically, we propose a
progressive mapping strategy that dynamically allocates neural submaps to maintain high-
fidelity representations without memory explosion. For robust pose estimation, an
optical-flow-based tracking module is integrated to handle aggressive motions. To
address global consistency, we introduce a local-to-global loop closure framework
leveraging the foundation model for high-performance global descriptor extraction,
significantly enhancing relocalization accuracy under varying viewpoints. Furthermore,
an inter-submap online distillation algorithm is designed during back-end optimization
to enforce geometric and appearance consistency across overlapping submap boundaries. To
validate the system, we developed a customized handheld mechatronic platform and
conducted extensive evaluations on both public benchmarks and our large-scale indoor-
outdoor datasets. Experimental results, including direct deployment on an onboard
computing unit, demonstrate that our approach outperforms state-of-the-art neural SLAM
methods in reconstruction quality and localization robustness, providing a scalable
solution for real-world robotic perception and digital twinning. We will release the
code publicly on \href{https://github.com/dtc111111/MSN-
SLAM}{https://github.com/dtc111111/MSN-SLAM} .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09146v1
- Authors: Tianchen Deng, Chongdi Wang, Nailin Wang, Lei Zhao, Ziqi Ma, Tianjun Zhang, Zhe Liu, Danwei Wang, Hesheng Wang
- Published: 2026-08-10T05:49:55Z
- Age days: 1

</details>
