---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31357v1"
published: "2026-09-25T14:54:15Z"
age_days: 2
score: 29
created: 2026-09-28
concepts: ["具身智能评测与基准"]
---

# Transformer-based Monte Carlo Localization in Construction Meshes

> [!summary] 先说人话（基于摘要）
> 这项方法让施工机器人用 LiDAR 在建筑网格地图中找回全局位置。网络提供带不确定性的候选位置，蒙特卡洛定位再用粒子维护与更新位姿假设。

## 问题

施工巡检和数字化要求机器人定位到建筑地图共享的全局坐标系。相似房间和低纹理表面使现有 LiDAR、视觉定位容易混淆，并可能出现粒子退化后难以恢复的问题。

## 创新点或方法

仅用建筑网格内模拟的 LiDAR 扫描训练 PointNet++ 编码器与地点识别解码器，输出作为 MCL 的学习观测模型。不确定性感知解码器调整位置似然，重采样时注入模型假设帮助恢复。

## 证据

真实数据集评估中优于扩散方法和 ScanContext++ 基线，单次推理为 18 毫秒。摘要未给出定位误差、成功率或数据集规模。

## 局限

需核查网格与真实施工现场不一致时的表现，以及 18 毫秒对应网络调用还是完整定位更新。

- **判断**：施工机器人与全局重定位方向值得读实验，操作型 VLA 研究者可略读。

## 研究关联

对具身定位评测研究者，提供了将合成训练、学习观测模型与概率定位结合的案例；与 VLA 或操作世界模型的直接关联有限。

- **概念**：具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Transformer-based Monte Carlo Localization in Construction Meshes.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

To be able to perform inspection or digitization tasks, mobile robots on construction sites must be able to localize themselves reliably with respect to a global reference frame that is shared with a building map. Similar room layouts and low-texture surfaces pose a challenge for existing LiDAR- and vision-based localization methods. We approach this problem with a LiDAR-based global relocalization system that estimates the robot's pose relative to a building mesh and combines a PointNet++ encoder with a place recognition decoder, whose outputs serve as a learned observation model within a Monte Carlo Localization (MCL) framework. The pipeline is trained exclusively on synthetic LiDAR scans obtained by simulating the robot's sensors inside the building mesh. Our approach is robust in ambiguous environments due to an uncertainty-aware decoder that scales positional likelihoods and a resampling strategy that injects model hypotheses into the particle set, enabling recovery from potential particle depletion. Evaluations on real-world datasets show that our method outperforms both diffusion-based and ScanContext++ baselines while maintaining fast inference (18 ms per call), demonstrating the practicality of synthetic-data training for mesh-referenced global localization in construction robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31357v1
- Authors: Linus Kramer, William Talbot, Olga Vysotska, Marco Hutter
- Published: 2026-09-25T14:54:15Z
- Age days: 2

</details>
