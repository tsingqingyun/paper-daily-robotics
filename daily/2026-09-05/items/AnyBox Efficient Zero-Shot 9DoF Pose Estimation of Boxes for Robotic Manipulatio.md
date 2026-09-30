---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2511.15884"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-09-05
concepts: ["世界模型", "具身智能评测与基准"]
---

# AnyBox: Efficient Zero-Shot 9DoF Pose Estimation of Boxes for Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> AnyBox 利用箱体几何规则，从单帧 RGB-D 零样本估计6D姿态和3D尺寸。它交替估计位姿与尺度，用模板重投影和观测掩码误差搜索尺寸，并以深度一致性和提前停止加速、消歧。

## 问题

仓储箱体常有对称、弱纹理和严重遮挡；依赖每个实例 CAD 的方法维护成本高，而无模型或类别级方法又没有充分利用箱体结构先验，容易产生姿态歧义。

## 创新点或方法

从标准类别模板出发，AnyBox 在位姿与尺度之间交替优化，通过重投影轮廓差异对尺寸做二分搜索；深度一致性过滤器排除对称性造成的不合理假设，提前停止后以一次闭式更新替代剩余搜索。

## 证据

在公共基准和自建仓储数据上，检测 AP 最高提高36点、超过此前最佳两倍，并接近使用真实 CAD 的实例级管线；杂乱环境箱体上架成功率提高28%。


## 局限

该方法显然依赖箱体规则性；需核查对非理想纸箱、损坏、透明表面和极端遮挡的适用边界，以及 AP 的具体定义。

- **判断**：面向物流操作很值得精读，方法针对性强且有下游收益；若研究通用物体姿态，其可迁移价值较有限。

## 研究关联

对仓储机器人，这是无需维护实例 CAD 库的实用感知模块，可直接改善抓取和上架；对具身研究，它说明强任务几何先验有时比通用大模型更高效。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/AnyBox Efficient Zero-Shot 9DoF Pose Estimation of Boxes for Robotic Manipulatio.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2511.15884v2 Announce Type: replace-cross Abstract: Recovering the 9D pose of objects, both their 6D pose and 3D dimensions, under clutter and occlusion is a core requirement for warehouse automation, logistics, and manufacturing. Model-based methods are accurate but assume an instance-specific CAD model for every object, which is costly to maintain as inventories change. Model-free and category-level methods relax this assumption, yet they remain vulnerable to the symmetry, weak texture, and heavy occlusion that characterize stacked storage boxes, and they ignore the strong structural priors such scenes provide. We present \textbf{AnyBox}, an efficient zero-shot framework that exploits the geometric regularity of boxes to jointly recover pose and dimensions from a single RGB-D observation. Starting from a canonical category template, AnyBox alternates between pose and scale estimation, using the discrepancy between the reprojected template and the observed mask to drive a binary search over box dimensions. Two lightweight components make this practical: a depth-consistency filter that rejects the implausible hypotheses induced by box symmetry, and an early-stopping rule that replaces the remaining search with a single closed-form update. On public benchmarks and an in-house warehouse dataset, AnyBox improves detection AP by up to 36 points, more than doubling the previous best, and approaches instance-level pipelines that have access to ground-truth CAD models. These gains transfer downstream, raising success by 28\% on a cluttered robotic box-shelving task.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2511.15884
- Authors: Yintao Ma, Sajjad Pakdamansavoji, Charles Eret, Rui Heng Yang, Xuan Zhao, Yingxue Zhang, Tongtong Cao, Amir Rasouli
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
