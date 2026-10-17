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
url: "https://arxiv.org/abs/2610.22178v1"
published: "2026-10-15T16:34:06Z"
age_days: 1
score: 34
created: 2026-10-17
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# REKI: Registering Knowledge in VLAs

> [!summary] 这篇论文到底做了什么（基于摘要）
> REKI 是一个 2.4B 参数的视觉语言动作模型，用动作专家里的少量寄存器保存近期视觉信息，让机器人少因忘记刚才发生的事而来回摆动。它还展示了只用公开数据训练较小模型的可行性。

## 问题

机器人看到当前画面后，可能仍不知道自己是在接近物体、已经尝试抓取，还是正在撤回；这些阶段可能看起来相似，却需要不同动作。REKI 要解决的是近期历史不足带来的控制歧义，同时兼顾模型体积和运行成本。摘要没有说明此前哪些记忆方案成本过高，不能把所有已有 VLA 都视为无记忆模型。

### 用一个例子理解

理解用例（非论文实验）：输入是“把杯子放进托盘”和连续相机画面；机器人刚绕过杯柄，当前画面与此前相似。寄存器保留近期视觉线索，动作专家据此生成继续靠近的动作，而不是再次退回。这个例子说明记忆的用途，不代表论文验证过该任务。

## 创新点或方法

相较于只根据当前信息决定动作，REKI 在动作专家里加入少量寄存器 token：每帧把 VLM 的输出压缩进去，再让它们留在专家缓存中，供后续决策使用。训练时，VLM 接流匹配动作专家，使用筛选后的公开机器人、第一视角人类和视觉语言数据预训练；推理时，缓存随时间保留近期信息。记忆怎样压缩、保留多久、训练时怎样监督，摘要未说明。

### 方法如何工作

1. 把当前视觉和语言交给 VLM，得到动作生成所需的信息；具体输入格式摘要未说明。
2. 用动作专家中的少量寄存器概括该帧 VLM 输出，留下后续决策可能需要的线索。
3. 让寄存器持续存在于专家缓存中，使后续帧能利用近期过去。
4. 由流匹配动作专家生成控制动作；历史如何参与生成、一次输出多长的动作序列，摘要只说明到此。

### 必要术语

- VLA：把视觉、语言与动作连接起来的模型；本文用它根据观察和指令控制机器人。
- 寄存器 token：承载内部信息的少量向量位置；本文让它们概括并保存近期视觉输出。
- 流匹配：学习如何逐步生成目标样本的方法；本文用于动作专家，具体生成过程未展开。

## 证据

摘要称，在 LIBERO-Plus、RoboTwin Clean2Rand 和 RoboCasa365 上，REKI 只被约两倍体积的模型超过，但未提供具体分数、对手名称或速度数据。记忆在仿真和真机上都提高了成功率，姿态间振荡约减少到原来的四分之一。后者支持控制更稳定，但振荡定义、任务分布和消融配置仍需核查；不能据此断言它掌握了长期任务规划。

## 局限

摘要没有报告明确的失效条件。我会核查缓存是否在任务切换时清空、遮挡持续较久后是否仍有效，以及成功率收益能否与数据配方的贡献分开。公开数据预训练和真机改善都有摘要依据，但不代表无需目标机器人适配。

- **判断**：值得读到缓存更新机制和记忆消融，因为最可借鉴的是少量持久状态怎样改变连续控制，而非单看参数规模排名。

## 研究关联

值得借鉴的是把记忆放在动作生成端：不必让整个视觉语言主干反复处理全部历史，也可能保留控制必需的近期线索。对于当前画面不足以判断动作阶段的任务，这是一种值得检查成本与收益的设计。

### 下一步读哪里

优先核查寄存器读写、缓存长度及重置方式，再看无记忆对照是否保持训练数据与计算量一致；还应检查振荡统计和真机任务覆盖面。输入没有正文节选，无法指定图表。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/REKI Registering Knowledge in VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in the action expert summarise the output of the VLM at each frame and persist in the expert's cache. This memory improves success in simulation and on real robots, and makes oscillations between poses about four times rarer. REKI uses a simple model design and training paradigm, and is optimised to be efficient at training and inference. We release the full code across data curation, training, inference and evaluation, deployment, and all pretrained and finetuned model weights: https://github.com/kyutai-labs/reki.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22178v1
- Authors: Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary, Shizhe Chen, Moritz Böhle
- Published: 2026-10-15T16:34:06Z
- Age days: 1

</details>
