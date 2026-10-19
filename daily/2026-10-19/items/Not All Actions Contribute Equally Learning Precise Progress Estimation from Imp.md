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
url: "https://arxiv.org/abs/2610.23769v1"
published: "2026-10-16T17:07:39Z"
age_days: 2
score: 28
created: 2026-10-19
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations

> [!summary] 这篇论文到底做了什么（基于摘要）
> PRIME 不把演示里“时间往后走”直接当成“任务更接近成功”。它把多条演示中的状态连成图，用到成功状态的最短路径距离衡量进度，因此能把有效推进、停滞和退步分开。

## 问题

机器人强化学习需要中途反馈，尤其是插接这类精细操作，最后一点几何偏差就可能决定成败。依赖专家演示、默认每步都有贡献的进度学习，会把人的试错和错误动作也学成正向进展，继而给策略错误奖励。

### 用一个例子理解

理解用例（非论文实验）：多条插头演示中，有人先偏向一边，再退回重对齐。PRIME 把这些状态与其他轨迹连接；偏移后的最短成功距离若增大，就不把这一步算成推进，重新对齐后距离下降才给出进步信号。

## 创新点或方法

旧做法依赖单条演示中的先后顺序；PRIME 改为汇总多条轨迹，用跨轨迹关系建立评价参照。它根据空间接近和视觉一致性连接观察状态，以空间距离作为边的通行成本，再搜索到成功的最短路径。距离减少表示推进，保持或增加则允许表示停滞或退步，避免强迫进度随时间单调上升。训练侧利用演示构图并学习进度估计；使用侧可为策略学习提供密集反馈。但摘要未交代新状态如何映射到图、是否在线搜索，以及距离怎样转成具体奖励。

### 方法如何工作

1. 汇集多条演示中的观察状态，获得单条轨迹之外的成功参照。
2. 按空间接近和视觉一致性连边，以空间距离赋予成本，形成可搜索的状态图。
3. 搜索到成功的最短路径，用累计成本近似剩余距离，摆脱时间顺序约束。
4. 根据距离变化判断推进、停滞或退步，供进度学习和策略反馈使用；具体接入细节摘要只说明到此。

### 必要术语

- 密集奖励：任务中途也能得到的反馈；本文希望让它反映真实推进。
- 测地距离：沿允许路径累计的距离；本文用图上最短路径近似。
- SFT：监督微调，通常从示范学习动作；本文将其作为策略成功率比较对象。

## 证据

摘要称在仿真和真实世界的精细操作任务中测试，面对不同程度的次优演示仍有效，精度要求越高优势越明显。唯一具体效应量是充电器插入任务：策略成功率相对 SFT 基线最高改善 5 倍。摘要没有给绝对成功率、试验次数、其余任务数值，也未明确该数字对应仿真还是真机，因此不能把它解释为普遍收益或增加若干百分点。

## 局限

我最关心图里的“近”是否等于实际容易到达：两个画面和位置相似的状态，可能因接触、受力或隐藏状态而无法低成本转换。最短路径是进度代理，不能直接视为真实剩余动作数。摘要也未拆分奖励设计、额外数据与训练流程各自对成功率的贡献。

- **判断**：值得细读构图规则和奖励接入方式，因为它把演示失误变成可区分的数据，但有效性取决于图有没有制造不真实的捷径。

## 研究关联

可借鉴的改变是：示范中的动作无需全都正确，只要多条经历能提供接近成功的连通路线，就可能恢复比时间顺序更合理的进度标准。这适合研究含反复调整的演示，但依赖状态间的连接确实有操作意义。

### 下一步读哪里

先核查空间量是什么、视觉一致性怎样计算，以及成功节点如何确定；再看新状态的进度预测和强化学习奖励公式。重点寻找错误连边消融、绝对成功率，以及充电器插入的仿真与真机结果归属。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-19/Not All Actions Contribute Equally Learning Precise Progress Estimation from Imp.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Progress estimators play an essential role in providing dense reward signals for reinforcement learning in robotic manipulation, but accurately assessing task progress can be much challenging. Existing methods heavily rely on expert data and naively assume that all actions within a demonstration contribute to task success. This assumption often breaks down in real-world scenarios, especially in high-precision manipulation, where subtle geometric errors can lead to task failure. Therefore, these methods can erroneously interpret human mistakes as meaningful progress, further corrupting progress learning. We argue that a key limitation is the lack of a global prior regarding task evaluation criteria, which is crucial for distinguishing meaningful progress from human mistakes. To this end, we propose PRIME, a novel progress estimator capable of learning precise progress estimation from imprecise demonstrations by aggregating experience across trajectories. PRIME constructs a weighted graph over observed states, connecting states across trajectories based on spatial proximity and visual consistency. Edge weights encode spatial distances as transition costs, and shortest-path search approximates the geodesic distance to success. Changes in this distance naturally distinguish advancement, stagnation, and setbacks without assuming monotonic progress over time. Extensive experiments in both simulation and real world on precise manipulation tasks show that PRIME is consistently effective across diverse tasks, and robust to data with varying degrees of suboptimality. Notably, the advantage of PRIME gets more pronounced in higher-precision scenarios, yielding up to a \(5\times\) improvement in policy success rate over the SFT baselines on charger insertion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23769v1
- Authors: Huanqian Wang, Boshi Tang, Botong Xiao, Jie Zhang, Yang Yue, Danhua Tao, Shiji Song, Gao Huang
- Published: 2026-10-16T17:07:39Z
- Age days: 2

</details>
