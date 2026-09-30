---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08162v1"
published: "2026-09-08T02:46:13Z"
age_days: 1
score: 37
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# WorldAgen: Unified State-Action Prediction with Test-Time World Model Training

> [!summary] 先说人话（基于摘要）
> WorldAgen让VLA进入新环境后先探索、再用真实状态变化更新世界模型，以改善动作预测。关键是世界预测与动作预测共享骨干，使部署时学到的环境信息能够影响策略。

## 问题

任务是适应新物体配置或变化后的动力学。现有世界模型与VLA结合方法主要依赖静态数据预训练，部署后缺少主动获取新环境信息并更新模型的机制。

## 创新点或方法

共享Transformer连接两个头：世界模型头从历史状态—动作轨迹预测未来状态，智能体头根据任务指令预测动作，并以混合单向注意力掩码分隔信息流。测试时执行探索动作、收集真实转移，再进行轻量世界模型更新。

## 证据

在CALVIN和LIBERO上，基础模型与先进方法相当或部分更优；摘要称少量样本的测试时训练进一步超过现有先进模型。摘要未给出可核查的结果数字。


## 局限

最需要核查测试时更新哪些共享参数、用了多少交互样本，以及性能对照是否计入探索与更新成本。

- **判断**：值得精读适配协议和信息流设计，但“少量更新即领先”的强度需要结果表支撑。

## 研究关联

为世界模型如何实际帮助VLA部署适配提供了具体路径：利用新环境转移更新预测能力，再观察动作收益。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/WorldAgen Unified State-Action Prediction with Test-Time World Model Training.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

How can vision-language-action (VLA) models adapt to new environments where world dynamics shift? While recent research has combined world modeling and action prediction to improve VLA performance, existing methods largely rely on pretraining on static datasets, without mechanisms for active adaptation at deployment time. As a result, these models often fail to generalize when deployed in unseen scenarios with novel object configurations or dynamics. We present WorldAgen, a unified framework that jointly learns world modeling and action prediction while enabling Test-Time Training (TTT) to adapt to new environments. WorldAgen employs a shared Transformer backbone with two heads: (1) a world model head that predicts future states from past state-action trajectories, and (2) an agent model head that predicts actions conditioned on task instructions. We design a Mixed Unidirectional Attention Mask to separate these two models. During test time, WorldAgen samples exploratory actions, collects ground-truth state transitions, and performs lightweight TTT updates to refine its world model. This adaptation improves the model's understanding of the environment and leads to more accurate action predictions. Experiments on the CALVIN and LIBERO benchmarks demonstrate that our baseline model achieves comparable, and in some cases superior, performance to current state-of-the-art approaches. Moreover, with TTT on a small number of samples, our method surpasses existing state-of-the-art models, highlighting the effectiveness of adapting world models at inference time.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08162v1
- Authors: Chi Wan, Kangrui Wang, Yuan Si, Pingyue Zhang, Manling Li
- Published: 2026-09-08T02:46:13Z
- Age days: 1

</details>
