---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2602.00266"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 19
created: 2026-09-06
concepts: ["AI 核心知识地图"]
---

# Complete Identification of Deep ReLU Networks through {\L}ukasiewicz Logic

> [!summary] 先说人话（基于摘要）
> 作者用 Łukasiewicz 多值逻辑完整刻画深层 ReLU 网络的函数等价性：网络先转成替换图和逻辑公式，等价证明通过公理推导完成，再可构造回网络。

## 问题

不同架构和参数的深层 ReLU 网络可能实现完全相同的函数；任务是完整识别这种非唯一性。困难不只是找常见的单层参数对称，而是覆盖跨三层以上的深层等价变换。

## 创新点或方法

提取算法把网络转为分层 substitution graph，其公式真值函数等于网络输入输出映射；完备性定理保证函数等价公式可相互推导；构造算法再由图返回网络。整数、有理数和实数权重分别用 MV、divisible MV 与 Riesz MV 公理，节点改写、层折叠和层展开三种局部操作实现全部推导。

## 证据

摘要给出理论结论：两个非退化 ReLU 网络在单位立方体上函数相同，当且仅当可通过相应 MV 逻辑公理的有限次应用互相得到；未报告实验数字。


## 局限

适用条件限定为非退化 ReLU 网络及单位立方体，且不同权重域使用不同公理体系；需查全文了解算法复杂度和对实际规模网络的可计算性。

- **判断**：理论神经网络与形式化验证研究者值得精读定理和构造；应用型机器人研究者只需知道该完备刻画存在。

## 研究关联

它属于 AI 核心理论：可为网络化简、等价验证和参数对称性分析提供完整符号基础。对具身智能、VLA 和机器人学习没有摘要可支持的直接应用价值。

- **概念**：AI 核心知识地图
- **筛选分数**：19
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/Complete Identification of Deep ReLU Networks through { L}ukasiewicz Logic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2602.00266v2 Announce Type: replace Abstract: Two deep ReLU networks can have entirely different architectures and parameters, yet realize the same function. We provide a complete characterization of this nonuniqueness. This is effected by building a symbolic calculus for deep ReLU networks, equivalence and simplification of networks becoming derivation of formulae, in close parallel to Shannon's analysis of switching circuits through Boolean logic. Inspired by Shannon, who turned circuit synthesis into the manipulation of Boolean formulae by the axioms of Boolean algebra, we turn ReLU network identification into the derivation of {\L}ukasiewicz formulae by the axioms of many-valued (MV) logic. Two non-degenerate ReLU networks realize the same function on the unit cube if and only if one is obtained from the other by finitely many applications of the MV axioms for integer weights and biases, the divisible MV axioms for rational ones, and the Riesz MV axioms for real ones. The MV logic axioms characterize all symmetries of ReLU networks, the single-layer ones, which for tanh networks are the only kind, and the deep ones, spanning three or more layers. Our framework consists of three steps, an extraction algorithm turning a network into a substitution graph, whose represented formula has the network's input-output map as its truth function, a completeness theorem, by which functionally equivalent formulae are interderivable, and a construction algorithm returning from graphs to networks. The substitution graph is layered, carrying at each node a formula in the variables of the layer feeding it, encodes the network uniquely, and induces a new normal form for MV logic, compositional rather than flat as in the literature, hence retaining the algebraic structure of the network, with three local operations--node rewrite, layer collapse, layer expansion--realizing every derivation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2602.00266
- Authors: Yani Zhang, Helmut B\"olcskei
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
