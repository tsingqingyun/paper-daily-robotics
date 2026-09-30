---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00908"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-09-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs

> [!summary] 先说人话（基于摘要）
> 这项自适应动作分块方法让 VLA 判断一串动作执行到哪里就该重新观察。它利用内部交叉注意力熵的平台期截断动作，无需额外训练。

## 这篇到底在做什么

- **卡在哪里**：固定短动作块需要频繁推理，还可能产生振荡；固定长动作块则可能逐渐偏离环境新状态，难以兼顾效率与准确性。
- **关键解法**：监测动作专家中动作对观测的交叉注意力；当熵持续处于高位平台时，判断当前观测对后续开环动作的支撑减弱，动态缩短执行时域。
- **拿什么证明**：在 π0.5、X-VLA 上，覆盖 RoboTwin 2.0、LIBERO 和三项真机任务，平均成功率优于固定时域及自适应分块基线；摘要未给出提升数字，并称额外开销可忽略。

## 值不值得读

- **和你的研究有什么关系**：为 VLA 闭环执行提供无需训练的调节机制；对世界模型研究的联系主要是何时需要更新观测，并未学习环境动力学。
- **先别急着信**：注意力熵与误差的关联是核心依据，需核查平台检测规则及其跨模型、跨任务稳定性。
- **判断**：值得精读截断算法并评估接入成本，机制直接作用于推理期的效率与可靠性取舍。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/Knowing When to Stop Adaptive Action Chunking via Internal Cross-Attention Dynam.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.00908v2 Announce Type: replace Abstract: Action chunking is a standard execution strategy in modern Vision-Language-Action (VLA) frameworks, but fixed execution horizons impose a trade-off between efficiency and accuracy. Short chunks require frequent inference and may cause oscillatory behavior, whereas long chunks can become misaligned with newly observed states. We address this limitation with an adaptive action chunking approach based on internal cross-attention dynamics in the action expert. We observe that, as the prediction horizon extends, action-to-observation cross-attention becomes increasingly dispersed and its entropy rises toward a plateau. This pattern is associated with higher action prediction error and provides an online signal that the current observation offers limited grounding for further open-loop execution. Based on this observation, we introduce a training-free truncation mechanism that detects sustained high-entropy plateaus and dynamically selects the execution horizon during inference. The method uses attention weights already computed by the policy and introduces negligible additional overhead. Evaluations on $\pi_{0.5}$ and X-VLA across RoboTwin 2.0, LIBERO, and three real-world manipulation tasks show improved average task success over fixed-horizon and adaptive chunking baselines, while preserving efficient closed-loop control. These results show that cross-attention dynamics can provide a practical internal signal for adaptive action execution in VLAs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00908
- Authors: Runze Xu, Xiaolong Shan, Shuang Dai, Yu Wang, Jincheng Yu
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
