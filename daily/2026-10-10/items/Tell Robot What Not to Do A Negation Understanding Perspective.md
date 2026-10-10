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
url: "https://arxiv.org/abs/2610.11952v1"
published: "2026-10-08T13:39:08Z"
age_days: 1
score: 38
created: 2026-10-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Tell Robot What Not to Do: A Negation Understanding Perspective

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> NegaAlign 让已经会操作的 VLA 学会“做这件事，但排除那个对象或结果”。它用允许行为的肯定指令作老师，修正否定指令对应的语言和视觉表示，只训练少量插入层。

## 问题

机器人既要完成任务，又要遵守排除条件，例如递工具但不能递刀。肯定指令训练的模型可能抓住“刀”等显眼内容，却忽略排除关系；单纯图文否定理解方法又不直接解决动作落地。额外高层改写增加推理计算，重新采集否定操作示范则成本高 [S4](https://arxiv.org/html/2610.11952v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入汉堡、薯条和薯片的图像及“放一种食物到盘里，但不要薯片”。训练时以汉堡、薯条的肯定指令提供允许关系，以薯片指令提供排除关系；部署修正表示后，原动作生成器输出选择合法食物并放盘的动作。

## 创新点或方法

旧做法直接补充否定动作数据，或让另一个模型把指令改写成肯定句；NegaAlign 从已有肯定示范和手写否定指令构造关系：哪些肯定操作允许、哪个被排除。插入的 Negation Transformation Layers 修改中间语言表示，教师引导视觉对齐把允许指令的动作相关视觉定位传给否定指令 [S5](https://arxiv.org/html/2610.11952v1#S1.p3.1) [S18](https://arxiv.org/html/2610.11952v1#S3.SS2.p1.1)。先正常训练肯定技能，再冻结骨干和动作生成器，仅用图像语言监督训练插入层 [S19](https://arxiv.org/html/2610.11952v1#S3.SS5.p1.1)。部署由改过表示的原 VLA 输出动作；节选未展开插入层及视觉对齐的具体计算。

### 方法如何工作

1. 先用肯定示范训练目标操作，使原策略具备执行合法选择的能力。
2. 为否定指令列出允许的肯定解释和被排除解释，得到无需新增动作轨迹的关系监督。
3. 插入层修正语言表示，并借教师引导对齐相关视觉 token，让排除关系影响动作所读取的信息。
4. 冻结原骨干与动作生成器，只更新插入层；具体对齐和门控计算在所给节选中未说明。
5. 部署输入否定指令和当前画面，经修正表示驱动原动作生成器，评测同时检查完成目标与遵守约束。

### 必要术语

- 允许的肯定解释：满足否定约束的具体正向命令；本文把它作为监督来源。
- 视觉 token：模型内部表示图像内容的单元；本文让相关单元承接否定语义。
- 教师引导视觉对齐：让否定输入下的视觉表示向合法肯定输入的表示学习；本文用它连接语言修正与动作生成。

## 证据

NegaBench 是 RoboTwin 仿真中的十场景、五类约束，成功同时要求完成任务和不违反排除条件 [S23](https://arxiv.org/html/2610.11952v1#S3.SS6.p1.1) [S24](https://arxiv.org/html/2610.11952v1#S4.SS1.p1.1)。π₀.₅ 否定成功率从2.60%升至88.45%，肯定成功率92.77%变为92.51%；直接用否定轨迹训练为88.60%，外部 Qwen 改写为55.70% [S26](https://arxiv.org/html/2610.11952v1#S4.T1.4.1)。NegaAlign 在 GR00T、π₀ 上也改善，但否定成绩57.75%、63.30%低于直接轨迹训练的68.85%、71.25%。摘要报告 π₀.₅ 真机12.4%升至88.8%，但没有给出真机任务、试验次数及协议，证据范围需保留。

## 局限

作者明确依赖已有 VLA 能力，复杂或歧义否定指令可能退化 [S33](https://arxiv.org/html/2610.11952v1#S5.p2.1)。本文目标是适配给定的否定指令及关系 [S15](https://arxiv.org/html/2610.11952v1#S3.SS1.p1.1)，不能自动推成任意未见否定表达都有效。我的待核查问题是指令模板、对象和约束组合如何划分训练测试，以及视觉对齐消融是否排除模板记忆。高成功率也不是不违反约束的保证。

- **判断**：值得读到监督关系构造与视觉对齐消融：它展示了低成本复用肯定技能的路径，但适用范围取决于技能覆盖和未见约束测试。

## 研究关联

如果机器人已经会执行允许的肯定操作，约束适配可以先尝试改变“它看中了什么”，而不必重学动作。关键条件是已有技能覆盖合法选项，并且能构造可信的允许与排除关系；这不是让模型凭空获得新技能。

### 下一步读哪里

核查 NTL 插入位置、门控与教师视觉 token 的筛选方式，不能仅凭 [S20](https://arxiv.org/html/2610.11952v1#S3.E9) 的损失名称猜公式。查看 [S32](https://arxiv.org/html/2610.11952v1#S4.T2) 所指消融的实际结果，并检查 [S23](https://arxiv.org/html/2610.11952v1#S3.SS6.p1.1) 的配对指令及训练测试关系；真机成绩还需核查场景、次数和约束判据。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.11952v1
- 获取时间：2026-10-10T00:24:48.980108+00:00
- [S1] [Tell Robot What Not to Do: A Negation Understanding Perspective · 正文段落 1](https://arxiv.org/html/2610.11952v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.11952v1#S1.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.11952v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.11952v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.11952v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.11952v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.11952v1#S1.I1.i2)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.11952v1#S1.I1.i3)
- [S9] [2.1 Negation in Language, Vision, and Action · 正文段落 10](https://arxiv.org/html/2610.11952v1#S2.SS1.p1.1)
- [S10] [2.1 Negation in Language, Vision, and Action · 正文段落 11](https://arxiv.org/html/2610.11952v1#S2.SS1.p2.1)
- [S11] [2.2 Language Conditioning and Instruction Following in VLAs · 正文段落 12](https://arxiv.org/html/2610.11952v1#S2.SS2.p1.1)
- [S12] [2.2 Language Conditioning and Instruction Following in VLAs · 正文段落 13](https://arxiv.org/html/2610.11952v1#S2.SS2.p2.1)
- [S13] [3 Method · 正文段落 14](https://arxiv.org/html/2610.11952v1#S3.F2)
- [S14] [3 Method · 正文段落 15](https://arxiv.org/html/2610.11952v1#S3.p1.1)
- [S15] [3.1 Problem Formulation · 正文段落 16](https://arxiv.org/html/2610.11952v1#S3.SS1.p1.1)
- [S16] [3.1 Problem Formulation · 正文段落 17](https://arxiv.org/html/2610.11952v1#S3.SS1.p2.1)
- [S17] [3.1 Problem Formulation · 正文段落 19](https://arxiv.org/html/2610.11952v1#S3.SS1.p3.1)
- [S18] [3.2 Negation Supervision Construction · 正文段落 22](https://arxiv.org/html/2610.11952v1#S3.SS2.p1.1)
- [S19] [3.5 Training Recipe · 正文段落 37](https://arxiv.org/html/2610.11952v1#S3.SS5.p1.1)
- [S20] [3.5 Training Recipe · 正文段落 38](https://arxiv.org/html/2610.11952v1#S3.E9)
- [S21] [3.5 Training Recipe · 正文段落 39](https://arxiv.org/html/2610.11952v1#S3.SS5.p1.2)
- [S22] [3.5 Training Recipe · 正文段落 40](https://arxiv.org/html/2610.11952v1#S3.F3)
- [S23] [3.6 Negation Instruction Following Benchmark Construction · 正文段落 41](https://arxiv.org/html/2610.11952v1#S3.SS6.p1.1)
- [S24] [4.1 Experimental Setup and Evaluation Metrics · 正文段落 42](https://arxiv.org/html/2610.11952v1#S4.SS1.p1.1)
- [S25] [4.1 Experimental Setup and Evaluation Metrics · 正文段落 43](https://arxiv.org/html/2610.11952v1#S4.T1)
- [S26] [4.1 Experimental Setup and Evaluation Metrics · 正文段落 44](https://arxiv.org/html/2610.11952v1#S4.T1.4.1)
- [S27] [4.1 Experimental Setup and Evaluation Metrics · 正文段落 45](https://arxiv.org/html/2610.11952v1#S4.F4)
- [S28] [4.2 Comparison Results on NegaBench · 正文段落 46](https://arxiv.org/html/2610.11952v1#S4.SS2.p1.1)
- [S29] [4.2 Comparison Results on NegaBench · 正文段落 47](https://arxiv.org/html/2610.11952v1#S4.SS2.p2.1)
- [S30] [4.2 Comparison Results on NegaBench · 正文段落 48](https://arxiv.org/html/2610.11952v1#S4.SS2.p3.1)
- [S31] [4.3 Ablation Studies and Mechanism Analysis · 正文段落 49](https://arxiv.org/html/2610.11952v1#S4.F5)
- [S32] [4.3 Ablation Studies and Mechanism Analysis · 正文段落 50](https://arxiv.org/html/2610.11952v1#S4.T2)
- [S33] [5 Conclusion · 正文段落 61](https://arxiv.org/html/2610.11952v1#S5.p2.1)
- [S34] [Precision. · 正文段落 96](https://arxiv.org/html/2610.11952v1#A1.T5)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/Tell Robot What Not to Do A Negation Understanding Perspective.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-play framework that extends pretrained VLAs to follow negated instructions through image-language supervision alone. Specifically, we introduce Negation Transformation Layers into selected layers of the vision-language backbone to reshape intermediate instruction representations. Meanwhile, a teacher-guided alignment mechanism is designed to align instruction-relevant visual tokens, transferring action-relevant grounding from instructions that satisfy the negated constraint. The training phase uses supervision constructed from existing demonstrations and updates only the inserted layers, keeping all pretrained parameters frozen, including the action generator. We further introduce NegaBench, a simulation benchmark spanning 10 scenarios across five domains for systematically evaluating manipulation under negated constraints. Experiments across GR00T, $π_0$, and $π_{0.5}$ demonstrate consistent improvements in negated instruction following. With 11.6M trainable parameters, NegaAlign increases the negated-instruction success rate of $π_{0.5}$ from 2.60% to 88.45% on NegaBench and from 12.4% to 88.8% on real-world tasks, while retaining performance on affirmative instructions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11952v1
- Authors: Fazeng Li, Gan Sun, Hao Cheng, Weihong Ren, Yang Cong
- Published: 2026-10-08T13:39:08Z
- Age days: 1

</details>
