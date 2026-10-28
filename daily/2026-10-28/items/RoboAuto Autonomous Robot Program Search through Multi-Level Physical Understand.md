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
url: "https://arxiv.org/abs/2610.36533v1"
published: "2026-10-27T02:41:22Z"
age_days: 0
score: 33
created: 2026-10-28
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboAuto 让智能体搜索机器人程序时，同时回答物体怎么操作、现场哪里能动、失败可能由什么造成。它把这些知识接到当前场景，并主动设计小实验来消除影响动作的物理疑问。

## 问题

任务是自动生成、执行并修订操纵程序。仅靠成功或失败反馈，智能体可能知道程序不行，却不知道是物体用法、空间约束还是接触效果理解错了，下一轮修改便缺乏方向。

### 用一个例子理解

理解用例（非论文实验）：输入是“打开抽屉”及现场图像；拉动失败后，系统考虑抓点不对或运动方向不对，设计小幅试探来检查方向，再修改抓取与拉动程序，输出经执行检查的操作方案。

## 创新点或方法

旧做法主要根据执行反馈改代码；本文先建立包含可执行技能、物体可操作方式、空间关系和动作效果的分层知识库，再把相关知识对应到当前对象与动作所需量。规划分阶段进行，每阶段检查预期物理效果；有多种解释时，设计实验区分它们。知识来自具身数据及在线解题，但具体学习算法未说明。解题时会检索、落地知识并搜索程序，不能把这一过程直接等同于策略网络训练。

### 方法如何工作

1. 从数据与在线任务积累技能和物理知识，给程序搜索提供可调用的经验。
2. 识别当前相关物体并确定动作关键量，把一般知识变成现场约束。
3. 分阶段生成并执行程序，用预期物理效果检查阶段是否成立。
4. 遇到不确定性时设计实验区分解释，再据结果修订程序；具体搜索与停止规则摘要未说明。

### 必要术语

- Code-as-Policy：用可执行程序组织机器人行为；便于逐段修改与复用技能。
- 可供性：物体允许怎样被操作，例如哪里可抓；用于约束动作选择。
- 场景落地：把一般知识对应到眼前对象和具体量；连接知识与执行。

## 证据

摘要报告五类基准：LIBERO-PRO 短程任务成功率为 89.1%；在 LIBERO-PRO Long 和 LIBERO-Plus 上，平均成功率超过 ASPIRE 两倍。三个需要精确操作的长程真机任务上，优于 ASPIRE 和 π₀.₅，但未给绝对值。摘要还报告跨模拟器、跨机器人形态迁移及知识库增大带来的收益，未给曲线。这些支持所测条件下的程序搜索效果，不能推出任意物理知识都可迁移。

## 局限

我会核查主动实验消耗多少执行次数、是否可能损坏或扰乱任务状态，以及收益来自知识库还是更多交互预算。摘要没有披露这些条件；跨形态迁移也不意味着底层技能接口无需适配。

- **判断**：值得深入读场景落地与实验设计部分，它们决定“物理理解”是否真正改变程序搜索，而不只是增加描述。

## 研究关联

可以借鉴的是把失败变成可区分的假设，再选择能验证假设的动作。当多次改代码仍失败时，先补一次有目的的物理观察，可能比继续盲目搜索更有效。

### 下一步读哪里

下一步核查动作关键量如何获取、竞争假设怎样生成和判别，以及知识条目如何验证与更新；再比较相同交互预算下，去掉知识库或主动实验后的成绩。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/RoboAuto Autonomous Robot Program Search through Multi-Level Physical Understand.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program search requires physical understanding: agents must understand how objects can be manipulated, how scene geometry constrains actions, and why interactions succeed or fail. Existing methods rely mainly on execution feedback for program refinement, often leaving these physical questions unresolved. We introduce RoboAuto, a framework for robot program search that explicitly organizes physical understanding at the object, scene, and interaction levels through three components. First, a hierarchical knowledge base combines executable skills with object-centric knowledge of affordances, spatial relations, and action effects, learned from embodied data and online task solving. Second, scene grounding connects this knowledge to the current environment by identifying relevant objects and resolving action-critical quantities. Third, multi-stage planning with self-designed experiments checks whether each stage produces its expected physical effects and actively tests competing hypotheses to resolve physical uncertainties. RoboAuto achieves superior performance across five benchmark families, attaining an 89.1% success rate on short-horizon LIBERO-PRO tasks and more than twice the mean success rate of ASPIRE on LIBERO-PRO Long and LIBERO-Plus. It also outperforms ASPIRE and $π_{0.5}$ on three challenging long-horizon real-robot tasks requiring precise manipulation. We further show that the knowledge base transfers across simulators and embodiments, and that program search performance scales with its size. Project page: https://roboauto-ai.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36533v1
- Authors: Buzhao Liu, Jianing Ye, Xiu Yuan, Yangtong Feng, Chengsong Huang, Tyler Dinh, Yevgeniy Vorobeychik, Ning Zhang, Chongjie Zhang
- Published: 2026-10-27T02:41:22Z
- Age days: 0

</details>
