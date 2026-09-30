---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08636v1"
published: "2026-09-08T12:06:23Z"
age_days: 1
score: 25
created: 2026-09-10
concepts: ["世界模型", "具身智能评测与基准"]
---

# From Where to How: Continuous 4D Interaction Forecasting from Egocentric Video

> [!summary] 先说人话（基于摘要）
> HIGFlow 先预测人接下来会在哪里交互，再根据这些位置生成全身运动。配套 Coherent4D 把未来交互位置与姿态在时间和坐标上对齐，便于联合评测。

## 这篇到底在做什么

- **卡在哪里**：第一视角预测既需把语义转成精确连续三维位置，又需产生多样且结构合理的身体运动；分开建模会遗漏交互位置与姿态的时空对应。
- **关键解法**：输入第一视角视频，先结合语义定位和短时视觉动态预测未来位置序列，再用该序列条件化确定性运动锚点与残差 Flow Matching，输出多样的全身姿态预测。
- **拿什么证明**：Coherent4D 含约 233K 样本、覆盖三个领域，提供对齐的位置与全身姿态及连续空间指标。三个领域实验均报告位置与姿态预测改善，并有组件消融；摘要未给出改善幅度。

## 值不值得读

- **和你的研究有什么关系**：对世界模型和具身评测研究者，可用于研究人类交互未来的几何与运动一致性，也可为辅助机器人提供意图预测研究素材。
- **先别急着信**：需核查位置预测误差向姿态生成的传播，以及数据划分是否充分测试跨场景与跨动作泛化。
- **判断**：做人类动作预测值得细读数据协议和级联建模，机器人辅助效果仍需另行验证。

## 研究关联

- **概念**：[[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/From Where to How Continuous 4D Interaction Forecasting from Egocentric Video.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Egocentric 4D interaction forecasting aims to anticipate both where future interactions will occur in 3D and how the human body will move to realize them, providing an important capability for assistive robotics and human-computer interaction. Existing methods struggle to translate semantic understanding into precise continuous 3D localization and to balance motion diversity with structural consistency in pose forecasting. More fundamentally, these tasks are often modeled separately, leaving the continuous geometric and temporal correspondence between interaction locations and body motion insufficiently captured. To address these challenges, we introduce Coherent4D, a large-scale egocentric dataset for continuous 4D interaction forecasting, comprising approximately 233K samples across three domains. Each sample pairs a sequence of future 3D interaction locations with corresponding full-body poses, aligned in time and expressed in a shared coordinate system. We also provide evaluation metrics in continuous space. Building on this formulation, we propose HIGFlow, a Hand Interaction Guided Residual Flow framework that models forecasting as a cascaded where-to-how process. HIGFlow first forecasts continuous future interaction locations by combining semantic grounding with short-horizon visual dynamics, and then uses the predicted location sequence to condition a deterministic motion anchor and residual Flow Matching for diverse yet structurally consistent full-body motion forecasting. Extensive experiments across all three domains demonstrate consistent improvements over representative baselines on both location and pose forecasting, while ablations validate the contributions of the proposed components. The project page is available at https://corrineqiu.github.io/from-where-to-how/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08636v1
- Authors: Qiaohui Chu, Haoyu Zhang, Meng Liu, Haoxiang Shi, Dongmei Jiang, Liqiang Nie
- Published: 2026-09-08T12:06:23Z
- Age days: 1

</details>
