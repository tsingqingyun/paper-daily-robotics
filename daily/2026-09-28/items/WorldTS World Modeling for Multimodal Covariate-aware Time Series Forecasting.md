---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31162v1"
published: "2026-09-25T11:54:18Z"
age_days: 2
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型"]
---

# WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting

> [!summary] 先说人话（基于摘要）
> WorldTS 用潜在动力学预测时间序列，并让外部多模态信息直接影响状态的形成与演化。它先学习状态预测，再冻结动力学、训练解码器输出未来观测。

## 问题

历史观测只部分反映底层系统，未来还受外部因素影响。已有潜在空间预测改善了表示，但如何让多模态协变量直接进入状态演化仍缺少充分探索。

## 创新点或方法

两阶段训练：先学习受多模态协变量条件控制的预测相关潜在动力学，得到未来状态；再固定动力学，训练观测解码器映射到未来时间序列。

## 证据

摘要报告在 21 个真实数据集上进行了广泛实验，并称验证了有效性；未列出具体误差、增益或数据集名称。摘要未给出可核查的结果数字。

## 局限

需核查预测时哪些协变量可获得，以及两阶段训练相对联合训练的作用；不能仅凭“世界模型”名称推断控制能力。

- **判断**：时间序列与多模态状态建模方向值得读方法，机器人方向可先看架构与适用输入。

## 研究关联

对世界模型研究者，协变量如何进入潜在状态演化值得参考；但摘要没有机器人动作、规划或闭环控制实验，对具身研究的价值主要是方法启发。

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/WorldTS World Modeling for Multimodal Covariate-aware Time Series Forecasting.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Time series forecasting is typically framed as learning a direct mapping from historical to future observations in the observation space. However, sequences of observations generally provide only a partial view of the dynamics of the underlying system, with future observations being shaped by latent dynamics. Recent latent-space forecasting methods thus achieve improved performance by predicting future observations from latent-space representations of historical observations rather than directly forecasting future observations in the observation space. Next, while future observations are also shaped by external factors, how to incorporate external, often multimodal, information into forecasting, so that it can shape latent-state formation and evolution directly, remains underexplored. We propose WorldTS, a world-modeling based forecasting framework that integrates multimodal covariates directly into the forecasting to further improve forecasting performance. Specifically, WorldTS employs a two-stage training strategy. First, it learns forecasting-relevant latent state dynamics conditioned on multimodal covariates, yielding encoded future states. Next, the learned state dynamics are frozen, and an observation decoder is trained to map the predicted future states back to future observations. Extensive experiments on 21 real-world datasets offer insight into WorldTS and its effectiveness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31162v1
- Authors: Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng, Wangmeng Shen, Chenjuan Guo, Bin Yang, Jilin Hu, Christian S. Jensen
- Published: 2026-09-25T11:54:18Z
- Age days: 2

</details>
