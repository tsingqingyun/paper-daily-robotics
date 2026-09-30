---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09591v1"
published: "2026-09-09T01:36:44Z"
age_days: 1
score: 39
created: 2026-09-11
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G

> [!summary] 先说人话（基于摘要）
> A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedA…

## 问题

However, training and adapting VLA models to distributed robotic agents introduce challenges in privacy protection, communication efficiency, and model heterogeneity.

## 创新点或方法

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing.

## 证据

A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedAvg by 22.2 percentage points, sustains a widening margin whe…


## 局限

摘要未明确说明；需阅读全文核查。

- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

需结合研究方向判断；规则式回退未做语义评审。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Sixth-generation (6G) wireless networks are expected to provide a key infrastructure for large-scale embodied intelligence, where heterogeneous robots collaborate through low-latency connectivity, edge intelligence, and distributed sensing. Vision-language-action (VLA) models offer a foundation by integrating visual perception, language understanding, and action generation into a unified closed-loop policy. However, training and adapting VLA models to distributed robotic agents introduce challenges in privacy protection, communication efficiency, and model heterogeneity. Existing federated learning (FL) methods overlook the intrinsic differences among vision, language, and action pathways in parameter scale, privacy exposure, update dynamics, and tolerance to compression or perturbation. To address this issue, this article proposes FedMVLA, a modality-decoupled FL framework for privacy-preserving embodied intelligence in 6G networks. FedMVLA incorporates three mechanisms: modality-aware federated aggregation (MAFA), modality-aware privacy allocation (MAPA), and modality-aware communication compression (MACO), together with a modality-sliced transport design that routes the precision-critical action stream through a protected ultra-reliable low-latency slice. A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedAvg by 22.2 percentage points, sustains a widening margin when scaling to 128 clients across eight cells, and reduces the schedule-averaged per-client uplink model-update payload by 95.6% (approximately 96%), while keeping the 95th percentile (p95) of the round-critical uplink completion time near 1.5s.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09591v1
- Authors: Zhuodong Liu, Xiangyu Li, Chunhong Yuan, Hongyang Du, Bodong Shang, Qingqing Wu, Tony Q. S. Quek, Mohsen Guizani
- Published: 2026-09-09T01:36:44Z
- Age days: 1

</details>
