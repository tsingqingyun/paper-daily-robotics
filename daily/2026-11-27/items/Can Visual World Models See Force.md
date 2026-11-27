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
url: "https://arxiv.org/abs/2611.34422v1"
published: "2026-11-25T14:12:10Z"
age_days: 1
score: 37
created: 2026-11-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# Can Visual World Models See Force?

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> 《Can Visual World Models See Force?》用一个小读出器检查冻结模型的视觉特征能透露多少接触力。受测模型大多能看出何时接触，但要从特征里读出实际用了多大的力，仍然很难。

## 问题

相近的运动轨迹可以由不同的力产生，例如阻力不同的门也可能以相同速度打开。预测画面或动作目标做得好，仍需单独检查特征能否区分这种力差。作者因此问了三个具体问题：能否看出接触、能否跟上力的变化、能否估准力的大小 [S2](https://arxiv.org/html/2611.34422v1#S1.p1.1) [S3](https://arxiv.org/html/2611.34422v1#S1.p2.1) [S4](https://arxiv.org/html/2611.34422v1#S1.F1) [S5](https://arxiv.org/html/2611.34422v1#S1.p3.1) [S6](https://arxiv.org/html/2611.34422v1#S1.p4.1)。

### 用一个例子理解

理解用例（非论文实验）。输入两段速度近似的合盖视频，以及训练片段对应的测力记录。冻结模型产出视觉特征，小读出器生成两条力曲线。若两条曲线都在碰到盒盖时上升，却没有反映较紧盒盖所需的更大推力，那么它读出了接触时机，大小估计仍有误差。

## 创新点或方法

给各类冻结模型输入观测，取中间层空间特征。训练时，只拟合一个共享的仿射映射给每个空间 token 打分，再取该时刻最高分作为力预测。监督来自同步的实测力，选层用验证场景，测试时把预测还原为牛顿。主实验固定特征提取模型。额外实验则先用 RH20T 的力标签微调 V-JEPA 2.1，再检查它的特征能否让读出器更准确地预测力 [S13](https://arxiv.org/html/2611.34422v1#S3.F2) [S14](https://arxiv.org/html/2611.34422v1#S3.p1.1) [S15](https://arxiv.org/html/2611.34422v1#S3.SS2.p1.2) [S16](https://arxiv.org/html/2611.34422v1#S3.SS2.p2.1) [S17](https://arxiv.org/html/2611.34422v1#S3.SS2.p2.2) [S18](https://arxiv.org/html/2611.34422v1#S3.SS4.SSS0.Px1.p4.3) [S19](https://arxiv.org/html/2611.34422v1#S3.SS4.SSS0.Px2.p1.1)[S22](https://arxiv.org/html/2611.34422v1#S4.SS5.p1.1)。

### 方法如何工作

1. 将真实操作视频和测力记录按时间对齐，让每个样本都有对应的力目标。
2. 用冻结模型提取空间特征，固定读出器形式，使各模型接受可比的测试。
3. 在训练集拟合逐 token 打分和取最大值的读出器，在验证场景选层，再在留出场景输出力曲线。
4. 分别比较接触、曲线变化和数值误差，再用配对模型及有力监督的微调检查哪些训练条件改善了读出。

### 必要术语

- 探针：从模型特征里读取指定信息的小模型；本文用它测试力有多容易被解码。
- 相关系数 r：衡量两条曲线的升降是否同步；本文用它检查一次交互中能否跟上力的变化。
- 接触 R²：衡量接触期间的力值预测能解释多少实际变化；尺度和偏移不准会拉低它。

## 证据

Hoi! 是人持测力夹爪操作门和抽屉的数据，RH20T 提供机器人操作记录 [S6](https://arxiv.org/html/2611.34422v1#S1.p4.1)[S20](https://arxiv.org/html/2611.34422v1#S4.SS1.SSS0.Px1.p1.1)。Hoi! 夹爪视角中，DreamZero 相对基础模型 Wan 的力跟踪相关系数为 0.46 对 0.35，换到 RH20T 为 0.15 对 0.18。四组基础与机器人后训练模型的对照整体未显示稳定改善 [S21](https://arxiv.org/html/2611.34422v1#S4.SS3.SSS0.Px3.p1.1)。Hoi! 夹爪视角的冻结 V-JEPA 2.1 接触 R² 为 0.166，事后用评估数据做仿射校准也只有 0.190 [S25](https://arxiv.org/html/2611.34422v1#S10.T14.6)。力监督后，把 RH20T 读出器原样搬到 Hoi!，相关系数由 0.03 升到 0.21，接触 R² 仍明显为负 [S22](https://arxiv.org/html/2611.34422v1#S4.SS5.p1.1)。

## 局限

结论取决于观测视角、数据和读出方式。作者在 Hoi! 人视角的部分模型上试了注意力读出，V-JEPA 有改善，整体排序相同 [S29](https://arxiv.org/html/2611.34422v1#S10.T17) [S30](https://arxiv.org/html/2611.34422v1#S10.T17.6) [S31](https://arxiv.org/html/2611.34422v1#S10.SS4.p1.1) [S32](https://arxiv.org/html/2611.34422v1#S10.SS4.p2.1)。这些是已有轨迹上的解码结果。我会核查改变阻力、同时尽量匹配运动轨迹时，预测是否仍跟得上实测力，以及能否服务于闭环控制。

- **判断**：值得细读探针协议和力监督迁移实验，尤其要对着看相关系数与接触 R²，避免把曲线同步当成定量估力。

## 研究关联

评估视觉力反馈时，接触报警、变化跟踪和定量估力应分别验收。一个信号可以在碰到目标时提醒机器人切换控制阶段，却仍不足以判断压力是否超过任务允许的范围。

### 下一步读哪里

从 [S19](https://arxiv.org/html/2611.34422v1#S3.SS4.SSS0.Px2.p1.1) 核对各指标是否分别选层，再看 [S24](https://arxiv.org/html/2611.34422v1#S10.T14) [S25](https://arxiv.org/html/2611.34422v1#S10.T14.6) [S26](https://arxiv.org/html/2611.34422v1#S10.T15) [S27](https://arxiv.org/html/2611.34422v1#S10.T15.5) [S28](https://arxiv.org/html/2611.34422v1#S10.SS2.p1.1) 如何检验尺度偏差和训练目标。读 [S22](https://arxiv.org/html/2611.34422v1#S4.SS5.p1.1) 时分别看原读出器跨数据集测试、在目标数据上重训读出器，以及两种视角的结果。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34422v1
- 获取时间：2026-11-27T02:55:43.502366+00:00
- [S1] [Can Visual World Models See Force? · 正文段落 1](https://arxiv.org/html/2611.34422v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.34422v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34422v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34422v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34422v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34422v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.34422v1#S1.I1.i3)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.34422v1#S1.p6.1)
- [S9] [World models and policies for manipulation. · 正文段落 11](https://arxiv.org/html/2611.34422v1#S2.SS0.SSS0.Px1.p1.1)
- [S10] [Why force matters for manipulation. · 正文段落 12](https://arxiv.org/html/2611.34422v1#S2.SS0.SSS0.Px2.p1.1)
- [S11] [Estimating force from visual observations. · 正文段落 13](https://arxiv.org/html/2611.34422v1#S2.SS0.SSS0.Px3.p1.1)
- [S12] [Probing physical understanding. · 正文段落 14](https://arxiv.org/html/2611.34422v1#S2.SS0.SSS0.Px4.p1.1)
- [S13] [3 Probing Force in Frozen Representations · 正文段落 15](https://arxiv.org/html/2611.34422v1#S3.F2)
- [S14] [3 Probing Force in Frozen Representations · 正文段落 16](https://arxiv.org/html/2611.34422v1#S3.p1.1)
- [S15] [3.2 Probe · 正文段落 22](https://arxiv.org/html/2611.34422v1#S3.SS2.p1.2)
- [S16] [3.2 Probe · 正文段落 23](https://arxiv.org/html/2611.34422v1#S3.SS2.p2.1)
- [S17] [3.2 Probe · 正文段落 25](https://arxiv.org/html/2611.34422v1#S3.SS2.p2.2)
- [S18] [Metrics. · 正文段落 41](https://arxiv.org/html/2611.34422v1#S3.SS4.SSS0.Px1.p4.3)
- [S19] [Layer selection. · 正文段落 42](https://arxiv.org/html/2611.34422v1#S3.SS4.SSS0.Px2.p1.1)
- [S20] [Hoi!. · 正文段落 45](https://arxiv.org/html/2611.34422v1#S4.SS1.SSS0.Px1.p1.1)
- [S21] [Robot training does not reliably improve force awareness. · 正文段落 57](https://arxiv.org/html/2611.34422v1#S4.SS3.SSS0.Px3.p1.1)
- [S22] [4.5 Learning force from data · 正文段落 68](https://arxiv.org/html/2611.34422v1#S4.SS5.p1.1)
- [S23] [5 Conclusion · 正文段落 69](https://arxiv.org/html/2611.34422v1#S5.p1.1)
- [S24] [10.2 Calibration and training objective · 正文段落 118](https://arxiv.org/html/2611.34422v1#S10.T14)
- [S25] [10.2 Calibration and training objective · 正文段落 119](https://arxiv.org/html/2611.34422v1#S10.T14.6)
- [S26] [10.2 Calibration and training objective · 正文段落 120](https://arxiv.org/html/2611.34422v1#S10.T15)
- [S27] [10.2 Calibration and training objective · 正文段落 121](https://arxiv.org/html/2611.34422v1#S10.T15.5)
- [S28] [10.2 Calibration and training objective · 正文段落 122](https://arxiv.org/html/2611.34422v1#S10.SS2.p1.1)
- [S29] [10.4 Attentive readouts and training seeds · 正文段落 129](https://arxiv.org/html/2611.34422v1#S10.T17)
- [S30] [10.4 Attentive readouts and training seeds · 正文段落 130](https://arxiv.org/html/2611.34422v1#S10.T17.6)
- [S31] [10.4 Attentive readouts and training seeds · 正文段落 131](https://arxiv.org/html/2611.34422v1#S10.SS4.p1.1)
- [S32] [10.4 Attentive readouts and training seeds · 正文段落 132](https://arxiv.org/html/2611.34422v1#S10.SS4.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Can Visual World Models See Force.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation. They predict how scenes evolve and which actions to take, yet successful manipulation depends not solely on following observable trajectories but also on the hidden variable of interaction force. Neurophysiology has shown that humans possess a visual prior for this hidden variable, motivating us to ask the question: Do the representations of visual foundation models also capture the forces involved in an interaction? We define force awareness as the ability of representations to (1) indicate when contact force is applied, (2) track how it changes during an interaction, and (3) reflect how large it is. We probe frozen image, video, world- and policy model representations with a lightweight readout trained on synchronized video and force measurements from two manipulation datasets. Our experiments show that most models capture when contact occurs but not how much force is being applied. Surprisingly, robot post-training does not improve this either, highlighting an important gap in current models capabilities.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34422v1
- Authors: Felix Tristram, Benjamin D. Killeen, Nassir Navab
- Published: 2026-11-25T14:12:10Z
- Age days: 1

</details>
