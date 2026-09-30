---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19665v1"
published: "2026-09-17T04:08:39Z"
age_days: 0
score: 29
created: 2026-09-18
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling

> [!summary] 先说人话（基于摘要）
> 这篇工作比较电池双端子危险的运行时过滤策略，发现调好安全余量和拒绝动作后的退让行为，可能比选择更精细的危险逻辑更重要。

## 问题

导电物同时接近两个端子才构成特定短路危险，按每个端子分别设置禁入区可能过度限制操作。但过滤动作后如何继续执行，同样会改变风险与任务完成率。

## 创新点或方法

在冻结OpenVLA策略外分别比较合取危险谓词、双区域禁入和二者组合，扫描各自几何余量；再在匹配工作点比较保持、退让、采样搜索和连续动作屏障投影。

## 证据

三个工作单元中，各谓词扫描余量后的安全—效用前沿几乎相同。保持相较退让最多降低0.302的任务成功率，却未减少危险；两种最小干预回退留下更多残余危险。排序迁移到第二策略和任务套件，相关载荷尺寸误差比更大的独立端子位置误差更具破坏性。

## 局限

研究针对LIBERO中的接近关系危险；摘要不支持将结论直接视为真实电池回收的电气安全验证。

- **判断**：值得精读实验设计与失败案例，尤其适合正在给学习策略加运行时过滤器的研究者。

## 研究关联

对VLA安全评测，直接提示应把拒绝后的行为与阈值调节纳入比较，而不能只比较危险条件表达形式。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Runtime safety filters for learned manipulation policies typically define unsafe states as unions of object-wise keep-out regions. This representation can be unnecessarily restrictive for hazards that depend on a joint spatial relation, such as battery recycling, where a conductive payload can short a charged cell only when it approaches both terminals simultaneously. We study runtime filtering for this two-terminal hazard in LIBERO using frozen OpenVLA policies. We factor a runtime filter into three design choices: the predicate structure, its geometric margin, and the fallback action applied when a commanded action is rejected. We compare a conjunctive predicate, a conventional two-site keep-out, and a composite of the two. For each predicate, we vary its margin to obtain a frontier between task success and residual hazard. We then compare four fallback strategies at matched operating points: holding, retreat, sampled search, and a continuous-action barrier projection. Across three workcells, the three predicate families trace nearly identical safety--utility frontiers once each is evaluated over its own margin. In contrast, the fallback strategy has a substantially larger effect: holding reduces task success by up to 0.302 relative to retreat without reducing hazard, while both minimally invasive fallbacks leave substantially more residual hazard. This ordering transfers to a second policy and task suite, while retreat-based filtering remains effective under standing errors in the clearances available to the filter, although correlated error in the estimated payload size is more damaging than larger independent errors in terminal position. These results show that, for proximity-defined manipulation hazards, margin selection and fallback strategy can matter more than predicate structure in determining the safety--utility trade-off of a runtime filter.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19665v1
- Authors: Yuxin Cao, Wei Song, Xianglin Yang, Fusen Guo, Lin Li, Xiao Cheng, Jin Song Dong
- Published: 2026-09-17T04:08:39Z
- Age days: 0

</details>
