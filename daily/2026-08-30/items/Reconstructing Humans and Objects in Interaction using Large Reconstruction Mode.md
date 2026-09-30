---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27407v1"
published: "2026-08-27T17:35:46Z"
age_days: 2
score: 30
created: 2026-08-30
concepts: ["具身智能评测与基准"]
---

# Reconstructing Humans and Objects in Interaction using Large Reconstruction Models

> [!summary] 先说人话（基于摘要）
> MILO用大型重建模型的网格作为人—物三维关系脚手架，再把网格分割成人与物，拟合人体模型，并在有模板时对齐物体。

## 问题

单图 3D 人物交互重建受深度歧义、遮挡和物体形状多样性影响；现有方法主要靠二维重投影、接触约束和模板拟合，难恢复细致几何及可靠相对布局。

## 创新点或方法

输入单张交互图像，先由 LRM生成保留人物相对位置与邻近关系的网格；随后解释和分割该网格，对人体部分拟合参数化身体模型，物体模板可用时再选择性对齐。区别是以生成式三维网格为几何先验，而非主要从二维约束优化。

## 证据

摘要称在多个基准和交互场景上取得较强重建精度并超过现有基线；未给出数据集、指标或结果数字。


## 局限

需核查 LRM 网格错误如何传播，以及无物体模板、强遮挡和新物体上的精度；“强结果”缺少数字。

- **判断**：3D HOI 研究者值得看完整评测；机器人学习读者可先读方法，确认输出精度足以支持下游再深入。

## 研究关联

对具身感知研究者，它可能为从人类示范中提取空间关系、接触上下文和物体布局提供前端；但摘要没有证明其直接改善机器人策略。

- **概念**：具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Reconstructing Humans and Objects in Interaction using Large Reconstruction Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Estimation of Human-Object Interactions in 3D (3D HOI) is a fundamental problem in 3D computer vision with applications in AR/VR, robotics, and embodied AI. However, reconstructing these interactions in 3D remains challenging due to depth ambiguities, occlusions, and object shape variability. Existing approaches are primarily concerned with reprojection and contact constraints, fitting parametric human models and object templates to 2D images. In this paper, we explore a different avenue. We present MILO, a framework that leverages the visual capabilities of Large Reconstruction Models (LRMs) to recover detailed 3D human-object interactions from a single image. Our key observation is that LRMs provide a powerful geometric scaffold that preserves relative human-object arrangement and proximity cues. This significantly simplifies the reconstruction procedure, reframing the problem as interpreting the LRM mesh: we segment it into human and object components, fit a parametric body model to the human part, and optionally align an object template to the object part (if such a template is available). MILO achieves strong reconstruction accuracy and outperforms existing baselines across multiple benchmarks and interaction scenarios. Our code is available at https://ac5113.github.io/MILO.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27407v1
- Authors: Agniv Chatterjee, Georgios Pavlakos
- Published: 2026-08-27T17:35:46Z
- Age days: 2

</details>
