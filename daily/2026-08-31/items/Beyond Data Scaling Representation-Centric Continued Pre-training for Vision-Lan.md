---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27550v1"
published: "2026-08-27T17:59:40Z"
age_days: 3
score: 45
created: 2026-08-31
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> VLAct 不靠继续堆机器人轨迹，而是通过保留 VLM 先验、多头连续动作协同监督和部分统一的跨本体动作布局，把有限数据转成可迁移的视觉—动作表征。随后仍允许各任务使用专属动作头。

## 这篇到底在做什么

- **卡在哪里**：通用 VLA 需要大量机器人数据，但实体轨迹昂贵且覆盖稀疏；固定数据预算下，普通持续预训练容易只拟合动作，破坏原有视觉语言知识，也难以在不同机器人本体间共享动作语义。
- **关键解法**：先在广泛、异构、多本体机器人数据上持续预训练 VLA 导向的 VLM 骨干；训练时保留 VLM 先验，以多个连续动作头协同监督，并用部分统一的动作布局对齐跨本体语义。微调时输出由任务专属动作头适配，不强求所有本体共用完全一致的动作空间。
- **拿什么证明**：LIBERO-Plus 和 RoboTwin 2.0 成功率分别为 82.6% 和 92.5%，超过摘要所列 ABot-M0、LingBot-VLA；RoboDojo 成功率排名第六，并在两项指标上超过所有明确标为 WAM 的条目。面对未见过的 RoboCasa-GR1 人形本体，仅用 20% 下游轨迹便超过使用全量数据的 GR00T-N1.6；训练使用开源数据和 16 张 GPU。

## 值不值得读

- **和你的研究有什么关系**：对 VLA 和多模态基础模型研究者，它提供了一条独立于数据扩张的路线：在数据和算力有限时，通过跨本体表征设计争取迁移性能。对世界模型研究者的直接价值较弱，主要是其在 RoboDojo 上与 WAM 条目的经验比较。
- **先别急着信**：最需全文核查的是各基准比较是否使用同等模型规模、预训练数据和评测协议；摘要只明确固定了下游微调协议，不能据此断言所有外部系统比较完全等成本。
- **判断**：值得精读方法和跨本体实验：结果覆盖面广且数字具体，但“表示优于扩数”的强结论仍取决于完整的受控比较。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Beyond Data Scaling Representation-Centric Continued Pre-training for Vision-Lan.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling robot data is crucial for building generalist Vision-Language-Action (VLA) models, yet robot trajectories are harder to scale than web-scale image-text data because embodied collection is costly and sparsely covers the physical world. This makes representation quality a central bottleneck: under a fixed robot-data budget, continued pre-training must turn limited trajectories into transferable visual-action knowledge rather than merely fit actions. We propose VLAct, a VLA-oriented VLM backbone trained on broad, heterogeneous, multi-embodiment robot data before task-specific fine-tuning. VLAct preserves the broad VLM prior and encourages shared action semantics across embodiments through VLM-prior preservation, multi-head continuous action co-supervision, and a partially unified cross-embodiment action layout, while allowing task-specific action heads during fine-tuning. Across simulation, real-world, and unseen-embodiment transfer, VLAct consistently improves downstream performance under fixed fine-tuning protocols. On LIBERO-Plus and RoboTwin 2.0, VLAct surpasses industrial VLA systems including ABot-M0 and LingBot-VLA, achieving success rates of 82.6% and 92.5%. On RoboDojo, VLAct ranks sixth among all policies by success rate and outperforms all explicitly designated world-action model (WAM) entries on both metrics. Most notably, on RoboCasa-GR1, an unseen humanoid embodiment, VLAct using only 20% of downstream trajectories outperforms the full-data GR00T-N1.6 baseline. These results are obtained using fully open-source data and only a 16-GPU training setup, showing that representation-centric continued pre-training can deliver highly competitive performance under a modest compute budget and is an important independent axis of VLA progress beyond data scaling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27550v1
- Authors: Senqiao Yang, Chengyao Wang, Yuxin Chen, Zixuan Wang, Longxiang Tang, Haokun Gui, Jinhui Ye, Changsheng Lu, Xiaoyang Wu, Mingkang Zhu, Pengguang Chen, Shu Liu, Zhuotao Tian, Hengshuang Zhao, Bei Yu, Jiaya Jia
- Published: 2026-08-27T17:59:40Z
- Age days: 3

</details>
