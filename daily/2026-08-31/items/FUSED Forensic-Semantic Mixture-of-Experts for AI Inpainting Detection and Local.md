---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28302v1"
published: "2026-08-28T13:05:43Z"
age_days: 2
score: 22
created: 2026-08-31
concepts: ["具身智能评测与基准"]
---

# FUSED: Forensic-Semantic Mixture-of-Experts for AI Inpainting Detection and Localization

> [!summary] 先说人话（基于摘要）
> FUSED 同时判断图像是否被扩散模型局部修补，并输出被修改区域掩码。稀疏门控 MoE 按 token 动态融合低层取证痕迹和高层语义特征，以提升跨生成器迁移。

## 这篇到底在做什么

- **卡在哪里**：局部 inpainting 只改变少量像素，而许多检测器依赖全局生成器伪影且不能定位；这些伪影随生成器变化，恢复未修改区域的真实像素又会削弱检测器，导致分布外失效。
- **关键解法**：输入图像，输出图像级操纵分数和像素级修补掩码。稀疏门控专家混合在每个 token 上选择低层取证或高层语义线索，区别于依赖单一全局伪影的检测器。
- **拿什么证明**：在 OpenSDID 跨生成器基准上取得最佳平均检测与定位，未见生成器增益最大；同一模型直接迁移到 AutoSplice 和 CocoGlide 后，定位性能提高到基线的两倍以上。去除或保留全局伪影时 FUSED 均最强，但包括 FUSED 在内的所有方法仍部分依赖该伪影。

## 值不值得读

- **和你的研究有什么关系**：它与具身智能联系很弱；对多模态内容真实性和视觉取证评测者有价值，尤其是同时评价检测、定位与伪影依赖的协议。
- **先别急着信**：作者自己证明模型仍读取全局生成器伪影，因此不能宣称已经学到纯局部取证证据；摘要也未给绝对指标。
- **判断**：做生成图像取证者值得精读，机器人研究者可跳过；方法领先，但未摆脱分布伪影这一核心风险。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：22
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/FUSED Forensic-Semantic Mixture-of-Experts for AI Inpainting Detection and Local.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion-based inpainting models modify only a localized part of an image, while many AI-image detectors rely on global artifacts and do not localize. These artifacts vary across generators, limiting detector transfer under distribution shifts. Recent work shows that restoring the authentic pixels outside the inpainted region removes these cues and can degrade pretrained detectors. To address this, we present FUSED, a unified framework for the joint detection and localization of AI-generated inpainting. FUSED combines low-level forensic cues with high-level semantic features using a sparsely-gated Mixture-of-Experts architecture, enabling the model to adaptively prioritize the most relevant signal for each token. For each input, FUSED predicts both an image-level manipulation score and a pixel-level mask of the inpainted area. On the OpenSDID cross-generator benchmark, FUSED achieves the best average detection and localization, with the largest gains on unseen generators. The same model transfers directly to the held-out AutoSplice and CocoGlide benchmarks, more than doubling localization performance. Evaluating each held-out benchmark with and without the global generator artifact further shows that all evaluated methods, ours included, partly read the artifact as evidence of manipulation, and FUSED remains the strongest under both conditions. Code and pretrained models are available at https://github.com/AntonNuzhdin/FUSED.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28302v1
- Authors: Anton Nuzhdin, Marcel Worring, Ivona Najdenkoska
- Published: 2026-08-28T13:05:43Z
- Age days: 2

</details>
