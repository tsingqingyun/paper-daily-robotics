---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2602.06504"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-09-04
concepts: ["具身智能评测与基准"]
---

# MultiGraspNet: A Multitask 3D Vision Model for Multi-gripper Robotic Grasping

> [!summary] 先说人话（基于摘要）
> MultiGraspNet用一个多任务3D网络同时为平行夹爪和吸盘预测可行位姿与逐点可抓取性。它共享早期场景特征、保留夹具专属精炼器，使单臂能高效切换末端执行器。

## 问题

现有抓取模型往往只支持单一夹具，可能需要昂贵双臂系统；另一类定制混合夹具又依赖不可迁移的专用学习逻辑，难以跨任务复用。

## 创新点或方法

先对齐GraspNet-1Billion和SuctionNet-1Billion标注，以统一3D场景输入训练两种夹具任务；共享前段特征提取，之后分别精炼平行抓取和真空吸附候选，并输出场景点抓取适宜度掩码及可行姿态。

## 证据

模型规模为15.75M参数，可在单GPU快速推理；摘要称在相关基准上与单任务模型有竞争力且计算成本更低，真实单臂多夹具实验优于基于归一化的多夹具方法。未给出成功率或时延数字。


## 局限

摘要仅涉及平行夹爪和吸盘，且没有定量说明共享学习对各任务是否存在负迁移；真实实验规模也需全文确认。

- **判断**：需要单臂多夹具抓取的人值得精读数据对齐与多任务结构；其通用性目前不应外推到更多夹具类型。

## 研究关联

对工业机器人和抓取评测研究者，它把多种末端执行器纳入统一感知表示，可降低为每种夹具维护独立模型的成本，并为策略选择“用什么夹具抓”提供输入。

- **概念**：具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/MultiGraspNet A Multitask 3D Vision Model for Multi-gripper Robotic Grasping.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2602.06504v2 Announce Type: replace Abstract: Vision-based models for robotic grasping automate critical, repetitive, and draining industrial tasks. Existing approaches are typically limited in two ways: they either target a single gripper and are potentially applied on costly dual-arm setups, or rely on custom hybrid grippers that require ad-hoc learning procedures with logic that cannot be transferred across tasks, restricting their general applicability. In this work, we present MultiGraspNet, a novel multitask 3D deep learning method that predicts feasible poses simultaneously for parallel and vacuum grippers within a unified framework, enabling a single robot to handle multiple end effectors. The model is trained on the richly annotated GraspNet-1Billion and SuctionNet-1Billion datasets, which have been aligned for the purpose, and generates graspability masks quantifying the suitability of each scene point for successful grasps. By sharing early-stage features while maintaining gripper-specific refiners, MultiGraspNet effectively leverages complementary information across grasping modalities. This design preserves a compact architectural footprint of only 15.75M parameters and enables fast inference on a single GPU, enhancing adaptability and efficiency in cluttered scenes. We characterize MultiGraspnet's performance with an extensive experimental analysis, demonstrating its competitiveness with single-task models on relevant benchmarks while reducing computational cost. Moreover, real-world experiments on a single-arm multi-gripper robotic setup show that our approach outperforms normalization-based multi-gripper approaches. Project page: https://vandal-lab.github.io/multigraspnet-project

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2602.06504
- Authors: Stephany Ortuno-Chanelo, Paolo Rabino, Enrico Civitelli, Tatiana Tommasi, Raffaello Camoriano
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
