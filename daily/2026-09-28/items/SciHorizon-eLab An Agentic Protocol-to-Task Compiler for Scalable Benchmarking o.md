---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30971v1"
published: "2026-09-25T08:18:45Z"
age_days: 3
score: 29
created: 2026-09-28
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents

> [!summary] 先说人话（基于摘要）
> SciHorizon-eLab 把自然语言实验规程编译成可执行、可逐步验收的具身任务。它试图让实验室机器人基准的生成摆脱逐项手工编写。

## 问题

科学具身智能缺少可靠且系统化的评估环境；现有实验室仿真基准依赖人工任务工程，难以规模化覆盖多样规程，同时保证任务可执行和可验证。

## 创新点或方法

经过语义落地、可执行任务合成和多阶段仿真认证，将实验规程转换成环境、操作程序及步骤级成功条件，并支持可复现的专家示范与执行轨迹生成。

## 证据

构建了包含 300 个认证任务的基准，支持 HIL 执行和有序步骤评估。代表性任务上最强策略平均成功率为 49.7%，进一步评估显示人类与具身智能体协调存在明显弱点；摘要中的基准名仍是占位符。

## 局限

仿真认证是否充分保留科学规程语义需核查；49.7% 来自代表性任务，不能视为全部 300 项任务的总体成绩。

- **判断**：做科学机器人或自动基准构建值得精读认证标准与任务实例，优先检查任务有效性。

## 研究关联

对具身评测与机器人学习研究者，价值是把任务定义、成功判据和示范生成纳入同一流水线，有利于研究实验规程执行与人机协作。

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/SciHorizon-eLab An Agentic Protocol-to-Task Compiler for Scalable Benchmarking o.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executable and verifiable embodied tasks at scale. To address this challenge, we introduce SciHorizon-eLab, an agentic protocol-to-task compiler that formulates scientific embodied task construction as a compilation problem. Given a natural-language protocol of scientific experiments, SciHorizon-eLab progressively compiles laboratory protocols into semantic-preserving embodied tasks through semantic grounding, executable task synthesis, and multi-stage simulation-based certification. The system generates semantically grounded environments, executable manipulation programs, and step-level success specifications, while enabling reproducible generation of expert demonstrations and execution traces. Using this pipeline, we further construct \BenchName, a ready-to-use benchmark comprising 300 certified tasks across diverse laboratory operations. It supports HIL task execution, reproducible expert-demonstration generation, and ordered step-level evaluation. Across representative tasks, the strongest policy attains an average success rate of only 49.7%, with further evaluations revealing pronounced weaknesses in human and embodied agent coordination. We publicly release the code, benchmark data, and evaluation toolkit at https://github.com/SciHorizon-elab/SciHorizon-elab.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30971v1
- Authors: Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu
- Published: 2026-09-25T08:18:45Z
- Age days: 3

</details>
