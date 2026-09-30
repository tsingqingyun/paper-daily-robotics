---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08678v1"
published: "2026-09-08T12:44:38Z"
age_days: 1
score: 24
created: 2026-09-10
concepts: ["AI 核心知识地图"]
---

# HiBRIDGE: A Hierarchical Bayesian Neural Network Framework for Interpretable Dialogue Management in Group-Robot Interaction

> [!summary] 先说人话（基于摘要）
> HiBRIDGE 把群体对话中“对谁说、说什么”拆成分层决策，并用贝叶斯预测表达多个选择都合理时的不确定性。

## 这篇到底在做什么

- **卡在哪里**：多人交互中可能同时存在多种合理行为，现有方法难以表达这种不确定性，也缺少语义清晰的中间决策步骤来解释机器人选择。
- **关键解法**：以分层贝叶斯神经网络进行多阶段行为选择，再用决策树代理分析决策结构并生成解释，对比平坦模型与确定性版本。
- **拿什么证明**：三个离线群体人机交互数据集上，贝叶斯版本优于确定性对应模型和多个基线；20 人在线研究更偏好分层解释，12 人现场研究展示实时自主交互可行性，两类贝叶斯版本均获正面评价。

## 值不值得读

- **和你的研究有什么关系**：对机器人交互研究者，提供了不确定性建模与可解释决策结合的案例；对 VLA、操作学习和物理世界模型的直接价值有限。
- **先别急着信**：代理解释更受欢迎不等于忠实反映原模型计算，需核查解释保真度；用户研究样本也较小。
- **判断**：做人机对话值得读分层设计与解释评测，其他机器人方向浏览结论即可。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/HiBRIDGE A Hierarchical Bayesian Neural Network Framework for Interpretable Dial.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In multi-party human-robot interaction, a robot must continuously decide whom to address and what to say to participate effectively in the conversation. In real-world interactions, this is challenging because several behaviours may be plausible at the same time: a robot might continue a topic with one participant, involve another through a question, or address the whole group, with the appropriate choice depending on both whom it addresses and the interaction context. Current approaches remain limited in representing uncertainty when several behaviours are plausible and in structuring decisions into semantically meaningful intermediate steps that make robot decisions easier to interpret. Addressing these, we present HiBRIDGE, a hierarchical Bayesian neural network framework for group-robot dialogue management. Its Bayesian formulation enables uncertainty-aware prediction and robust learning from limited interaction data, while the hierarchical approach formulates behaviour selection as a structured, multi-stage decision process. We further use decision-tree surrogates to investigate whether this structure can support more interpretable explanations. Across three offline group-HRI datasets, our findings show that Bayesian formulations outperform their deterministic counterparts and several state-of-the-art baselines. Next, through an online study (N=20), we show that explanations derived from the hierarchical model are rated as more helpful for understanding robot behaviour and are preferred over those derived from the flat model. Finally, through our in-person study (N=12), we demonstrate the feasibility of HiBRIDGE for autonomous real-time group interaction, with both hierarchical and flat Bayesian variants positively perceived. Overall, HiBRIDGE combines strong predictive performance with a structured decision process that supports more interpretable explanations of robot behaviour.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08678v1
- Authors: Massimiliano Nigro, Hatice Gunes, Micol Spitale, Fethiye Irmak Dogan
- Published: 2026-09-08T12:44:38Z
- Age days: 1

</details>
