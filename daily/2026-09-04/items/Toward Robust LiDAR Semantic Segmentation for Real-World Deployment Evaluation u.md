---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02830"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-09-04
concepts: ["具身智能评测与基准"]
---

# Toward Robust LiDAR Semantic Segmentation for Real-World Deployment: Evaluation under Coarse Labels, Adverse Conditions, and Domain Shifts

> [!summary] 先说人话（基于摘要）
> 论文不再只看干净数据上的细粒度mIoU，而从安全相关粗标签、8类LiDAR损坏、无适配跨域以及嵌入式推理速度四方面评估语义分割的部署准备度。

## 问题

现有LiDAR分割评测集中于干净、单域和细粒度标签，无法反映安全语义、恶劣传感条件、域变化和硬件时延，标准榜单因而可能误导真实部署判断。

## 创新点或方法

协议把细粒度类别映射到自动驾驶安全优先的粗标签，分别施加模拟大气、几何及传感器退化的8类损坏，执行无适配跨数据集测试，并在Jetson AGX Orin上测推理速度。输出是多维部署鲁棒性画像，而非单一干净集排名。

## 证据

结果显示，细粒度榜单排序不总能反映安全相关表现；所有方法在损坏下都显著退化，且鲁棒性依赖架构；现有跨域泛化不足以支撑可靠部署。摘要未给出可核查的结果数字。


## 局限

摘要没有披露参与比较的方法、数据集、损坏强度及粗标签映射，协议是否覆盖真实故障分布需要全文核查。

- **判断**：做LiDAR部署或鲁棒评测者应精读协议；它的价值主要在揭示榜单失真，而不是提出新的分割模型。

## 研究关联

对移动机器人和具身评测研究者，该协议把安全语义、传感退化、域偏移及边缘硬件成本放进同一框架，可用于更实际地筛选感知模块。

- **概念**：具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Toward Robust LiDAR Semantic Segmentation for Real-World Deployment Evaluation u.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02830v1 Announce Type: new Abstract: LiDAR-based semantic segmentation is a core perception module for autonomous vehicles and mobile robots. Despite the strong performance of recent state-of-the-art methods on standard benchmarks, existing evaluation protocols remain focused on clean, single-domain settings and fine-grained label taxonomies, leaving deployment readiness largely unassessed. Real-world systems must handle safety-critical label semantics, degraded sensing conditions, and cross-domain variability, yet no unified protocol currently addresses all three aspects together. In this paper, we propose a structured evaluation protocol that assesses the deployment readiness of LiDAR semantic segmentation models along three complementary dimensions: (i) coarse-label evaluation aligned with autonomous driving safety priorities, revealing how label granularity affects different methods; (ii) robustness under eight types of LiDAR corruptions designed to emulate real-world atmospheric, geometric, and sensor degradations; and (iii) domain generalization across datasets without adaptation. The evaluation includes inference speed measured on an embedded Jetson AGX Orin platform, directly reflecting deployment constraints. Our results show that fine-grained benchmark rankings do not always reflect safety-relevant performance, that all methods experience substantial degradation under corruptions with architecture-dependent robustness characteristics, and that current domain generalization remains insufficient for reliable deployment. These findings expose concrete gaps between benchmark performance and deployment readiness, and provide a reference protocol for more practically grounded evaluation of LiDAR semantic segmentation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02830
- Authors: Samir Abou Haidar, Alexandre Chariot, Mehdi Darouich, Cyril Joly, Jean-Emmanuel Deschaud
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
