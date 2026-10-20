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
url: "https://arxiv.org/abs/2604.20012"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 46
created: 2026-10-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training

> [!summary] 这篇论文到底做了什么（基于摘要）
> EmbodiedMidtrain 在通用 VLM 变成机器人 VLA 之前，加一道贴近具身任务的中间训练。关键是从大规模视觉语言数据中挑选更接近机器人数据的样本，让动作学习从更合适的起点开始。

## 问题

VLA 需要理解观测和指令并输出动作，但通常直接继承通用 VLM。摘要指出，机器人数据集中在较小、且与广泛 VLM 数据明显分离的区域；同一数据源内部也有差异，因此直接使用现成检查点，或仅按数据集名称挑数据，都可能不够贴合任务。

### 用一个例子理解

理解用例（非论文实验）：目标是让机器人按“把杯子放到盘子左边”操作；先筛选贴近机器人数据的视觉语言样本做中间训练，再用动作数据微调；部署时输入相机画面和指令，输出动作。

## 创新点或方法

旧流程是通用 VLM 直接进行 VLA 微调；本文先训练一个轻量接近度估计器，从 VLM 数据池筛出更贴近 VLA 的候选，构成 EmbodiedMidtrain-1M，再依次进行 VLM 中间训练和下游 VLA 微调。接近度如何定义、估计器如何监督，摘要未说明。改动位于训练准备阶段，摘要未描述推理时增加额外模块。

### 方法如何工作

1. 比较 VLM 与 VLA 数据分布，确定通用数据并非同样适合机器人任务。
2. 用可学习的接近度估计器筛选候选，使中间训练更集中于目标相关内容。
3. 用筛选出的 EmbodiedMidtrain-1M 训练 VLM，得到新的初始化。
4. 再做 VLA 动作微调，并在仿真和真机任务上检验初始化是否带来收益。

### 必要术语

- 中间训练：通用预训练与下游微调之间的一段训练；本文用它衔接视觉语言能力与机器人任务。
- 接近度估计器：给数据与目标分布的接近程度打分的模型；本文用它选样。
- 动作头：把模型内部信息转成动作的部分；本文在不同动作头上检验收益。

## 证据

摘要报告，在仿真操作基准和真机任务上，相比现成 VLM 检查点，不同骨干与动作头均获得提升；收益也覆盖未用于指导选样的下游任务。训练分析称收益从微调早期出现并持续扩大。摘要没有给出基准名称、成功率、训练成本或误差范围，因此能支持跨设置的一致方向，不能判断收益大小及性价比。

## 局限

我的待核查问题是：收益有多少来自选样，有多少来自额外训练计算？还需检查指导选样的任务与测试任务如何划分。摘要称偏好空间推理且保留多样性，但没有给出衡量多样性的具体方法。

- **判断**：值得读到选样目标和等预算消融，因为它们决定这套数据准备方式能否迁移到其他 VLA。

## 研究关联

这里可借鉴的是先检查预训练数据与目标任务的距离，再决定中间训练内容。若动作微调数据有限，补充与空间理解更接近的视觉语言样本，是值得检验的路径。

### 下一步读哪里

先查接近度估计器的输入、监督信号和目标数据需求，再查随机选样、全池训练及等计算预算对照；最后核查未参与选样的下游任务划分。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：46
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/EmbodiedMidtrain Bridging the Gap between Vision-Language Models and Vision-Lang.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2604.20012v2 Announce Type: cross Abstract: Vision-Language-Action Models (VLAs) inherit their visual and linguistic capabilities from Vision-Language Models (VLMs), yet most VLAs are built from off-the-shelf VLMs that are not adapted to the embodied domain, limiting their downstream performance. In this work, we propose EmbodiedMidtrain to bridge the gap between VLMs and VLAs. We first characterize the data distribution gap between them, showing that VLA data occupy compact regions that are largely separated from the broader VLM distribution, while the degree of alignment varies substantially both across and within VLM data sources. Then, we build a mid-training data engine that leverages a lightweight learnable proximity estimator to select the most VLA-aligned candidates from a large VLM pool, and produce EmbodiedMidtrain-1M, a VLM dataset that we further use to mid-train the VLM before downstream VLA fine-tuning. Experiments on both simulated robot manipulation benchmarks and real-world tasks show consistent VLA performance gains over off-the-shelf checkpoints across VLM backbones and VLA action heads. These gains extend to downstream tasks not used to guide data selection. Further analysis reveals that mid-training provides a stronger initialization for VLA fine-tuning, with gains emerging from the earliest steps and widening throughout training. Moreover, the data engine captures both dataset-level and sample-level alignment signals, favoring spatial reasoning over text-centric tasks while preserving the diversity of the VLM data. We will release all code, data and models for future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2604.20012
- Authors: Yiyang Du, Zhanqiu Guo, Haochen Zhang, Annabella Macaluso, Xin Ye, Liu Ren, Yonatan Bisk, Chenyan Xiong
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
