---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08250v1"
published: "2026-09-08T04:49:42Z"
age_days: 1
score: 26
created: 2026-09-10
concepts: ["世界模型", "具身智能评测与基准"]
---

# CALIPER: Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Representations

> [!summary] 先说人话（基于摘要）
> CALIPER 指出，干净固定视角的测试可能让随机特征也显得很懂物理。它用“先看两次撞击，再预测第三次滑动”及视觉扰动，检查模型是否真正利用交互证据、评测是否能区分模型。

## 问题

操作世界模型常用视觉编码器，但干净场景中的扰动测试与线性探针可能只利用像素位移捷径，无法识别有价值的物理推断表示。

## 创新点或方法

对未知质量和摩擦的物体提供两次已知速度撞击，再从第三次接触前信息预测滑行距离；冻结表示并训练线性读出，交换校准片段检验证据使用，再逐片段改变相机、光照和杂物。

## 证据

2,000 个仿真回合、八种表示中，校准增加 0.50 R²，交换校准则消除增益；干净场景下所有表示距真实状态上限不足 0.02 R²，扰动后差距达 0.50 R²。目标距离控制中，V-JEPA 2 误差 4 mm，随机 ViT 为 20 mm。


## 局限

结论来自特定仿真撞击任务，需核查视觉扰动分布与读出设置，不能据此否定所有线性探针或物理评测。

- **判断**：今天优先精读，尤其值得复用其评测诊断思路，避免在缺乏区分力的基准上选模型。

## 研究关联

直接关系世界模型表示的选型和具身基准设计：高预测分数未必足以给模型排序，必须检查捷径、证据依赖和下游控制价值。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/CALIPER Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Represe.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

How far a pushed object slides depends on its mass and friction, which no single image reveals. Pretrained visual encoders are increasingly used as the perception front end of world models for manipulation, and their physical competence is assessed with perturbation benchmarks and linear probes, almost always in a clean, fixed-camera scene. We show that these assessments cannot distinguish an encoder that infers physics from one that does not. CALIPER (calibrate, then predict) is a direct test: an object of unknown mass and friction is struck twice at known speeds, a third strike is shown only up to the moment of contact, and a linear readout on frozen features must predict how far the object slides. Swapping in another object's calibration clips checks that the evidence is actually used. Across 2,000 simulated episodes and eight representations, from V-JEPA 2 to a randomly initialised ViT and raw pixels, calibration adds +0.50 R^2 and the swap removes it. Yet in the clean scene every representation lands within 0.02 R^2 of the ceiling set by true simulator state, because a fixed camera exposes the object's displacement directly in pixel coordinates. Resampling camera, lighting, and clutter for every clip spreads the same representations across 0.50 R^2; when the readout chooses a push speed for a goal distance, V-JEPA 2 misses by 4 mm and the random ViT by 20 mm, no better than ignoring the object. Linear probes track none of this: a change in frame aggregation moves a probe more than pretraining does, and erasing the probed mass direction from the same representation costs nothing in one scene and 0.35 R^2 in the other. Whether a benchmark can rank models is an empirical property, and we give three checks that establish it.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08250v1
- Authors: Aman Mehta, Riya Baviskar
- Published: 2026-09-08T04:49:42Z
- Age days: 1

</details>
