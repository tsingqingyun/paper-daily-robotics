---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19475v1"
published: "2026-09-16T22:36:35Z"
age_days: 1
score: 38
created: 2026-09-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FASA: Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models

> [!summary] 先说人话（基于摘要）
> FASA根据机器人当前看到的情况、夹爪受力和自身状态，动态调整扩散VLA的采样步骤，让不同交互阶段使用不同计算量，无需额外训练。

## 问题

扩散VLA的反复采样带来计算和访存成本。已有加速方法要么依赖昂贵训练，要么采用固定剪枝或缓存计划，忽略交互过程中动态变化的计算需求，并可能损害感知。

## 创新点或方法

交互驱动的范围适配器利用视觉和夹爪力反馈调整全局采样步数预算，本体感知适配器再在范围内确定优化的采样步骤。与固定执行计划相比，去噪流程由实时反馈调节。

## 证据

摘要报告在若干基准上最高达到1.45倍推理加速，并保持有竞争力的成功率；未给出基准名称、绝对成功率或具体硬件结果。

## 局限

“有竞争力”不等于成功率无损；需核查最高加速对应的任务、硬件和性能变化，以及力反馈要求。

- **判断**：值得读运行时调度机制，但在看到逐任务速度与成功率对照前，不宜据摘要判断部署优势。

## 研究关联

为资源受限平台上的VLA提供运行时计算分配思路，适合研究交互状态与推理预算之间的关系。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/FASA Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion-based Vision-Language-Action (VLA) models achieve strong performance in embodied tasks, but their iterative sampling imposes heavy computational and memory-access cost, blocking real-time deployment on edge platforms. Existing acceleration methods either require expensive training (e.g., distillation, flow matching) or degrade perception via statically scheduled pruning and caching, ignoring the dynamic workload variance of robotic interactions. This paper presents FASA (Feedback-Aware Sampling Adaptation), a training-free runtime framework that treats real-time multimodal feedback as a control signal for the denoising pipeline: an interaction-driven range adaptor modulates the global sampling-step budget based on visual and gripper-force feedback, and a proprioception-aware step adaptor pinpoints the optimized step within the adapted range. This co-designed framework allows the underlying hardware architecture to adaptively match the workload demands of different execution phases. Comparative evaluations across several benchmarks show that the inference speed can be increased by up to 1.45$\times$ while maintaining competitive success rates, providing a novel dynamic runtime architecture paradigm for deploying heavy generative embodied AI workloads onto resource-constrained computing platforms.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19475v1
- Authors: Yuchen Han, Jianhan Wu, Xiaoyang Qu, Lingwei Kong, Shiyi Li, Jianzong Wang
- Published: 2026-09-16T22:36:35Z
- Age days: 1

</details>
