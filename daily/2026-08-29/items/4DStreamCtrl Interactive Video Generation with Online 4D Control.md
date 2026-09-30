---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25479"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 26
created: 2026-08-29
concepts: ["智能体 Agent", "世界模型"]
---

# 4DStreamCtrl: Interactive Video Generation with Online 4D Control

> [!summary] 先说人话（基于摘要）
> 4DStreamCtrl用统一3D点轨迹同时表示相机运动、物体运动和深度编辑，并把视频扩散模型蒸馏成四步去噪的因果流式生成器，实现在线4D控制。

## 问题

现有相机控制不能移动物体，二维轨迹忽略深度和遮挡，三维控制方法又多为固定长度的离线生成；缺少同时控制相机与物体、保持3D一致且实时流式运行的方案。

## 创新点或方法

从野外视频挖掘3D运动监督形成OpenVidHD-Motion3D，以轻量Geometric Motion Head接入预训练扩散模型。时间可分编码器进一步蒸馏为因果学生，输入在线点轨迹控制，输出任意长度视频，且内存不随长度增长。

## 证据

摘要称运动控制精度超过相机、二维及离线三维方法；480p下单张高端GPU达到20 FPS、四步去噪，并在数百帧上保持时间连贯。未给出精度指标。


## 局限

需核查“内存与长度无关”的运行条件、数百帧一致性的量化方式，以及生成速度是否包含全部控制与解码开销。

- **判断**：值得精读，尤其是交互世界模型研究者；核心接口清晰且有速度数字，但物理正确性仍需看实验。

## 研究关联

对世界模型与具身Agent，这是把显式3D控制、实时视觉想象和长时流式推演结合起来的工程范式，可能用于闭环模拟与规划；但摘要未展示机器人控制收益。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/4DStreamCtrl Interactive Video Generation with Online 4D Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.25479v2 Announce Type: replace Abstract: Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combines 3D-consistent control of both camera and objects with real-time, streaming generation. Here we show that camera motion, object trajectories, and depth can be unified into a single 3D point-track representation, from which one model performs joint camera and object control, depth editing, and motion transfer in a single forward pass. To learn this interface at scale, we mine in-the-wild video for 3D motion supervision, yielding OpenVidHD-Motion3D, and encode it with a lightweight Geometric Motion Head that plugs into a pretrained video diffusion model. Because this encoder is temporally separable, we distill the model into a causal streaming student that generates arbitrarily long video in four denoising steps at memory independent of length. This unified design surpasses prior camera-only, 2D, and offline-3D methods in motion-control precision while covering modalities they address only in isolation. 4DStreamCtrl runs at 20 FPS on a single high-end GPU for 480p video and stays temporally coherent over hundreds of frames, enabling, to our knowledge, interactive 4D-controllable streaming generation for the first time. More broadly, grounding generation in explicit 3D geometry with efficient causal inference points toward interactive world models with closed-loop spatiotemporal control, from controllable simulators to real-time visual imagination for embodied agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25479
- Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
