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
url: "https://arxiv.org/abs/2610.10288v1"
published: "2026-10-07T15:49:41Z"
age_days: 1
score: 36
created: 2026-10-09
concepts: ["具身智能评测与基准"]
---

# TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> TouchScale 用统一设备记录大规模同步人类视频与双手压力，让模型学习画面背后的接触信息。机器人先用这些无动作标签的人类数据做视觉—触觉中间训练，再用机器人示范学控制，无需把人手动作转换成机器人动作。

## 问题

视频能看到手怎么动，却记录不了哪里接触、如何施压。此前触觉数据较小，拼接不同传感器数据又把规模和采集差异混在一起，难判断数据增加究竟有没有帮助 [S4](https://arxiv.org/html/2610.10288v1#S1.p1.1)。

### 用一个例子理解

理解用例（非论文实验）：人类捏不同软硬物体，同步视频和压力成为训练对；模型学接触与外观变化的对应，再用机器人示范后训练，输入机器人观察后输出分拣动作。

## 创新点或方法

相比只用视频或混合异构触觉数据，本文统一同步头部 RGB-D、双腕视频和全手压力，规模为 500 小时、约 87K 段 [S3](https://arxiv.org/html/2610.10288v1#S0.F1)。跨传感器测试将读数汇聚到共同解剖区域。机器人路线从同一 N₀-VTLA 检查点出发，先用人类数据学视觉到触觉，再在同样机器人示范上后训练；基线跳过中间阶段。推理是训练后的机器人策略，不依赖现场人类手套；节选未完整说明预测触觉如何进入动作计算 [S12](https://arxiv.org/html/2610.10288v1#S2.SS2.p1.1) [S16](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px1.p1.1) [S22](https://arxiv.org/html/2610.10288v1#S6.F7)。

### 方法如何工作

1. 统一设备同步视觉与双手压力，提供视频里缺失的物理监督。
2. 学习视觉到触觉的对应，让视觉表示关注接触相关信息。
3. 用人类数据中间训练已有机器人模型，先补接触知识而不学习人手动作。
4. 再用固定机器人示范后训练，建立机器人自身的动作对应。
5. 改变人类数据量并保持后训练协议一致，检查收益是否随规模变化。

### 必要术语

- 中间训练：基础模型与机器人任务训练之间的学习阶段；本文补充接触监督。
- 接触 IoU：预测与实际接触区域的重合程度；衡量跨传感器预测。
- 动作重定向：把人体运动转换成机器人动作；本文人类数据阶段无需这一步。

## 证据

未见传感器 EgoTactile 上，接触 IoU 从以 EgoTouch 训练的 0.134 到全量 TouchScale 的 0.383；同为 16 小时的 TouchScale 子集为 0.181 [S6](https://arxiv.org/html/2610.10288v1#S1.p3.1)。xArm6 与 Revo 2 手上四项任务各收集 50 个示范，中间训练使平均真机成功率从 22.5% 到 57.5% [S17](https://arxiv.org/html/2610.10288v1#S4.F5) [S18](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px3.p1.1)。规模从 20% 到全量时为 30.0%、32.5%、50.0%、50.0%、57.5%，是总体上升而非严格递增 [S19](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px4.p1.1)。测试轮数未在节选给出。

## 局限

作者明确只测试一个平台、四项任务，数据无动作标签，未来触觉误差与动作误差仅弱相关 [S21](https://arxiv.org/html/2610.10288v1#S5.p1.1)。因此不能把成功提升归因成“触觉预测越准必然控制越好”。固定传感器减少了混杂，但随规模增加的场景多样性和额外训练投入仍值得核查。

- **判断**：值得读数据协议与机器人对照实验，因为它给出了不依赖人机动作对齐的数据利用路径，但规模结论仍有测试范围。

## 研究关联

人类数据不必提供可直接执行的机器人动作，也能帮助控制学习：先用同步触觉让模型学会理解接触，再用少量机器人数据建立动作对应。统一采集还让规模实验更容易解释。

### 下一步读哪里

重点看 [S16](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px1.p1.1) [S17](https://arxiv.org/html/2610.10288v1#S4.F5) [S18](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px3.p1.1) [S19](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px4.p1.1) 的同示范对照和 [S21](https://arxiv.org/html/2610.10288v1#S5.p1.1) 的机制边界；核查采样、训练步数、重复试验及机器人阶段触觉接口。跨传感器结果须结合 [S22](https://arxiv.org/html/2610.10288v1#S6.F7) 的区域汇聚理解。

- **概念**：具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.10288v1
- 获取时间：2026-10-09T00:15:45.340841+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.10288v1#p1.1)
- [S2] [TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning · 正文段落 2](https://arxiv.org/html/2610.10288v1#abstract1.1)
- [S3] [TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning · 正文段落 3](https://arxiv.org/html/2610.10288v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.10288v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.10288v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.10288v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.10288v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.10288v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.10288v1#S1.I1.i3)
- [S10] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.10288v1#S2.T1.3.1)
- [S11] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.10288v1#S2.T1)
- [S12] [2.2 Human Visual–Tactile Data for Robot Learning · 正文段落 14](https://arxiv.org/html/2610.10288v1#S2.SS2.p1.1)
- [S13] [4 Experiments · 正文段落 24](https://arxiv.org/html/2610.10288v1#S4.p1.1)
- [S14] [4.2 Visual Representation Learning · 正文段落 32](https://arxiv.org/html/2610.10288v1#S4.SS2.p1.1)
- [S15] [4.2 Visual Representation Learning · 正文段落 34](https://arxiv.org/html/2610.10288v1#S4.T3.6)
- [S16] [TouchScale mid-training and robot post-training. · 正文段落 36](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px1.p1.1)
- [S17] [TouchScale mid-training and robot post-training. · 正文段落 37](https://arxiv.org/html/2610.10288v1#S4.F5)
- [S18] [Effect of TouchScale mid-training. · 正文段落 41](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px3.p1.1)
- [S19] [Effect of TouchScale data scale on robot policy. · 正文段落 42](https://arxiv.org/html/2610.10288v1#S4.SS3.SSS0.Px4.p1.1)
- [S20] [Effect of TouchScale data scale on robot policy. · 正文段落 43](https://arxiv.org/html/2610.10288v1#S4.F6)
- [S21] [5 Conclusion and Limitations · 正文段落 46](https://arxiv.org/html/2610.10288v1#S5.p1.1)
- [S22] [6.2 Region-level tactile representation · 正文段落 58](https://arxiv.org/html/2610.10288v1#S6.F7)
- [S23] [6.4 Qualitative Results of Tactile Prediction · 正文段落 91](https://arxiv.org/html/2610.10288v1#S6.SS4.p1.1)
- [S24] [Evaluation protocol. · 正文段落 115](https://arxiv.org/html/2610.10288v1#S9.SS0.SSS0.Px2.p1.1)
- [S25] [Evaluation protocol. · 正文段落 116](https://arxiv.org/html/2610.10288v1#S9.T5)
- [S26] [Evaluation protocol. · 正文段落 117](https://arxiv.org/html/2610.10288v1#S9.T5.6)
- [S27] [Evaluation protocol. · 正文段落 118](https://arxiv.org/html/2610.10288v1#S9.SS0.SSS0.Px2.p2.1)
- [S28] [10.1 Qualitative Results · 正文段落 119](https://arxiv.org/html/2610.10288v1#S10.SS1.p1.1)
- [S29] [10.1 Qualitative Results · 正文段落 120](https://arxiv.org/html/2610.10288v1#S10.SS1.p2.1)
- [S30] [10.1 Qualitative Results · 正文段落 121](https://arxiv.org/html/2610.10288v1#S10.F11)
- [S31] [10.1 Qualitative Results · 正文段落 122](https://arxiv.org/html/2610.10288v1#S10.F12)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/TouchScale 500 Hours of Human Vision and Touch for Visual-Tactile Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale egocentric human interaction data is becoming an important source of physical supervision for embodied learning, yet video alone leaves the contact and pressure that characterize physical interaction unrecorded. Recent visual-tactile datasets provide this missing supervision, but their synchronized tactile data remain far smaller in volume than human video. Moreover, the largest resources often merge recordings from different sensors or annotation procedures, which makes the effect of data scale difficult to isolate. We therefore introduce TouchScale, a 500-hour dataset of contact-rich human interaction recorded with a single unified wearable setup. Its approximately 2K predefined task descriptions span everyday activities and structured manipulation, and each recording temporally aligns egocentric RGB-D video with wrist RGB video and dense full-hand bimanual tactile measurements. Compared with prior tactile data, training on the full TouchScale raises zero-shot contact IoU on data from an unseen tactile sensor from 0.134 to 0.383. Pretraining a visual encoder on TouchScale also yields the highest action recognition accuracy on three benchmarks among the compared visual-tactile datasets. Used for visual-tactile mid-training of a robot policy, TouchScale improves the average real-world success rate across four contact-rich manipulation tasks from 22.5% to 57.5%. With the sensor and collection protocol held fixed, both zero-shot tactile prediction and robot success show an overall upward trend as more TouchScale data is used. These results suggest that human visual-tactile data collected at scale with consistent sensing benefits both perception and robot manipulation. We will publicly release TouchScale, including all synchronized visual-tactile recordings and reconstructed object models, to support future research on scalable visual-tactile learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10288v1
- Authors: Dayou Li, Hao Wang, Qianqian Yang, Zihao Zhu, Haoquan Fang, Ziyao Zeng, Yan Han, Zihan Wang, Yan Wang, Baoru Huang, Dilin Wang, Kenji Shimada, Yiyue Luo, Manling Li, Teresa Lv, Mustafa Mukadam, Rakesh Ranjan, Ruohan Zhang, Qi He, Changliu Liu, Xu Chen, Marco Pavone, Bangya Liu, Jiachen Li, Masayoshi Tomizuka, Zhiwen Fan
- Published: 2026-10-07T15:49:41Z
- Age days: 1

</details>
