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
url: "https://arxiv.org/abs/2610.22372v1"
published: "2026-10-15T17:59:59Z"
age_days: 1
score: 41
created: 2026-10-17
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> LIBERO-PeRM 把“任务做完”和“按用户喜欢的方式做完”分开测。它在相同任务目标下生成有偏好、无偏好的示范，并检查策略是否学会了可迁移的执行要求。

## 问题

杯子放上桌就算成功，无法说明杯柄方向、移动路线或杯垫选择是否符合用户要求。此前个性化工作的输入和评分不统一，高层选物或记忆测试也难区分真正的偏好学习与任务实例记忆。[S5](https://arxiv.org/html/2610.22372v1#S1.p3.1) 本文要建立可控制变量、可自动评分的操作测试。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放桌上；杯柄朝外”及两路图像→策略完成抓取、旋转、放置→评测分别检查杯子是否到桌面、杯柄方向是否符合要求，避免只凭到位就判定个性化成功。

## 创新点或方法

旧评测主要换任务；本文把任务、布局和偏好分别控制。固定布局与目标后，VLM 生成两类子任务计划，再调用由人类示范提取路点、经运动规划扩充的技能生成轨迹。画像改变计划，技能偏好改变技能选择，运动偏好改变轨迹生成。[S20](https://arxiv.org/html/2610.22372v1#S3.SS2.p3.1) 训练时用这些示范做监督微调；推理时输入两路图像及分别标注的任务、偏好文本，输出动作。[S19](https://arxiv.org/html/2610.22372v1#S3.SS1.p3.1) 它首先是评测与数据方案，不是新的动作模型。

### 方法如何工作

1. 固定任务目标，附加运动、技能或画像偏好，得到可比较的执行条件。
2. 分别生成无偏好和有偏好的计划，再用技能库生成轨迹，使训练数据具有对应关系。
3. 用示范训练策略，测试时给任务与偏好文本，观察要求能否进入实际动作。
4. 分别记录任务成功与成功后的偏好满足程度，再改变任务、布局或组合条件，检查学到的要求能否复用。

### 必要术语

- 运动偏好：约束移动过程；本文用路线距离等可观测量检查。
- 技能偏好：约束某个操作怎样完成；例如放杯时调整杯柄方向。
- SA：成功回合的偏好得分在所有回合上的平均；失败回合记零，因此同时受任务能力影响。

## 证据

基准含五套任务、312个偏好条件任务，覆盖37个单偏好实例及18个双偏好组合。[S6](https://arxiv.org/html/2610.22372v1#S1.p4.1) [S8](https://arxiv.org/html/2610.22372v1#S1.p6.1) 六种 VLA 的零样本测试中，π0.5 无偏好成功率97.6%，加偏好后任务成功率66.67%、偏好满足度37.92%；运动偏好下成功率97.50%，满足度仅24.38%，清楚显示做完不等于听从偏好。[S31](https://arxiv.org/html/2610.22372v1#S4.T2.7) 满足度只在任务成功时计分。[S23](https://arxiv.org/html/2610.22372v1#S3.SS4.p1.1) 摘要称混合训练更保留无偏好能力，但可能削弱运动偏好学习；节选未给对应训练结果表，无法量化收益。

## 局限

作者明确限定为仿真中预定义、语言可表达且能自动测量的偏好，不覆盖互动历史推断、演变偏好或真机长期使用；生成技能也可能留下数据偏差。[S35](https://arxiv.org/html/2610.22372v1#S5.p2.1) 冲突评分取两项偏好中较高的满足分，并不测试发现冲突或询问用户。[S24](https://arxiv.org/html/2610.22372v1#S3.SS4.p2.1) 因而高分不能直接解释为理解用户意图。

- **判断**：值得重点读变量划分、评分和数据生成；使用前先确认自动规则是否对应自己真正想测的偏好。

## 研究关联

最值得借鉴的是保留目标不变，只改变完成方式，再换任务和布局测试同一偏好。只有这样，才能检查模型学到的是“绕开指定区域”这类要求，还是某条熟悉轨迹。

### 下一步读哪里

先看[S14](https://arxiv.org/html/2610.22372v1#S3.SS1.p1.1) [S15](https://arxiv.org/html/2610.22372v1#S3.I1.i1) [S16](https://arxiv.org/html/2610.22372v1#S3.I1.i2) [S17](https://arxiv.org/html/2610.22372v1#S3.I1.i3) [S18](https://arxiv.org/html/2610.22372v1#S3.SS1.p2.1) [S19](https://arxiv.org/html/2610.22372v1#S3.SS1.p3.1) [S20](https://arxiv.org/html/2610.22372v1#S3.SS2.p3.1) [S21](https://arxiv.org/html/2610.22372v1#S3.SS2.p5.1) [S22](https://arxiv.org/html/2610.22372v1#S3.SS2.p6.1) [S23](https://arxiv.org/html/2610.22372v1#S3.SS4.p1.1) [S24](https://arxiv.org/html/2610.22372v1#S3.SS4.p2.1)，尤其是连续统计如何分成四档满足标签，以及冲突评分约定；再核查训练表中的混合比例、数据量和跨布局划分。[S28](https://arxiv.org/html/2610.22372v1#S4.SS1.p1.1)的误差条来自固定检查点的重复评估，不能当作训练种子稳定性。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22372v1
- 获取时间：2026-10-17T00:17:18.038087+00:00
- [S1] [LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2610.22372v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.22372v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.22372v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.22372v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.22372v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.22372v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.22372v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.22372v1#S1.p6.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.22372v1#S1.p7.1)
- [S10] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.22372v1#S1.T1)
- [S11] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.22372v1#S1.T1.5.1)
- [S12] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.22372v1#S1.I1.i1)
- [S13] [1 Introduction · 正文段落 14](https://arxiv.org/html/2610.22372v1#S1.I1.i2)
- [S14] [3.1 Preference Formulation · 正文段落 21](https://arxiv.org/html/2610.22372v1#S3.SS1.p1.1)
- [S15] [3.1 Preference Formulation · 正文段落 22](https://arxiv.org/html/2610.22372v1#S3.I1.i1)
- [S16] [3.1 Preference Formulation · 正文段落 23](https://arxiv.org/html/2610.22372v1#S3.I1.i2)
- [S17] [3.1 Preference Formulation · 正文段落 24](https://arxiv.org/html/2610.22372v1#S3.I1.i3)
- [S18] [3.1 Preference Formulation · 正文段落 26](https://arxiv.org/html/2610.22372v1#S3.SS1.p2.1)
- [S19] [3.1 Preference Formulation · 正文段落 27](https://arxiv.org/html/2610.22372v1#S3.SS1.p3.1)
- [S20] [3.2 Preference-Conditioned Data Generation Pipeline · 正文段落 31](https://arxiv.org/html/2610.22372v1#S3.SS2.p3.1)
- [S21] [3.2 Preference-Conditioned Data Generation Pipeline · 正文段落 33](https://arxiv.org/html/2610.22372v1#S3.SS2.p5.1)
- [S22] [3.2 Preference-Conditioned Data Generation Pipeline · 正文段落 34](https://arxiv.org/html/2610.22372v1#S3.SS2.p6.1)
- [S23] [3.4 Evaluation · 正文段落 37](https://arxiv.org/html/2610.22372v1#S3.SS4.p1.1)
- [S24] [3.4 Evaluation · 正文段落 38](https://arxiv.org/html/2610.22372v1#S3.SS4.p2.1)
- [S25] [3.4 Evaluation · 正文段落 39](https://arxiv.org/html/2610.22372v1#S3.SS4.p3.1)
- [S26] [4 Experiments · 正文段落 40](https://arxiv.org/html/2610.22372v1#S4.p1.1)
- [S27] [4 Experiments · 正文段落 41](https://arxiv.org/html/2610.22372v1#S4.p2.1)
- [S28] [4.1 Experimental Setup · 正文段落 42](https://arxiv.org/html/2610.22372v1#S4.SS1.p1.1)
- [S29] [4.2 Experimental Results · 正文段落 43](https://arxiv.org/html/2610.22372v1#S4.SS2.p1.1)
- [S30] [4.2 Experimental Results · 正文段落 44](https://arxiv.org/html/2610.22372v1#S4.T2)
- [S31] [4.2 Experimental Results · 正文段落 45](https://arxiv.org/html/2610.22372v1#S4.T2.7)
- [S32] [4.2 Experimental Results · 正文段落 46](https://arxiv.org/html/2610.22372v1#S4.SS2.p2.1)
- [S33] [4.2 Experimental Results · 正文段落 48](https://arxiv.org/html/2610.22372v1#S4.SS2.p4.1)
- [S34] [4.2 Experimental Results · 正文段落 53](https://arxiv.org/html/2610.22372v1#S4.SS2.p7.1)
- [S35] [5 Conclusion · 正文段落 68](https://arxiv.org/html/2610.22372v1#S5.p2.1)
- [S36] [A.1 Ethics Statement · 正文段落 70](https://arxiv.org/html/2610.22372v1#A1.SS1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/LIBERO-PeRM Benchmarking Personalized Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings; 2) how they learn single preferences from demonstrations; 3) how efficiently they acquire preferences as demonstrations increase; 4) how learned preferences generalize across layouts and tasks; and 5) how policies compose preferences and behave under conflicts. We propose a controlled formulation and taxonomy of observable preferences in simulation, covering motion, skill, and user-profile choices. This formulation is restricted to language-expressible preferences that can be instantiated in LIBERO without changing the task goal, evaluated automatically, and reused across tasks. Building on LIBERO, our procedural pipeline generates paired demonstrations with and without preferences. We create five task suites (312 tasks) with high-quality demonstrations, rich metadata, and preference-satisfaction metrics. Experiments show that current VLA policies struggle with zero-shot personalization, while SFT makes preferences learnable. Mixed training achieves better no-preference retention than sequential adaptation and improves performance with contextual prompts compared with preference-only training, but can weaken motion-preference learning; preference generalization, decomposition, and conflict handling remain difficult. The code, datasets, and demos can be found on the project website: https://libero-perm.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22372v1
- Authors: Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang, Tianze Xu, Zehao Wang, Yuping Wang, Junge Zhang, Jiachen Li
- Published: 2026-10-15T17:59:59Z
- Age days: 1

</details>
