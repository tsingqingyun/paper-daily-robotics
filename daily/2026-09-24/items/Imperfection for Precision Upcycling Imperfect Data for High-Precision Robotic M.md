---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26672v1"
published: "2026-09-22T16:32:24Z"
age_days: 1
score: 32
created: 2026-09-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> ε4P 把两类不完美数据分工使用：目标任务的粗糙示范教模型做什么，其他任务的精细示范教模型怎样做得准。分工通过 flow matching 的不同噪声阶段实现。

## 问题

高精度操作依赖昂贵的目标任务优质示范。低精度目标数据缺动作精度，其他任务的高精度数据又存在任务错配，直接混合训练不能明确利用各自优势。

## 创新点或方法

在高噪声阶段使用目标任务低精度数据，以保持任务上下文；在低噪声阶段使用任务不匹配的高精度数据，迁移细粒度动作精度。关键是按生成轨迹的位置分配数据来源。

## 证据

真实机器人实验覆盖亚毫米级高精度任务和粗粒度任务。额外使用不完美数据最多提高 31.7 个百分点；用其等量替代目标任务优质数据时，平均表现仅下降 4.2 个百分点。

## 局限

31.7 个百分点是最大提升，4.2 个百分点是平均下降，口径不同；需核查可迁移的任务差异范围及不同任务的替代收益。

- **判断**：建议优先细读，数据分配机制清晰且有真实实验量化，但适用性取决于异任务精度能否有效迁移。

## 研究关联

对 VLA 和机器人学习研究者，它给出了复用既有低质量或异任务数据的具体训练规则，可用于研究如何减少高精度示范需求。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/Imperfection for Precision Upcycling Imperfect Data for High-Precision Robotic M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Training vision-language-action (VLA) models for high-precision manipulation typically requires task-specific, high-quality data (e.g., teleoperation), which is slow and expensive to collect. To reduce this burden without compromising manipulation precision, we propose $\varepsilon$4P (Imperfection for Precision), a simple yet effective method that "upcycles" two otherwise discarded data sources: (1) low-precision data from the target task and (2) high-precision data from mismatched tasks. Rather than naively mixing these imperfect data sources throughout co-training, $\varepsilon$4P controls where each source contributes along the flow-matching trajectory. Specifically, low-precision, target-task data is used at high noise to preserve high-level task context and high-precision, task-mismatched data is used at low noise to transfer low-level action precision. Through real-robot experiments on both sub-millimeter, high-precision tasks and coarse-grained tasks, we demonstrate that the proposed method (1) effectively leverages additional imperfect data to improve policy performance by up to 31.7 percentage points, and (2) can replace an equal amount of task-specific, high-quality data with an average performance drop of only 4.2 percentage points. Overall, $\varepsilon$4P points toward a scalable paradigm for high-precision manipulation, in which heterogeneous, imperfect data can be systematically repurposed to reduce reliance on costly task-specific, high-quality data. More details are available at https://varepsilon4p.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26672v1
- Authors: Hao Wei, Yang Liu, Chao Tang, Shengbao Li, Jiangtao Chen, Jinxuan Zhu, Jiaheng Wang, Hong Yin, Zhaofeng Cao, Tingguang Li
- Published: 2026-09-22T16:32:24Z
- Age days: 1

</details>
