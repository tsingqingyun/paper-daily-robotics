---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07775"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 19
created: 2026-08-29
concepts: ["世界模型", "具身智能评测与基准"]
---

# DALE-CT: Depth-Aware 2D Slice Encoders Learn an Anatomical World Model of Chest CT

> [!summary] 先说人话（基于摘要）
> DALE-CT让二维切片ViT通过跨物理z轴厚层采样，自监督学习相邻切片间的解剖变化，因而形成连续的胸部CT“解剖世界模型”，无需三维或位置监督。

## 问题

胸部CT量大但体素级专家标注昂贵；孤立切片训练看不到沿身体纵轴的结构变化，难以形成扫描级解剖组织。纯二维方法又通常缺少三维与位置监督。

## 创新点或方法

以depth-aware slab sampling从一个物理厚层内抽取多个自监督视图，用LeJEPA从零训练二维ViT。冻结表示应形成扫描的平滑轨迹；部分版本再以解剖和异常掩码监督patch与slice token，并与持续预训练的DINOv2比较。

## 证据

孤立切片对照未形成该表示。九个模型统一评测中，DALE-CT-2S在CT-RATE达到0.825 Macro AUROC，比COLIPRI-CRM低0.024且无需文本监督；无监督版本扩展到约28.7万次扫描，并取得最佳二维外部迁移点估计。


## 局限

“世界模型”在此主要指解剖序列表征，需避免与动力学模拟混同；外部迁移只报告最佳点估计，统计可靠性需全文核查。

- **判断**：医学影像自监督研究者值得精读；通用世界模型研究者可读采样设计，但不应将其视为交互环境建模证据。

## 研究关联

对世界模型概念，它展示了用局部序列预测学到隐式解剖坐标；但这是医学表征模型，不是可行动、可交互的具身世界模型。对基准研究的价值在统一评测协议。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：19
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/DALE-CT Depth-Aware 2D Slice Encoders Learn an Anatomical World Model of Chest C.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.07775v2 Announce Type: replace Abstract: Chest CT is among the highest-volume imaging exams in medicine, yet expert voxel-level annotations are scarce and costly, motivating encoders that learn directly from unlabeled scans. We present DALE-CT, a family of 2D slice-based Vision Transformers trained from scratch on chest CT with the heuristics-free LeJEPA objective. We introduce depth-aware slab sampling, which draws self-supervised views from across a physical $z$-axis slab rather than a single slice, implicitly tasking the 2D encoder with representing how anatomy changes between neighboring slices. The frozen representations trace each scan as a smooth anatomical trajectory, recover cranio-caudal slice ordering without labels, and distinguish slices by the anatomy they contain rather than by position alone. This anatomical world model emerges without any 3D or positional supervision, and an otherwise-identical encoder trained on slices in isolation never develops it. Building on this backbone, we introduce dense auxiliary supervision into the pretraining objective, using anatomical and abnormality masks to supervise patch and slice tokens alongside the self-supervised loss, and we compare the resulting variants against a DINOv2 baseline continually pretrained on CT-RATE. Among nine public and in-house models evaluated under the same protocol, DALE-CT-2S is the strongest 2D model in-domain, reaching 0.825 Macro AUROC on CT-RATE, within 0.024 of COLIPRI-CRM and without any text supervision. We subsequently scale the supervision-free configuration to a $\sim$287k-scan multi-source pool, to our knowledge the largest reported chest-CT pretraining corpus. The resulting DALE-CT-0-L posts the best 2D external-transfer point estimates, and we release it as our recommended backbone with the full model family, training code, and evaluation pipeline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07775
- Authors: Evan W. Damron, Mahmut S. Gokmen, Mitchell A. Klusty, Caroline N. Leach, Emily B. Collier, V. K. Cody Bumgardner
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
