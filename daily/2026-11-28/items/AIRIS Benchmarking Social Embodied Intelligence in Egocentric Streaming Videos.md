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
url: "https://arxiv.org/abs/2611.34347v1"
published: "2026-11-25T13:18:30Z"
age_days: 2
score: 26
created: 2026-11-28
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> AIRIS 用第一视角视频测试模型能否看懂社交线索、等到证据足够，再选对什么时候介入和怎么回应。它在同一段互动的多个时间点提问，每次只给当时能看到、听到的信息。

## 问题

看完视频后猜对一个人的意图，无法说明当时就有足够证据做判断。分别测试目光识别、意图识别和反应选择，也会漏掉一种失败：模型每项都能答对一些题，却在同一次互动里把介入时机和具体回应配错。[S3](https://arxiv.org/html/2611.34347v1#S1.p1.1)–[S5](https://arxiv.org/html/2611.34347v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）。第一视角画面里，一位顾客看向高处货架。此时输入只有目光和货架，意图题可以输出“证据不足”。顾客随后指向蓝盒并请你帮忙，模型才有依据识别请求，并选择确认是哪盒、再取下递给对方的回应。

## 创新点或方法

作者给片段标出线索出现、意图开始可推断、第一视角一方开始回应、互动结束四个时间点。标注员和专家审核线索、解释和可接受的回答，再生成并逐题检查问题。测评采用零样本推理。模型在查询时只看到截至当时的片段；意图可推断时点之前的题把“证据不足”设为正确答案，结局题才看到互动结束。回应既按各子决策给分，也检查是否介入、行动类型和具体回应能否同时答对。[S6](https://arxiv.org/html/2611.34347v1#S1.p4.1)[S12](https://arxiv.org/html/2611.34347v1#S2.SS2.p5.1)–[S16](https://arxiv.org/html/2611.34347v1#S2.SS3.p3.1)[S21](https://arxiv.org/html/2611.34347v1#S3.SS1.p2.1)

### 方法如何工作

1. 给同一段互动标注线索、可推断意图、回应和结局的时间点，为不同决策指定可用证据。
2. 按查询时刻截断输入，在线索刚出现时允许回答证据不足，让提前猜测能被计量。
3. 逐项测线索、意图和回应，并在同一事件上检查多个回应决定能否同时成立。
4. 结合互动结局和规范判断，定位错误出现在看漏线索、过早判断，还是回应不完整。

### 必要术语

- 观察前缀：从视频开始到提问时刻的可用信息；限制模型只能依据当时的证据。
- 过早承诺率（FCR）：证据不足时仍给出具体意图的比例；用于衡量模型有多常提前下判断。
- 严格联合匹配（Joint-EM）：同一事件的介入决定、行动域、子动作及适用的言语功能都答对才计分；用于检验整套回应是否一致。

## 证据

评测比较 45 个通用、具身、流式视频和全模态模型，在 357 段第一视角片段上回答 8,000 道题 [S6](https://arxiv.org/html/2611.34347v1#S1.p4.1)[S20](https://arxiv.org/html/2611.34347v1#S3.SS1.p1.1)[S21](https://arxiv.org/html/2611.34347v1#S3.SS1.p2.1)。Gemini-3.7-Flash 在证据不足时仍有 42% 的查询给出具体意图 [S24](https://arxiv.org/html/2611.34347v1#S3.SS2.p3.1)。HY-Embodied-VLM-1.0 的回应分项汇总为 0.688，严格联合得分只有 0.028，所有模型的联合得分都未超过 0.147 [S25](https://arxiv.org/html/2611.34347v1#S3.SS2.p4.1)。这说明在这套视频问答里，看懂线索、选对单项回应与完整答对同一事件之间存在明显差距。

## 局限

作者把开放式生成和真机进入互动列为后续工作 [S30](https://arxiv.org/html/2611.34347v1#S4.p3.1)。当前结果来自预录视频，其中全模态模型听原声，标准 VLM 读转录 [S21](https://arxiv.org/html/2611.34347v1#S3.SS1.p2.1)。我会核查意图可推断时点的标注分歧和输入差异是否影响排名。这里的“因果”指输入按时间截断，模型间差异无法单独归因于具身训练或流式架构。

- **判断**：值得读到时间标注和严格联合评分，因为它们把“猜得过早”和“局部答对、整体配错”变成了可单独检查的错误。

## 研究关联

评估会主动介入的智能体，可以在同一事件的早晚阶段分别发问，并给恰当等待记分。再对同一次回应做联合评分，才能看出模型是否把几个各自合理的答案拼成了时机和内容都合适的行动。

### 下一步读哪里

先看 [S12](https://arxiv.org/html/2611.34347v1#S2.SS2.p5.1)–[S14](https://arxiv.org/html/2611.34347v1#S2.SS2.p7.1) 怎样裁定证据充足的时间点，再对照 [S16](https://arxiv.org/html/2611.34347v1#S2.SS3.p3.1)[S24](https://arxiv.org/html/2611.34347v1#S3.SS2.p3.1)[S25](https://arxiv.org/html/2611.34347v1#S3.SS2.p4.1)。重点核查同一事件有多种合理回应时，专家如何设答案，以及严格联合匹配怎样处理这些答案。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34347v1
- 获取时间：2026-11-28T03:58:19.758518+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.34347v1#p1.2)
- [S2] [AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos · 正文段落 2](https://arxiv.org/html/2611.34347v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34347v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34347v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34347v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.34347v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.34347v1#S1.I1.i2)
- [S8] [2.2 Dataset Construction · 正文段落 26](https://arxiv.org/html/2611.34347v1#S2.SS2.p1.1)
- [S9] [2.2 Dataset Construction · 正文段落 27](https://arxiv.org/html/2611.34347v1#S2.SS2.p2.1)
- [S10] [2.2 Dataset Construction · 正文段落 28](https://arxiv.org/html/2611.34347v1#S2.SS2.p3.1)
- [S11] [2.2 Dataset Construction · 正文段落 29](https://arxiv.org/html/2611.34347v1#S2.SS2.p4.1)
- [S12] [2.2 Dataset Construction · 正文段落 30](https://arxiv.org/html/2611.34347v1#S2.SS2.p5.1)
- [S13] [2.2 Dataset Construction · 正文段落 31](https://arxiv.org/html/2611.34347v1#S2.SS2.p6.1)
- [S14] [2.2 Dataset Construction · 正文段落 32](https://arxiv.org/html/2611.34347v1#S2.SS2.p7.1)
- [S15] [2.2 Dataset Construction · 正文段落 33](https://arxiv.org/html/2611.34347v1#S2.F3)
- [S16] [2.3 Evaluation Protocol and Metrics · 正文段落 41](https://arxiv.org/html/2611.34347v1#S2.SS3.p3.1)
- [S17] [2.4 Benchmark Statistics · 正文段落 45](https://arxiv.org/html/2611.34347v1#S2.SS4.p1.1)
- [S18] [2.4 Benchmark Statistics · 正文段落 46](https://arxiv.org/html/2611.34347v1#S2.SS4.p2.1)
- [S19] [3 Experiments · 正文段落 48](https://arxiv.org/html/2611.34347v1#S3.F4)
- [S20] [3.1 Experimental Setup · 正文段落 49](https://arxiv.org/html/2611.34347v1#S3.SS1.p1.1)
- [S21] [3.1 Experimental Setup · 正文段落 50](https://arxiv.org/html/2611.34347v1#S3.SS1.p2.1)
- [S22] [3.2 Experimental Results and Insights · 正文段落 51](https://arxiv.org/html/2611.34347v1#S3.SS2.p1.1)
- [S23] [3.2 Experimental Results and Insights · 正文段落 52](https://arxiv.org/html/2611.34347v1#S3.SS2.p2.1)
- [S24] [3.2 Experimental Results and Insights · 正文段落 53](https://arxiv.org/html/2611.34347v1#S3.SS2.p3.1)
- [S25] [3.2 Experimental Results and Insights · 正文段落 54](https://arxiv.org/html/2611.34347v1#S3.SS2.p4.1)
- [S26] [3.2 Experimental Results and Insights · 正文段落 55](https://arxiv.org/html/2611.34347v1#S3.SS2.p5.1)
- [S27] [3.2 Experimental Results and Insights · 正文段落 56](https://arxiv.org/html/2611.34347v1#S3.SS2.p6.1)
- [S28] [3.2 Experimental Results and Insights · 正文段落 57](https://arxiv.org/html/2611.34347v1#S3.F5)
- [S29] [3.2 Experimental Results and Insights · 正文段落 58](https://arxiv.org/html/2611.34347v1#S3.SS2.p7.1)
- [S30] [4 Conclusion · 正文段落 61](https://arxiv.org/html/2611.34347v1#S4.p3.1)
- [S31] [Supplementary Material · 正文段落 73](https://arxiv.org/html/2611.34347v1#Ax1.p12.1)
- [S32] [C.2 Supplementary Evaluation Protocol and Metrics · 正文段落 120](https://arxiv.org/html/2611.34347v1#Ax1.I4.i3)
- [S33] [C.4 Expert Annotation and Audit Process · 正文段落 125](https://arxiv.org/html/2611.34347v1#Ax1.SS3.SSS4.p1.1)
- [S34] [D.1 Model evaluation pool · 正文段落 138](https://arxiv.org/html/2611.34347v1#Ax1.I6.i5)
- [S35] [D.1 Model evaluation pool · 正文段落 143](https://arxiv.org/html/2611.34347v1#Ax1.I6.i10)
- [S36] [D.1 Model evaluation pool · 正文段落 147](https://arxiv.org/html/2611.34347v1#Ax1.I6.i14)
- [S37] [D.1 Model evaluation pool · 正文段落 169](https://arxiv.org/html/2611.34347v1#Ax1.I9.i4)
- [S38] [D.1 Model evaluation pool · 正文段落 170](https://arxiv.org/html/2611.34347v1#Ax1.I9.i5)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/AIRIS Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that formulates social embodied intelligence as a time-anchored chain of Attention, Intention, Reaction, and Interaction (A-I-R-I). AIRIS contains 8,000 expert-curated questions grounded in 357 egocentric clips across 11 context categories and 36 capability dimensions. At each query, models receive only the observation prefix available at that time; decision-aware metrics reward calibrated waiting and complete reactions while penalizing premature commitment. Evaluating 45 proprietary and open-source general-purpose, embodied, streaming-video, and omni-modal models reveals fragmented and temporally miscalibrated competence. General-purpose VLMs excel at passive cue grounding and intent recognition, whereas embodied specialists lead on isolated reaction sub-decisions; yet across all families, models frequently guess intents before sufficient evidence emerges and fail to jointly align intervention timing, action domain, and concrete execution within the same episode. AIRIS thus provides a diagnostic foundation for bridging the gap between passive social perception and reliable embodied interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34347v1
- Authors: Yuchen Zhou, Hongsheng Wu, Jiayu Tang, Yunxuan Mao, Hanjing Ye, Shenghao Zhang, Jing Tang, Chun-Kai Fan, Yufei Huang, Yonggen Ling, He Zhang
- Published: 2026-11-25T13:18:30Z
- Age days: 2

</details>
