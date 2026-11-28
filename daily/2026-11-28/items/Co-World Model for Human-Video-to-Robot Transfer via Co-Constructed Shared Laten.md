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
url: "https://arxiv.org/abs/2611.34302v1"
published: "2026-11-25T12:54:52Z"
age_days: 2
score: 27
created: 2026-11-28
concepts: ["世界模型", "机器人学习"]
---

# Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CoWM 让机器人看一段未见过的人类示范，学着复现物体发生的一连串变化。它按动作对物体的效果来对齐人和机器人，再用机器人已有的动作经验约束执行。

## 问题

把人的手腕轨迹直接映射到机械手，容易在手型、关节和接触方式不同的地方失效。只匹配最终画面又会丢掉中间步骤，例如物体要先脱离卡槽才能挪走。任务是在测试视频没有配套机器人轨迹时，判断哪些物体变化应该依次发生，以及机器人当前能用什么动作实现它们。[S5](https://arxiv.org/html/2611.34302v1#S1.p1.1)[S18](https://arxiv.org/html/2611.34302v1#S3.SS1.p1.1)

### 用一个例子理解

理解用例（非论文实验）。输入是一段人把抽屉拉开再取出笔的第一视角视频，以及机器人当前的观测。CoWM 跟踪抽屉与柜体的相对位移和笔的位置变化。抽屉还没拉够时，控制器继续搜索机器人能执行的开抽屉动作；观察到开口足够后，再输出取笔的控制指令。

## 创新点或方法

训练时把配对但逐帧不同步的人与机器人片段一起用。两边各自把运动编码成潜在动作，把观察拆成共享的物体关系和各自的身体、传感与控制信息。同一个预测器根据物体状态和潜在动作预测物体变化。效果互换要求效果相同的动作换进去后仍预测出相容的变化；动作敏感性约束则要求区分那些编码相近、实际效果却不同的动作，防止预测器忽略动作。执行时先估计机器人做到视频的哪一段，再用当前机器人状态修正从视频提取的动作建议，优先搜索机器人经验支持的动作，执行后根据新观测重算。[S7](https://arxiv.org/html/2611.34302v1#S1.p3.1)[S8](https://arxiv.org/html/2611.34302v1#S1.p4.1)[S15](https://arxiv.org/html/2611.34302v1#S2.F2)[S19](https://arxiv.org/html/2611.34302v1#S3.SS1.p2.1)

### 方法如何工作

1. 从两路观察提取物体关系，并保留各自的身体与控制信息，让同一个预测器能使用双方的物体状态。
2. 把两路运动变成潜在动作，按预测出的物体变化检验哪些动作可以互换、哪些必须区分。
3. 用机器人当前的物体状态匹配示范进度，提取该阶段的人类动作建议。
4. 用机器人状态修正建议，在有经验支持的范围内搜索并输出指令，再根据新观测更新计划。

### 必要术语

- 共享物体关系状态：两种身体都能观察到的物体关系编码；供同一个模型预测变化。
- 动作支持密度：机器人以往经验中哪些潜在动作较常出现的估计；用于限制执行搜索。
- 滚动时域规划：先规划一小段，获取新观测后重算；用于应对执行速度和预测偏差。

## 证据

仿真覆盖 30 个 LIBERO 操作任务和 120 段留出视频，另用 ManiSkill 做跨基准测试 [S23](https://arxiv.org/html/2611.34302v1#S4.SS1.p1.1)。两台实体机器人各做同样的 5 个桌面任务，每任务 15 次 [S24](https://arxiv.org/html/2611.34302v1#S4.SS1.p2.1)。对照包括直接映射、只看终点的规划器，以及共用骨干和规划器但省去联合训练的模型 [S28](https://arxiv.org/html/2611.34302v1#S4.SS1.p3.1)。指标包括任务成功率、末端物体平移误差，以及同一仿真状态下的效果复现率和不同效果拒绝率 [S29](https://arxiv.org/html/2611.34302v1#S4.SS1.p4.1)[S31](https://arxiv.org/html/2611.34302v1#S4.SS2.p2.1)。摘要报告两类环境均验证了方法，但节选没有给出各平台的成绩、对照差值或干预结果，因而无法量化优势和各组件的贡献。

## 局限

作者点出严重遮挡、缺少力感知、全局动作支持密度，以及灵巧和可变形物体操作等限制 [S45](https://arxiv.org/html/2611.34302v1#S5.p1.1)。还值得核查两台真机分别需要什么训练经验和标定。节选中的同状态干预在仿真中进行，真机上的机制贡献仍需对应的对照结果。

- **判断**：值得读到两条训练约束和同状态干预协议，它们决定了“效果相同就可以替换”究竟能检验到什么程度。

## 研究关联

跨机器人迁移时，可以先明确什么结果值得复用，再决定控制信号该怎么映射。物体关系的变化若容易跟踪，就可以用同起点换动作的测试，检查共享表示能否支撑实际替换，早于整段任务成功率暴露问题。

### 下一步读哪里

沿 [S15](https://arxiv.org/html/2611.34302v1#S2.F2) 查式（15）和（16），确认不同步片段怎样判定同效果、怎样选不同效果的近邻。再用 [S28](https://arxiv.org/html/2611.34302v1#S4.SS1.p3.1)–[S34](https://arxiv.org/html/2611.34302v1#S4.SS2.p4.1) 对照结果，核查共用规划器的基线和两条约束各自改变了哪些指标。

- **概念**：世界模型 机器人学习
- **筛选分数**：27
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34302v1
- 获取时间：2026-11-28T03:58:16.754322+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.34302v1#p1.2)
- [S2] [正文 · 正文段落 2](https://arxiv.org/html/2611.34302v1#p2.1)
- [S3] [正文 · 正文段落 3](https://arxiv.org/html/2611.34302v1#p3.1)
- [S4] [Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics · 正文段落 4](https://arxiv.org/html/2611.34302v1#abstract1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34302v1#S1.p1.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34302v1#S1.F1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.34302v1#S1.p3.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.34302v1#S1.p4.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.34302v1#S1.I1.ix1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.34302v1#S1.I1.ix2)
- [S11] [1 Introduction · 正文段落 13](https://arxiv.org/html/2611.34302v1#S1.I1.ix3)
- [S12] [2.1 Robot Learning from Human Video · 正文段落 14](https://arxiv.org/html/2611.34302v1#S2.SS1.p1.1)
- [S13] [2.2 Demonstration-Conditioned Robot Policies · 正文段落 15](https://arxiv.org/html/2611.34302v1#S2.SS2.p1.1)
- [S14] [2.2 Demonstration-Conditioned Robot Policies · 正文段落 16](https://arxiv.org/html/2611.34302v1#S2.F2.pic1)
- [S15] [2.2 Demonstration-Conditioned Robot Policies · 正文段落 17](https://arxiv.org/html/2611.34302v1#S2.F2)
- [S16] [2.3 Cross-Embodiment Latent World Models · 正文段落 18](https://arxiv.org/html/2611.34302v1#S2.SS3.p1.1)
- [S17] [3 Co-World Model · 正文段落 19](https://arxiv.org/html/2611.34302v1#S3.p1.1)
- [S18] [3.1 Human–Robot Co-Construction Objective · 正文段落 20](https://arxiv.org/html/2611.34302v1#S3.SS1.p1.1)
- [S19] [3.1 Human–Robot Co-Construction Objective · 正文段落 21](https://arxiv.org/html/2611.34302v1#S3.SS1.p2.1)
- [S20] [3.2 Shared World State and Private Context · 正文段落 30](https://arxiv.org/html/2611.34302v1#S3.SS2.p2.2)
- [S21] [3.2 Shared World State and Private Context · 正文段落 31](https://arxiv.org/html/2611.34302v1#S3.F3)
- [S22] [3.2 Shared World State and Private Context · 正文段落 32](https://arxiv.org/html/2611.34302v1#S3.SS2.p3.1)
- [S23] [4.1 Experimental Setup · 正文段落 114](https://arxiv.org/html/2611.34302v1#S4.SS1.p1.1)
- [S24] [4.1 Experimental Setup · 正文段落 115](https://arxiv.org/html/2611.34302v1#S4.SS1.p2.1)
- [S25] [4.1 Experimental Setup · 正文段落 116](https://arxiv.org/html/2611.34302v1#S4.F4.sf1)
- [S26] [4.1 Experimental Setup · 正文段落 117](https://arxiv.org/html/2611.34302v1#S4.F4.sf2)
- [S27] [4.1 Experimental Setup · 正文段落 118](https://arxiv.org/html/2611.34302v1#S4.F4)
- [S28] [4.1 Experimental Setup · 正文段落 119](https://arxiv.org/html/2611.34302v1#S4.SS1.p3.1)
- [S29] [4.1 Experimental Setup · 正文段落 120](https://arxiv.org/html/2611.34302v1#S4.SS1.p4.1)
- [S30] [4.1 Experimental Setup · 正文段落 121](https://arxiv.org/html/2611.34302v1#S4.SS1.p5.1)
- [S31] [4.2 Evaluation Protocol · 正文段落 123](https://arxiv.org/html/2611.34302v1#S4.SS2.p2.1)
- [S32] [4.2 Evaluation Protocol · 正文段落 128](https://arxiv.org/html/2611.34302v1#S4.SS2.p3.2)
- [S33] [4.2 Evaluation Protocol · 正文段落 130](https://arxiv.org/html/2611.34302v1#S4.SS2.p3.3)
- [S34] [4.2 Evaluation Protocol · 正文段落 131](https://arxiv.org/html/2611.34302v1#S4.SS2.p4.1)
- [S35] [4.2 Evaluation Protocol · 正文段落 134](https://arxiv.org/html/2611.34302v1#S4.SS2.p5.1)
- [S36] [4.2 Evaluation Protocol · 正文段落 136](https://arxiv.org/html/2611.34302v1#S4.SS2.p5.2)
- [S37] [4.2 Evaluation Protocol · 正文段落 143](https://arxiv.org/html/2611.34302v1#S4.SS2.p6.4)
- [S38] [4.2 Evaluation Protocol · 正文段落 144](https://arxiv.org/html/2611.34302v1#S4.SS2.p7.1)
- [S39] [4.2 Evaluation Protocol · 正文段落 146](https://arxiv.org/html/2611.34302v1#S4.SS2.p7.2)
- [S40] [4.2 Evaluation Protocol · 正文段落 149](https://arxiv.org/html/2611.34302v1#S4.SS2.p10.1)
- [S41] [4.2 Evaluation Protocol · 正文段落 153](https://arxiv.org/html/2611.34302v1#S4.I1.i4)
- [S42] [4.2 Evaluation Protocol · 正文段落 157](https://arxiv.org/html/2611.34302v1#S4.SS2.p13.1)
- [S43] [4.4 Ablation Study · 正文段落 186](https://arxiv.org/html/2611.34302v1#S4.T4.sf1)
- [S44] [4.4 Ablation Study · 正文段落 188](https://arxiv.org/html/2611.34302v1#S4.T4.sf2)
- [S45] [5 Conclusion · 正文段落 192](https://arxiv.org/html/2611.34302v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Laten.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning. Existing methods, however, either retarget human-specific geometry or match only static visual goals, and thus stumble over the cross-embodiment dynamics mismatch and the ungrounded action execution. We present the Co-World Model (CoWM), a predictive framework jointly optimized from paired yet unsynchronized human and robot streams. To bridge the cross-embodiment dynamics gap, CoWM disentangles each observation into a shared object-relation state and embodiment-specific context. It aligns latent actions across embodiments using effect-swap and action-sensitivity objectives,such that actions are matched by their predicted effects on the manipulated objects rather than by embodimentdependent kinematics. For grounded execution, a phase-aware receding-horizon controller estimates demonstration progress, projects the inferred human action prior onto the robot action-support density, and translates the resulting latent dynamics into executable robot commands. Extensive experiments in simulation and on two physical robot platforms demonstrate the effectiveness of CoWM, its cross-platform generalizability, and the contribution of each component. See the demo video in the supporting information for details.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34302v1
- Authors: Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling, Hui Wang, Sheng Liu, Miao Li
- Published: 2026-11-25T12:54:52Z
- Age days: 2

</details>
