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
url: "https://arxiv.org/abs/2611.26969v1"
published: "2026-11-20T01:44:10Z"
age_days: 4
score: 31
created: 2026-11-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboDyna 用仿真评测机械臂能否在物体持续运动时完成操作。它让策略分别在推理时暂停和继续演化的环境中行动，量出延迟会改写多少次任务的成败。

## 问题

动态操作要求机械臂边观察边出手。物理预测基准能测模型猜得准不准，却测不到它能否利用预测完成操作。有些操作基准又给物体设定过度简化的运动，或者在策略计算期间暂停环境，回避了现实中物体会继续滑动、滚动或碰撞的难题。

### 用一个例子理解

理解用例（非论文实验）——机械臂要把滚向开口的圆柱拨进收纳槽。输入是当前画面和目标，策略计算下一步动作。同步时圆柱在计算期间暂停，异步时它可能已滚过拦截位置。最终分别记录入槽、碰到但未入槽等结果。

## 创新点或方法

RoboDyna 先用简单物体和低杂乱场景考查具体动态操作能力，再把同类能力放进复杂的模拟家居场景。同步协议在推理时暂停环境，异步协议让环境继续演化。任务同时记录成功和部分完成，也提供专家示范与人类交互工具。摘要描述的是评测，两类模型如何训练、是否使用示范以及示范如何使用仍需核查。

### 方法如何工作

1. 用低杂乱场景隔开各类操作能力，再在模拟家居任务里加入更复杂的视觉与场景条件。
2. 在配对的同步和异步协议中执行策略，让环境是否在推理期间演化成为可比较条件。
3. 同时记录成功与部分完成，区分一步都没做对和只差最后一步的回合。
4. 对照模型、人类和逐回合成败，检查场景难度、延迟敏感性及预测质量与行动结果之间的关系。

### 必要术语

- 闭环操作：执行动作后再看环境，并用新观测决定下一步；本文用它测策略能否跟上动态变化。
- 同步与异步评测：策略计算期间分别暂停和继续推进环境；本文用两者的差异衡量推理延迟的影响。
- 部分完成：给达到中间目标的回合记录进度；本文用它补足二元成功标签。

## 证据

据摘要，基准含五类能力下的 20 个概念任务、10 个模拟家居任务和 3,500 条专家示范。在约 5,400 个评测回合中，受测视觉语言动作策略和世界动作模型的成功率均低于 20%，人类在匹配条件下表现更好。同步与异步比较中，延迟改写了 5%–12% 回合的成败，平均成功率变化至多 3%。世界动作模型能处理简单动力学，但摘要报告其预测保真度和任务成功并不总是一致。这些结果来自基准内的仿真。

## 局限

作者把测试放在仿真里，延迟结论对应同步与异步协议下的比较。预测保真度与任务成功不一致属于结果之间的观察，我会核查初始条件怎样配对，以及异步协议如何把真实推理耗时映射到模拟时间。

- **判断**：优先读异步协议、逐回合结果和部分完成指标，那里最能说明现有测试会漏掉哪些动态失败。

## 研究关联

有些回合会因延迟从成功变失败，有些可能向相反方向变化。只看总体平均，容易漏掉大量逐回合差异。评估实时策略时，配对对比值得借鉴，还可以追查哪种运动阶段最怕动作发晚。

### 下一步读哪里

先检查两套协议是否复用初始状态和随机条件，再核查延迟的计时边界、动作更新频率、部分完成的判定。对照预测与成功的关系时，逐任务看比只看整体均值更直观。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/RoboDyna A Benchmark for Evaluating Robotic Manipulation under Physically Ground.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Object manipulation in the dynamic real world requires understanding how the environment functions and evolves, and acting accordingly. Existing benchmarks, however, do not adequately address these needs. Physics-oriented benchmarks evaluate predictive fidelity but not closed-loop action. Dynamic robotic manipulation benchmarks often use simplified, physically implausible object motions, limiting evaluation of reasoning and action under realistic dynamics. Evaluation is also typically synchronized, freezing the environment during inference and making computation time irrelevant to task outcomes. To this end, we propose RoboDyna, a benchmark for evaluating the physical understanding and action capabilities of manipulation policies in dynamic scenes. RoboDyna comprises 20 conceptual dynamic tasks spanning five capability categories, with simple objects and minimal scene clutter, under a two-factor difficulty design, and 10 household tasks that instantiate the same capabilities in visually and semantically richer simulated real-world environments. RoboDyna provides 3,500 expert demonstrations, paired synchronous and asynchronous evaluation protocols, metrics for task success and partial completion, and interactive tools for human baseline evaluation. Evaluating vision-language-action models and a world-action model across 5.4K episodes, we find that all policies achieve success rates below 20%, revealing substantial limitations in dynamic manipulation. The world-action model captures simple physical dynamics but struggles with complex interactions, and its prediction fidelity does not consistently align with task success. Sync-async comparisons show that inference latency flips 5-12% of episode outcomes while changing average success rates by at most 3%. Human baselines substantially outperform all policies under matched conditions. Project page: https://robodyna.github.io/robodyna/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.26969v1
- Authors: Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Amir Rasouli
- Published: 2026-11-20T01:44:10Z
- Age days: 4

</details>
