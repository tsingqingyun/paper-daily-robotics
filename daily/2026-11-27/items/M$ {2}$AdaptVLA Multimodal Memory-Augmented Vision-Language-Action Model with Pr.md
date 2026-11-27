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
url: "https://arxiv.org/abs/2611.34560v1"
published: "2026-11-25T15:32:21Z"
age_days: 1
score: 39
created: 2026-11-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> M2AdaptVLA 同时记住机器人看到了什么、接触时受了什么力，并按任务阶段决定多依赖哪种信息。部署时，它用预测接触力与实测值的误差微调动作策略。

## 问题

机器人可能需要记得先前看到的操作顺序，也需要通过手腕受力判定当前动作是否到位。固定长度的图像缓存终会丢掉早期画面，只把过去压进权重又可能找不回具体时刻的细节。仅从受力信号决定该信多少力觉，也缺少任务阶段线索。即使政策能读取力历史，换了接触表面后，同样的动作仍可能产生它没学过的力 [S2](https://arxiv.org/html/2611.34560v1#S1.p1.1) [S3](https://arxiv.org/html/2611.34560v1#S1.p2.1) [S4](https://arxiv.org/html/2611.34560v1#S1.p3.1)。

### 用一个例子理解

理解用例（非论文实验）。机器人看完一段把卡片依次插入不同卡槽的演示，开始操作。视觉记忆提供下一个卡槽的线索，腕部历史帮助判断当前卡片是否卡住。若新卡槽的弹片更紧，执行后得到的实测受力与预测有偏差，策略用这次误差更新适配器，随后输出下一段插入动作。

## 创新点或方法

视觉分支把每一帧的特征与快权重对过往观测的读出一起存入有限缓存。旧帧退出后，后续条目仍可能带着它留下的线索。动作分支用指令、视觉、机器人自身状态及力历史算出门控，调节力历史的影响，并联合生成动作和对应的力与力矩预测。离线训练按示范的时间顺序推进记忆。部署时，视觉记忆随新观测更新，另一路等对应动作执行完，用对齐的实测力监督策略适配器，只从最后一次去噪反传 [S8](https://arxiv.org/html/2611.34560v1#S2.SS1.p1.1)[S11](https://arxiv.org/html/2611.34560v1#S3.p1.1) [S12](https://arxiv.org/html/2611.34560v1#S3.SS1.p3.3) [S13](https://arxiv.org/html/2611.34560v1#S3.SS2.p2.2) [S14](https://arxiv.org/html/2611.34560v1#S3.SS3.p3.2)[S23](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p2.1)。

### 方法如何工作

1. 读取指令、当前画面和上一轮缓存，从新观测更新快权重，并写入供后续决策读取的视觉条目。
2. 用当前任务上下文和近期力历史算门控，让动作专家按任务阶段调整接触信息的权重。
3. 联合预测一段动作及相应的力和力矩，执行其中前一部分，为下一次决策取得新观测。
4. 将已经执行的动作与有效力测量对齐，计算预测误差，经最后一次去噪更新低秩适配器。

### 必要术语

- 快权重：随观测序列更新的记忆参数；本文把它的读出写入视觉缓存，让近期条目携带更早的线索。
- Wrench：力和力矩；本文既使用近期测量来选动作，也预测后续测量来获得适配信号。
- 联合去噪：逐步从带噪表示恢复动作和受力序列；本文用同一生成过程产出两者的预测。

## 证据

八项真机任务按所有阶段均完成计成功，平均成功率 82.71%，最强整体基线 π-Mem 为 51.25% [S27](https://arxiv.org/html/2611.34560v1#S4.T1.6) [S28](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px5.p1.1)。同骨干的初始抽屉回忆任务中，带快权重的缓存为 90%，独立帧缓存为 70%，只用快权重为 75% [S23](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p2.1)[S36](https://arxiv.org/html/2611.34560v1#S4.T3.6) [S37](https://arxiv.org/html/2611.34560v1#S4.SS3.SSS0.Px1.p3.1)。同一擦板策略在两种板面位置变化下，开启适配使平均成功率从 85.0% 升到 97.5%，RTX 5090 上每次更新平均 159.5 毫秒 [S5](https://arxiv.org/html/2611.34560v1#S1.p5.1)[S25](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p4.1)。后一个对照直接检验这两种变化下的更新效果。

## 局限

作者指出，两种记忆会增加整体推理延迟 [S38](https://arxiv.org/html/2611.34560v1#S5.p1.1)。单次适配用时只覆盖更新本身，实际控制还取决于传感器对齐、预测和执行调度。我会核查传感器偏差持续存在时，适配是否会把测量误差当成环境变化。

- **判断**：值得读到 §3.3 和部署时序 [S42](https://arxiv.org/html/2611.34560v1#A2.SS0.SSS0.Px1.p1.1)，因为能否复用这套方法，取决于预测、执行与测量是否能对上。

## 研究关联

实测接触信号既能告诉策略刚刚发生了什么，也能在动作执行后检验它原先的预测。能把预测和传感器读数按时间对齐时，机器人便可以在没有新增人工示范的情况下获得更新信号。

### 下一步读哪里

先看 [S12](https://arxiv.org/html/2611.34560v1#S3.SS1.p3.3)[S33](https://arxiv.org/html/2611.34560v1#S4.F5)[S42](https://arxiv.org/html/2611.34560v1#A2.SS0.SSS0.Px1.p1.1) 确认新条目何时可读、动作块执行到哪里就重新预测。再查附录 C 所引的有效测量选择规则 [S14](https://arxiv.org/html/2611.34560v1#S3.SS3.p3.2)，以及 [S43](https://arxiv.org/html/2611.34560v1#A4.SS0.SSS0.Px2.p1.1) 的更新层数对照，核对测量对齐和更新范围怎样影响结果。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34560v1
- 获取时间：2026-11-27T02:55:40.432199+00:00
- [S1] [M2AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation · 正文段落 1](https://arxiv.org/html/2611.34560v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.34560v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34560v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34560v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34560v1#S1.p5.1)
- [S6] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.34560v1#S1.I1.i1)
- [S7] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.34560v1#S1.I1.i3)
- [S8] [2.1 Visual Memory for Robotic Manipulation · 正文段落 12](https://arxiv.org/html/2611.34560v1#S2.SS1.p1.1)
- [S9] [2.2 Wrench Memory for Robotic Manipulation · 正文段落 13](https://arxiv.org/html/2611.34560v1#S2.SS2.p1.1)
- [S10] [2.3 Online Adaptation for Robot Policies · 正文段落 14](https://arxiv.org/html/2611.34560v1#S2.SS3.p1.1)
- [S11] [3 Method · 正文段落 15](https://arxiv.org/html/2611.34560v1#S3.p1.1)
- [S12] [3.1 TTT-Augmented Visual Memory Bank · 正文段落 24](https://arxiv.org/html/2611.34560v1#S3.SS1.p3.3)
- [S13] [3.2 Context Gate for Wrench Memory · 正文段落 26](https://arxiv.org/html/2611.34560v1#S3.SS2.p2.2)
- [S14] [3.3 Joint Denoising for Test-Time Adaptation · 正文段落 35](https://arxiv.org/html/2611.34560v1#S3.SS3.p3.2)
- [S15] [4 Experiments · 正文段落 36](https://arxiv.org/html/2611.34560v1#S4.p1.1)
- [S16] [4 Experiments · 正文段落 37](https://arxiv.org/html/2611.34560v1#S4.p2.1)
- [S17] [4 Experiments · 正文段落 38](https://arxiv.org/html/2611.34560v1#S4.p3.1)
- [S18] [4 Experiments · 正文段落 39](https://arxiv.org/html/2611.34560v1#S4.p4.1)
- [S19] [4 Experiments · 正文段落 40](https://arxiv.org/html/2611.34560v1#S4.p5.1)
- [S20] [Training and inference · 正文段落 44](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px2.p1.1)
- [S21] [Tasks · 正文段落 45](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px3.p1.1)
- [S22] [Baselines · 正文段落 47](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p1.1)
- [S23] [Baselines · 正文段落 48](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p2.1)
- [S24] [Baselines · 正文段落 49](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p3.1)
- [S25] [Baselines · 正文段落 50](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px4.p4.1)
- [S26] [Baselines · 正文段落 51](https://arxiv.org/html/2611.34560v1#S4.T1)
- [S27] [Baselines · 正文段落 52](https://arxiv.org/html/2611.34560v1#S4.T1.6)
- [S28] [Evaluation protocol · 正文段落 53](https://arxiv.org/html/2611.34560v1#S4.SS1.SSS0.Px5.p1.1)
- [S29] [Evaluation protocol · 正文段落 54](https://arxiv.org/html/2611.34560v1#S4.T2)
- [S30] [M2AdaptVLA outperforms state-of-the-art VLA baselines (Q1) · 正文段落 56](https://arxiv.org/html/2611.34560v1#S4.SS2.SSS0.Px1.p1.1)
- [S31] [M2AdaptVLA outperforms state-of-the-art VLA baselines (Q1) · 正文段落 57](https://arxiv.org/html/2611.34560v1#S4.SS2.SSS0.Px1.p2.1)
- [S32] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 58](https://arxiv.org/html/2611.34560v1#S4.SS3.SSS0.Px1.p1.1)
- [S33] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 59](https://arxiv.org/html/2611.34560v1#S4.F5)
- [S34] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 60](https://arxiv.org/html/2611.34560v1#S4.SS3.SSS0.Px1.p2.1)
- [S35] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 61](https://arxiv.org/html/2611.34560v1#S4.T3)
- [S36] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 62](https://arxiv.org/html/2611.34560v1#S4.T3.6)
- [S37] [The TTT bank improves progress tracking, initial-scene recall, and demonstration following (Q2) · 正文段落 63](https://arxiv.org/html/2611.34560v1#S4.SS3.SSS0.Px1.p3.1)
- [S38] [5 Conclusion · 正文段落 74](https://arxiv.org/html/2611.34560v1#S5.p1.1)
- [S39] [Sampling the Open Safe training context · 正文段落 77](https://arxiv.org/html/2611.34560v1#A1.SS0.SSS0.Px1.p1.1)
- [S40] [A.2 Offline objective and hyperparameters · 正文段落 87](https://arxiv.org/html/2611.34560v1#A1.T5)
- [S41] [Which decisions train the outer model? · 正文段落 115](https://arxiv.org/html/2611.34560v1#A1.SS4.SSS0.Px4.p1.1)
- [S42] [Matching the training time axis · 正文段落 118](https://arxiv.org/html/2611.34560v1#A2.SS0.SSS0.Px1.p1.1)
- [S43] [Results · 正文段落 145](https://arxiv.org/html/2611.34560v1#A4.SS0.SSS0.Px2.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/M$ {2}$AdaptVLA Multimodal Memory-Augmented Vision-Language-Action Model with Pr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Effective robotic manipulation calls for multimodal memory and rapid adaptation to shifts in contact dynamics. However, many existing policies, which retain either visual or wrench history, may miss key cues from the other modality. Moreover, even with wrench memory, fixed policies can struggle when contact conditions shift at deployment. To this end, we introduce M$^{2}$AdaptVLA, a vision-language-action model that integrates visual and wrench memories with predictive test-time adaptation. For visual memory, the model uses test-time training (TTT) to encode observation history in fast weights. Each entry in the bounded TTT bank combines the corresponding frame's features with a readout from these weights, preserving cues that predate the oldest retained frame. For wrench memory, a context gate controls how much the action expert draws on wrench history as it jointly denoises future actions and wrenches. For predictive test-time adaptation, the auxiliary wrench prediction loss also provides online self-supervision. Using measured wrenches as targets, we update low-rank policy adapters by backpropagating only through the final denoising step. Real-world experiments show that the TTT bank outperforms visual memory baselines on progress tracking, scene recall, and demonstration following. On contact-sensitive tasks, the context gate yields higher success rates than direct injection or gated cross-attention. Predictive test-time adaptation improves robustness to shifts in contact dynamics. On eight tasks requiring visual and wrench memory, M$^{2}$AdaptVLA achieves a mean success rate of 82.71%, a 31.46% absolute gain over the strongest baseline. The project page is available at https://tlf-tlf.github.io/M2AdaptVLAPage/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34560v1
- Authors: Liufan Tan, Tong Wang, Yuehao Yin, Jian Chen, Yihang Yin, Ying Qu, Wenyu Li, Ruyi Gan, Hao Wang
- Published: 2026-11-25T15:32:21Z
- Age days: 1

</details>
