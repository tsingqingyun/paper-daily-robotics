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
url: "https://arxiv.org/abs/2610.12470v1"
published: "2026-10-08T17:59:58Z"
age_days: 3
score: 24
created: 2026-10-12
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Dex-One2Many 从单个人类视频提取每个阶段必须满足的关系，再让灵巧手在仿真中学习怎样实现它们。关键是同一关系能生成许多姿态和抓法，同时允许策略从后续阶段直接开始练习。

## 问题

任务是从一段视频学习多指抓取、移动和工具使用，还要适应没演示过的初始与目标姿态。照着手或物体轨迹模仿容易绑定原配置；完全放开 RL，又很难偶然发现多阶段、复杂接触动作 [S5](https://arxiv.org/html/2610.12470v1#S1.p2.1) [S6](https://arxiv.org/html/2610.12470v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：输入人拿印章盖向目标的视频；抽成抓住印章、工作面接近目标、完成接触等关系，生成不同位置和抓法练习，最终策略根据新场景位姿执行盖印。

## 创新点或方法

本文把“复现这条轨迹”改成“按顺序满足这些手—物体、物体—物体关系”。训练用阶段图约束生成初始状态、观测和奖励，改变位置与抓法，并过滤碰撞及不稳定状态；从各阶段重置，缩短探索距离。PPO 在仿真学习策略。部署不再跟踪视频，而从真实物体位姿和机器人状态输出掌心、指尖速度，由低层控制器执行 [S16](https://arxiv.org/html/2610.12470v1#S3.SS2.p1.1) [S17](https://arxiv.org/html/2610.12470v1#S3.SS2.p2.1) [S18](https://arxiv.org/html/2610.12470v1#S3.SS2.p5.1) [S19](https://arxiv.org/html/2610.12470v1#S3.SS2.p6.1) [S35](https://arxiv.org/html/2610.12470v1#A3.SS5.p2.1) [S36](https://arxiv.org/html/2610.12470v1#A4.p1.1)。

### 方法如何工作

1. 把视频抽成有顺序的阶段关系，保留任务目标，放开具体动作。
2. 按关系生成多姿态和多抓法，经过仿真检查得到有效重置状态。
3. 从各阶段启动训练并给关系进度奖励，使策略无需先完成前段才能练后段。
4. 仿真训练后用真机位姿观测驱动策略，再由低层控制器跟踪任务空间速度。

### 必要术语

- 谓词：可检查的关系条件；用于定义阶段、奖励和重置约束。
- 重置状态：一次训练开始时的场景状态；让策略直接练习不同阶段。
- 零样本迁移：部署前不做真实数据训练或微调；不意味着无需模型和感知配置。

## 证据

五项任务包括 Doll、Can、Stamp、Hammer、Sweep，对比 Do as I Do 与 CHORD [S24](https://arxiv.org/html/2610.12470v1#S4.SS1.p1.1) [S26](https://arxiv.org/html/2610.12470v1#S4.SS1.p3.1)。真机使用 UR3 加 20 自由度 Wuji 1 手及双 RGB-D 相机 [S25](https://arxiv.org/html/2610.12470v1#S4.SS1.p2.1)。未见配置平均成功率 75%，比次优基线高 71 个百分点；各任务为 60—85%，基线不超过 15% [S9](https://arxiv.org/html/2610.12470v1#S1.p7.1) [S12](https://arxiv.org/html/2610.12470v1#S1.I1.i3)。摘要另报已见配置优势 6.5%，但未澄清其口径。节选未给逐任务试验次数和置信区间。

## 局限

作者明确指出位姿估计噪声和几何误差会影响接触操作，自动重建目前只覆盖刚体，关节物体需手工资产 [S31](https://arxiv.org/html/2610.12470v1#S5.p2.1)。单视频不等于直接从 RGB 学控制：部署依赖物体模型与位姿跟踪。图抽取如何纠错、失败关系如何处理，是节选未展开的待核查问题。

- **判断**：值得读到阶段图和重置生成实现：它给出从一条演示获得多种练习状态的具体办法，也有真实硬件证据。

## 研究关联

值得借鉴的是让任务描述同时决定奖励和“从哪里开始练”。只保留关系会扩大搜索空间，阶段重置再把这个空间切成可练习的片段；两者配合，才使放开轨迹约束变得可行。

### 下一步读哪里

先核查视频转关系图的自动化程度与谓词奖励，再读 [S18](https://arxiv.org/html/2610.12470v1#S3.SS2.p5.1) [S19](https://arxiv.org/html/2610.12470v1#S3.SS2.p6.1) [S33](https://arxiv.org/html/2610.12470v1#A3.SS3.p1.1) 的物理过滤；每阶段保留 10,000 个状态，其生成成本和可达性很关键。补查逐任务结果、消融及真实姿态变化范围。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：24
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12470v1
- 获取时间：2026-10-12T00:17:08.254779+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.12470v1#p1.2)
- [S2] [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration · 正文段落 2](https://arxiv.org/html/2610.12470v1#abstract1.1)
- [S3] [Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration · 正文段落 3](https://arxiv.org/html/2610.12470v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.12470v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12470v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.12470v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12470v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.12470v1#S1.p6.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.12470v1#S1.p7.1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.12470v1#S1.I1.i1)
- [S11] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.12470v1#S1.I1.i2)
- [S12] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.12470v1#S1.I1.i3)
- [S13] [2 Related Work · 正文段落 15](https://arxiv.org/html/2610.12470v1#S2.p2.1)
- [S14] [2 Related Work · 正文段落 16](https://arxiv.org/html/2610.12470v1#S2.p3.1)
- [S15] [3 Method · 正文段落 18](https://arxiv.org/html/2610.12470v1#S3.p1.1)
- [S16] [3.2 Scene-graph-grounded Reinforcement Learning · 正文段落 23](https://arxiv.org/html/2610.12470v1#S3.SS2.p1.1)
- [S17] [3.2 Scene-graph-grounded Reinforcement Learning · 正文段落 24](https://arxiv.org/html/2610.12470v1#S3.SS2.p2.1)
- [S18] [3.2 Scene-graph-grounded Reinforcement Learning · 正文段落 27](https://arxiv.org/html/2610.12470v1#S3.SS2.p5.1)
- [S19] [3.2 Scene-graph-grounded Reinforcement Learning · 正文段落 28](https://arxiv.org/html/2610.12470v1#S3.SS2.p6.1)
- [S20] [4 Experiments · 正文段落 30](https://arxiv.org/html/2610.12470v1#S4.p1.1)
- [S21] [4 Experiments · 正文段落 31](https://arxiv.org/html/2610.12470v1#S4.I1.ix1)
- [S22] [4 Experiments · 正文段落 32](https://arxiv.org/html/2610.12470v1#S4.I1.ix2)
- [S23] [4 Experiments · 正文段落 33](https://arxiv.org/html/2610.12470v1#S4.I1.ix3)
- [S24] [4.1 Experimental Setup · 正文段落 34](https://arxiv.org/html/2610.12470v1#S4.SS1.p1.1)
- [S25] [4.1 Experimental Setup · 正文段落 35](https://arxiv.org/html/2610.12470v1#S4.SS1.p2.1)
- [S26] [4.1 Experimental Setup · 正文段落 36](https://arxiv.org/html/2610.12470v1#S4.SS1.p3.1)
- [S27] [4.2 Does Dex-One2Many Generalize Beyond the Human Video? · 正文段落 40](https://arxiv.org/html/2610.12470v1#S4.SS2.p3.1)
- [S28] [4.4 Which Design Choices Are Critical to Dex-One2Many? · 正文段落 48](https://arxiv.org/html/2610.12470v1#S4.F7.3.1)
- [S29] [4.4 Which Design Choices Are Critical to Dex-One2Many? · 正文段落 49](https://arxiv.org/html/2610.12470v1#S4.F7.4.1)
- [S30] [5 Conclusion · 正文段落 54](https://arxiv.org/html/2610.12470v1#S5.p1.1)
- [S31] [5 Conclusion · 正文段落 55](https://arxiv.org/html/2610.12470v1#S5.p2.1)
- [S32] [C.3 Reset Generation · 正文段落 114](https://arxiv.org/html/2610.12470v1#A3.F10)
- [S33] [C.3 Reset Generation · 正文段落 115](https://arxiv.org/html/2610.12470v1#A3.SS3.p1.1)
- [S34] [C.5 Simulation Training Details · 正文段落 138](https://arxiv.org/html/2610.12470v1#A3.SS5.p1.1)
- [S35] [C.5 Simulation Training Details · 正文段落 139](https://arxiv.org/html/2610.12470v1#A3.SS5.p2.1)
- [S36] [Appendix D Real-World Perception · 正文段落 145](https://arxiv.org/html/2610.12470v1#A4.p1.1)
- [S37] [Appendix D Real-World Perception · 正文段落 147](https://arxiv.org/html/2610.12470v1#A4.E9)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-12/Dex-One2Many Learning Dexterous Manipulation from a Single Human Demonstration.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for broad generalization, but without prior guidance, it struggles with high-dimensional exploration in complex, multi-stage tasks. To address these coupled generalization and exploration challenges, we present Dex-One2Many, a real-to-sim-to-real framework that learns a generalizable dexterous manipulation policy from a single human video. Our key insight is to abstract the video into sequential scene graphs that guide RL, enabling efficient exploration while preserving broad generalizability. The graphs serve as generative constraints for sampling diverse reset states and provide dense rewards for each stage. Because the graphs constrain relations rather than exact poses, these reset states cover object poses and grasps beyond the video, while initializing each stage from them with dense rewards keeps exploration short and guided. Trained entirely in simulation, Dex-One2Many transfers zero-shot to a real multi-fingered hand. Across five tool-use and manipulation tasks, Dex-One2Many exceeds baselines by 6.5% in seen configurations, while its robust generalization widens this gap to 71% in unseen scenarios.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12470v1
- Authors: Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung, Yongjun You, H. Jin Kim, Jia-Bin Huang, Furong Huang, Youngseok Jang, Seungjae Lee
- Published: 2026-10-08T17:59:58Z
- Age days: 3

</details>
