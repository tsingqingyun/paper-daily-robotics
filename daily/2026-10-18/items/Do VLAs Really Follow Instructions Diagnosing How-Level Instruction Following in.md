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
url: "https://arxiv.org/abs/2610.21251v1"
published: "2026-10-15T04:45:21Z"
age_days: 2
score: 27
created: 2026-10-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇检查 VLA 是否能听懂“怎么做”，例如指定动作方式，而不只是识别“做什么”。作者用分段丰富指令训练增强了动作对语言的响应，但发现这种响应既不稳定增加任务成功，也难以应付更难或分布外的要求。

## 问题

同样是完成一个操作，用户可能对过程另有要求。只统计物体是否到达终点，无法判断这些要求是否被遵守。摘要指出，既有工作主要关注指定任务的 What-level 指令，对指定执行方式的 How-level 指令检查不足；作者诊断发现，给当前 VLA 加上这类要求反而降低任务成功。

### 用一个例子理解

理解用例（非论文实验）：输入是桌面图像和“把杯子移到右边，途中保持杯口朝上”；模型输出移动动作，评估同时检查终点和全过程朝向。杯子到了右边但途中倾倒，仍不满足这条指令。

## 创新点或方法

通常一整段训练轨迹只配一条指令，过程中的动作变化缺少更细的语言对应。作者据此提出假设，并改用片段级丰富指令训练，使动作片段获得更具体的描述。执行时检验动作是否随方式要求改变，再用 SIMPLER-IN 检查只由指令给出的成功条件是否满足。巧处是把“动作响应了语言”和“满足要求地完成任务”分开。具体指令生成、训练损失与模型结构，摘要未说明。

### 方法如何工作

1. 在任务指令中加入执行方式要求，观察当前 VLA 的动作与成功率，确认基础能力的缺口。
2. 把训练轨迹按片段配上更丰富的指令，加强局部动作与语言的对应，检验作者的数据监督假设。
3. 执行时改变方式要求，检查动作是否随之变化，以测量响应性。
4. 用 SIMPLER-IN 检查仅由语言规定的成功条件，再测试困难和分布外要求，判断响应能否转化为可靠遵循。

### 必要术语

- VLA：把视觉和语言输入转成机器人动作的模型；本文检查其语言约束是否落实到动作。
- How-level 指令：规定如何执行的要求；本文将它与指定任务的指令区分。
- 片段级监督：给轨迹局部片段配语言描述；本文用它加强动作与方式要求的关联。
- 分布外要求：偏离训练中常见要求的指令；本文用它检验遵循能力的边界。

## 证据

摘要给出三项定性发现：原有 VLA 在 How-level 指令下成功率下降；片段级训练能增强动作响应，但不持续提高任务成功；SIMPLER-IN 上的收益无法延伸到更难或分布外要求。未提供模型名单、任务数量、指令类型、数值或误差范围，因此能复述诊断方向，无法判断效应大小和各模型的一致性。

## 局限

单轨迹单指令是作者提出并干预检验的解释，但输入不足以证明它是唯一原因。我的待核查问题是，分段训练是否同时改变了数据量或描述质量，以及动作响应怎样测量；这些影响因果判断。

- **判断**：值得先读诊断与评测定义，再看训练改动；它最直接的用途是纠正“任务完成就等于听懂指令”的评估习惯。

## 研究关联

可以借鉴的是评估设计：如果一种要求只写在语言里，成功判据就必须检查它。否则模型可能凭场景完成常见任务，得到高分，却没有执行用户指定的方式。

### 下一步读哪里

先检查 SIMPLER-IN 如何确保要求只能从语言获得，再查任务成功与方式遵循是否分别计分。训练部分应核查片段标注来源、公平的数据量对照，以及分布外要求具体改变了什么。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/Do VLAs Really Follow Instructions Diagnosing How-Level Instruction Following in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions that specify how to carry it out. Through our diagnoses, we find that How-level instructions do not help current VLAs and lower task success. We hypothesize that pairing each training episode with a single instruction limits How-level instruction following, and show that training with segment-level enriched instructions makes actions respond to such instructions without consistently raising task success. To measure How-level instruction following beyond standard benchmarks, we introduce SIMPLER-IN, where success requires conditions given only in the instruction. It shows that the gained responsiveness does not extend to demanding or out-of-distribution How-level instructions. How-level instruction following thus remains an open challenge.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21251v1
- Authors: Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park
- Published: 2026-10-15T04:45:21Z
- Age days: 2

</details>
