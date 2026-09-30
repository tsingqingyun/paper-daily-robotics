---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03657v1"
published: "2026-09-03T10:54:49Z"
age_days: 3
score: 29
created: 2026-09-07
concepts: ["具身智能评测与基准"]
---

# Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations

> [!summary] 先说人话（基于摘要）
> 论文把3DGS中的高斯视作三维“像素”，直接扰动其尺度、旋转和删减，低成本生成跨视角一致的伪影训练样本，从而训练更强的3D视频先验。

## 问题

稀疏视角NeRF/3DGS易产生严重伪影；现有生成式修复器依赖每个场景分别重建腐坏—干净配对数据，成本高，而普通2D增强不能保持多视角空间一致性。

## 创新点或方法

3D Morphological Perturbations直接作用于显式3DGS参数，无需优化循环即可构造空间一致扰动；作者先在轻量视频扩散沙箱诊断，再通过ControlNet扩展到14B视频模型，输出用于修复或建模的3D感知视频先验。

## 证据

相对先进图像到图像3D伪影修复器，平均深度误差降低12.5%；在4个操作任务中的3个上，下游机器人策略成功率最高提升8.0%。摘要称同时保持视觉保真度。


## 局限

“最高提升8.0%”未说明是相对还是绝对变化，且1个任务未提升；视觉保真和不同扰动强度的权衡需核查。

- **判断**：做3D数据生成或视频先验者值得精读；机器人学习读者重点看下游迁移实验即可。

## 研究关联

对用生成视频或3D重建训练机器人策略的人，它提供了无需逐场景优化的数据增强机制，并显示几何改进可传递到操作成功率。

- **概念**：具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Rethinking 3D Noise Learning 3D-Aware Video Priors via Optimization-Free Morphol.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

3D scene representations like NeRF and 3D Gaussian Splatting (3DGS) suffer severe artifacts in sparse-view settings. Recent generative 3D artifact fixers attempt to address this, but rely on paired corrupted and clean renders requiring costly, per-scene reconstructions across varying view configurations. While 2D image augmentations act as instant regularizers, no explicit equivalents exist for 3D representations to preserve spatial consistency across views, an essential property for 3D-aware training. We propose 3D Morphological Perturbations as an optimization-free regularizer that preserves spatial consistency. Leveraging explicit 3DGS, we treat each Gaussian as a fundamental building block - analogous to a 2D pixel - and apply perturbations across its morphological parameter space via scale, rotation, and pruning. Our method eliminates per-scene 3DGS optimization loops from dataset curation while enabling models to learn stronger geometric priors than sparse-view baselines in diagnostic ablations conducted on a lightweight video diffusion sandbox. Scaled to a 14B-parameter video model via ControlNet, our approach maintains visual fidelity while reducing mean depth error by 12.5% over state-of-the-art image-to-image 3D artifact refiners, ultimately boosting downstream robotics policy success rates by up to 8.0% across 3 of 4 manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03657v1
- Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
- Published: 2026-09-03T10:54:49Z
- Age days: 3

</details>
