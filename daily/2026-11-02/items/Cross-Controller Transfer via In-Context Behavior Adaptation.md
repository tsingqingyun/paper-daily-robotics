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
url: "https://arxiv.org/abs/2610.39280v1"
published: "2026-10-29T03:31:22Z"
age_days: 3
score: 27
created: 2026-11-02
concepts: ["AI 核心知识地图"]
---

# Cross-Controller Transfer via In-Context Behavior Adaptation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Cross-Controller Transfer 用“发了什么动作、机器人实际怎么动”的示例，让同一个策略判断当前控制器的行为。它处理的是一个容易被忽视的数据冲突：相同动作数值，在不同控制器下可能代表不同运动。

## 问题

通用机器人策略会混合不同任务和机器人本体的数据，但通常默认每台机器人只有一种控制器。控制器一变，相同指令的物理含义、响应强度乃至完成任务的策略都可能变化；直接混合数据，就可能把互不兼容的动作解释一起学进去。本文同时考虑跨本体和跨控制器的数据迁移。

### 用一个例子理解

理解用例（非论文实验）：输入插接头任务和几段“指令—实际位移”记录；编码器从记录中提取当前控制响应，策略结合任务观察生成动作；输出适应该控制器的插入动作序列。具体采用何种插入策略，不能从摘要推断。

## 创新点或方法

直接混合数据让策略自行消化冲突，本文则额外提供控制器下的行为示例：指令及其造成的机器人运动。Transformer上下文编码器将这些交互压缩成条件信息，策略据此决定动作。训练面向共享策略和编码器，运行时通过交互上下文适配；摘要没有说明训练目标、示例采样方式，也没有交代测试时是否更新参数。

### 方法如何工作

1. 收集某控制器下的指令和实际运动配对，让动作的物理含义有可观察依据。
2. 用Transformer编码这些交互，得到控制行为的上下文表示，减少策略对隐藏控制差异的猜测。
3. 让同一个策略结合上下文处理任务，使不同控制器的数据能够支持共享学习。
4. 在新控制器下提供行为上下文并执行任务；示例怎样获取、适配是否更新权重，摘要只说明到此。

### 必要术语

- 控制器：把策略指令转成机器人实际运动的执行规则；其差异是本文处理的数据冲突来源。
- 上下文适配：依据当前提供的示例调整行为；本文用动作与运动的配对示例提供依据。
- 增益与顺应性：分别影响响应强度和接触时的让步程度；本文将它们作为控制差异的一部分。

## 证据

摘要称设置覆盖六种控制器，以及增益和顺应性变化。真机实验中，平均成功率比直接混合数据高33个百分点；未见控制器模式成功率为50%，未见控制器增益为52%，并能迁移到控制器专属数据较少的任务。USB插入、表面擦拭用于说明接触任务中的策略适应。摘要没有给每项试验次数、误差范围或策略改变的具体轨迹，因此还不能判断收益是否均匀分布。

## 局限

未见模式约一半的成功率说明迁移仍有限。我的待核查问题是：适配需要多少交互，获取这些交互是否安全，以及上下文能否覆盖真实任务中的接触响应。摘要没有提供这些条件，也不能仅凭总体成功率把收益全部归因于学会了控制器动力学。

- **判断**：值得深入读上下文构造和未见控制器划分，因为它具体解释了一种多源机器人数据为何混合失效，以及怎样缓解。

## 研究关联

可借鉴的想法是：动作标签之外，还要提供解释动作的证据。汇集机器人数据时，如果冲突来自控制器语义，扩大数据量未必足够；加入动作与结果的配对示例，可能比让策略猜测隐藏差异更直接。

### 下一步读哪里

优先核查上下文长度、采集成本、动作与运动的表示，以及训练和测试控制器如何隔离；再看33个百分点对应的任务构成，以及接触任务是否有轨迹或消融证明策略确实改变。

- **概念**：AI 核心知识地图
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/Cross-Controller Transfer via In-Context Behavior Adaptation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies increasingly learn from data collected across diverse tasks and embodiments, yet typically assume a single controller for each robot. This assumption limits transfer because different controllers can assign different physical meanings to the same action and may require different strategies to complete a task. We study how to transfer robot data across both embodiments and controllers without allowing conflicting action interpretations to interfere with learning. Our setting spans six controller types as well as variations in controller gains and compliance. We propose a framework that encodes behavioral interaction under a controller through examples of commanded actions and the resulting robot motions. A transformer context encoder summarizes these interactions, allowing a single policy to adapt in context. Across real-world experiments, our method improves average success by 33 percentage points over naive data pooling, achieves 50\% success on unseen controller modes and 52\% on unseen controller gains, and transfers to tasks with limited controller-specific data. On contact-rich tasks such as USB insertion and surface wiping, behavioral interaction context enables the policy to adapt not only its actions but also its strategy. Our results provide a path toward generalist robot policies that can leverage data collected across diverse action interpretations. For more information, visit \href{https://controller-transfer.github.io}{https://controller-transfer.github.io}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39280v1
- Authors: Jonathan Yang, Chelsea Finn, Dorsa Sadigh
- Published: 2026-10-29T03:31:22Z
- Age days: 3

</details>
