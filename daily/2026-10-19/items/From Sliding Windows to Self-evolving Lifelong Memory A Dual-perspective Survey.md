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
url: "https://arxiv.org/abs/2610.23319v1"
published: "2026-10-16T11:23:17Z"
age_days: 3
score: 44
created: 2026-10-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇 VLA 记忆综述讨论机器人怎样把过去的信息留到以后使用，而不只依赖眼前一小段观测。它按记忆覆盖范围和保留时间组织已有方法，但摘要没有给出各类别的具体定义。

## 问题

长任务里，当前画面经常不足以决定下一步：机器人可能需要记住已经完成什么，或复用以前任务中的经验。摘要指出，现有 VLA 的时间上下文受限，妨碍经验积累和复用；不过它没有逐一说明哪些既有系统在哪种任务上失败，因此不能据此认定所有 VLA 都缺少长期记忆。

### 用一个例子理解

理解用例（非论文实验）：输入“继续整理昨天没收完的工具”和当前画面；一个有跨任务记忆的系统检索昨日进度，再结合当前观测确认工具是否仍在原位；输出下一步收纳动作。这个例子说明为什么历史记录需要复核，不是本文提出或验证的算法。

## 创新点或方法

这是一篇整理已有研究的综述，不是新控制策略。它把“模型能看多少历史”进一步拆成记忆作用范围和持久性，再据此划分五种代表范式及一个新兴方向，比较记忆特性、架构复杂度与开源成熟度。这个拆法有助于区分短期保留观测和跨任务积累知识，但摘要未列出六类名称，不能自行补成作者分类。各类系统训练时如何建立记忆、推理时如何写入和检索，也未说明。

### 方法如何工作

1. 先把长任务中的历史依赖识别出来，明确为什么当前观测不足以决策；这是综述的问题起点。
2. 按记忆范围和持久性整理已有系统，得到可比较的类别；具体类别摘要只说明到此。
3. 比较各类系统的记忆特性、架构复杂度和开源成熟度，帮助读者定位实现取舍。
4. 由比较提出记忆管理和知识持续演化的挑战；摘要没有进一步提供统一实现或验证流程。

### 必要术语

- 时间上下文：模型当前能直接利用的历史信息范围；本文把它受限视为长任务瓶颈。
- 记忆范围：记忆覆盖哪一段活动或经验；是本文分类的一个维度，精确定义需查正文。
- 持久性：信息能保留多久、能否跨执行继续存在；是另一个分类维度。
- 终身知识演化：长期运行时持续整理和更新经验；摘要将其列为待解决方向。

## 证据

摘要报告的主要观察是：架构越复杂，开源成熟度通常越低。这是综述对代表系统的归纳，不是统一机器人实验中的性能结论。输入没有文献数量、检索时间范围、纳入标准、复杂度与成熟度评分，也没有任务、基线或成功率。因此可以把它作为寻找设计路线的地图，暂不能据此判断哪种记忆最好，或复杂架构是否导致开源不足。

## 局限

目前的主要边界来自输入只有摘要：我还无法判断分类是否互斥、是否覆盖混合系统，以及“终身演化”指存储内容更新还是模型参数更新。摘要提到高效记忆管理和终身知识演化仍是挑战，但没有提供作者对各类方法的详细局限。

- **判断**：适合先读分类定义和系统比较表，帮助明确记忆需求；仅凭摘要，还不适合据此选择实现路线。

## 研究关联

具体启示是先判断“需要记住什么、记多久”，再选存储方案。只需记住本次任务进度，与需要跨天复用操作经验，涉及不同的写入、遗忘和检索要求；把它们都处理成长上下文，容易掩盖真正需求。这是从分类轴得到的设计启示，并非摘要验证过的性能收益。

### 下一步读哪里

下一步应核查五种范式和新兴方向的定义、边界实例，以及文献收集协议；重点问开源成熟度如何评分、比较是否控制发表时间，以及记忆过期、误检索和错误经验如何处理。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：44
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：HTTPError: HTTP Error 404: Not Found

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/From Sliding Windows to Self-evolving Lifelong Memory A Dual-perspective Survey.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23319v1
- Authors: Yong Wang, Boyu Shen, Xinwei Zhang, Yizheng Li, Keyuan Luo
- Published: 2026-10-16T11:23:17Z
- Age days: 3

</details>
