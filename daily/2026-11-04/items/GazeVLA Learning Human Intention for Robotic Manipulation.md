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
url: "https://arxiv.org/abs/2604.22615"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 43
created: 2026-11-04
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# GazeVLA: Learning Human Intention for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> GazeVLA 用人的注视线索表示“正在关注和准备操作什么”，帮助机器人从人类示范学习。推理时，它用思维链式过程连接意图与动作，尝试缩小人和机器人身体不同带来的迁移困难。

## 问题

任务是把人类示范中的知识迁移到机器人操作，覆盖长时序和精细动作。人类行为数据来源丰富，但人的肢体、运动方式与机器人不同，直接迁移动作存在身体差异。论文因此寻找比具体肢体动作更容易共享、又能指导操作的中间信息。

### 用一个例子理解

理解用例（非论文实验）：输入人整理餐具的示范及注视线索；系统将视线落在勺子和收纳格上的信息用于学习当前操作意图；机器人结合自己的观测生成取放动作。部署是否还需注视输入，摘要未说明。

## 创新点或方法

本文把关注点从直接对应人和机器人的动作，移到用注视建模意图。作者认为注视既包含任务语义，又与低层动作相互配合，因此可作为两者之间的中层表示。机器人再学习利用这种意图表示，摘要称无需机器人的意图标注。推理时采用思维链式推理连接意图和动作。摘要未说明注视如何采集、训练损失如何定义，也未说明思维链是文本还是内部表示；不能据此补出具体网络结构。

### 方法如何工作

1. 从人类行为中利用注视线索，提取与任务和动作相关的关注信息；采集方式未说明。
2. 将这些信息建模为中层意图表示，减少对人类具体肢体动作的依赖。
3. 让机器人学习利用意图信息完成操作，且不要求机器人的意图标注；监督细节未说明。
4. 推理时用思维链式过程连接意图与动作，输出机器人操作；具体推理形式摘要只说明到此。

### 必要术语

- 身体差异：人和机器人在结构与动作能力上的不同；本文试图减少它对示范迁移的阻碍。
- 中层表示：介于任务目标和具体动作之间的信息；本文用注视建模的意图承担这一作用。
- 思维链：分步组织推理的方式；本文用它连接意图与动作，但摘要未交代实现形式。

## 证据

摘要报告仿真与真机实验，称在不同身体形态下完成长时序、精细任务，相比基线表现更好，并能迁移到未见设置。但没有列出机器人型号、任务、基线名称、评价指标或数值。因此现有材料只能支持作者报告了这些比较，不能量化注视贡献，也不能分离意图建模与推理过程各自的作用。

## 局限

注视是意图的线索，并非意图的直接证明；人也会看向干扰物。我的待核查问题是系统如何处理误导性注视，以及部署时是否仍需人的实时注视。摘要中的跨形态结果也不能直接解释为任意机器人都可迁移。

- **判断**：值得先读意图表示与注视消融；只有确认收益确实来自可迁移的注视信息，才能判断方法是否适合复用。

## 研究关联

可借鉴的是迁移表示的选择：人和机器人可能无法共享动作坐标，却可以共享当前关注的对象或操作目标。寻找这种既连接任务、又贴近动作的中间表示，可能比直接对齐肢体运动更合适。

### 下一步读哪里

先核查注视来源、意图表示及人机训练数据如何配合，再检查去掉注视或思维链的消融，以及未见设置具体改变了什么。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：43
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/GazeVLA Learning Human Intention for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2604.22615v3 Announce Type: replace Abstract: Embodied foundation models have significantly propelled the advancement of artificial general intelligence, yet they rely heavily on large-scale data. Recent studies identify human behavior as one of the most scalable sources for fostering robotic physical intelligence. However, the inherent embodiment gap remains a fundamental challenge for effective human-to-robot learning. In this work, we model human intention to enable efficient learning from human demonstrations. Among human behavioral cues, gaze simultaneously encodes high-level task semantics and exhibits a synergistic coupling with low-level action. By modeling intention through gaze, we derive a mid-level representation that facilitates cross-embodiment knowledge transfer. We demonstrate that robots can internalize human intentions to enhance manipulation, even without robotic intention annotations. To capture the synergy between intention and action, we adopt a Chain-of-Thought reasoning paradigm during inference. Our approach enables the execution of long-horizon and fine-grained tasks across diverse embodiments. Extensive experiments in both simulation and real-world demonstrate that our method consistently outperforms baseline approaches and generalizes to unseen settings. Project page: https://gazevla.github.io .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2604.22615
- Authors: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
