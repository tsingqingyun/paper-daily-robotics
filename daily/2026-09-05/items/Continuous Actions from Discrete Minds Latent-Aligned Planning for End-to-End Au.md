---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04070"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-09-05
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving

> [!summary] 先说人话（基于摘要）
> LaPla 用残差 VQ-VAE 学到的动作潜空间作为物理先验，但不做离散码本查找；VLA 一次前向直接输出连续潜变量，再由冻结解码器生成平滑、可行动作。

## 问题

VLM 的推理通常是离散的，而自动驾驶轨迹连续且受物理约束；离散动作 token 会引入量化误差，自回归生成又增加延迟，导致语义理解难以落到精确运动。

## 创新点或方法

输入多视角图像、历史动作和文本指令后，并发动作 query 在一次前向中因果关注多模态上下文，将隐藏状态投影到预训练 VQ-VAE 的潜空间；冻结解码器输出动作。与常规方法相比，它利用码器学到的结构，却绕开离散检索和自回归。

## 证据

nuScenes 开环测试中，长时程 L2 误差相对先进 VLA 降低15.52%；NVIDIA AlpaSim 闭环测试中成功率提高33.34个百分点，并显著降低推理延迟，但未给绝对成功率和延迟数值。


## 局限

需核查连续投影是否真的“消除”量化误差、物理可行性由何种训练约束保证，以及开环与闭环基线设置。

- **判断**：值得精读动作表示与闭环实验；机制简洁且提升明显，但“物理合理”的强表述需要轨迹约束证据支持。

## 研究关联

对 VLA 与具身控制研究，它提供了连接语言语义和连续动力学动作的通用思路，尤其适合受实时性和轨迹平滑性约束的系统。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/Continuous Actions from Discrete Minds Latent-Aligned Planning for End-to-End Au.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04070v1 Announce Type: cross Abstract: Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematics and encoding trajectory features into a structured latent space. Rather than discrete codebook lookups that inevitably introduce quantization errors, LaPla repurposes this representation as a physical prior to bridge the modality gap between high-dimensional semantics and the raw action space. Specifically, given multimodal inputs integrating multi-view images, historical actions, and textual instructions, LaPla incorporates concurrent action queries to causally attend to the multimodal context in a single forward pass, projecting hidden states directly into the pretrained VQ-VAE latent space. The frozen decoder then translates these continuous latents into actions, effectively eliminating quantization errors and ensuring physically plausible trajectories while bypassing time-consuming autoregressive generation. Extensive experiments on the nuScenes benchmark demonstrate that LaPla achieves competitive open-loop performance, reducing long-horizon L2 error by 15.52% compared to state-of-the-art VLA methods. Closed-loop evaluations on the NVIDIA AlpaSim simulator further confirm its superior capability in ensuring smooth driving progress, improving the success rate by 33.34 percentage points with significantly reduced inference latency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04070
- Authors: Ruoyu Yao, Yusen Xie, Qingzhao Liu, Pei Liu, Zewei Yang, Yipeng Zhu, Xiaolong Wang, Jun Ma
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
