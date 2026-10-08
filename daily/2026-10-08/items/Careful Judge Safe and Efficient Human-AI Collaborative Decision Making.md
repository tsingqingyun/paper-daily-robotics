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
url: "https://arxiv.org/abs/2610.09043v1"
published: "2026-10-06T19:44:15Z"
age_days: 1
score: 30
created: 2026-10-08
concepts: ["具身智能评测与基准"]
---

# Careful Judge: Safe and Efficient Human-AI Collaborative Decision Making

> [!summary] 这篇论文到底做了什么（基于摘要）
> CARE 把人工复核变成持续改进决策的反馈，同时让风险校准跟着模型更新。它解决的是：AI 越学越多时，怎样减少人工查询，又不继续沿用已经过时的安全门槛。

## 问题

任务是在 AI 和人工协作中作出符合人类判断的决策，并控制风险与人工成本。只把 AI 弃权后的复核当一次性补救，会浪费反馈；但从选择性查询到的反馈持续学习，又会改变模型，使为旧模型校准的安全规则失效。瓶颈是学习、查询和风险控制必须一起更新。

### 用一个例子理解

理解用例（非论文实验）：输入一条待审核文本，黑盒模型给出决策；CARE 判断该结果是否可自动接受，否则提交人工。人工纠正进入后续学习，校准规则也随之更新，使以后类似输入可能自动处理。摘要未验证这个具体流程配置。

## 创新点或方法

旧做法是模型不确定时找人，然后继续使用原有安全规则；CARE 将纠正与升级人工处理组成持续流程，并加入自适应校准模块。反馈用于改进未来决策，校准随更新维持风险控制，决定哪些决策可自动处理。摘要声称校准对任意纠正模块都提供逐时间步风险保证，也支持黑盒 AI。训练或持续适应阶段如何更新纠正模块、运行时具体怎样触发人工查询，摘要均未说明；不能把这种保证理解为无条件零错误。

### 方法如何工作

1. 取得黑盒 AI 对当前输入的决策，为纠正和风险判断提供对象。
2. 由纠正模块处理决策，并通过自适应校准判断是否需要升级人工；具体顺序与公式未说明。
3. 对需要人工处理的输入获得反馈，用于改善后续决策，避免复核只起一次作用。
4. 随纠正模块变化更新校准，使风险规则对应当前系统，再继续处理后续输入。

### 必要术语

- 弃权：AI 暂不自动作出最终决策；为人工介入留出入口。
- 选择性反馈：只对部分被查询的输入获得人类判断；可能改变学习所见数据。
- 风险校准：依据目标风险设置决策规则；本文要求它随模型变化自适应更新。

## 证据

摘要报告四个来自驾驶、语言和机器人领域的真实数据集，称 CARE 实现符合人类判断的决策，并相对基线减少 25%–81% 的人工查询。数字来自摘要，但没有基线名称、各数据集结果、风险定义、阈值或样本量。因此支持作者在这些数据上评估了查询节省，不能判断各场景的收益，也不能把真实数据集评估当成真实驾驶或机器人部署。

## 局限

保证的实际含义取决于风险定义和定理假设。我会核查人类判断是否被当作可靠标签、选择性反馈如何处理，以及逐步风险控制是何种概率陈述。摘要另指出查询效率分析依赖模型训练较好、错位具有清晰结构，这不是所有任务都会满足的条件。

- **判断**：值得先读风险保证的定义与假设，再看查询成本实验；省下多少人工有意义，前提是弄清系统承诺控制哪一种风险。

## 研究关联

这里值得借鉴的是：人工反馈更新的不应只有预测模型，还应包括决定何时相信模型的规则。若系统持续学习、同时允许部分决策自动通过，静态校准可能逐渐失配；CARE 将这种失配纳入设计。

### 下一步读哪里

优先核查风险函数、校准数据使用方式、逐时间步保证的概率含义，以及选择性查询下的假设；再比较相同风险要求下各基线的查询量。

- **概念**：具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Careful Judge Safe and Efficient Human-AI Collaborative Decision Making.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In human-AI collaborative decision making, human review can prevent unsafe AI decisions, but each human judgment is costly. Treating human intervention after AI abstention as a one-off fallback misses the opportunity to improve future AI decisions for greater automation, yet AI adaptively learning from selectively queried human feedback breaks safety guardrails calibrated for old models. We approach this challenge with CARE---calibrated adaptive rectification and escalation---an end-to-end pipeline that combines AI models and human reviewers to guarantee safe, human-aligned decisions, while continuously learning from human feedback to achieve greater automation with fewer human queries. CARE is principled, general, modular, and works with any black-box AI model. Our novel adaptive calibration module guarantees risk control at every time step for any rectification module. We further show how CARE improves query efficiency when the AI model is well trained and the human-AI misalignment has a clear structure. Experiments on four safety-critical real-world datasets spanning driving, language, and robotics demonstrate that CARE achieves human-aligned decisions while reducing human queries by 25-81% relative to baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09043v1
- Authors: Chenyu Zhang, Rachel Luo, Boyi Li, Anjali Parashar, Marco Pavone, Apoorva Sharma
- Published: 2026-10-06T19:44:15Z
- Age days: 1

</details>
