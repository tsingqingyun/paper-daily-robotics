---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24118v1"
published: "2026-09-21T05:14:34Z"
age_days: 1
score: 39
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies

> [!summary] 先说人话（基于摘要）
> CARE让VLA从实际执行失败中学习如何补救，而不是只学顺利完成任务的轨迹。它按任务阶段归纳常见偏差，再训练小幅修正或局部重做。

## 问题

VLA一旦偏离正常轨迹就容易失效；手工设计或随机施加扰动得到的纠错数据，未必对应策略真正遇到的失败状态。

## 创新点或方法

收集失败运行，建立分阶段的失败偏差分布并合成纠错示范；推理时结合阶段规划和三维监测，在保留已有进度的情况下触发原子调整或重新操作。

## 证据

引入FSR-Bench评测中途失败状态下的局部偏差与结构异常恢复。多个VLA骨干、仿真基准和真实双臂任务上，平均任务成功率分别提高14.5和15.9个百分点。

## 局限

需核查阶段划分和三维监测如何实现，以及经验失败分布对未见结构异常的覆盖范围。

- **判断**：值得精读数据构造与恢复协议，收益明确且直接针对部署中的常见瓶颈。

## 研究关联

对机器人学习与Agent执行系统，价值在于将失败收集、纠错数据生成和在线恢复连接起来，直接研究策略偏离后的行为。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/CARE Experience-Guided Atomic Corrective Execution for Vision-Language-Action Po.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies achieve strong performance in robotic manipulation but remain brittle once execution deviates from nominal trajectories. We propose CARE (Corrective Atomic Robotic Execution), a framework that improves recovery by learning from failures encountered during execution. Instead of generating corrective data from manually designed or random perturbations, CARE collects failed rollouts, models stage-conditioned post-failure deviations, and uses the resulting empirical distributions to synthesize representative failure states and corrective demonstrations. At inference time, CARE combines stage-wise planning with physically grounded 3D monitoring to trigger atomic adjustments or re-operations while preserving task progress. We further introduce the Failure State Recovery Benchmark (FSR-Bench), which evaluates recovery from intermediate failure states under local deviations and structural anomalies. Experiments across multiple VLA backbones, simulation benchmarks, and real-world dual-arm tasks show consistent improvements, with average task-success gains of 14.5 points in simulation and 15.9 points in the real world. Code, models, and data are available at https://github.com/xiaojunlan/care

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24118v1
- Authors: Junlan Xiao, Junwei Jiang, Zaibin Zhang, Yifan Wang, Zhongbo Zhang, Huchuan Lu, Lijun Wang
- Published: 2026-09-21T05:14:34Z
- Age days: 1

</details>
