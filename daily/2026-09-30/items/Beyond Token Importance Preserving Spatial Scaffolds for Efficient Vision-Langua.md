---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.36967v1"
published: "2026-09-29T08:03:21Z"
age_days: 0
score: 32
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference

> [!summary] 先说人话（基于摘要）
> GeoScaffold 压缩 VLA 的视觉 token 时，同时保留任务相关信息和画面的空间覆盖。它避免只留下显眼物体、却让其他区域出现大块视觉盲区。

## 问题

已有剪枝主要按语义重要性挑选单个 token，忽略操作需要的空间结构。简单几何采样在某些预算下反而更好，却可能因预算略减而崩溃，说明成功率对保留位置的分布敏感。

## 创新点或方法

用最大空间盲区定义覆盖半径，分析 token 空间结构与任务成功的关系。GeoScaffold 将图像分区，按任务相关性分配区域预算，再用最远点采样选取区域内 token，兼顾相关性和覆盖；无需训练。

## 证据

在 π₀.₅ 和 LIBERO 上，仅保留 20% 视觉 token 时平均成功率为 93.2%，相对未剪枝基线实现 1.78 倍 prefill 加速。摘要还报告空间结构与任务成功存在强相关。

## 局限

1.78 倍是 prefill 加速，不能等同端到端控制提速；摘要未给出未剪枝成功率，无法仅据此计算性能损失。

- **判断**：值得读算法并复现 token 预算曲线，方法切口清楚，但部署收益要结合完整推理耗时评估。

## 研究关联

对高效 VLA，提供了可直接检验的几何保留原则，也提醒多模态模型压缩不能只依赖语言任务式的语义重要性。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Beyond Token Importance Preserving Spatial Scaffolds for Efficient Vision-Langua.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a purely geometric pruning strategy. Surprisingly, Stride outperforms semantic pruning and random pruning at certain pruning ratios, but collapses when the token budget is only slightly reduced. We characterize this phenomenon through the spatial coverage radius, defined as the largest spatial blind spot induced by the retained token set after pruning. Our analysis reveals a strong correlation between the spatial structure of retained tokens and task success, suggesting that reliable VLA pruning requires preserving not only task-relevant tokens but also the spatial scaffold of the scene. Motivated by this diagnosis, we propose GeoScaffold, a training-free visual token pruning method that partitions each image into spatial regions, allocates inter-region token budgets using task-relevance weights, and selects intra-region scaffold tokens via farthest point sampling to reduce the local coverage radius. On pi 0.5 and LIBERO, GeoScaffold retains only 20% of visual tokens while preserving a 93.2% average success rate, and achieves a 1.78 times prefill speedup over the unpruned baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.36967v1
- Authors: Jiayu Chen, Shuyong Gao, Jingkai Jia, Xiaosheng Bu, Jiyuan Fu, Lingyi Hong, Kaixun Jiang, Yipan Xu, Wenqiang Zhang
- Published: 2026-09-29T08:03:21Z
- Age days: 0

</details>
