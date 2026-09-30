---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04070v1"
published: "2026-09-03T16:42:11Z"
age_days: 3
score: 31
created: 2026-09-07
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving

> [!summary] 先说人话（基于摘要）
> LaPla 用VQ-VAE学到的动作潜空间作为物理先验，却不做离散码本查询；VLA一次前向直接输出连续潜变量，再由冻结解码器生成平滑轨迹。

## 这篇到底在做什么

- **卡在哪里**：VLM偏离散语义推理，而自动驾驶动作连续且受物理约束；离散动作token会带来量化误差，自回归生成又增加时延。
- **关键解法**：输入包括多视角图像、历史动作和文本指令；并发action queries因果关注这些上下文，将隐藏状态投影到预训练VQ-VAE潜空间，冻结解码器输出连续动作。关键差异是借用离散表征学习出的结构，但绕过码本查找和自回归。
- **拿什么证明**：nuScenes开放环评测中，长时L2误差相对先进VLA降低15.52%；NVIDIA AlpaSim闭环评测成功率提高33.34个百分点，并显著降低推理延迟，但摘要未给绝对成功率和延迟。

## 值不值得读

- **和你的研究有什么关系**：对VLA和具身规划研究者，它给出从语言视觉隐状态到连续、物理合理控制的高效接口，尤其适合时延敏感任务。
- **先别急着信**：开放环与模拟闭环结果不能直接证明真实道路安全；需核查物理合理性约束究竟来自潜空间还是训练数据，以及比较时延的统一口径。
- **判断**：值得读动作表示和闭环实验；它对“连续控制是否必须离散token化”给出了明确且实用的反例。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Continuous Actions from Discrete Minds Latent-Aligned Planning for End-to-End Au.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematics and encoding trajectory features into a structured latent space. Rather than discrete codebook lookups that inevitably introduce quantization errors, LaPla repurposes this representation as a physical prior to bridge the modality gap between high-dimensional semantics and the raw action space. Specifically, given multimodal inputs integrating multi-view images, historical actions, and textual instructions, LaPla incorporates concurrent action queries to causally attend to the multimodal context in a single forward pass, projecting hidden states directly into the pretrained VQ-VAE latent space. The frozen decoder then translates these continuous latents into actions, effectively eliminating quantization errors and ensuring physically plausible trajectories while bypassing time-consuming autoregressive generation. Extensive experiments on the nuScenes benchmark demonstrate that LaPla achieves competitive open-loop performance, reducing long-horizon L2 error by 15.52% compared to state-of-the-art VLA methods. Closed-loop evaluations on the NVIDIA AlpaSim simulator further confirm its superior capability in ensuring smooth driving progress, improving the success rate by 33.34 percentage points with significantly reduced inference latency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04070v1
- Authors: Ruoyu Yao, Yusen Xie, Qingzhao Liu, Pei Liu, Zewei Yang, Yipeng Zhu, Xiaolong Wang, Jun Ma
- Published: 2026-09-03T16:42:11Z
- Age days: 3

</details>
