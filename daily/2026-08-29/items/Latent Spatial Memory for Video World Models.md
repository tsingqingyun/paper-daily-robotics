---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09828"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 18
created: 2026-08-29
concepts: ["世界模型"]
---

# Latent Spatial Memory for Video World Models

> [!summary] 先说人话（基于摘要）
> Mirage不再把世界模型的三维记忆存成RGB点云，而是把扩散潜token按深度反投影到3D缓存，并直接在潜空间扭曲生成新视角，减少信息损失和重复编解码。

## 这篇到底在做什么

- **卡在哪里**：现有保持3D一致性的视频世界模型常使用RGB点云记忆，需要反复渲染和VAE编码，计算昂贵；潜表示往返像素空间还会丢失丰富特征。
- **关键解法**：输入视频潜表示和深度，将潜token反投影到持久3D空间缓存；查询时直接将缓存中的潜特征扭曲到新视角，再供扩散模型生成。关键差异是整个空间记忆与视图合成都留在潜空间。
- **拿什么证明**：相对显式3D基线，端到端视频生成最高加速10.57倍、记忆占用降低55倍；摘要称其在WorldScore达到先进水平，并在RealEstate10K有较强重建质量，但未给出质量分数。

## 值不值得读

- **和你的研究有什么关系**：对世界模型研究者价值直接：它同时处理长期空间一致性、速度与内存瓶颈，更接近可用于交互Agent的持久场景记忆。
- **先别急着信**：需核查速度与内存比较是否在相同分辨率、轨迹和质量下进行，以及深度误差累积会怎样污染持久潜记忆。
- **判断**：今天值得精读的世界模型系统论文之一；效率数字突出，优先看对比设置、记忆更新和长期一致性实验。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：18
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Latent Spatial Memory for Video World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.09828v2 Announce Type: replace Abstract: Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space. This design is both computationally expensive, requiring repeated rendering and VAE encoding, and inherently lossy, as the round trip through pixel space discards rich features of the learned latent representation. In this paper, we introduce \emph{latent spatial memory} for video world models, a persistent 3D cache that stores scene information directly in the diffusion latent space, avoiding pixel-space reconstruction. Building on this, we propose Mirage, a latent-space spatial memory framework that constructs the memory by lifting latent tokens into 3D via depth-guided back-projection and queries it by synthesizing novel views through direct latent-space warping. This unified formulation eliminates both the information loss of pixel-space reconstruction and the computational burden of repeated encoding and rendering. Experiments show that latent spatial memory achieves up to \textbf{10.57}$\times$ faster end-to-end video generation and \textbf{55}$\times$ reduction in memory footprint relative to explicit 3D baselines. Leveraging the geometric prior of the diffusion model, Mirage attains state-of-the-art performance on WorldScore and strong reconstruction quality on RealEstate10K.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09828
- Authors: Weijie Wang, Haoyu Zhao, Yifan Yang, Feng Chen, Zeyu Zhang, Yefei He, Zicheng Duan, Donny Y. Chen, Yuqing Yang, Bohan Zhuang
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
