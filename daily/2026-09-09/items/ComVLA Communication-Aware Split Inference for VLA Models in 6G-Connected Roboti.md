---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07838v1"
published: "2026-09-07T18:00:14Z"
age_days: 1
score: 36
created: 2026-09-09
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics

> [!summary] 先说人话（基于摘要）
> ComVLA根据任务指令挑选关键视觉token，再按无线链路容量决定传多少。它让云端VLA少看大量冗余信息，以小幅成功率损失换取计算和延迟下降。

## 问题

机器人卸载VLA推理时，每个控制步骤能上传的感知数据受带宽限制。语义压缩器需要针对信道重新训练，而普通视觉token裁剪忽略实时信道容量。

## 创新点或方法

作用于机器人与云端之间的视觉token传输，用语言语义判断视觉信息的重要性，并让token预算随信道容量调整，将任务需求与通信限制共同纳入分割推理。

## 证据

LIBERO上从512个token降至32个，相对OpenVLA-OFT计算量减少74%、推理延迟降低22%；平均成功率从96.9%降至95.4%，下降1.5个百分点，并在Rayleigh和Rician衰落条件下满足容量预算。


## 局限

需要核查延迟的计时范围、信道条件及分割位置；摘要中的基准与衰落条件结果尚不足以说明真实移动网络部署表现。

- **判断**：部署与系统方向值得精读实验设置，纯策略学习方向掌握语言引导的容量自适应机制即可。

## 研究关联

对需要云端推理的VLA系统具有直接价值，给出了通信预算、推理成本和任务成功率之间可量化的取舍。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/ComVLA Communication-Aware Split Inference for VLA Models in 6G-Connected Roboti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Connected robotics is an emerging 6G application where mobile robots follow natural-language instructions to manipulate physical objects. The Vision-Language-Action (VLA) models that enable this are too large to run on the robot; a common trend is to offload inference to the cloud. The wireless link, however, limits how much sensing data the edge can transmit per control step. Two recent lines address this constraint: semantic communication codecs compress sensor data but require channel-specific retraining, and VLA token pruners select tokens from image but ignore the channel. Our insight is that the dense semantic information contained in the language already indicates which visual tokens matter. We propose ComVLA, a framework that uses this language guidance to adapt the VLA token budget to the channel capacity. Transmitting 32 tokens instead of 512 on the LIBERO benchmark, ComVLA cuts inference compute by 74% and inference latency by 22% versus the original OpenVLA-OFT baseline, at a cost of 1.5 pp in average task success (95.4% vs. 96.9%), and it stays within the capacity budget under Rayleigh and Rician fading. These results demonstrate that co-designing VLA inference and wireless communication is a practical direction for 6G-connected robotics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07838v1
- Authors: Boliang Liu, Wint Yi Poe, Jingyun Di, Riccardo Trivisonno, Giuseppe Caire
- Published: 2026-09-07T18:00:14Z
- Age days: 1

</details>
