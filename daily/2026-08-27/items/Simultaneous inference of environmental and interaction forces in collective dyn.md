---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25181v1"
published: "2026-08-25T21:55:12Z"
age_days: 1
score: 28
created: 2026-08-27
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Simultaneous inference of environmental and interaction forces in collective dynamics

> [!summary] 先说人话（基于摘要）
> 该工作从群体轨迹中同时反演个体间的非参数交互核与环境/个体内力，并用基于该学习框架的模型选择恢复潜在机制。

## 问题

群体系统的宏观协调来自局部交互，但仅学习交互核会把环境外力混入交互机制；通用方程发现又可能忽略群体动力学的物理结构，影响精度与解释。

## 创新点或方法

输入多智能体轨迹，变分框架以非参数形式学习交互核，同时用半参数或全非参数形式学习环境力；随后利用所学特征进行模型选择，输出最能解释轨迹的动力学框架与机制。

## 证据

在同步、对齐、吸引—排斥和外部环境力等多个基准模型上验证，摘要称能够区分不同群体动力学框架并恢复机制；未给出可核查的误差或数字。


## 局限

摘要未说明轨迹数量、噪声鲁棒性或可辨识条件，交互核与环境力能否唯一分离是最需要全文证明的地方。

- **判断**：群体动力学与系统辨识研究者值得精读理论条件；一般具身智能日报读结论即可。

## 研究关联

对群体机器人世界模型和可解释系统辨识有价值，可帮助从轨迹分离环境作用与智能体交互；对主流单机器人VLA几乎没有直接价值。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/Simultaneous inference of environmental and interaction forces in collective dyn.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Collective dynamics arise in a wide range of physical, biological, and engineering applications. Examples include cell migration, swarm robotics, social dynamics, and animal behavior. A defining characteristic of these systems is the emergence of large-scale coordination from local interactions among agents; a fundamental question is thus to understand the local interactions that give rise to the observed emergent dynamics. We are interested in methods for learning interactions generally, which can describe a wide class of physical systems exhibiting collective dynamics defined by an interaction kernel, without a priori assumptions on the analytical form of this kernel (i.e. it is nonparametric). The advantage of this kernel-based approach is that it incorporates the underlying physics of the model (i.e. collective dynamics), which more general equation-learning approaches may ignore, potentially limiting their effectiveness for model accuracy and predictions. In this work, we extend existing variational learning approaches to collective systems with both interaction kernels and environmental/intra-agent forces. The proposed framework simultaneously infers the interaction kernel non-parametrically while learning the environmental force using either semi-parametric or fully nonparametric representations. The methodology is validated on several benchmark models exhibiting synchronization, alignment, attraction-repulsion, and external environmental forces. We also introduce a model-selection procedure based on our nonparametric learning framework to identify models that optimally explain a given set of trajectory observations. By exploiting the feature-identification capability of the learned models, the proposed procedure can distinguish among different collective dynamics frameworks and recover mechanistic interaction mechanisms directly from trajectory data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25181v1
- Authors: Nipuni de Silva, Ming Zhong, James M. Greene
- Published: 2026-08-25T21:55:12Z
- Age days: 1

</details>
