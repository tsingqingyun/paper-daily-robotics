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
url: "https://arxiv.org/abs/2610.09016v1"
published: "2026-10-06T19:11:19Z"
age_days: 1
score: 32
created: 2026-10-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PAIR: Bridging Perception and Action in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> PAIR 给视觉语言动作模型补了一道“把看懂的场景变成动作准备”的接口：训练时用专家动作教会中间表示该保留什么，执行时只靠图像和指令生成这个表示，再交给动作模块细化。

## 问题

任务是根据当前图像和语言指令输出连续机器人动作。瓶颈在于，描述物体和任务的表示并不天然适合生成动作。许多现有模型把这次转换藏在内部，主要靠最终动作预测误差监督；中间表示应该包含怎样的动作结构，没有直接的学习目标。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把杯子放进托盘”；桥接模块从杯子、托盘及指令中生成带有动作结构的令牌，动作模块据此输出连续的接近、抓取和移动动作。执行时不需要先提供正确动作。

## 创新点或方法

旧做法让动作模块自己从视觉语言特征中摸索；PAIR 先从专家动作片段提取按动作时间范围组织的潜在令牌，再让 Bridge Module 提取的任务特征与它们对齐。得到的 Bridge Tokens 经投影后注入初始 Action Tokens，使 Action Expert 从已有动作线索的状态开始细化。训练时，Masked Action Autoencoder 提供动作侧监督；推理时移除它，仅用当前观察和指令生成桥接令牌。掩码方式、对齐损失和注入公式，摘要未说明。

### 方法如何工作

1. 训练时编码专家动作片段，得到动作潜在令牌，为中间表示提供直接的动作监督。
2. 从当前视觉语言表示提取任务相关特征，使桥接输入聚焦于当前要完成的操作。
3. 将这些特征与动作潜在令牌对齐，得到兼有任务信息和动作结构的 Bridge Tokens。
4. 把桥接令牌投影并注入初始动作令牌，再由 Action Expert 细化；推理时仅保留观察到桥接令牌的路径。

### 必要术语

- 动作片段：一段连续动作序列；为本文提供动作结构的训练目标。
- 潜在令牌：压缩后的内部表示单元；承载专家动作的信息。
- Action Expert：进一步生成或细化动作的模块；接收 PAIR 提供的初始动作线索。

## 证据

摘要报告了 LIBERO、LIBERO-Plus、CALVIN ABC-D，以及七个真机任务，评估对象包括 OpenVLA-OFT 和 VLA-Adapter。LIBERO-Plus 上，VLA-Adapter 成功率从 59.1% 到 64.2%；CALVIN 上平均完成序列长度从 4.42 到 4.53；七个真机任务中，OpenVLA-OFT 成功率从 51.4% 到 65.0%。这些数字来自摘要，支持在所测模型和任务上有效。摘要还报告表示分析，但未给分析方法、试验次数或误差范围，不能据此确定收益都来自哪一步。

## 局限

真机结果使证据超出了仿真，但摘要未交代七个任务的难度和变化条件。我会核查是否增加训练量或参数量，以及去掉对齐、只保留额外令牌时的结果；这些是待核查问题，不是已知缺陷。

- **判断**：值得读到方法和消融实验：核心价值在于明确监督感知到动作的转换，而不仅是增加一个中间模块。

## 研究关联

值得借鉴的是：用训练时可获得、部署时拿不到的专家动作，教会一个部署时能从观察生成的接口。若感知模块与动作模块之间缺乏直接监督，这种做法提供了具体的改进方向。

### 下一步读哪里

先检查动作潜在令牌如何对应预测时间范围、对齐是否保留任务信息，再看注入方式的消融、相同训练预算下的对比和真机任务设置。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/PAIR Bridging Perception and Action in Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Latent Tokens. A Bridge Module extracts task-relevant features from the current visual-language representations. PAIR aligns these features with the Action Latent Tokens to form Bridge Tokens that preserve task information and capture the structure of expert actions. The Bridge Tokens are then projected into the action-token space and injected into the initial Action Tokens, providing an action-ready starting point for Action Expert refinement. At inference, the autoencoder is removed, and the Bridge Tokens are generated only from the current observation and instruction. Experiments on LIBERO, LIBERO-Plus, and CALVIN ABC-D show gains for the evaluated OpenVLA-OFT and VLA-Adapter models. On LIBERO-Plus, PAIR raises VLA-Adapter's success rate from 59.1% to 64.2%. On CALVIN, it increases VLA-Adapter's average completed sequence length from 4.42 to 4.53. Across seven real-world tasks, PAIR raises OpenVLA-OFT's success rate from 51.4% to 65.0%. Representation analyses show that Bridge Tokens retain task information while making continuous-action information accessible before Action Expert refinement. These results support a shared intermediate representation as a useful interface between perception and action in continuous-action VLAs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09016v1
- Authors: Kaixi Feng, Guoheng Sun, Ang li
- Published: 2026-10-06T19:11:19Z
- Age days: 1

</details>
