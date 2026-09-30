---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03255"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-09-05
concepts: ["多模态基础模型"]
---

# Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot

> [!summary] 先说人话（基于摘要）
> 这篇论文目前主要提出一套人形机器人交互数据采集实验设计，把可穿戴生理信号、行为数据和自报告联合起来研究用户投入度，并用任务复杂度制造条件差异。

## 问题

既有 HRI 投入度研究多依赖可观察行为线索，缺少把生理反应与行为、自报告联合分析的框架，因而难以完整刻画用户在不同交互负荷下的状态。

## 创新点或方法

作者设计结构化采集协议，在预先定义的不同任务复杂度条件下，同步收集可穿戴生理信号、行为数据和用户自评，目标输出是可用于投入度分析的动态多模态数据集。

## 证据

摘要只描述实验设计和拟建数据集，未报告样本规模、采集结果、模型实验或可核查的结果数字。


## 局限

数据集似乎尚处于建设或设计阶段；最需核查受试者规模、信号同步、投入度标签可靠性和伦理隐私处理。

- **判断**：仅建议从事 HRI 数据采集者阅读全文参考协议；对寻求已验证模型或公开大规模数据的研究者，目前优先级较低。

## 研究关联

对多模态具身交互研究，它可能提供超越视频与语音的用户状态监督，用于社交机器人感知和主动交互；但目前摘要体现的价值主要是数据设计。

- **概念**：多模态基础模型
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Hum.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03255v1 Announce Type: new Abstract: This paper presents an experimental design for constructing a multimodal dataset to analyze user engagement in human-robot interaction (HRI). Prior studies have mainly relied on observable behavioral cues, with limited frameworks integrating physiological signals. We therefore propose a structured data-collection protocol to build a multimodal dataset that includes wearable physiological signals, behavioral data, and self-report measures under different levels of task complexity defined in this experiment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03255
- Authors: Buwan Kim, Wonse Jo
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
