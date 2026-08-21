---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18618v1"
published: "2026-08-19T07:11:06Z"
age_days: 1
score: 31
created: 2026-08-21
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories

> [!summary] 一句话结论（基于摘要）
> To bridge this gap, we introduce LabDex, a large-scale real-world dataset and benchmark for dexterous manipulation in chemistry laboratories, organized around a hierarchical task taxonomy spanning atomic skills, compositional tasks, and long-horizon experimen…

## 关键点

- **问题**：Autonomous laboratories hold great promise for accelerating scientific discovery.
- **创新点 / 方法**：To bridge this gap, we introduce LabDex, a large-scale real-world dataset and benchmark for dexterous manipulation in chemistry laboratories, organized around a hierarchical task taxonomy spanning atomic skills, compositional tasks, and long-horizon experiments.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/LabDex A Hierarchical Benchmark for Dexterous Manipulation in Laboratories.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous laboratories hold great promise for accelerating scientific discovery. To achieve this vision, robots are supposed to dexterously manipulate diverse labware and instruments and execute long-horizon, state-dependent experimental procedures. Yet existing benchmarks do not jointly capture dexterous hand use, real-world laboratory interactions, and multi-stage experimental procedures, limiting systematic training and evaluation. To bridge this gap, we introduce LabDex, a large-scale real-world dataset and benchmark for dexterous manipulation in chemistry laboratories, organized around a hierarchical task taxonomy spanning atomic skills, compositional tasks, and long-horizon experiments. First, LabDex is cross-platform and, for the first time, unifies real-world and simulation platforms under a common framework, providing standardized task definitions, demonstrations, and evaluation protocols. Second, LabDex is large-scale and systematically organizes chemistry laboratory operations into three interconnected levels: Atomic Skills, which characterize fundamental dexterous manipulation capabilities; Compositional Skills; and Long-Horizon Laboratory Workflows. This hierarchical design not only supports the evaluation of end-task performance, but also enables the analysis of how fundamental dexterous skills compose and influence more complex laboratory operations. We conduct cross-level evaluations of representative robot learning methods in both real-world and simulation environments. The experimental results validate the effectiveness of the LabDex task design and demonstration data, and show that the benchmark supports the training and systematic evaluation of existing robotic policies across laboratory dexterous manipulation tasks at different levels, providing a foundation for further research and development of autonomous laboratory robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18618v1
- Authors: Zhipeng Tang, Sihang Chen, Sha Zhang, Peihao Yang, Yan Liu, Wentao Zhao, Xinrui Liu, Rui Huang, Wensheng Du, Yuting Huang, Jiajun Deng, Lidian Wang, Yuan Zhang, Yanyong Zhang
- Published: 2026-08-19T07:11:06Z
- Age days: 1

</details>
