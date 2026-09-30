---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27406v1"
published: "2026-08-27T17:35:10Z"
age_days: 2
score: 39
created: 2026-08-30
concepts: ["智能体 Agent", "世界模型"]
---

# CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

> [!summary] 先说人话（基于摘要）
> CLAP把不同机器人乃至人类视频放进同一个动作条件视频世界模型：先用潜在动作从无标签视频学物理先验，再落到末端位姿等可执行动作空间。

## 问题

现有动作条件视频模型通常绑定单一机器人本体，无法利用异构人类与机器人视频；关键障碍是各平台动作空间差异巨大，而且人类视频通常没有动作标签。

## 创新点或方法

作用对象是跨本体视频及动作条件，输出条件化未来视频。CLAP用末端位姿、语言和潜在动作协调不同动作空间，并采用课程学习：先从无标签视频学习跨本体动态，再对齐末端动作以零样本部署；区别于从头训练单一本体模型。

## 证据

摘要称其在 DROID 等环境中接近或超过先进单本体视频模型，且少样本适配后优势进一步扩大；覆盖 DROID、Bridge、双臂 YAM 和 G1 等本体，但未给出可核查数字。


## 局限

最需核查“通用物理先验”是否真正带来跨本体因果迁移，以及零样本部署的任务、动作接口和比较公平性；摘要没有数字支撑。

- **判断**：值得精读训练课程和动作统一方式；跨本体规模化很重要，但性能主张需看完整表格后再判断。

## 研究关联

对世界模型研究者，价值在于把互联网人类视频转化为机器人动力学先验，并提供跨本体预训练后再适配单平台的路线。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/CLAP Cross-Embodiment Video World Models are Zero-Shot Physical Simulators.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. However, cross-embodiment learning is non-trivial because action representations vary sharply across robot platforms and are typically absent in human videos. CLAP addresses this fundamental challenge through the following core contributions. First, CLAP reconciles disparate action spaces using end-effector poses, language instructions, and latent actions. Second, to resolve their individual limitations, CLAP introduces a curriculum-based cross-embodiment learning recipe that first learns foundational physical priors across unlabeled video data using latent actions and subsequently grounds them in end-effector action spaces for zero-shot deployment to real-world tasks. Crucially, CLAP approaches or surpasses state-of-the-art single-embodiment video models in challenging environments like DROID. These performance advantages compound via few-shot adaptation to establish a novel paradigm for training single-embodiment video world models. Ultimately, CLAP delivers the most comprehensive suite of action-conditioned video world models to date - spanning diverse action-conditioning spaces (end-effector, language, and latent) and robot morphologies (including cross-embodiment, DROID, Bridge, bimanual YAM robots, and G1 humanoids). We open-source all code and models. Project Website at https://omni-clap.github.io .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27406v1
- Authors: Kechen Liu, Ola Shorinwa
- Published: 2026-08-27T17:35:10Z
- Age days: 2

</details>
