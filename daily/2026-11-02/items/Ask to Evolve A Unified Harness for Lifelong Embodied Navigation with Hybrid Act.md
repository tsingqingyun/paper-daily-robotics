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
url: "https://arxiv.org/abs/2610.39446v1"
published: "2026-10-29T06:19:44Z"
age_days: 3
score: 27
created: 2026-11-02
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory

> [!summary] 这篇论文到底做了什么（基于摘要）
> EvoLife 让导航智能体同时决定怎么走、何时求助，以及把什么经历记下来供下次使用。关键是把多种移动方式、主动交互和绑定地点的持久记忆放进同一个导航系统。

## 问题

任务包括按语言找路、寻找物体、交互寻找指定实例，以及连续完成多个导航任务。真正的难点不只是走到目标：指令可能含糊，途中可能卡住，下次来还应利用上次经验。摘要认为行动、交互和记忆需要协同，但没有具体拆解现有方案各自失败在哪里。

### 用一个例子理解

理解用例（非论文实验）：输入“去上次讨论过的打印机旁”；系统检索地点关联的对话，发现曾确认过打印机位置，选择目标导航，靠近后局部调整；若发现两台相似设备则询问，输出到达结果，并保存本次确认。

## 创新点或方法

从单次任务中选择移动动作，改为联合选择移动、询问和经验保留：远处可用航点或目标物体导航，局部可用离散微调，也支持按图像像素指定导航目标；遇到歧义或困难时主动求助。观察和对话绑定到地点，后续重访时再取用。它描述的是运行时组织方式；是否额外训练、动作如何切换、记忆如何检索，摘要未说明。

### 方法如何工作

1. 接收目标并结合当前观察、地点经验判断下一步需求，让历史经历能够参与当前决策。
2. 根据情况选择航点、离散调整、像素或物体导航，以适配不同移动粒度；选择规则摘要未说明。
3. 遇到歧义或困难时主动交互，取得澄清或帮助，使任务能够继续。
4. 把观察和对话关联到地点并保留，供后续访问使用；存储与检索细节摘要只说明到此。

### 必要术语

- 混合动作空间：同时提供几种表达移动目标的方式；本文用它支持不同粒度的导航。
- 持久空间记忆：跨任务保存与地点相关的经历；本文用于重访时复用观察和对话。
- SPL：综合成功与路径长度的指标；本文用它衡量保留经验后的重访表现。

## 证据

摘要报告八个基准、四类任务。覆盖语言导航和物体导航的四组各100回合测试，首次到访成功率均为100%，平均每回合主动交互1.87次；50条LHPR-VLN序列和50条GOAT-Bench序列的整序列成功率分别为98%和94%。R2R重访保留经验后，SPL从82.23%升至93.31%。这些支持系统在所测设置中的完成能力与经验复用收益；摘要未给基线、求助条件或消融。另有多日真机展示，但没有对应量化结果。

## 局限

100%成功率需要结合可获得的帮助解读，不能直接等同于无人支持的自主导航。我的待核查问题是：回答者提供多少信息，失败如何计数，场景变化后旧记忆会不会误导；摘要不足以回答。多日真机展示也不能直接继承基准上的成功率。

- **判断**：值得细读决策流程、交互协议和记忆消融，因为成绩很强，而决定其可迁移性的恰好是帮助与记忆如何使用。

## 研究关联

值得借鉴的是，把求助当成正常决策选项，并把回答连同地点保存。对于允许重复访问、且有人能提供帮助的导航任务，一次澄清可能既解决眼前歧义，也减少后续重复询问。

### 下一步读哪里

下一步检查四组首次到访测试的选样与交互预算、整序列成功的定义，以及去掉求助或记忆后的结果；再核查真机运行天数、任务数量和环境变化。当前依据只有摘要。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/Ask to Evolve A Unified Harness for Lifelong Embodied Navigation with Hybrid Act.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Giving embodied agents the freedom to act autonomously, initiate interactions, and understand their surroundings through experience is a step toward bringing them to life in the physical world. Realizing this vision requires action, interaction, and memory to work together, so that each encounter can inform current decisions and contribute experience for future tasks. We present EvoLife, a unified navigation harness that enables a multimodal embodied agent to choose how to move, when to ask, and what experience to carry forward. Its hybrid action space supports waypoint navigation, local discrete adjustments, pixel-based navigation, and object-directed navigation. Active interaction allows the agent to seek clarification or assistance when it encounters ambiguity or difficulty, while persistent spatial memory binds observations and dialogue to places, retaining useful experience to guide subsequent visits. We evaluate eight benchmarks across four task families: vision-language navigation, object navigation, interactive instance navigation, and continuous multi-task navigation. With an average of only 1.87 active interactions per episode, our method achieves a first-visit success rate (SR) of 100% across four 100-episode sets spanning vision-language navigation and object navigation. Complete-sequence SR reaches 98% on 50 LHPR-VLN sequences and 94% on 50 GOAT-Bench sequences. In the R2R revisit setting, success weighted by path length (SPL) increases from 82.23% to 93.31% with retained experience. Multi-day physical navigation further demonstrates exploration, proactive help-seeking, and revisiting remembered places. Together, these results advance the vision of bringing embodied agents to life through autonomous action, proactive interaction, and the accumulation and reuse of experience.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39446v1
- Authors: Kai Sheng, Liuyi Wang, Jinlong Li, Haojie Dai, Chengju Liu, Qijun Chen
- Published: 2026-10-29T06:19:44Z
- Age days: 3

</details>
