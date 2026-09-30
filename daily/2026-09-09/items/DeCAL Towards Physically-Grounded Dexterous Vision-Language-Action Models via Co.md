---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09119v1"
published: "2026-09-08T17:47:43Z"
age_days: 0
score: 35
created: 2026-09-09
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination

> [!summary] 先说人话（基于摘要）
> DeCAL面向遮挡严重、接触复杂的灵巧操作，让模型按接触状态选择如何使用触觉，并共同预测视觉与触觉变化。关键是把感知、动态想象和动作生成接入专门化专家。

## 问题

精细接触操作中，视觉遮挡与复杂接触动力学会削弱VLA。已有触觉方法多采用同质化多模态融合，缺少按接触情况调整的触觉整合和显式动力学建模。

## 创新点或方法

以Mixture-of-Transformers组织理解、想象和动作专家；接触感知门控动态调节视觉—触觉融合，Visuo-Tactile Latent Co-Imagination联合建模两种模态的动态变化，为动作生成提供物理信息。

## 证据

摘要称所有测试任务均达到最优，平均成功率71%、进度成功率83.4%，并报告对未见场景有较强泛化。


## 局限

摘要未列出任务、比较基线及进度成功率定义，需核查71%的评测范围和未见场景到底改变了什么。

- **判断**：灵巧手与触觉方向值得精读架构及实验；目前不能仅凭两个汇总数字判断泛化强度。

## 研究关联

对触觉VLA和世界模型研究者，价值在于把触觉的作用从额外输入推进到动态预测，并明确考虑接触阶段对模态需求的影响。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/DeCAL Towards Physically-Grounded Dexterous Vision-Language-Action Models via Co.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Dexterous manipulation involves contact-rich and fine-grained interactions with the physical world, posing significant challenges for existing vision-language-action (VLA) models due to severe visual occlusions and complex contact dynamics. While recent works have incorporated tactile sensing into robotic manipulation, most approaches still rely on homogeneous multimodal fusion, lacking adaptive tactile integration and explicit modeling of physical dynamics. In this work, we present DeCAL, a physically-grounded dexterous vision-language-action model that unifies understanding, imagination and action generation for contact-rich dexterous manipulation. Built upon a Mixture-of-Transformers (MoT) architecture, DeCAL leverages specialized experts for each capability while enabling efficient information flow among them. To effectively leverage tactile information, we introduce Adaptive Visuo-Tactile Fusion that dynamically regulates tactile interactions via a contact-aware gating strategy. Furthermore, we propose Visuo-Tactile Latent Co-Imagination to jointly model visual and tactile dynamics, equipping the policy with implicit physical world knowledge. Experimental results show that DeCAL consistently achieves state-of-the-art performance across all tasks, attaining a 71% average success rate and an 83.4% progress success rate, while also demonstrating strong generalization to unseen scenarios. The website is available at https://aureleopku.github.io/DeCAL.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09119v1
- Authors: Yankai Fu, Ning Chen, Junkai Zhao, Heng Zhang, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- Published: 2026-09-08T17:47:43Z
- Age days: 0

</details>
