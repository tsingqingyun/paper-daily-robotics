---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00908v1"
published: "2026-09-01T08:38:16Z"
age_days: 1
score: 35
created: 2026-09-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs

> [!summary] 先说人话（基于摘要）
> 论文用 VLA 动作专家内部的交叉注意力熵判断“什么时候该停下当前动作块”。其训练-free 截断器检测持续高熵平台，动态缩短缺乏观测支撑的开环执行。

## 这篇到底在做什么

- **卡在哪里**：固定动作块存在效率—精度冲突：过短会频繁推理并振荡，过长则可能因环境变化而与最新状态错位。瓶颈是在线判断当前观测还能可靠支撑多远的动作预测。
- **关键解法**：方法读取策略本已计算的动作到观测交叉注意力；当预测跨度增加、注意力变分散且熵进入持续高位平台时，截断执行 horizon。与固定长度或另训一个调度器不同，它无需训练且几乎不增加计算。
- **拿什么证明**：在 π0.5、X-VLA，RoboTwin 2.0、LIBERO及3个真实操作任务上，平均成功率优于固定 horizon 和其他自适应分块基线，同时保持高效闭环控制；摘要未给出具体增益数字。

## 值不值得读

- **和你的研究有什么关系**：对 VLA 部署很实用：它把模型内部注意力变成执行置信信号，可在不重训策略的情况下改善闭环频率，并为研究模型自我监控提供入口。
- **先别急着信**：摘要只报告注意力熵与预测误差相关，尚不足以证明该信号跨架构、任务和失败类型都可靠；阈值稳定性需全文核查。
- **判断**：值得精读算法和真实机器人结果；若阈值无需任务级调参，这会是很容易接入现有 VLA 的实用改进。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Knowing When to Stop Adaptive Action Chunking via Internal Cross-Attention Dynam.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action chunking is a standard execution strategy in modern Vision-Language-Action (VLA) frameworks, but fixed execution horizons impose a trade-off between efficiency and accuracy. Short chunks require frequent inference and may cause oscillatory behavior, whereas long chunks can become misaligned with newly observed states. We address this limitation with an adaptive action chunking approach based on internal cross-attention dynamics in the action expert. We observe that, as the prediction horizon extends, action-to-observation cross-attention becomes increasingly dispersed and its entropy rises toward a plateau. This pattern is associated with higher action prediction error and provides an online signal that the current observation offers limited grounding for further open-loop execution. Based on this observation, we introduce a training-free truncation mechanism that detects sustained high-entropy plateaus and dynamically selects the execution horizon during inference. The method uses attention weights already computed by the policy and introduces negligible additional overhead. Evaluations on $π_{0.5}$ and X-VLA across RoboTwin 2.0, LIBERO, and three real-world manipulation tasks show improved average task success over fixed-horizon and adaptive chunking baselines, while preserving efficient closed-loop control. These results show that cross-attention dynamics can provide a practical internal signal for adaptive action execution in VLAs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00908v1
- Authors: Runze Xu, Xiaolong Shan, Shuang Dai, Yu Wang, Jincheng Yu
- Published: 2026-09-01T08:38:16Z
- Age days: 1

</details>
