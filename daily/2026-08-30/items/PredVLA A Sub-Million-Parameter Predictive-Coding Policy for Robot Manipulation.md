---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26673v1"
published: "2026-08-27T06:27:11Z"
age_days: 2
score: 40
created: 2026-08-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation

> [!summary] 先说人话（基于摘要）
> PredVLA说明语言条件操控未必需要巨型 VLA：它用仅 0.68M 可训练参数的预测编码循环策略，通过感知预测误差在线修正隐状态。

## 这篇到底在做什么

- **卡在哪里**：任务是在 LIBERO 上完成语言条件机器人操控；瓶颈是大规模预训练 VLA 参数昂贵，而小型 Transformer/LSTM 在同等条件下控制能力不足，且通常难以严格分离观测反馈与开环动力学。
- **关键解法**：输入视觉特征、语言条件和本体感觉，输出机器人动作。层级生成式循环动力学预测视觉特征与本体状态，真实观测只能借由预测误差驱动的在线隐变量推断影响状态；区别于直接把观测写入循环状态，并可通过关闭推断得到严格开环条件。
- **拿什么证明**：短时程三个 LIBERO 套件平均成功率 86.9%，计入长时程套件后为 75.4%。在冻结前端、演示、动作解码器和评测协议一致时，成功率分别是参数匹配 Transformer 和 LSTM 的 3.7 倍、7.4 倍。

## 值不值得读

- **和你的研究有什么关系**：对 VLA 和机器人学习研究者，它给出了研究小模型控制、反馈修正及世界模型式内部预测的强基线，也便于分析闭环观测到底贡献了多少。
- **先别急着信**：主要结果来自 LIBERO；摘要没有说明不同视觉前端、真实机器人或更广任务分布下，小参数优势是否保持。
- **判断**：值得精读方法和受控对比：亮点不只是小，而是把预测误差反馈做成了可测量的控制机制。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/PredVLA A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large pretrained vision-language-action models dominate modern robot-manipulation benchmarks, but it remains unclear how much model scale is necessary for strong language-conditioned control, or whether fundamentally different control architectures can remain competitive at much smaller parameter budgets. We present PredVLA, a language-conditioned predictive-coding policy with only 0.68 million trainable network parameters and no robot-data pretraining, whose hierarchical generative recurrent dynamics predict visual features and proprioception while observations influence latent state only through online inference from the resulting sensory prediction errors. On LIBERO, PredVLA achieves an 86.9% mean success rate across the three short-horizon suites and 75.4% when the long-horizon suite is included. Under a controlled comparison using the same frozen front end, demonstrations, action decoder, and evaluation protocol, PredVLA achieves 3.7x and 7.4x mean success rates of parameter-matched Transformer and LSTM policies, respectively. The predictive-coding formulation also makes the contribution of observation-driven correction directly measurable: because observations influence the recurrent state only through prediction-error-based latent inference, disabling this inference yields an exact open-loop control condition. Together, these results show that a sub-million-parameter recurrent generative policy can achieve strong performance on modern language-conditioned manipulation benchmarks while providing an explicit mechanism for prediction-error-driven online state correction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26673v1
- Authors: Hiroki Sawada, Shunichi Kasahara
- Published: 2026-08-27T06:27:11Z
- Age days: 2

</details>
