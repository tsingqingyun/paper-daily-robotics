---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.35450"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-02
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Uni-VLaT: Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Uni-VLaT 让人形机器人利用全身触觉决定怎样行走和操作。关键不只是把触觉送进 VLA，还要求触觉通路预测后续触觉、身体状态和视觉表示，让它学会接触之后会发生什么。

## 问题

在人机接触和边走边操作时，接触位置可能被遮挡，视觉与本体感知不足以说明身体正在怎样受力。少数固定位置的力或力矩传感器也难以保留全身接触的空间分布。

### 用一个例子理解

理解用例（非论文实验）：机器人收到“背部被轻拍后前进”的指令；背部触觉输入进入策略，结合视觉和身体状态形成接触上下文；策略输出行走动作。训练时还要求该表示预测后续身体及感官变化。

## 创新点或方法

相较于只用视觉和身体状态，本文增加分布式触觉通路；相较于直接拼入触觉，又在训练时要求其隐状态预测未来多模态表示，同时服务动作生成。这样，触觉特征需要反映接触与后续变化的关系。执行时策略利用触觉上下文产生动作；摘要未说明是否仍运行预测分支，也未说明原 VLA 哪些参数参与训练。

### 方法如何工作

1. 采集身体不同位置的触觉，保留接触发生在哪里的信息，补充可能被遮挡的视觉。
2. 训练触觉通路隐状态同时支持动作和未来多模态预测，促使它编码接触的后续影响。
3. 执行时利用形成的触觉上下文生成动作；具体融合结构和预测分支的运行方式，摘要只说明到此。

### 必要术语

- 本体感知：机器人对自身关节等身体状态的测量；与触觉共同描述物理交互。
- 分布式触觉：在身体多个位置感知接触；本文依靠它保留空间接触模式。
- 预测监督：用未来观测作为训练目标；本文用它约束触觉隐状态。
- 绝对未来目标：预测未来目标本身，而非只预测相对变化；本文消融指出其重要性，具体定义仍需核查。

## 证据

摘要报告五项真机任务，覆盖触觉触发行走、持续交互、人机接触及移动操作，平均成功率为 75%。它比无触觉基线高 43 个百分点，比有触觉但无预测监督的基线高 7 个百分点。在两个预训练 VLA 骨干上，Table Sweeping 均提高 30 个百分点，Back-Tap Walking 提高 85–90 个百分点；这两项增幅的具体参照未在摘要中写明。消融支持上下文化触觉预测和绝对未来目标的作用，但未给数值。

## 局限

这些是真机结果，但尚不能外推到不同触觉硬件或任意接触情形。我会核查重复次数、传感器布局、接触强度范围，以及各基线是否使用相同数据和训练预算；输入未提供这些条件。

- **判断**：值得深入读预测目标和消融，因为最有辨别力的证据是相对“已经有触觉”的基线仍有收益。

## 研究关联

这里值得借鉴的是新传感器的训练目标：不仅让它帮助拟合动作，还让它解释后续可观测变化。当传感器信息丰富、动作监督却不足以迫使模型利用它时，这条路线值得测试。

### 下一步读哪里

优先核查预测多远的未来、目标表示如何生成、“上下文化”和“绝对目标”具体指什么，再检查触觉延迟与真机控制频率是否匹配。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/Uni-VLaT Whole-Body Tactile Adaptation of VLA Policies for Humanoid Loco-Manipul.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.35450v2 Announce Type: replace Abstract: Physical contact often determines how a humanoid should respond during loco-manipulation, yet vision and proprioception alone are often insufficient to characterize physical interaction, especially when the contact region is occluded. Unlike sparse force or torque measurements at predefined regions, distributed tactile sensing preserves spatially resolved contact patterns across the robot body. We therefore study how to integrate such whole-body tactile information into vision-language-action (VLA) policies for contact-rich control. Our approach, Uni-VLaT, introduces a tactile pathway whose latent state is trained not only for action generation, but also to predict future tactile, proprioceptive, and visual representations. This predictive objective builds a tactile-anchored multimodal context, encouraging a more structured understanding of the physical world. We evaluate Uni-VLaT on five real-robot tasks covering tactile-triggered locomotion, sustained physical interaction, human-robot contact, and loco-manipulation. Uni-VLaT achieves a 75% average success rate, outperforming a baseline without tactile input by 43 points and a tactile-input baseline without predictive supervision by 7 points. Across two pretrained VLA backbones, our method improves Table Sweeping by 30 points on both backbones and Back-Tap Walking by 85-90 points. Ablations further show that contextualized tactile prediction and absolute future targets are critical to performance. These results indicate that predictive tactile learning provides an effective route for extending pretrained VLA policies to whole-body physical interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.35450
- Authors: Zihao Wang, Shutong Liu, Siqi Zheng, Liu Cao, Ruoqu Chen, Rundong Liu, Yanchao Yang, Mengdi Xu
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
