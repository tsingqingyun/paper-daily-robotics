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
url: "https://arxiv.org/abs/2611.08577v1"
published: "2026-11-05T18:55:42Z"
age_days: 4
score: 55
created: 2026-11-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Meituan-Robotics-0（MR0）让桌面机器人先从多来源数据学动作，再用真实执行中的纠错补上恢复能力。最值得注意的是 Rollback：保留机器人走错的一段，并从共同起点采集人工替代动作，让策略同时学“该怎么做”和“该避开什么”。

## 问题

任务是固定底座机器人的桌面操作。瓶颈有三层：不同机器人的动作和数据格式不一致；只模仿成功示范，很少学到自己犯错后的恢复；只看当前画面的策略，会忘记已经离开视野的任务信息。[S3](https://arxiv.org/html/2611.08577v1#S1.p1.1) 因而，单纯扩大动作模型不能同时解决这些问题。

### 用一个例子理解

理解用例（非论文实验）：输入“把插头插进接口”和当前图像；机器人偏着推进后暂停，回到接近接口前的位置，由人重新对齐插入。训练保留两段作正负对照；下次策略结合当前图像生成更偏向纠正方向的动作。

## 创新点或方法

训练先把动作编码成离散 token，与图文数据共训；再换成连续动作头，用 flow matching 学精细控制，避免离散编码的重建误差。[S6](https://arxiv.org/html/2611.08577v1#S1.p3.1) [S24](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS1.p3.1) 真机后训练中，Rollback 回到早先状态，将被替换动作标负、人工纠正标正；CFG-DAgger 学条件分支，推理时组合正负预测，引导动作远离错误段，无需先学价值模型。[S28](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p3.1) [S29](https://arxiv.org/html/2611.08577v1#S3.F6) [S30](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p4.1) [S31](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p5.1) [S32](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p6.1) 部署另用异步动作块合并维持连续执行，事件记忆则在进度或可行性变化时触发重规划。[S7](https://arxiv.org/html/2611.08577v1#S1.p4.1)

### 方法如何工作

1. 统一异构数据的动作表示，得到可共训的机器人经验，先消除监督格式冲突。
2. 离散动作与图文联合预训练，再转连续动作生成，把语义知识接到精细控制上。[S6](https://arxiv.org/html/2611.08577v1#S1.p3.1)
3. 真实执行时回退采集人工替代段，保留原错误段，得到 CFG-DAgger 的正负监督。
4. 部署时由策略连续输出动作块；事件记录保留任务状态，条件变化后才请求任务级调整。

### 必要术语

- 动作块：一次预测一小段连续动作；本文用异步合并处理推理等待。
- Flow matching：学习把噪声逐步变成动作序列；本文用于连续动作生成。
- CFG：组合不同条件下的预测来引导生成；本文用正负分支偏向纠正行为。

## 证据

RoboTwin 2.0 仿真成功率为 93.6%，RoboDojo VLA 赛道排名第五；三项真机任务中，相同 HG-DAgger 后训练下，MR0 的平均成功率与进度分高于 π₀.₅。[S8](https://arxiv.org/html/2611.08577v1#S1.p5.1) 网线插入中，同一 Rollback 数据上，CFG-DAgger 优于 HG-DAgger 和 RECAP，达到 70% 成功率、0.90 进度分。[S8](https://arxiv.org/html/2611.08577v1#S1.p5.1) 节选未给试验次数、误差范围及对照具体数值；事件检索与任务恢复仅有定性展示。

## 局限

我会核查 Rollback 对物体状态能恢复到什么程度：机械臂回位不保证衣物或接触状态也复原。还应分开判断动作策略与事件代理的贡献，当前定性展示不足以量化长期记忆的收益。

- **判断**：值得重点读 Rollback 和 CFG-DAgger；它们给出了具体可复用的数据采集思路，比整体系统成绩更容易转化为实验。

## 研究关联

纠错采集不必只留下“正确答案”：从相近起点保留错误与替代动作，可以直接形成有方向的监督。如果任务允许可靠回到历史状态，这比额外训练价值估计器更值得先尝试。

### 下一步读哪里

先读 [S28](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p3.1) [S29](https://arxiv.org/html/2611.08577v1#S3.F6) [S30](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p4.1) [S31](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p5.1) 的配对与条件训练，再核查附录中的 CFG 组合公式、回退误差和人工成本。对实验应查网线插入的重复次数、进度分定义，以及异步执行和事件记忆各自的消融。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：55
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.08577v1
- 获取时间：2026-11-10T00:15:37.496723+00:00
- [S1] [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation · 正文段落 1](https://arxiv.org/html/2611.08577v1#abstract1.1)
- [S2] [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation · 正文段落 2](https://arxiv.org/html/2611.08577v1#abstract1.2)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.08577v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.08577v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.08577v1#S1.F1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.08577v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.08577v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.08577v1#S1.p5.1)
- [S9] [2 Data Curation · 正文段落 9](https://arxiv.org/html/2611.08577v1#S2.T1)
- [S10] [2 Data Curation · 正文段落 10](https://arxiv.org/html/2611.08577v1#S2.T1.4.1)
- [S11] [2 Data Curation · 正文段落 11](https://arxiv.org/html/2611.08577v1#S2.p1.1)
- [S12] [2.1 Vision-Language Data · 正文段落 12](https://arxiv.org/html/2611.08577v1#S2.F2)
- [S13] [2.1 Vision-Language Data · 正文段落 13](https://arxiv.org/html/2611.08577v1#S2.SS1.p1.1)
- [S14] [2.1 Vision-Language Data · 正文段落 16](https://arxiv.org/html/2611.08577v1#S2.F3)
- [S15] [3.1 Policy Architecture · 正文段落 34](https://arxiv.org/html/2611.08577v1#S3.F5)
- [S16] [3.1 Policy Architecture · 正文段落 35](https://arxiv.org/html/2611.08577v1#S3.SS1.p1.1)
- [S17] [3.1 Policy Architecture · 正文段落 36](https://arxiv.org/html/2611.08577v1#S3.E4)
- [S18] [3.1 Policy Architecture · 正文段落 37](https://arxiv.org/html/2611.08577v1#S3.SS1.p2.1)
- [S19] [3.1 Policy Architecture · 正文段落 38](https://arxiv.org/html/2611.08577v1#S3.SS1.p3.1)
- [S20] [3.2 Progressive Training · 正文段落 39](https://arxiv.org/html/2611.08577v1#S3.SS2.p1.1)
- [S21] [3.2.1 Discrete Multimodal Pre-Training · 正文段落 40](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS1.p1.1)
- [S22] [3.2.1 Discrete Multimodal Pre-Training · 正文段落 41](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS1.p2.1)
- [S23] [3.2.1 Discrete Multimodal Pre-Training · 正文段落 42](https://arxiv.org/html/2611.08577v1#S3.E5)
- [S24] [3.2.1 Discrete Multimodal Pre-Training · 正文段落 43](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS1.p3.1)
- [S25] [3.2.1 Discrete Multimodal Pre-Training · 正文段落 44](https://arxiv.org/html/2611.08577v1#S3.T3)
- [S26] [3.2.3 Real-World Policy Optimization · 正文段落 52](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p1.1)
- [S27] [3.2.3 Real-World Policy Optimization · 正文段落 53](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p2.1)
- [S28] [3.2.3 Real-World Policy Optimization · 正文段落 54](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p3.1)
- [S29] [3.2.3 Real-World Policy Optimization · 正文段落 55](https://arxiv.org/html/2611.08577v1#S3.F6)
- [S30] [3.2.3 Real-World Policy Optimization · 正文段落 56](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p4.1)
- [S31] [3.2.3 Real-World Policy Optimization · 正文段落 57](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p5.1)
- [S32] [3.2.3 Real-World Policy Optimization · 正文段落 58](https://arxiv.org/html/2611.08577v1#S3.SS2.SSS3.p6.1)
- [S33] [5.2 Real-Robot Evaluation · 正文段落 87](https://arxiv.org/html/2611.08577v1#S5.SS2.p1.1)
- [S34] [5.2.1 Experimental Setup · 正文段落 88](https://arxiv.org/html/2611.08577v1#S5.SS2.SSS1.p1.1)
- [S35] [5.2.1 Experimental Setup · 正文段落 89](https://arxiv.org/html/2611.08577v1#S5.I1.i1)
- [S36] [5.2.1 Experimental Setup · 正文段落 90](https://arxiv.org/html/2611.08577v1#S5.I1.i2)
- [S37] [6 Conclusion · 正文段落 111](https://arxiv.org/html/2611.08577v1#S6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/Meituan-Robotics-0 A Vision-Language-Action Foundation Model for Desktop Manipul.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced policy segments with human corrections to provide positive and negative supervision for CFG-DAgger without value learning or advantage labeling. A unified end-effector interface supports heterogeneous embodiments, while asynchronous action-chunk merging maintains smooth execution under variable inference latency. An event-driven agent maintains persistent task events and reassesses plans when progress or feasibility changes, enabling cross-task retrieval and conditional task resumption. MR0 achieves 93.6% success on RoboTwin 2.0 and ranks fifth in the RoboDojo VLA track. Under matched HG-DAgger post-training, MR0 achieves higher average success rate and progress score than $π_{0.5}$ across three real-robot tasks. On Ethernet insertion, CFG-DAgger trained with Rollback data reaches 70% success and a progress score of 0.90. Qualitative agent deployments demonstrate cross-task event retrieval and recovery from temporarily unsatisfied task conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08577v1
- Authors: Meituan Robotics Team, Caicheng Wang, Chen Zhao, Chengpeng Jin, Duo Xu, Fengjiao Chen, Guanglu Wan, Heqing Yang, Jia Wang, Jiacong Zhou, Jie Hu, Jiyuan Ru, Lingfeng Zhang, Linjiang Huang, Manyuan Zhang, Ningchu Liu, Shijie Zhou, Si Liu, Shuo Li, Tianyi Zhang, Xi Zhang, Xin Chen, Xuezhi Cao, Xunliang Cai, Yanbin Zeng, Yang Yang, Yang Yi, Yanli Tan, Yifu Xu, Yimeng Jia, Yuchen Tang, Yuchen Xie, Yuxiang Zheng, Zerwei Chng, Zilong Huang, Zipeng Ye, Ziyuan Qin, Ziqin Wang
- Published: 2026-11-05T18:55:42Z
- Age days: 4

</details>
