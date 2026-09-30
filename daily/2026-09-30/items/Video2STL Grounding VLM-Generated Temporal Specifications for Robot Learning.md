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
url: "https://arxiv.org/abs/2609.37519v1"
published: "2026-09-29T13:10:14Z"
age_days: 0
score: 31
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Video2STL: Grounding VLM-Generated Temporal Specifications for Robot Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> 看人做一件事，机器人最该学的可能是“先完成什么，再完成什么”。Video2STL 从视频提取这套顺序规则，再用成功的机器人轨迹把规则变成可计算的奖励，让机器人学会用自己的身体完成任务。

## 问题

任务是从没有动作标注、甚至由人或动物演示的视频学习机器人行为。瓶颈是确定究竟迁移哪些信息：把视频压成相似度或价值分数，或直接生成奖励代码，都可能让任务的先后关系难以检查、落地和复用。

### 用一个例子理解

理解用例（非论文实验）：输入人把杯子放上架子的视频→提取“拿起、移动、放稳”的顺序→用成功机器人轨迹校准高度、距离和时限→根据短期条件满足程度及长期顺序进展给奖励，训练机器人完成放置。

## 创新点或方法

Video2STL 用显式时序规格替代难以检查的单一信号。VLM 先抽取不依赖具体身体形态的事件轨迹，再构造参数化 STL 规格库；成功机器人轨迹提供谓词阈值和时间边界。策略训练时，短期规格的滚动窗口鲁棒度产生密集奖励，长期规格的因果监测器只为有效事件前缀发放一次进度奖励，减少重复记分。训练后执行策略时是否仍运行监测器或调用 VLM，摘要未说明。

### 方法如何工作

1. VLM 从视频提取语义事件，得到可跨身体表达的任务结构，避免依赖原演示的关节动作。
2. 把事件组织成参数化 STL 规格，再用成功机器人轨迹确定数值与时间参数，使语言结构可计算。
3. 在短窗口内计算规格鲁棒度，产生连续反馈，帮助策略学习局部行为。
4. 长期监测已发生的有效前缀，只在取得新进展时奖励，使局部优化仍服从整体顺序。

### 必要术语

- STL：描述数值条件及其时间关系的逻辑语言；本文用它表达任务要求。
- 谓词阈值：判定某件事是否成立的数值边界；本文从成功轨迹中确定。
- 定量鲁棒度：条件满足得有多充分或违反得有多严重；本文将其用于短期奖励。
- 有效时间前缀：截至当前已按要求完成的事件序列部分；本文据此发放长期进度奖励。

## 证据

摘要报告四项操作任务：平均 success-once/success-at-end 为 85.8%/67.0%，原生密集奖励 PPO 为 81.5%/59.5%，Text2Reward 为 65.0%/42.3%。这分别涉及过程曾成功与结束时成功，具体判定仍需核查。四足运动中，基于 Qwen-3.8 和 GPT-5.6 的版本在 0.3—2.1 m/s 范围达到 100% 成功，高速能效保持竞争力，但未给能耗数值。摘要未标明这些实验哪些属于仿真或真机。

## 局限

摘要没有交代的关键问题是：成功机器人轨迹从哪里获得、需要多少，VLM 误读事件后如何纠正，以及不同身体能否用同类状态量表达谓词。视频无需动作标注，不代表整个训练流程无需机器人数据；所报成功率也不构成任意环境下的形式化保证。

- **判断**：做人类视频学技能，或正在手写复杂奖励，值得读。重点看视频里的事件怎样对应到机器人状态；摘要中的成功率有参考价值，但没有说明各项实验是仿真还是真机。

## 研究关联

如果任务难点是步骤顺序，可以先从演示中提取可检查的事件，再奖励新完成的步骤，避免机器人反复做同一步刷分。这个思路需要你能测出事件是否发生，并有成功机器人轨迹来确定距离、时间等条件，不能只靠一段视频就落地。

### 下一步读哪里

下一步核查事件如何映射到机器人状态、成功轨迹采集成本、短长期规格如何选择，以及一次性奖励如何处理失败重试；实验需确认环境类型、成功指标和能效比较条件。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Video2STL Grounding VLM-Generated Temporal Specifications for Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video-based policy learning is particularly promising, as it illustrates target behaviors without requiring action annotations or embodiment-matched demonstrations. A central challenge is deciding what information should be transferred from the video to the robot. Existing approaches commonly convert visual observations into scalar similarity or value signals, or ask foundation models to directly generate reward code. These approaches can make the temporal structure of a task difficult to inspect, ground, and reuse. We present Video2STL, a framework that converts observation-only videos into parametric Signal Temporal Logic (STL) specifications and uses the resulting formal representation for robot learning. A vision-language model extracts an embodiment-independent semantic event trace and constructs a bank of symbolic temporal specifications. The model determines the task structure, while numerical predicate thresholds and temporal bounds are grounded from successful robot trajectories. For policy learning, we separate short- and long-timescale temporal information: short-horizon specifications provide dense rewards through rolling-window quantitative robustness, while a causal monitor over a retained long-horizon specification provides one-time progress rewards for valid temporal prefixes. The same representation supports cross-embodiment transfer from human or animal videos to robot control. Across four manipulation tasks, Video2STL achieves $85.8\%$ average success-once and $67.0\%$ success-at-end, compared with $81.5\%/59.5\%$ for native dense PPO and $65.0\%/42.3\%$ for Text2Reward; in quadruped locomotion, Qwen-3.8 and GPT-5.6-based Video2STL policies achieve $100\%$ success across velocities from $0.3$ to $2.1\,\mathrm{m/s}$ while remaining competitive in high-speed energy efficiency. Project webpage: \href{https://video2stl.github.io/}{video2stl}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37519v1
- Authors: Merve Atasever, Keyan Azbijari, Cagan Bakirci, Bo-Ruei Huang, Tolga Izdas, Zahra Shahrooei, Richard Yang, Erdem Biyik, Jyotirmoy V. Deshmukh
- Published: 2026-09-29T13:10:14Z
- Age days: 0

</details>
