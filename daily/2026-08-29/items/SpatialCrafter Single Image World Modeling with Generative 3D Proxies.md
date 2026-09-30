---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27073"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-08-29
concepts: ["世界模型", "具身智能评测与基准"]
---

# SpatialCrafter: Single Image World Modeling with Generative 3D Proxies

> [!summary] 先说人话（基于摘要）
> SpatialCrafter把单图场景生成拆成“先搭可对齐的3D骨架、再补照片级外观”：PaSS Flow生成全局3D代理，Generative Deferred Refiner沿该几何细化视频。

## 问题

以稀疏点云或二维全景为条件的视频扩散模型缺少完整几何约束，容易随机脑补、长期漂移，并在快速相机运动或极端视角下失去3D一致性。

## 创新点或方法

输入单张图像，先由Point-anchored Sparse Structure Flow预测空间对齐、几何一致的3D代理，再让预训练VDM作为生成式延迟细化器补充高频外观。并行几何注入与代理感知损坏训练用于接入代理、容忍其伪影且尽量不破坏预训练生成分布。

## 证据

构建了11.5万场景的混合图像到场景数据集；摘要称在合成和真实数据上超过先进方法，并改善长期漂移及极端视角一致性，但没有具体性能数字。


## 局限

需要核查3D代理的真实几何精度、长轨迹一致性指标，以及对代理错误的鲁棒性是否牺牲细节或多样性。

- **判断**：值得精读架构和数据构建；若目标是物理世界模型，则先看实验是否超出视图合成。

## 研究关联

对世界模型研究者，这是用全局几何代理约束视觉想象的实用途径；对具身评测，可生成可探索场景，但摘要未证明其物理交互性或可作为机器人动力学模拟器。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/SpatialCrafter Single Image World Modeling with Generative 3D Proxies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27073v1 Announce Type: new Abstract: Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generation. Specifically, we decompose the generation process into global proxy generation and appearance refinement. For proxy generation, we propose a Point-anchored Sparse Structure~(PaSS) Flow module that predicts a spatially aligned and geometrically consistent 3D proxy. For appearance refinement, we re-frame the VDM as a Generative Deferred Refiner which synthesizes high-frequency photorealistic details upon proxy-defined scene geometry. To better integrate the proxy with the pre-trained VDM, we introduce Parallel Geometry Injection and Proxy-Aware Corruption training strategies, which improve robustness to proxy artifacts without disrupting the pretrained generative manifold. Furthermore, as no suitable dataset exists for this explorable scene generation task, we construct a new large-scale dataset of 115K scenes. To the best of our knowledge, it is the first hybrid dataset for image-to-scene generation. Extensive experiments on both synthetic and real-world datasets show that SpatialCrafter outperforms state-of-the-art methods, mitigates long-term drift, and remains robust and consistent under rapid camera motion and extreme viewpoint changes. Code, models, and the newly constructed dataset will be publicly released. See more at https://fangchuan.github.io/SpatialCrafter/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27073
- Authors: Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
