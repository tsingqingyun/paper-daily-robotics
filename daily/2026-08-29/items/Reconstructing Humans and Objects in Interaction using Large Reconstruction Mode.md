---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27407"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 30
created: 2026-08-29
concepts: ["具身智能评测与基准"]
---

# Reconstructing Humans and Objects in Interaction using Large Reconstruction Models

> [!summary] 先说人话（基于摘要）
> MILO利用大重建模型生成的网格作为人—物相对几何脚手架，再分割人体与物体、拟合人体参数模型，并可选对齐物体模板，从单图恢复3D交互。

## 这篇到底在做什么

- **卡在哪里**：单图3D人—物交互重建受深度歧义、遮挡和物体形状变化影响。旧方法主要靠二维重投影与接触约束拟合人体和物体模板，难以直接获得可靠的相对三维布局。
- **关键解法**：输入一张人—物交互图像，先取得LRM网格并将其分成人体和物体组件；随后对人体部分拟合参数化身体模型，有模板时再对齐物体。关键差异是解释已有重建网格，而非主要从二维约束联合优化两个模板。
- **拿什么证明**：摘要称在多个基准和交互场景中取得较强精度并超过现有基线，但未给出数据集名称、指标或数字。

## 值不值得读

- **和你的研究有什么关系**：可为具身智能数据和评测恢复人—物空间关系、接触上下文或示范几何；它本身不是控制策略或世界模型。
- **先别急着信**：最需核查LRM网格在严重遮挡和陌生物体上的可靠性，以及无物体模板时输出能保留多少可用形状。
- **判断**：做人—物交互感知或示范重建值得读实验与失败案例；机器人控制研究者浏览即可。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Reconstructing Humans and Objects in Interaction using Large Reconstruction Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27407v1 Announce Type: new Abstract: Estimation of Human-Object Interactions in 3D (3D HOI) is a fundamental problem in 3D computer vision with applications in AR/VR, robotics, and embodied AI. However, reconstructing these interactions in 3D remains challenging due to depth ambiguities, occlusions, and object shape variability. Existing approaches are primarily concerned with reprojection and contact constraints, fitting parametric human models and object templates to 2D images. In this paper, we explore a different avenue. We present MILO, a framework that leverages the visual capabilities of Large Reconstruction Models (LRMs) to recover detailed 3D human-object interactions from a single image. Our key observation is that LRMs provide a powerful geometric scaffold that preserves relative human-object arrangement and proximity cues. This significantly simplifies the reconstruction procedure, reframing the problem as interpreting the LRM mesh: we segment it into human and object components, fit a parametric body model to the human part, and optionally align an object template to the object part (if such a template is available). MILO achieves strong reconstruction accuracy and outperforms existing baselines across multiple benchmarks and interaction scenarios. Our code is available at https://ac5113.github.io/MILO.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27407
- Authors: Agniv Chatterjee, Georgios Pavlakos
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
