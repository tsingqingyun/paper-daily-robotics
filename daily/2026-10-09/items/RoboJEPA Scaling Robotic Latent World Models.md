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
url: "https://arxiv.org/abs/2610.10515v1"
published: "2026-10-07T17:54:42Z"
age_days: 1
score: 34
created: 2026-10-09
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# RoboJEPA: Scaling Robotic Latent World Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboJEPA 在内部特征空间预测机器人行动后的未来，并研究投入更多计算后，这种预测和规划能力能否提前估算。它还展示了以一张目标图片为任务目标、直接在真机上规划的用法。

## 问题

任务一方面是学习可用于机器人规划的世界模型，另一方面是预测扩大模型、数据和计算投入的收益。摘要指出现有潜在世界模型虽然能预测和规划，却缺少有原则的能力增长估计方式，导致扩规模时难以判断投入是否划算。

### 用一个例子理解

理解用例（非论文实验）：输入当前桌面图像和“杯子已经放进托盘”的目标图像；模型预测候选动作之后的内部状态，规划器据此选择动作；机器人执行并逐步接近目标。候选动作的搜索算法未在摘要中给出。

## 创新点或方法

相较于只训练模型再测任务成绩，本文采用 JEPA，在涵盖 12 种机器人形态的数据上训练，并把潜在空间中连续预测的误差作为规模分析对象。训练侧学习未来表示并拟合误差与计算量的关系；部署侧利用模型预测，以单张目标图像指导规划，摘要称无需任务专项适配即可作为机器人智能体使用。动作如何搜索、目标距离如何计算、编码器如何训练均未说明。

### 方法如何工作

1. 用多种机器人形态的数据训练 JEPA，使模型获得预测未来内部表示的能力。
2. 让模型连续预测未来状态，测量潜在 rollout 的想象误差，形成统一质量指标。
3. 比较不同计算规模的误差并拟合规律，用来估计更大规模的质量。
4. 以目标图像进行机器人规划，再检查规划成绩是否对应误差变化；具体规划算法摘要只说明到此。

### 必要术语

- JEPA：在内部表示之间学习预测的架构；本文据此构建机器人世界模型。
- 潜在 rollout：在内部特征空间连续推演未来；本文测量其误差。
- 规模律：投入与模型质量之间可拟合的关系；本文用于预测扩规模结果。
- 零样本部署：部署时不为目标任务再做专项训练；本文报告这种真机规划用法。

## 证据

摘要给出 12 种机器人形态和最大 8B 参数，并称想象误差服从关于计算量的二阶幂律，能预测超出拟合规模的模型质量。下游规划随计算量可预测地改善，且与想象误差强相关；另有真机长时程任务展示。但没有任务名称、成功率、相关系数、外推误差或基线数据，不能据此量化扩规模收益。

## 局限

强相关并不证明降低想象误差必然导致规划变好，两者可能都随规模增长。摘要也未界定零样本部署覆盖哪些机器人与任务；在 12 种形态上训练，不等于对任意新形态都能直接部署。这些边界需要正文确认。

- **判断**：值得深入读规模拟合和真机评估，重点看外推是否准确、误差代理是否跨任务稳定，而不只看最大模型有多大。

## 研究关联

这里可借鉴的是先寻找便宜、可重复测量的模型误差，再检查它是否对应昂贵的真机任务表现。若这种关系在目标任务分布上稳定，便能用离线测量筛选候选模型，减少每次训练后都上真机比较的成本。

### 下一步读哪里

核查二阶幂律的具体形式、拟合与外推的规模区间，以及计算量变化时数据和模型大小如何控制；再看想象误差与真机成绩的相关性是否在不同任务中分别成立。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/RoboJEPA Scaling Robotic Latent World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring long-horizon planning on real hardware. We release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10515v1
- Authors: Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
- Published: 2026-10-07T17:54:42Z
- Age days: 1

</details>
