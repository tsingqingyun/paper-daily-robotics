---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27406"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-08-29
concepts: ["智能体 Agent", "世界模型"]
---

# CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

> [!summary] 先说人话（基于摘要）
> CLAP把不同机器人乃至无动作标注的人类视频放进同一个动作条件视频世界模型：先用潜动作学习跨本体物理先验，再以末端执行器动作完成落地，支持零样本部署。

## 问题

动作条件视频模型通常绑定单一机器人，无法利用异构人类与机器人视频；核心障碍是各平台动作空间差异巨大，而且人类视频通常没有动作标签。单用末端位姿、语言或潜动作又各有局限。

## 创新点或方法

输入多来源视频以及可用的末端位姿、语言指令或潜动作，输出动作条件下的未来视频。课程式训练先借潜动作从无标注视频学习通用动力学，再将其对齐到末端执行器动作空间；关键差异是共享跨本体物理先验，而非为每种机器人单独训练。

## 证据

摘要称其在DROID等困难环境中接近或超过先进单本体视频模型，少样本适配后优势进一步扩大；覆盖DROID、Bridge、双臂YAM和G1人形机器人，但未报告具体指标或数字。


## 局限

最需全文核查的是所谓“通用物理先验”在多大程度上真正跨本体迁移，以及零样本比较的任务、基线和公平性；摘要没有可核查数字。

- **判断**：值得精读方法与跨本体实验：问题关键、路线完整，但领先幅度和零样本泛化边界必须看全文才能判断。

## 研究关联

对世界模型与机器人学习研究者，价值在于把互联网人类视频转化为机器人动力学预训练资源，并提供跨本体初始化后再少样本适配的路线；对Agent研究，其零样本物理模拟能力可能支持规划。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/CLAP Cross-Embodiment Video World Models are Zero-Shot Physical Simulators.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27406v1 Announce Type: cross Abstract: State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. However, cross-embodiment learning is non-trivial because action representations vary sharply across robot platforms and are typically absent in human videos. CLAP addresses this fundamental challenge through the following core contributions. First, CLAP reconciles disparate action spaces using end-effector poses, language instructions, and latent actions. Second, to resolve their individual limitations, CLAP introduces a curriculum-based cross-embodiment learning recipe that first learns foundational physical priors across unlabeled video data using latent actions and subsequently grounds them in end-effector action spaces for zero-shot deployment to real-world tasks. Crucially, CLAP approaches or surpasses state-of-the-art single-embodiment video models in challenging environments like DROID. These performance advantages compound via few-shot adaptation to establish a novel paradigm for training single-embodiment video world models. Ultimately, CLAP delivers the most comprehensive suite of action-conditioned video world models to date - spanning diverse action-conditioning spaces (end-effector, language, and latent) and robot morphologies (including cross-embodiment, DROID, Bridge, bimanual YAM robots, and G1 humanoids). We open-source all code and models. Project Website at https://omni-clap.github.io .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27406
- Authors: Kechen Liu, Ola Shorinwa
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
