---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09148v1"
published: "2026-09-08T17:59:03Z"
age_days: 0
score: 30
created: 2026-09-09
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Proxy Policy Steering

> [!summary] 先说人话（基于摘要）
> Proxy Policy Steering（PPS）用两个小代理策略的差值，在每一步去噪时引导冻结的通用策略完成新任务。它通过局部引导保留调用基础策略能力的可能，无需修改基础模型参数。

## 这篇到底在做什么

- **卡在哪里**：通用机器人策略需要从少量示范中获得任务专门能力，同时保留原有广泛行为；直接专门化难以兼顾这两点。
- **关键解法**：参考代理拟合基础策略在目标任务观察上的行为，任务代理从参考代理初始化后接受任务监督。两者经校准的速度空间差值作为残差引导基础采样器，训练只需基础模型前向速度预测，不要求访问其参数。
- **拿什么证明**：在8项真实和4项仿真操作任务上，摘要报告相对pi 0.5基础策略平均成功率绝对提升53%，部分基础策略完全失败的任务实现从零到成功；超过LoRA、从头训练专门策略、残差策略及既有推理引导方法，并保留广泛能力。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习具有直接价值，尤其适合基础策略参数不可访问、但可获取速度预测的情形；也提供研究任务适配与失败恢复能力能否共存的方案。
- **先别急着信**：需要核查残差隔离任务监督变化的成立条件，以及“保留广泛能力”的评测范围；“53% absolute”的统计口径也应查原始结果表。
- **判断**：优先精读推导、代理训练和能力保留实验，部署接口清晰且报告收益很大。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Proxy Policy Steering.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies carry broad manipulation priors from large-scale data, but specializing them to a new task remains the deployment bottleneck. This requires eliciting task-specific behavior from limited demonstrations without degrading their broad capabilities. We introduce Proxy Policy Steering (PPS), an inference-time adaptation method that resolves this challenge by training two lightweight proxy policies whose calibrated velocity-space difference steers the frozen base sampler. A reference proxy models the frozen base's behavior on target-task observations, and a task proxy, initialized from the reference, captures how this behavior changes under task supervision. Their difference forms a calibrated velocity-space residual that steers the frozen base sampler at every denoising step. We identify the conditions under which this residual isolates the change induced by task supervision, and validate them empirically. Because the base is never directly modified, its broad capabilities remain available at inference, including behaviors such as recovery from failure that the demonstrations themselves do not exercise. Adaptation requires only forward velocity predictions from the base, making PPS lightweight to train and applicable even without access to the base's parameters. On 8 real-world and 4 simulation manipulation tasks, PPS lifts the state-of-the-art pi 0.5 base policy by 53% absolute success rate on average, with zero-to-one gains on tasks the base never solves, while preserving the base's broad capabilities. PPS outperforms LoRA fine-tuning, from-scratch specialists, residual policies, and prior inference-time steering methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09148v1
- Authors: Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma, Kuan Fang
- Published: 2026-09-08T17:59:03Z
- Age days: 0

</details>
