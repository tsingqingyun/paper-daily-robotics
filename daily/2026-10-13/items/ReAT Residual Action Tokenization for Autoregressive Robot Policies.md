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
url: "https://arxiv.org/abs/2610.13093v1"
published: "2026-10-09T06:45:35Z"
age_days: 3
score: 29
created: 2026-10-13
concepts: ["世界模型", "具身智能评测与基准"]
---

# ReAT: Residual Action Tokenization for Autoregressive Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> ReAT 把一段连续机器人动作编码成几个离散 token，每个新 token 都负责修正前面真正解码后留下的误差。巧处是后续编码依据实际重建结果，而不是默认前面的编码已经表达好了动作。

## 问题

自回归机器人策略需要把连续动作块变成紧凑的离散预测目标。已有 tokenizer 能重建动作，但单个 token 到底贡献了什么往往不明确，难以直接组织成逐步修正的动作表示。

### 用一个例子理解

理解用例（非论文实验）：输入一段目标抓取动作；第一个 token 解码后仍有末端位置误差，后续 token 编码剩余修正量；输出少量 token 及更接近目标的重建动作，作为策略学习目标。

## 创新点或方法

旧做法中 token 的作用较隐含；ReAT 每次先解码已有 token，比较重建动作与目标动作，再从剩余误差构造下一 token。训练编码时有目标动作可计算残差；策略推理时则自回归预测 token，再解码成动作。摘要没有说明推理时各 token 如何读取重建反馈，不能理解为机器人执行后依据真实误差在线纠错。

### 方法如何工作

1. 取目标动作块，并解码当前 token 前缀，得到实际重建动作。
2. 比较目标与重建结果，找出尚未表达的动作误差。
3. 从残差构造下一 token，使新增信息针对当前缺口。
4. 重复得到离散序列，供自回归策略学习；具体网络与损失摘要未说明。

### 必要术语

- 动作块：连续多步动作的组合；本文将它整体编码。
- 残差：目标动作与当前重建动作之差；决定下一 token 表达什么。
- 自回归：依次预测后续 token；本文策略通过这种方式生成动作表示。

## 证据

摘要报告跨三个仿真基准和真实设置的 19 个操作任务，8-token ReAT 策略成功率优于所评估基线；LIBERO 上，4-token ReAT 也超过所评估的 8-token 动作编码基线，token 数减半。没有具体成功率、基线名单或分项结果，因此不能断言每个任务都获胜，也不能把 token 减半等同于延迟减半。

## 局限

摘要将结果解释为支持自我修正策略学习的一条路径，但逐步修正的表示是否就是成功率收益的原因，还需核查消融。重建误差下降也不自动保证任务成功，尤其是对接触时机敏感的动作。

- **判断**：值得读到残差编码和策略训练接口，因为“每个 token 修正什么”是一个清楚、可检验的设计选择。

## 研究关联

值得借鉴的是让压缩表示的每一步直接面对最终解码误差。若编码器内部的近似与实际解码结果存在偏差，这种反馈可能使有限的 token 更集中地表达尚未解决的动作细节。

### 下一步读哪里

我会检查残差如何量化、动作各维度如何衡量误差、训练与推理反馈是否一致，再看相同 token 数和相同计算预算下的对照。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/ReAT Residual Action Tokenization for Autoregressive Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autoregressive robot policies rely on action tokenizers to convert continuous action chunks into compact sequences of discrete prediction targets. Existing tokenizers can reconstruct action chunks from discrete codes, but often leave implicit what each individual token contributes to the reconstructed action. We introduce Residual Action Tokenization (ReAT), which gives each token an explicit role in refining the current action reconstruction. It uses the decoded reconstruction as feedback to construct the next token from the remaining action error. This closes the loop between encoding and decoding, making each new token responsive to the errors left by the actual decoded prefix. Across 19 manipulation tasks spanning three simulation benchmarks and real-world settings, 8-token ReAT policies outperform the evaluated baselines in task success; on LIBERO, even 4-token ReAT surpasses the evaluated 8-token action-tokenization baselines at half the token budget. These results suggest a path toward action tokenization that supports self-corrective policy learning, helping autoregressive policies learn to progressively refine their own action plans.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13093v1
- Authors: Dijia Zhan, Zhuo Li, Xuemiao Xu, Sun Zheng, Jinyi Li, Wenjun Wang, Jie Tang
- Published: 2026-10-09T06:45:35Z
- Age days: 3

</details>
