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
url: "https://arxiv.org/abs/2610.12407v1"
published: "2026-10-08T17:46:03Z"
age_days: 3
score: 23
created: 2026-10-12
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC

> [!summary] 这篇论文到底做了什么（基于摘要）
> LeWAM 在不重建图像的潜在表征上，同时学习世界怎样变化和机器人该怎样行动。规划时，它搜索策略头的噪声输入来产生候选动作，减少直接搜索动作时钻动力学模型漏洞的问题。

## 问题

世界动作模型需要预测动作和未来观察，既用于执行，也用于规划。摘要指出两处瓶颈：重建式表征携带视觉噪声与冗余，增加预测负担；规划器直接采样动作时，可能找到模型预测很好、真实执行却不好的动作，因为它利用了动力学预测误差。

### 用一个例子理解

理解用例（非论文实验）：输入机械臂与杯子的当前画面和目标；策略头从候选噪声生成动作，世界模型预测动作后的状态，MPC 选出较好的候选并执行第一段；新画面到来后重新规划，输出连续控制动作。

## 创新点或方法

旧路线先学能重建观察的表示，再做动作和未来预测；LeWAM 改用无解码器 JEPA 潜在表示，通过双向 Transformer 联合训练前向、后向、逆动力学和策略四种模式，让表征同时接受状态演化与行动需求的约束。推理时可用策略执行，也可做 MPC：不直接任意搜索动作，而是在策略头的噪声空间搜索，再由策略生成候选动作。这样有望缩小不可信动作的搜索范围；具体 steering 更新与目标函数摘要未说明。

### 方法如何工作

1. 将观察编码为不需要重建图像的潜在状态，为后续预测减少必须解释的像素细节。
2. 用四种预测模式端到端训练，让同一表征既支持状态演化预测，也支持从状态关系推断动作和输出策略。
3. 规划时搜索策略头的噪声输入，由策略将噪声变成候选动作，避免完全自由的动作搜索。
4. 用世界模型评估候选，执行所选动作的一部分，再根据新观察重规划；具体时域和评价方式摘要只说明到此。

### 必要术语

- JEPA：在表示空间预测目标表示，无须重建原始画面；本文用它学习控制所需的潜在状态。
- 逆动力学：根据状态变化推断对应动作；它是联合训练的四种模式之一。
- MPC：预测一段未来、先执行一部分，再根据新观察重算；本文用它做闭环规划。
- 噪声空间：策略生成动作时所用随机输入的空间；本文在这里搜索候选，而非直接搜索动作。

## 证据

摘要给出三组比较：线性探针读取机器人和物体状态优于仅做前向预测的 LeWM；忽略视觉干扰的表现与 LeWM 相当，明显优于重建式 WAM；同编码器、规模匹配下，闭环表现与常规流匹配策略相当，同时保有世界模型。噪声空间规划也改善了 WAM 的闭环表现。没有任务名称、环境是真机还是仿真、指标数值或重复次数，因此只能确认作者报告的相对关系。

## 局限

我的待核查问题是噪声搜索为何有效：它是否确实减少预测误差利用，还是主要受益于策略本身？探针能读出状态只是表征可读性的证据，不能单独证明这些信息造成了控制收益。输入也没有明确的作者局限或真机验证信息。

- **判断**：值得细读规划算法及其对照实验，因为它给出了世界模型预测、策略执行和规划搜索之间一个具体、可检验的连接。

## 研究关联

这里值得借鉴的是：规划效果不好，未必只该继续提高世界模型精度，也可以改变搜索空间。让候选动作经过学到的策略生成，可能减少规划器进入模型不熟悉区域的机会；但这种约束也可能限制动作多样性。

### 下一步读哪里

先检查四种模式各自的输入、预测目标与损失，再看噪声如何被 steering、规划计算预算是否匹配，以及直接动作搜索的对照是否公平。还需核查闭环任务、干扰设置和仿真或真机条件。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：23
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-12/LeWAM A JEPA World Action Model with Diffusion-Steering-Based MPC.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions. We introduce LeWAM, a bidirectional transformer for forward, backward, inverse dynamics and policy prediction, on a decoder-free JEPA latent trained end-to-end through all four modes. We see the following benefits: 1) Alignment: linear probes read robot and object state from LeWAM's latent better than from a regular Le World Model (a forward-only JEPA world model), while the latent ignores visual distractors as well as LeWM does and far better than a reconstruction-based WAM. 2) Acting: Closed-loop evaluations of LeWAM match a regular flow-matching policy trained on the same encoder at matched size, while also providing a world model. 3) Planning: Sampling raw actions when planning with WAMs lets MPC exploit dynamics-model inaccuracies; planning in the noise space of the policy head instead improves the closed-loop performance of these WAMs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12407v1
- Authors: Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy
- Published: 2026-10-08T17:46:03Z
- Age days: 3

</details>
