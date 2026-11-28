---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.33769v1"
published: "2026-11-25T04:48:42Z"
age_days: 2
score: 27
created: 2026-11-28
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> FailPoint-X 让机器人策略从同一个失败现场重新开始，测它能不能自己补救。它用同样的更新次数比较模仿人工接管和继续学原示范，并另外测正常开局的成功率。

## 问题

正常开局的成功率混合了两种能力：避免出错和出错后补救。直接比较后训练策略与原策略，又会把新数据的作用与多做几轮更新的作用混在一起。还有一个采集难点：夹爪开始滑落到物体彻底掉下之间，往往很难选出唯一的失败起点。[S4](https://arxiv.org/html/2611.33769v1#S1.p1.1)–[S6](https://arxiv.org/html/2611.33769v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）。让策略把海绵放进托盘。底座策略把海绵滑到托盘旁，人工从这段失误中的抽样状态接管，重新夹起并放好。后训练后，把各策略放回同一个留出的滑落现场，记录它们能否在时限内完成原指令，再从正常开局测一次。

## 创新点或方法

同一个 π₀.₅ 检查点既生成失败轨迹，也作为各后训练方法的起点。标注员圈出失误开始的时间区间，训练侧在区间内按固定随机种子抽帧，让人工从这些状态接管。Takeover-BC 模仿通过验收的恢复，Demo-continue 用同一训练配方继续学旧示范，IQL-R2 引入失败轨迹并用价值估计影响训练，Mix-BC 混合示范与恢复。推理时恢复留出区间的固定中点，各策略从相同仿真状态接着完成原任务，另外从正常开局测试原技能保留情况。[S7](https://arxiv.org/html/2611.33769v1#S1.p4.1)[S8](https://arxiv.org/html/2611.33769v1#S1.p5.1)[S20](https://arxiv.org/html/2611.33769v1#S4.SS1.SSS0.Px1.p1.1)[S31](https://arxiv.org/html/2611.33769v1#A5.I1.ix2.p1.1)[S32](https://arxiv.org/html/2611.33769v1#A5.I1.ix4.p1.1)

### 方法如何工作

1. 运行固定策略并记录自然失败，对失误开始标记一个区间，保留可还原的仿真状态。
2. 在训练区间抽帧收集人工接管，同时记录失败尝试，使恢复数据的来源和采集成本可追溯。
3. 从同一检查点用等量策略更新训练各组，让纯克隆与继续示范训练可以直接比较。
4. 在同一留出失败中点测恢复，再从正常起点测原任务成功率，检查收益是否伴随保留损失。

### 必要术语

- 行为克隆：用记录中的动作直接监督策略；Takeover-BC 学的是人工恢复动作。
- 价值估计：预测某状态或动作通向好结果的程度；IQL-R2 用它调整离线策略学习。
- 失败中点重启：恢复人工标注区间中点的仿真状态；让不同策略面对相同的补救起点。

## 证据

在 LIBERO-X 仿真的 240 个 L1–L3 留出失败上，给 1,200 步，Takeover-BC 恢复成功率为 51.9%，Demo-continue 为 22.5%，差 +29.4 个百分点，按任务家族配对的 95% 区间为 +16.9 至 +44.7 [S1](https://arxiv.org/html/2611.33769v1#abstract1.1)[S23](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)。IQL-R2 相对克隆多 1.5 个百分点，区间跨零 [S18](https://arxiv.org/html/2611.33769v1#S4.T3.10)。探索性正常开局测试中，纯克隆和混合训练比原策略低 30.0 和 16.5 个百分点，缩短时限后两者的损失更接近 [S9](https://arxiv.org/html/2611.33769v1#S1.p6.1)。主对照支持这批接管数据整体带来恢复收益 [S23](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)。

## 局限

作者把范围限定为仿真、一个检查点、一名接管者和每组一次训练 [S25](https://arxiv.org/html/2611.33769v1#S6.p2.1)。主对照同时改变了训练见到的状态和动作标签，无法拆出两者各自的贡献 [S23](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)。还值得核查从同一失败区间的早端或晚端重启时，优势是否稳定。

- **判断**：值得细读表 3 和恢复评测协议。这里最可复用的是如何控制起点和训练预算，以及如何同时发现恢复收益与原技能损失。

## 研究关联

做纠错后训练时，值得保留两套起点：真实出错后到达的状态，用于测补救；任务自然开局的状态，用于测原技能。混合数据看起来能保住多少原技能，还可能取决于给策略多少时间。

### 下一步读哪里

对读 [S17](https://arxiv.org/html/2611.33769v1#S4.T3)[S18](https://arxiv.org/html/2611.33769v1#S4.T3.10)[S20](https://arxiv.org/html/2611.33769v1#S4.SS1.SSS0.Px1.p1.1)，核查训练步数、各组实际看到的数据和置信区间。再看 [S31](https://arxiv.org/html/2611.33769v1#A5.I1.ix2.p1.1)–[S33](https://arxiv.org/html/2611.33769v1#A5.I1.ix6.p1.1) 怎样恢复状态、清空动作队列和设定时限，并核查补充材料中的同 GPU 正常开局比较。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.33769v1
- 获取时间：2026-11-28T03:58:17.824495+00:00
- [S1] [FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers · 正文段落 1](https://arxiv.org/html/2611.33769v1#abstract1.1)
- [S2] [FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers · 正文段落 2](https://arxiv.org/html/2611.33769v1#p2.1)
- [S3] [FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers · 正文段落 3](https://arxiv.org/html/2611.33769v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.33769v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.33769v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.33769v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.33769v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.33769v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.33769v1#S1.p6.1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.33769v1#S1.I1.i1)
- [S11] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.33769v1#S1.I1.i2)
- [S12] [1 Introduction · 正文段落 13](https://arxiv.org/html/2611.33769v1#S1.I1.i3)
- [S13] [1 Introduction · 正文段落 15](https://arxiv.org/html/2611.33769v1#S1.T1.10)
- [S14] [Learning from human interventions. · 正文段落 17](https://arxiv.org/html/2611.33769v1#S2.SS0.SSS0.Px1.p1.1)
- [S15] [Learning from human interventions. · 正文段落 18](https://arxiv.org/html/2611.33769v1#S2.F2)
- [S16] [Offline learning from corrections and failures. · 正文段落 19](https://arxiv.org/html/2611.33769v1#S2.SS0.SSS0.Px2.p1.1)
- [S17] [4 Controlled Post-Training and Evaluation · 正文段落 39](https://arxiv.org/html/2611.33769v1#S4.T3)
- [S18] [4 Controlled Post-Training and Evaluation · 正文段落 40](https://arxiv.org/html/2611.33769v1#S4.T3.10)
- [S19] [4 Controlled Post-Training and Evaluation · 正文段落 41](https://arxiv.org/html/2611.33769v1#S4.p1.1)
- [S20] [Shared training and controls. · 正文段落 42](https://arxiv.org/html/2611.33769v1#S4.SS1.SSS0.Px1.p1.1)
- [S21] [5 Experiments and Analysis · 正文段落 53](https://arxiv.org/html/2611.33769v1#S5.F3)
- [S22] [5 Experiments and Analysis · 正文段落 54](https://arxiv.org/html/2611.33769v1#S5.p1.1)
- [S23] [Takeover data improve recovery beyond continued training (Q1). · 正文段落 55](https://arxiv.org/html/2611.33769v1#S5.SS1.SSS0.Px1.p1.1)
- [S24] [6 Conclusion and Outlook · 正文段落 63](https://arxiv.org/html/2611.33769v1#S6.p1.1)
- [S25] [6 Conclusion and Outlook · 正文段落 64](https://arxiv.org/html/2611.33769v1#S6.p2.1)
- [S26] [Appendix A Benchmark Construction: Platform, Base Policy, Task Families and Screening · 正文段落 67](https://arxiv.org/html/2611.33769v1#A1.p1.1)
- [S27] [A.1 Platform and base policy · 正文段落 68](https://arxiv.org/html/2611.33769v1#A1.I1.ix1.p1.1)
- [S28] [A.1 Platform and base policy · 正文段落 69](https://arxiv.org/html/2611.33769v1#A1.I1.ix2.p1.1)
- [S29] [A.1 Platform and base policy · 正文段落 70](https://arxiv.org/html/2611.33769v1#A1.I1.ix3.p1.1)
- [S30] [Evaluation and artifact mapping. · 正文段落 150](https://arxiv.org/html/2611.33769v1#A4.SS4.SSS0.Px2.p1.1)
- [S31] [E.1 Restore-and-continue evaluation · 正文段落 154](https://arxiv.org/html/2611.33769v1#A5.I1.ix2.p1.1)
- [S32] [E.1 Restore-and-continue evaluation · 正文段落 156](https://arxiv.org/html/2611.33769v1#A5.I1.ix4.p1.1)
- [S33] [E.1 Restore-and-continue evaluation · 正文段落 158](https://arxiv.org/html/2611.33769v1#A5.I1.ix6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/FailPoint-X A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Tr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human takeovers offer corrective supervision for vision-language-action (VLA) policies, but their contribution to offline post-training must be separated from that of continued optimization. We introduce FailPoint-X, a benchmark for offline VLA post-training with human takeovers. To represent uncertainty in failure onset, an annotator marks an interval for each failure, and training takeovers start at seeded frames sampled within it. From one fixed $π_{0.5}$ checkpoint, which also initializes post-training, we assemble 629 natural failures across 10 LIBERO-X task families at up to five difficulty levels. All 2,823 takeover attempts are logged; 2,400 are accepted recoveries, of which 2,320 are used for post-training. Evaluation restarts every method from the fixed midpoints of 384 held-out failure intervals. Under matched actor-update counts, we compare behavior cloning of recoveries, value-based offline learning on recoveries and failed rollouts, and continued training on existing demonstrations. Within 1,200 steps on the 240 L1-L3 held-out failures, cloning improves recovery by 29.4 percentage points (pp) over the demonstration-only control; the value-based learner does not establish a further gain (1.5 pp). In exploratory evaluation from L1-L5 nominal starts at the same horizon, cloning loses 30.0 pp of success relative to the base policy; mixing in demonstrations reduces the loss to 16.5 pp, a reduction that shrinks under a stricter, pre-specified horizon. Restorable failure states and a shared evaluator let all methods be compared from identical starts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33769v1
- Authors: Zirui Li, Yujie Yan, Jingxuan Qian, Yangang Ren, Haizhou Yin, Haoran Xu, Chen Lv
- Published: 2026-11-25T04:48:42Z
- Age days: 2

</details>
