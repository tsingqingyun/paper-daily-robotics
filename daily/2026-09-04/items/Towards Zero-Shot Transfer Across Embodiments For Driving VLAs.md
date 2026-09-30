---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02341"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 43
created: 2026-09-04
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Towards Zero-Shot Transfer Across Embodiments For Driving VLAs

> [!summary] 先说人话（基于摘要）
> 论文研究驾驶VLA如何跨数据集和相机布局零样本迁移，并提出BEV-Forcing：用专用鸟瞰模型的地面物体布局监督VLA形成共享空间接口。其核心发现是，这类辅助几何约束在训练本体较少时有效，但会随相机布局多样性扩大而减弱。

## 这篇到底在做什么

- **卡在哪里**：驾驶VLA多在单一数据集上训练，缺少对未见数据集和相机阵列的零样本评估；简单加入更多数据集也未必提升已见本体性能，因此需要区分数据多样性与辅助空间监督的作用。
- **关键解法**：进行多数据集驾驶训练，并以BEV-Forcing辅助目标把鸟瞰视角中的地面物体位置知识迁入VLA骨干。它不直接替换VLA输出，而是让不同相机布局通过共享BEV空间表示对齐，并分析该目标在不同训练本体规模下的边际作用。
- **拿什么证明**：摘要报告BEV-Forcing在训练相机阵列较少时同时改善分布内和分布外表现；随着训练本体数量增加，辅助任务收益下降。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对驾驶VLA研究者，论文提示几何中间接口可缓解相机本体差异，但新机制必须与训练数据规模联合报告，否则小数据下的收益可能被误认为可持续扩展。
- **先别急着信**：摘要没有披露数据集、指标、数值及真正未见相机阵列上的绝对表现，BEV-Forcing的迁移幅度和适用边界必须查全文。
- **判断**：值得细读实验缩放曲线和零样本协议；若只关心一种固定训练规模，可先读方法与主要图表，不宜仅凭摘要判断优势大小。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Towards Zero-Shot Transfer Across Embodiments For Driving VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02341v1 Announce Type: new Abstract: Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual datasets and are rarely evaluated for zero-shot transfer to unseen datasets and camera rigs; furthermore naively adding more datasets to the training data does not necessarily lead to better performance within seen embodiments. To address these problems, we study multi-dataset training for the driving task and BEV-Forcing, an auxiliary objective that transfers ground-plane object-layout information from a specialized Bird's-Eye-View model into the VLA backbone. By encouraging the model to represent object position through a shared BEV spatial interface, we show that an auxiliary task such as BEV-Forcing can improve both in-distribution and out-of-distribution performance when training on a small number of camera rigs. As the number of training embodiments increases, however, the benefits of the auxiliary task are reduced; we present this as evidence that new techniques in the literature may see their benefits diminish when simply scaling up training diversity, which motivates presenting results taking into account data scaling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02341
- Authors: Caio Azevedo, Stefano Sabatini, Sascha Hornauer, Fabien Moutarde
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
