---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27345"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-08-29
concepts: ["世界模型", "具身智能评测与基准"]
---

# PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

> [!summary] 先说人话（基于摘要）
> PAWBench要求世界模型在同一起点和动作下多次生成时，不仅产出合理结果，还要复现各种物理结果的真实概率。PAWEval把重复视频 rollout 转成结果分布进行比较。

## 问题

物理过程常有多个有效未来，单条视频看起来合理不能证明模型学对了随机动力学。现有评测多看单视频质量，忽略生成结果的概率和模式覆盖。

## 创新点或方法

将概率对齐形式化为分布级世界模型标准；对每个情景重复采样视频，用结果级协议归纳为可能物理行为的经验分布，再与参考概率和有效行为范围比较。还测试提示、初始噪声与训练能否重塑分布。

## 证据

覆盖50个情景和11个现有系统；没有模型能持续同时匹配参考概率并恢复有效行为范围。摘要未给出具体距离指标或各模型分数。


## 局限

最需核查结果类别如何定义、参考概率如何获得，以及有限重复采样能否可靠估计分布。

- **判断**：值得所有随机视频世界模型研究者精读评测定义；它指出的缺口比任何单一模型排名更重要。

## 研究关联

对世界模型研究者，这是重要的评测升级：规划和风险判断依赖事件概率，而非一条视觉上可信的未来。它也可揭示模式坍缩或概率偏置。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/PAWBench How Far Are We from Probabilistically Aligned World Modeling.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27345v1 Announce Type: new Abstract: Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recover the correct distribution. This raises a central question: how far are current video generators from probabilistically aligned world modeling? To answer it, we formalize probabilistic alignment as a distributional criterion for world models and introduce PAWBench, a benchmark for evaluating video generators as stochastic samplers of world dynamics. We further introduce PAWEval, an outcome-level protocol that converts repeated video rollouts into empirical distributions over possible physical behaviors. Across 50 scenarios and eleven current systems, no model consistently matches the reference probabilities while recovering the range of valid behaviors. Having established this gap, we test whether language prompts, initial noise sampling, or model training can reshape the model's predictive distribution. We believe our work can serve as a foundation for future efforts to move towards probabilistically aligned world modeling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27345
- Authors: Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram {\DJ}or{\dj}evi\'c, Shiyang Li, Yifan Zhou, Bin Fu, Wenlong Zhang, Junjun He, Yu Qiao, Yihao Liu, Jingbo Xing, Xi Chen
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
