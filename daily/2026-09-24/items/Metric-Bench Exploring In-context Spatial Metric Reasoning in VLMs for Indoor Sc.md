---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25841v1"
published: "2026-09-22T08:09:21Z"
age_days: 1
score: 32
created: 2026-09-24
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes

> [!summary] 先说人话（基于摘要）
> Metric-Bench 用图中已知尺寸的物体作为尺子，测试 VLM 能否推断室内空间的真实尺度。MetricReasoner 再通过结构化提示和可验证数值奖励训练这种能力。

## 问题

具身任务需要尺度判断，而摘要认为现有像素级空间监督过于局部，可能损伤一般多模态推理能力。目标是在缺少相机内参时，利用上下文建立二维图像到三维尺度的联系。

## 创新点或方法

输入包含已知物理尺寸的图内参照物；MetricReasoner 采用任务适配的强化微调，以结构化提示组织推理，并用可验证数值奖励监督尺度回答。

## 证据

摘要报告：在 Metric-Bench 上较现有模型、包括更大的专有模型提升 43.1%；相对空间专用对照，RoboSpatial 总体准确率和 ERQA 分别提升 30.4% 与 9.3%；V⋆Bench 和 BLINK 增益为 15.9% 与 88.9%。摘要未说明这些百分比是否均为相对提升。

## 局限

需核查百分比计算口径、参照尺寸的获取方式及其误差敏感性，不能将这些成绩直接等同于机器人定位精度提升。

- **判断**：值得读评测构造和数值奖励设计，但应先厘清提升口径，再判断结果强度。

## 研究关联

对多模态基础模型和具身评测研究者，它提供了借助场景参照物获得尺度信息的训练与诊断方式；摘要中的下游证据仍是基准表现。

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/Metric-Bench Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Sc.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric-Bench, a focused benchmark designed to guide metric-spatial reasoning using contextual information. By incorporating in-image reference objects with known physical dimensions, Metric-Bench guides models to implicitly learn the 2D-to-3D mapping without camera intrinsics. We further present MetricReasoner, a task-adapted reinforcement fine-tuning recipe for reference-grounded metric reasoning, using structured prompts and verifiable numerical rewards. Extensive experiments on Metric-Bench demonstrate that our approach significantly enhances spatial metric understanding, outperforming existing and even larger proprietary models by 43.1\%, while improving downstream embodied performance over a spatial-specialized counterpart by 30.4\% on RoboSpatial overall accuracy and 9.3\% on ERQA, and additionally delivering consistent gains on general benchmarks (15.9\% on V$\star$Bench, 88.9\% on BLINK), indicating that the proposed adaptation does not necessarily compromise general VLM capabilities.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25841v1
- Authors: Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen, Chunhua Shen
- Published: 2026-09-22T08:09:21Z
- Age days: 1

</details>
