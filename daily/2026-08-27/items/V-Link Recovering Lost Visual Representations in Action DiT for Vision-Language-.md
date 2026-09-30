---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25308v1"
published: "2026-08-26T02:32:18Z"
age_days: 1
score: 43
created: 2026-08-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# V-Link: Recovering Lost Visual Representations in Action DiT for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> V-Link 针对 VLM 到 Action DiT 的视觉信息损失，学习互补的 Spatial Query 和 Semantic Query，并经非对称路径注入动作专家，分别补回几何条件和语义信息。

## 问题

VLA的动作专家无法充分访问VLM特征中的3D几何和2D语义，导致精细操作的感知落地不足。仅把原始图像token传给动作模块，不能保证空间信息被保留。

## 创新点或方法

在VLM内部产生空间与语义查询；语义查询补充原有图像token，空间查询则为Action DiT提供专门的几何条件。与普通VL到动作特征传递相比，它显式区分并恢复两类视觉表示。

## 证据

相对GR00T N1.6，LIBERO、LIBERO-Plus和RoboTwin 2.0平均成功率分别提升1.9、31.2和18.8个百分点；AGIBOT A3 Ultra两个真实人形任务提升20和24个百分点。


## 局限

各基准增益差异很大，摘要没有给出绝对成功率，也无法判断查询机制与额外容量谁是主要贡献。

- **判断**：值得精读接口设计和特征分析；LIBERO-Plus与真实任务增益醒目，但需核查绝对基线和公平计算预算。

## 研究关联

这是改造现有VLA动作头的针对性方案，说明基础VLM“看见了”不等于动作专家“用得上”；对精细空间操作尤其有参考价值。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/V-Link Recovering Lost Visual Representations in Action DiT for Vision-Language-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models provide a scalable path toward generalist robotic manipulation by integrating visual perception, language understanding, and continuous action control. However, we reveal a critical limitation of VLA architectures: the action expert has limited access to the 3D geometric and 2D semantic information available in VLM features. This accessibility gap weakens perceptual grounding and limits performance on fine-grained robotic manipulation. To address this issue, we propose V-Link, which explicitly recovers visual representations during the vision-language (VL) to action (A) feature transfer. Specifically, V-Link learns complementary Spatial and Semantic Query representations within the VLM and injects them into Action DiT through asymmetric pathways. Semantic Queries complement the original VLM image tokens, whereas Spatial Queries provide dedicated geometric conditioning for spatially grounded action generation. Across LIBERO, LIBERO-Plus, and RoboTwin 2.0, our V-Link improves the average success rate over base model GR00T N1.6 by +1.9%, +31.2%, and +18.8%, respectively. On the AGIBOT A3 Ultra, V-Link further achieves gains of +20% and +24% on two real-world humanoid tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25308v1
- Authors: Yehao Lu, Jiarui Yang, Yuning Su, Yufeng Xie, Yu Zhong, Yazhou Zhang, Haiyu Lan, Kaixiang Lu, Peiwen Lin, Chuang Wang, Zequn Qin, Enyu Li, Xi Li
- Published: 2026-08-26T02:32:18Z
- Age days: 1

</details>
