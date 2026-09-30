---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25490v1"
published: "2026-09-21T23:39:19Z"
age_days: 2
score: 29
created: 2026-09-24
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation

> [!summary] 先说人话（基于摘要）
> SAM-V 把多视角几何特征直接送入 SAM，让被提示的同一物体在不同视角下得到一致分割，减少遮挡和视角变化造成的身份混淆。

## 问题

点云三维实例分割受限于三维标注不足，先逐帧分割再离线匹配又容易混淆物体身份。机器人需要在视角和遮挡变化下持续识别同一个操作对象。

## 创新点或方法

将 VGGT 几何特征端到端融入 SAM：用视角相机 token 和局部几何特征丰富稀疏提示，再让掩码解码器同时关注稠密二维与三维特征。一次前向传播生成跨视角掩码，无需离线匹配或显式三维重建。

## 证据

在 IGGT 三维跟踪基准的 ScanNet++ 划分上，相比所述最先进多视角实例分割基线，总体 IoU 提高 5 点、帧级召回提高 12 点；在零样本 ScanNet 划分上所有指标领先。

## 局限

需核查提示输入方式、所需视角数量和推理成本；跟踪基准上的提升不能直接证明机器人动态操作中的实时可靠性。

- **判断**：做多视角感知值得细读融合与解码机制，做纯 VLA 控制可先关注其作为感知模块的适配条件。

## 研究关联

对机器人感知和多模态基础模型研究者，它提供了将几何先验融入提示式分割的方案，可作为跨视角对象关联模块；摘要未验证下游控制收益。

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/SAM-V Geometry-Aware Segment Anything for Multi-View Instance Segmentation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Consistent multi-view object segmentation is critical for 3D perception and robotics, yet remains challenging under severe viewpoint and occlusion changes. Existing methods typically perform 3D instance segmentation on point clouds or rely on offline 2D mask-matching pipelines. However, 3D instance segmentation is limited by scarce 3D annotations, while offline 2D matching suffers from object identity ambiguity across frames. To leverage strong 2D and 3D priors jointly, we propose SAM-V (Geometry-Aware Segment Anything for Multi-View Instance Segmentation). Instead of combining the two priors through post-hoc matching, SAM-V directly integrates features from a feed-forward geometry model (VGGT) into a 2D segmentation foundation model (SAM), trained end-to-end for cross-view instance prediction. SAM-V introduces a prompt-fusion mechanism that enriches sparse SAM prompt tokens with view-specific camera tokens and local VGGT features, making the prompt representation both view-aware and spatially grounded, together with a mask decoder that attends to dense 2D and 3D features. By conditioning the mask decoding directly on multi-view geometry, SAM-V produces consistent multi-view segmentation of a prompted object in a single forward pass without offline mask matching or explicit 3D reconstruction. On the IGGT 3D tracking benchmark, where consistent instance identity across frames directly determines performance, SAM-V improves overall IoU by 5 points and frame-level recall by 12 points on the ScanNet++ split over the state-of-the-art multi-view instance segmentation baseline and leads on all metrics in the zero-shot ScanNet split. Our code and pretrained models are available at https://github.com/gong208/SAM-V.git.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25490v1
- Authors: Jiangshan Gong, Yuqun Wu, Qiqian Fu, Yao Xiao, Chuhang Zou, Shenlong Wang, Derek Hoiem
- Published: 2026-09-21T23:39:19Z
- Age days: 2

</details>
