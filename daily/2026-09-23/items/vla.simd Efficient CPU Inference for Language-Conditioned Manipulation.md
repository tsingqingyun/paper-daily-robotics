---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24274v1"
published: "2026-09-21T08:39:07Z"
age_days: 1
score: 31
created: 2026-09-23
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# vla.simd: Efficient CPU Inference for Language-Conditioned Manipulation

> [!summary] 先说人话（基于摘要）
> vla.simd优化没有独立GPU时的机器人策略推理，并说明动作块怎样覆盖等待下一次预测的时间。配套IMPACT策略通过缓存语言表示等设计，在树莓派上持续供应动作。

## 问题

CPU部署面临推理延迟，策略两次查询之间可能缺少可执行动作；一次输出很多动作能缓解供给问题，却不等于更频繁地根据观测纠正行为。

## 创新点或方法

推理引擎结合共享SIMD微内核、计算复用和面向处理器的优化；IMPACT基于ACT，缓存文本表示并用语言调制视觉特征，分析延迟执行和时间对齐执行下的动作可用性。

## 证据

6种策略、4款CPU上相对编译PyTorch中位加速约1.4倍，保持fp32数值一致性。树莓派5经过90秒热浸后，IMPACT供应33.5动作/秒，int8为81.2；独立GPU实验中4套LIBERO平均成功率76.4%，并在两类实体机器人上展示CPU部署。

## 局限

LIBERO成功率来自独立GPU评测，不能直接代表树莓派闭环表现；语言打乱实验只支持熟悉目标间的选择能力。

- **判断**：做CPU部署值得精读，尤其关注动作供应、反馈频率和热稳定条件的区别。

## 研究关联

对VLA部署与评测，价值是同时报告计算速度和执行时间覆盖，避免用动作吞吐量替代闭环响应能力。

- **概念**：[[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/vla.simd Efficient CPU Inference for Language-Conditioned Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Deploying language-conditioned manipulation without a dedicated GPU requires efficient inference and action chunks that cover the delay between policy queries. We present vla.simd, a CPU inference engine that combines shared SIMD micro-kernels, reusable computation, and target-specific optimization. We relate query latency and execution horizon to action availability under lagged and time-aligned execution, distinguishing action supply from feedback frequency. Across six policies and four CPUs, vla.simd achieves approximately $1.4\times$ median speedup over compiled PyTorch references while preserving fp32 numerical fidelity. We also introduce IMPACT, an ACT-based policy with cached text representations and language-modulated visual features. IMPACT is the only language-conditioned policy in our evaluated set that supplies at least 30 actions/s on the Raspberry Pi 5: after a 90 s thermal soak, it supplies 33.5 actions/s in fp32 and 81.2 with int8. Separate GPU evaluations yield $76.4\%$ mean success across four LIBERO suites without robot pretraining; instruction-shuffling tests demonstrate selection among familiar goals. Trials with IMPACT on an SO-101 arm and SmolVLA on a UR10e with a Robotiq gripper demonstrate CPU deployment on two robot embodiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24274v1
- Authors: Khanh D. Nguyen, Hoang M. Truong, An T. Le
- Published: 2026-09-21T08:39:07Z
- Age days: 1

</details>
