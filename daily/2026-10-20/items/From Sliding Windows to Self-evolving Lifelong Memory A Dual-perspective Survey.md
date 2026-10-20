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
url: "https://arxiv.org/abs/2610.23319"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 44
created: 2026-10-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇综述按记忆覆盖范围和保存时长，整理长流程 VLA 的记忆设计。它帮助读者区分模型究竟能记住当前任务的什么，哪些经验又能保留到以后。

## 问题

长流程任务中，当前画面和有限历史往往不足以支持决策，机器人还需要积累并复用过去经验。摘要指出，受限时间上下文妨碍这种积累；但增加记忆会涉及架构复杂度、管理成本和实现可用性，不能只看模型能输入多少帧。

### 用一个例子理解

理解用例（非论文实验）：机器人先看到钥匙被放进抽屉，稍后收到取钥匙指令；系统保存先前事件，决策时取回位置线索，输出开抽屉取物的动作。该例说明记忆需求，不代表综述验证了此任务。

## 创新点或方法

这是综述，没有提出一套新的训练或推理算法。作者以记忆范围和持久性为分类依据，整理五类代表范式与一个新兴方向，再比较记忆特征、架构复杂度和开源成熟度。摘要没有列出类别名称，因此不能补写分类细节。具体系统如何训练、何时写入或读取记忆，需要查看综述及原论文。

### 方法如何工作

1. 从长流程任务的历史信息需求出发，确定仅靠有限上下文存在什么限制。
2. 按记忆范围和保存时长分类，使不同设计可以在共同维度上比较。
3. 比较记忆特征、架构复杂度与开源成熟度，识别实现上的取舍。
4. 归纳管理和知识演化挑战；摘要只说明到此，没有给出可直接执行的统一方案。

### 必要术语

- 时间上下文：模型当前能看到的历史范围；范围有限会影响长流程决策。
- 记忆持久性：信息能够保存多久；本文用它区分记忆范式。
- 终身知识演化：长期使用中持续更新已有知识；本文将其作为待解决的方向。

## 证据

摘要给出的主要结论是：所比较系统中，架构越复杂通常伴随开源成熟度越低。它还讨论高效记忆管理和终身知识演化。没有提供机器人测试任务、统一基线、成功率或比较样本数量，因此这是文献整理所得的观察，不能当作某种记忆机制提升任务成功率的实验，也不能解释成复杂架构导致开源不足。

## 局限

我的待核查问题是分类边界如何划定，以及开源成熟度采用什么标准。摘要没有说明文献覆盖范围和检索截止时间，也不能据此断言综述遗漏了哪些方法。长期保存知识是否可靠，仍需回到各系统的实验判断。

- **判断**：适合作为选读地图，先读分类与比较表，再沿具体机制找原论文；不要仅凭综述摘要选择记忆架构。

## 研究关联

具体启示是先问信息需要保存多久、在哪些任务间复用，再选择记忆机制。例如，保存当前任务的一次观测，与跨任务保留操作经验，需要不同的写入、检索和更新策略。

### 下一步读哪里

先核查五类范式及新兴方向的定义，再找写入、读取、遗忘和跨任务保留机制的比较；检查复杂度与开源成熟度判断的依据，并追踪相关原始实验。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：44
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/From Sliding Windows to Self-evolving Lifelong Memory A Dual-perspective Survey.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.23319v1 Announce Type: new Abstract: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23319
- Authors: Yong Wang, Boyu Shen, Xinwei Zhang, Yizheng Li, Keyuan Luo
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
