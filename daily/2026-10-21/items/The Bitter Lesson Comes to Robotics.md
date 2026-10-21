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
url: "https://arxiv.org/abs/2610.25287v1"
published: "2026-10-18T14:07:36Z"
age_days: 2
score: 44
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# The Bitter Lesson Comes to Robotics

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> The Bitter Lesson Comes to Robotics 把多种通用多模态语言模型接到同一台真机上，比较它们直接指定夹爪位姿能做多少事、花多久和多少钱。它发现局部操作能力正在进步，但有限动作预算内完整完成任务仍然困难。

## 问题

已有展示难以回答通用模型控制真机到底进步了多少：模型、任务和硬件常不一致，仿真又未必复现机械臂下垂、视差和标定漂移。本文因此做统一物理测试，而不是设计新的控制模型[S4](https://arxiv.org/html/2610.25287v1#S1.p2.1) [S5](https://arxiv.org/html/2610.25287v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）：模型收到“把积木放入盒子”和三路图像，发出靠近、闭合、抬起、移到盒内等位姿命令；每步执行后看新图像确认是否抓住，直到结束或用完预算。

## 创新点或方法

相较于跨展示比较，本文固定双臂 I2RT YAM、三路相机及操作接口，让模型在观察后输出双臂末端位置、姿态和夹爪开度。逆运动学及边界检查负责执行，再把观察送回模型；每轮最多40次动作[S16](https://arxiv.org/html/2610.25287v1#S3.p2.1) [S17](https://arxiv.org/html/2610.25287v1#S3.p3.1) [S18](https://arxiv.org/html/2610.25287v1#S3.p4.1) [S19](https://arxiv.org/html/2610.25287v1#S3.p5.1) [S20](https://arxiv.org/html/2610.25287v1#S3.p6.1)。没有提供针对任务的训练流程，核心是推理时闭环调用。评分拆成累计子任务，并统计包括失败尝试在内的时间和API成本[S21](https://arxiv.org/html/2610.25287v1#S3.p7.1) [S29](https://arxiv.org/html/2610.25287v1#S5.p1.1)。

### 方法如何工作

1. 统一硬件、任务和动作接口，使模型差异能在共同条件下比较。
2. 给模型图像、自身状态及操作说明，得到末端目标而非完整底层控制信号。
3. 通过逆运动学与动作限制执行命令，再反馈观察，让模型修正下一步。
4. 按阶段进展评分，并把全部尝试消耗的时间和费用计入效率，避免只统计成功片段。

### 必要术语

- 末端位姿：夹爪的位置和朝向；是模型直接指定的控制目标。
- 闭环控制：执行后重新观察再决策；让模型有机会发现并纠正错误。
- 阶段得分：完成若干里程碑得到的部分成绩；不等于整项任务成功率。

## 证据

七个模型、十二种配置，在叠碗、收纳入保险箱、分类、盖笔帽、装倒水果和扶瓶六项真机任务上，每配置每任务20次[S13](https://arxiv.org/html/2610.25287v1#S3.F1.3) [S17](https://arxiv.org/html/2610.25287v1#S3.p3.1)。最强模型平均阶段得分45%–48%，主要来自局部进展，并非同等比例的完整成功[S22](https://arxiv.org/html/2610.25287v1#S4.p3.1)。摘要按2026年7月至9月的结果估计得分翻倍时间44.5天、最佳执行率提高4.4倍、最低成本下降6.2倍；这些是短期观测趋势。

## 局限

作者明确指出动作预算影响完成率，扶瓶还受工作空间与姿态限制[S23](https://arxiv.org/html/2610.25287v1#S4.p6.1) [S27](https://arxiv.org/html/2610.25287v1#S4.p10.1)。评分取曾经达到的最高进展，即使后来撤销成果仍保留分数，且由模型依据录像评分[S21](https://arxiv.org/html/2610.25287v1#S3.p7.1)；我的待核查问题是人工复核一致性。跨发布日期的增长不能证明规模扩张造成进步，更不能推出将持续指数增长或胜过专用策略。

- **判断**：值得细读评测协议和失败轨迹；标题里的长期判断应当作为待验证假设，当前证据更适合说明能力与效率的实际边界。

## 研究关联

值得借鉴的是把失败尝试也计入每项有效进展的时间与成本：模型能偶尔完成一个动作，不代表它能经济地完成任务。定位、验证抓取和错误恢复应当与语言推理能力分开观察。

### 下一步读哪里

先看[S18](https://arxiv.org/html/2610.25287v1#S3.p4.1) [S19](https://arxiv.org/html/2610.25287v1#S3.p5.1) [S20](https://arxiv.org/html/2610.25287v1#S3.p6.1) [S21](https://arxiv.org/html/2610.25287v1#S3.p7.1)弄清谁生成动作、谁执行、谁评分，再看[S24](https://arxiv.org/html/2610.25287v1#S4.p7.1) [S25](https://arxiv.org/html/2610.25287v1#S4.p8.1) [S26](https://arxiv.org/html/2610.25287v1#S4.p9.1) [S27](https://arxiv.org/html/2610.25287v1#S4.p10.1)定位失败原因。下一步核查得分增长拟合的不确定性、人工评分复核，以及最终状态成功率与最高阶段得分的差异。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.25287v1
- 获取时间：2026-10-21T00:33:51.231748+00:00
- [S1] [The Bitter Lesson Comes to Robotics · 正文段落 1](https://arxiv.org/html/2610.25287v1#abstract1.1)
- [S2] [The Bitter Lesson Comes to Robotics · 正文段落 2](https://arxiv.org/html/2610.25287v1#p2.1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.25287v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.25287v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.25287v1#S1.p3.1)
- [S6] [2 Related Work · 正文段落 7](https://arxiv.org/html/2610.25287v1#S2.p1.1)
- [S7] [2 Related Work · 正文段落 8](https://arxiv.org/html/2610.25287v1#S2.p2.1)
- [S8] [2 Related Work · 正文段落 9](https://arxiv.org/html/2610.25287v1#S2.p3.1)
- [S9] [2 Related Work · 正文段落 10](https://arxiv.org/html/2610.25287v1#S2.p4.1)
- [S10] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.25287v1#S2.p5.1)
- [S11] [3 Methodology · 正文段落 13](https://arxiv.org/html/2610.25287v1#S3.F1.2.1)
- [S12] [3 Methodology · 正文段落 14](https://arxiv.org/html/2610.25287v1#S3.F1.2.2)
- [S13] [3 Methodology · 正文段落 15](https://arxiv.org/html/2610.25287v1#S3.F1.3)
- [S14] [3 Methodology · 正文段落 16](https://arxiv.org/html/2610.25287v1#S3.F1)
- [S15] [3 Methodology · 正文段落 17](https://arxiv.org/html/2610.25287v1#S3.p1.1)
- [S16] [3 Methodology · 正文段落 18](https://arxiv.org/html/2610.25287v1#S3.p2.1)
- [S17] [3 Methodology · 正文段落 19](https://arxiv.org/html/2610.25287v1#S3.p3.1)
- [S18] [3 Methodology · 正文段落 20](https://arxiv.org/html/2610.25287v1#S3.p4.1)
- [S19] [3 Methodology · 正文段落 21](https://arxiv.org/html/2610.25287v1#S3.p5.1)
- [S20] [3 Methodology · 正文段落 22](https://arxiv.org/html/2610.25287v1#S3.p6.1)
- [S21] [3 Methodology · 正文段落 23](https://arxiv.org/html/2610.25287v1#S3.p7.1)
- [S22] [4 Evaluating Task Performance · 正文段落 28](https://arxiv.org/html/2610.25287v1#S4.p3.1)
- [S23] [4 Evaluating Task Performance · 正文段落 31](https://arxiv.org/html/2610.25287v1#S4.p6.1)
- [S24] [4 Evaluating Task Performance · 正文段落 32](https://arxiv.org/html/2610.25287v1#S4.p7.1)
- [S25] [4 Evaluating Task Performance · 正文段落 34](https://arxiv.org/html/2610.25287v1#S4.p8.1)
- [S26] [4 Evaluating Task Performance · 正文段落 35](https://arxiv.org/html/2610.25287v1#S4.p9.1)
- [S27] [4 Evaluating Task Performance · 正文段落 36](https://arxiv.org/html/2610.25287v1#S4.p10.1)
- [S28] [4 Evaluating Task Performance · 正文段落 38](https://arxiv.org/html/2610.25287v1#S4.p11.1)
- [S29] [5 Evaluating Subtask Completion Rate and Inference Cost · 正文段落 39](https://arxiv.org/html/2610.25287v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/The Bitter Lesson Comes to Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General purpose multimodal language models (LMs) are increasingly capable of directly controlling robotic arms (e.g., by commanding end effector poses) to manipulate their environment. Tracking the development of these capabilities is important for understanding their potential benefits, such as improving industrial automation, and risks, such as enabling malicious users to produce dangerous chemical or biological agents. To this end, we investigate the ability of frontier multimodal LMs to directly control physical robotic arms. We evaluate seven models at multiple reasoning-effort settings on six manipulation tasks taken from the RoboDojo benchmark. To our knowledge, this is the first systematic comparison of a broad range of frontier LMs across a common suite of manipulation tasks on physical hardware. We find that current frontier models can directly control real robotic arms to perform a variety of manipulation tasks but are not yet precise or efficient enough to complete them within a practical action budget. However, these capabilities are improving rapidly: performance increases on our benchmark between July and September 2026 (inclusive) correspond to a performance doubling time of 44.5 days, while the best recorded execution rate increased by a factor of 4.4 and the lowest recorded execution cost fell by a factor of 6.2. These trends raise the possibility that the Bitter Lesson is coming to robotics; the capabilities of embodied general purpose LMs may one day be comparable to those of more specialized models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25287v1
- Authors: Christopher Leet, Achyutha Menon, Sravanthi Machcha, Sven Koenig, Tzu Kit Chan, Jay Chooi
- Published: 2026-10-18T14:07:36Z
- Age days: 2

</details>
