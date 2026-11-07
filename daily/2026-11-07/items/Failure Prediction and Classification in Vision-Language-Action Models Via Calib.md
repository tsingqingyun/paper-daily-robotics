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
url: "https://arxiv.org/abs/2611.08425v1"
published: "2026-11-05T18:21:07Z"
age_days: 1
score: 38
created: 2026-11-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VLA-Tug 在机器人策略的内部表示上训练小探针，提前判断会不会失败、可能怎样失败。关键改动是学习失败发生前的信号，并同时校准误报和提前检出要求。

## 问题

任务不是判断一段操作最终是否失败，而是在失败前及时报警，给干预留下机会。既有方法常用整段失败标签，容易学到事故已发生的特征；只控制误报率，也可能得到几乎不报警、却大量漏检的监控器。[S8](https://arxiv.org/html/2611.08425v1#S1.p3.1) [S17](https://arxiv.org/html/2611.08425v1#S2.SS0.SSS0.Px1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：机器人准备夹取杯子，探针读取当前内部表示，发现高风险并给出“抓取”等候选类型；若超过校准阈值，系统暂停或调用重试策略。输出是干预依据，不是已经保证杯子不会掉落。

## 创新点或方法

旧做法混用失败前后表示或只校准一个指标；本文在失败时刻截断训练片段，排除失败后的表示，结合失败类型标签训练探针。[S28](https://arxiv.org/html/2611.08425v1#S4.SS1.SSS0.Px3.p1.1) [S44](https://arxiv.org/html/2611.08425v1#A1.SS1.SSS0.Px4.p1.1) 随后用 Learn-then-Test 检验阈值能否同时满足 FPR 和提前 TPR；不满足时可以拒绝认证。推理读取现成骨干表示，输出风险和类型，达到阈值才触发干预；节选未完整展示探针层结构。

### 方法如何工作

1. 收集成功与失败轨迹的骨干表示，并标注失败时刻和类型，让预警有时间参照。[S22](https://arxiv.org/html/2611.08425v1#S3.SS2.p1.1)
2. 排除失败后片段，以失败前表示训练风险和类型预测，减少事后识别捷径。[S28](https://arxiv.org/html/2611.08425v1#S4.SS1.SSS0.Px3.p1.1) [S44](https://arxiv.org/html/2611.08425v1#A1.SS1.SSS0.Px4.p1.1)
3. 在独立校准集检验候选阈值的误报与提前检出要求，不达标就不认证。[S18](https://arxiv.org/html/2611.08425v1#S2.SS0.SSS0.Px2.p1.1) [S35](https://arxiv.org/html/2611.08425v1#S6.I1.i2)
4. 运行时逐步读取表示并报警，把候选失败类型交给干预策略；检测与纠正效果须分别验证。[S40](https://arxiv.org/html/2611.08425v1#S6.SS3.p3.1) [S42](https://arxiv.org/html/2611.08425v1#S7.p1.1)

### 必要术语

- 潜表示探针：读取模型内部特征的小预测器；本文复用策略计算，避免另建大型监视模型。
- 提前 TPR：失败发生前或当时成功报警的失败比例；本文用它区分预警和事后识别。
- Learn-then-Test：学习候选方案后用统计检验筛选；本文用来联合检查报警阈值的多个要求。

## 证据

研究覆盖两个 VLA、两个仿真环境的 228 个任务及 8 个真机任务。[S10](https://arxiv.org/html/2611.08425v1#S1.p5.1) 未见任务六种设置中四种领先；相对 SAFE-LSTM，提前检测曲线面积在 new-task 为 −1%，new-skill 为 +30%，并非全面领先。[S32](https://arxiv.org/html/2611.08425v1#S6.F5) [S33](https://arxiv.org/html/2611.08425v1#S6.SS1.SSS0.Px4.p1.1) 已见任务所有获认证运行满足双目标；未见任务中 FPR、提前 TPR 目标分别在 40–86%、57–90% 的运行成立。[S34](https://arxiv.org/html/2611.08425v1#S6.I1.i1) 探针每步低于 1 毫秒。[S11](https://arxiv.org/html/2611.08425v1#S1.I1.i1)

## 局限

作者明确说明，任务变化破坏校准集与新样本的可交换性，因此未见任务上的表现只是经验结果；上述比例来自 14 次运行，不是精确保障概率。[S37](https://arxiv.org/html/2611.08425v1#S6.SS2.p3.1) 我的待核查问题是失败时刻标注是否足够一致，以及报警提前量能否覆盖真实干预延迟；节选也未给干预成功率的完整数字。

- **判断**：值得读到标签定义、校准拒绝条件和逐设置结果；它对“报警是否来得及”的处理，比摘要中的最高提升更值得关注。

## 研究关联

最值得借鉴的是把监督标签对准介入时机：如果目标是预防事故，就要用事故之前的证据训练和评估。另一个实用点是允许校准回答“现有模型无法满足要求”，而不是强行给出一个看似可靠的阈值。

### 下一步读哪里

先读 [S28](https://arxiv.org/html/2611.08425v1#S4.SS1.SSS0.Px3.p1.1) 四种标签策略，再核查提前检测曲线的定义与窗口。[S35](https://arxiv.org/html/2611.08425v1#S6.I1.i2) 的拒绝认证次数不可跳过；还应检查校准数据划分、置信水平，以及 [S45](https://arxiv.org/html/2611.08425v1#A1.SS3.SSS0.Px5.p1.1) 不同基线所用校准器的比较关系。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.08425v1
- 获取时间：2026-11-07T03:39:41.794647+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.08425v1#p1.1)
- [S2] [正文 · 正文段落 2](https://arxiv.org/html/2611.08425v1#p2.1)
- [S3] [正文 · 正文段落 3](https://arxiv.org/html/2611.08425v1#p3.1)
- [S4] [正文 · 正文段落 4](https://arxiv.org/html/2611.08425v1#p4.1)
- [S5] [正文 · 正文段落 8](https://arxiv.org/html/2611.08425v1#abstract1.1)
- [S6] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.08425v1#S1.p1.1)
- [S7] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.08425v1#S1.p2.1)
- [S8] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.08425v1#S1.p3.1)
- [S9] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.08425v1#S1.p4.1)
- [S10] [1 Introduction · 正文段落 13](https://arxiv.org/html/2611.08425v1#S1.p5.1)
- [S11] [1 Introduction · 正文段落 14](https://arxiv.org/html/2611.08425v1#S1.I1.i1)
- [S12] [1 Introduction · 正文段落 15](https://arxiv.org/html/2611.08425v1#S1.I1.i2)
- [S13] [1 Introduction · 正文段落 16](https://arxiv.org/html/2611.08425v1#S1.I1.i3)
- [S14] [1 Introduction · 正文段落 17](https://arxiv.org/html/2611.08425v1#S1.I1.i4)
- [S15] [2 Related Work · 正文段落 18](https://arxiv.org/html/2611.08425v1#S2.p1.1)
- [S16] [Existing works and their limitations. · 正文段落 19](https://arxiv.org/html/2611.08425v1#S2.SS0.SSS0.Px1.p1.1)
- [S17] [Existing works and their limitations. · 正文段落 20](https://arxiv.org/html/2611.08425v1#S2.SS0.SSS0.Px1.p2.1)
- [S18] [VLA-Tug addresses the limitations. · 正文段落 21](https://arxiv.org/html/2611.08425v1#S2.SS0.SSS0.Px2.p1.1)
- [S19] [VLA-Tug addresses the limitations. · 正文段落 22](https://arxiv.org/html/2611.08425v1#S2.T1)
- [S20] [VLA-Tug addresses the limitations. · 正文段落 24](https://arxiv.org/html/2611.08425v1#S2.T1.5)
- [S21] [3.1 Definitions · 正文段落 26](https://arxiv.org/html/2611.08425v1#S3.SS1.p1.1)
- [S22] [3.2 Problem Formulation · 正文段落 33](https://arxiv.org/html/2611.08425v1#S3.SS2.p1.1)
- [S23] [3.2 Problem Formulation · 正文段落 34](https://arxiv.org/html/2611.08425v1#S3.SS2.p2.1)
- [S24] [3.2 Problem Formulation · 正文段落 35](https://arxiv.org/html/2611.08425v1#S3.SS2.p3.1)
- [S25] [3.2 Problem Formulation · 正文段落 36](https://arxiv.org/html/2611.08425v1#S3.SS2.p4.1)
- [S26] [3.2 Problem Formulation · 正文段落 39](https://arxiv.org/html/2611.08425v1#S3.SS2.p7.1)
- [S27] [4 Methodology · 正文段落 40](https://arxiv.org/html/2611.08425v1#S4.p1.1)
- [S28] [We train the probe to predict features that precede a failure. · 正文段落 44](https://arxiv.org/html/2611.08425v1#S4.SS1.SSS0.Px3.p1.1)
- [S29] [We train the probe to predict features that precede a failure. · 正文段落 45](https://arxiv.org/html/2611.08425v1#S4.F2)
- [S30] [6 Experimental Results · 正文段落 74](https://arxiv.org/html/2611.08425v1#S6.p1.1)
- [S31] [6.1 Failure Detection and Timeliness Evaluation · 正文段落 75](https://arxiv.org/html/2611.08425v1#S6.SS1.p1.1)
- [S32] [Results and Discussion. · 正文段落 83](https://arxiv.org/html/2611.08425v1#S6.F5)
- [S33] [Results and Discussion. · 正文段落 84](https://arxiv.org/html/2611.08425v1#S6.SS1.SSS0.Px4.p1.1)
- [S34] [6.2 Calibration Evaluation · 正文段落 87](https://arxiv.org/html/2611.08425v1#S6.I1.i1)
- [S35] [6.2 Calibration Evaluation · 正文段落 88](https://arxiv.org/html/2611.08425v1#S6.I1.i2)
- [S36] [6.2 Calibration Evaluation · 正文段落 89](https://arxiv.org/html/2611.08425v1#S6.I1.i3)
- [S37] [6.2 Calibration Evaluation · 正文段落 90](https://arxiv.org/html/2611.08425v1#S6.SS2.p3.1)
- [S38] [6.3 Evaluation of Informativeness · 正文段落 92](https://arxiv.org/html/2611.08425v1#S6.SS3.p1.1)
- [S39] [6.3 Evaluation of Informativeness · 正文段落 93](https://arxiv.org/html/2611.08425v1#S6.SS3.p2.1)
- [S40] [6.3 Evaluation of Informativeness · 正文段落 94](https://arxiv.org/html/2611.08425v1#S6.SS3.p3.1)
- [S41] [Training. · 正文段落 101](https://arxiv.org/html/2611.08425v1#S6.SS4.SSS0.Px2.p1.1)
- [S42] [7 Conclusion · 正文段落 111](https://arxiv.org/html/2611.08425v1#S7.p1.1)
- [S43] [Appendix A Method Details · 正文段落 114](https://arxiv.org/html/2611.08425v1#A1.p1.1)
- [S44] [Loss and training. · 正文段落 118](https://arxiv.org/html/2611.08425v1#A1.SS1.SSS0.Px4.p1.1)
- [S45] [Which method gets which calibrator. · 正文段落 127](https://arxiv.org/html/2611.08425v1#A1.SS3.SSS0.Px5.p1.1)
- [S46] [C.3 Full Results · 正文段落 148](https://arxiv.org/html/2611.08425v1#A3.SS3.p1.1)
- [S47] [C.3 Full Results · 正文段落 149](https://arxiv.org/html/2611.08425v1#A3.T6)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/Failure Prediction and Classification in Vision-Language-Action Models Via Calib.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people. Deploying VLAs in real-world systems therefore requires a runtime monitor that is timely, calibrated, and informative while being efficient enough to run on the edge. Existing methods fail to fulfill these requirements. We present VLA-Tug, a lightweight probe over the latent layers of a VLA backbone that improves early failure detection and bounds the missed-detection and false-alarm rates, with minimal inference overhead. We show that supervising on the pre-failure segment of a trajectory increases early failure detection at matched false-positive rates by up to 30% over the strongest learned baseline. Under shift to unseen tasks, the bounds on missed-detection and false-alarm rates remain valid in up to 86% of runs, versus at most 21% for baselines. Unlike existing methods, VLA-Tug predicts the failure mode to enable corrective actions, raising top-3 accuracy on unseen tasks by up to 44% over a majority baseline. VLA-Tug enables real-time monitoring where the well-timed and informative probe supports lightweight steering that improves task success. We release a dataset of 3,180 annotated manipulation episodes to support future work on latent failure detection in VLAs at https://vla-tug.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08425v1
- Authors: Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva, Olin Goudey, Neel P. Bhatt, Matthias Scheutz, Ufuk Topcu
- Published: 2026-11-05T18:21:07Z
- Age days: 1

</details>
