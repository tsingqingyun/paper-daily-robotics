---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25756v1"
published: "2026-09-22T06:50:10Z"
age_days: 1
score: 44
created: 2026-09-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation

> [!summary] 先说人话（基于摘要）
> MedVLA 把医疗机器人控制拆成高层多模态推理与底层受约束的功能执行，使模型既能选择动作，也能调用闭环操作所需的系统功能。

## 问题

精密医疗操作需要兼顾安全、可解释性和执行约束。摘要认为，直接生成连续动作的 VLA 难以自然处理操作流程中的非动作系统调用，因此不能充分覆盖这类闭环任务。

## 创新点或方法

高层模型负责多模态决策，低层通过受约束的函数接口执行；同时用多智能体流水线生成面向技能的 CoT 训练数据。关键变化是把决策落到结构化功能调用，而非仅输出连续动作。

## 证据

在相同初始条件下进行了 100 次闭环柔性电极植入试验，MedVLA 成功率为 95.0%，OpenVLA 为 8%，π₀ 为 15%。摘要还报告不同多模态骨干微调后均有提升，但未量化安全性与稳定性。

## 局限

相同初始条件下的结果不能直接说明对环境变化的适应能力；巨大基线差距还需要核查训练条件、接口适配和成功判据。

- **判断**：值得细读执行接口和对照设置，95% 成功率是明确结果，但不足以单独支持可部署医疗系统的判断。

## 研究关联

对 VLA 和智能体研究者，这是把推理、工具调用和机器人执行统一到任务流程中的具体案例，也提示精密任务评测需要检查动作接口是否匹配实际需求。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/MedVLA A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $π_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25756v1
- Authors: Junjie Xie, Chuxuan He, Angen Ye, Yujia Song, Dapeng Zhang
- Published: 2026-09-22T06:50:10Z
- Age days: 1

</details>
