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
url: "https://arxiv.org/abs/2611.05163v2"
published: "2026-11-03T16:35:42Z"
age_days: 2
score: 38
created: 2026-11-06
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboTryOn 把第一视角人手示范改成指定机器人在原场景做同一件事的视频，再从生成画面反推关节动作，做成能微调策略的示范。关键是把动作走向、机器人外观和关节标签分开处理。

## 问题

灵巧手遥操作需要协调许多关节，新任务一多就难以采集。直接遮住人手或叠加机器人渲染会改变策略看到的画面，相关基线还要同步处理部署时的相机流。把人手骨架直接映射到机器人也有误差，两种手的形态、可动范围和接触方式不同。[S4](https://arxiv.org/html/2611.05163v2#S1.p1.1) [S5](https://arxiv.org/html/2611.05163v2#S1.p2.1) [S6](https://arxiv.org/html/2611.05163v2#S1.p3.1)[S27](https://arxiv.org/html/2611.05163v2#S4.SS1.p2.1)

### 用一个例子理解

理解用例（非论文实验）。输入是从固定头部视角拍的双手把托盘移到桌角的视频，以及目标机器人参考图。系统生成该机器人搬同一托盘的视频，从画面估计各段关节动作，输出可用于训练的画面与动作对。

## 创新点或方法

图像和视频生成器先用机器人录像学习，以手臂遮罩和手部骨架作为人和机器人都能提供的输入。转换人类视频时，先用机器人参考图确定外观，后续关键帧参考上一张机器人关键帧，减少外观跳变。视频模型用这些关键帧和人手骨架的时序变化填中间动作。逆动力学模型利用深度特征反推关节标签，腕部位置另用手部重建修正。合成示范可单独或混合遥操作数据微调 VLA；部署时策略根据原始相机画面、机器人状态和指令出动作。[S7](https://arxiv.org/html/2611.05163v2#S1.p4.1)[S14](https://arxiv.org/html/2611.05163v2#S3.F1) [S15](https://arxiv.org/html/2611.05163v2#S3.SS5.p1.1) [S16](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.1) [S17](https://arxiv.org/html/2611.05163v2#S3.E6) [S18](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.2)[S27](https://arxiv.org/html/2611.05163v2#S4.SS1.p2.1)[S34](https://arxiv.org/html/2611.05163v2#A1.p1.1) [S35](https://arxiv.org/html/2611.05163v2#A1.p2.1)

### 方法如何工作

1. 用机器人录像和可共用的遮罩、骨架条件训练生成模型，建立从条件到机器人外观与运动的映射。[S7](https://arxiv.org/html/2611.05163v2#S1.p4.1)[S39](https://arxiv.org/html/2611.05163v2#A2.SS2.SSS8.p1.1)
2. 对人类视频逐个重绘选定帧，每次参考前一张机器人帧，让同一只手跨帧保持一致。[S14](https://arxiv.org/html/2611.05163v2#S3.F1)
3. 用机器人关键帧定位动作阶段，用人手骨架流补足阶段之间的运动，得到完整机器人视频。[S14](https://arxiv.org/html/2611.05163v2#S3.F1)
4. 从视频反推关节动作并修正腕部位置，把视频配成有动作标签的示范，再训练独立执行的策略。[S15](https://arxiv.org/html/2611.05163v2#S3.SS5.p1.1) [S16](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.1) [S17](https://arxiv.org/html/2611.05163v2#S3.E6) [S18](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.2)[S34](https://arxiv.org/html/2611.05163v2#A1.p1.1) [S35](https://arxiv.org/html/2611.05163v2#A1.p2.1)

### 必要术语

- 骨架流：手部关键点随时间的变化；在本文中约束关键帧之间的运动。
- 逆动力学模型（IDM）：从看到的状态变化反推可能的控制动作；在本文中给生成视频补上关节动作标签。

## 证据

OpenArm 和 RB-Y1 都做真机桌面测试。七项只有人类视频的新任务覆盖新物体、新目标、新技能与双臂操作，每任务随机摆位试 28 次。两机平均成功率从仅遥操作训练的 2.1% 到加入合成数据后的 60.0%，双臂任务为 45.9%。EgoMimic 和 Masquerade 用相同的策略模型与源数据做对比，节选未给它们的逐项结果。作者另报告合成数据单训能以约三分之一采集成本匹敌纯遥操作训练，具体成本口径需看对应实验。[S8](https://arxiv.org/html/2611.05163v2#S1.p5.1)[S26](https://arxiv.org/html/2611.05163v2#S4.SS1.p1.1) [S27](https://arxiv.org/html/2611.05163v2#S4.SS1.p2.1) [S28](https://arxiv.org/html/2611.05163v2#S4.SS1.p3.1) [S29](https://arxiv.org/html/2611.05163v2#S4.T1)

## 局限

作者指出，新机型仍需数小时遥操作素材，固定头部视角限制了对随身晃动视频的使用，像素反推也读不出力，难给紧配合插装提供足够准确的标签。[S34](https://arxiv.org/html/2611.05163v2#A1.p1.1) 我会核查把新机型采集和视频生成算力计入后，成本优势从多少任务开始出现。

- **判断**：值得读到动作标注和成本实验，视频看起来像机器人只是第一关，策略能否从标签学会接触动作才决定数据能不能用。

## 研究关联

采集可以按机器和任务拆开。先用一批机器人录像学会这台机器长什么样、怎样动，再为新任务录人类演示。若动作在机器人可达范围内、相机视角稳定，这种分工有机会减少逐任务遥操作。

### 下一步读哪里

先沿 [S14](https://arxiv.org/html/2611.05163v2#S3.F1) 跟一段视频如何变成动作标签，再按 [S29](https://arxiv.org/html/2611.05163v2#S4.T1) 区分只用遥操作、混训和纯合成三种结果。用 [S34](https://arxiv.org/html/2611.05163v2#A1.p1.1) [S35](https://arxiv.org/html/2611.05163v2#A1.p2.1) [S36](https://arxiv.org/html/2611.05163v2#A2.SS1.p1.1) [S37](https://arxiv.org/html/2611.05163v2#A2.T4) [S38](https://arxiv.org/html/2611.05163v2#A2.T4.4.1) [S39](https://arxiv.org/html/2611.05163v2#A2.SS2.SSS8.p1.1) 核查腕部修正、视角和新机型采集条件，再查成本实验如何计算人工与算力。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.05163v2
- 获取时间：2026-11-06T00:08:04.472699+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.05163v2#p1.1)
- [S2] [Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On · 正文段落 2](https://arxiv.org/html/2611.05163v2#abstract1.1)
- [S3] [Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On · 正文段落 3](https://arxiv.org/html/2611.05163v2#p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.05163v2#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.05163v2#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.05163v2#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.05163v2#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.05163v2#S1.p5.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.05163v2#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.05163v2#S1.I1.i3)
- [S11] [2 Related Work · 正文段落 13](https://arxiv.org/html/2611.05163v2#S2.p1.1)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2611.05163v2#S2.p2.1)
- [S13] [2 Related Work · 正文段落 15](https://arxiv.org/html/2611.05163v2#S2.p3.1)
- [S14] [3 Method · 正文段落 16](https://arxiv.org/html/2611.05163v2#S3.F1)
- [S15] [3.5 Policy Training · 正文段落 37](https://arxiv.org/html/2611.05163v2#S3.SS5.p1.1)
- [S16] [3.5 Policy Training · 正文段落 38](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.1)
- [S17] [3.5 Policy Training · 正文段落 39](https://arxiv.org/html/2611.05163v2#S3.E6)
- [S18] [3.5 Policy Training · 正文段落 40](https://arxiv.org/html/2611.05163v2#S3.SS5.p2.2)
- [S19] [4 Experiments · 正文段落 41](https://arxiv.org/html/2611.05163v2#S4.p1.1)
- [S20] [4 Experiments · 正文段落 42](https://arxiv.org/html/2611.05163v2#S4.I1.i1)
- [S21] [4 Experiments · 正文段落 43](https://arxiv.org/html/2611.05163v2#S4.I1.i2)
- [S22] [4 Experiments · 正文段落 44](https://arxiv.org/html/2611.05163v2#S4.I1.i3)
- [S23] [4.1 Experimental Setup · 正文段落 45](https://arxiv.org/html/2611.05163v2#S4.F2.2)
- [S24] [4.1 Experimental Setup · 正文段落 46](https://arxiv.org/html/2611.05163v2#S4.F2.3)
- [S25] [4.1 Experimental Setup · 正文段落 47](https://arxiv.org/html/2611.05163v2#S4.F2)
- [S26] [4.1 Experimental Setup · 正文段落 48](https://arxiv.org/html/2611.05163v2#S4.SS1.p1.1)
- [S27] [4.1 Experimental Setup · 正文段落 49](https://arxiv.org/html/2611.05163v2#S4.SS1.p2.1)
- [S28] [4.1 Experimental Setup · 正文段落 50](https://arxiv.org/html/2611.05163v2#S4.SS1.p3.1)
- [S29] [4.1 Experimental Setup · 正文段落 51](https://arxiv.org/html/2611.05163v2#S4.T1)
- [S30] [4.1 Experimental Setup · 正文段落 52](https://arxiv.org/html/2611.05163v2#S4.T1.st1)
- [S31] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2611.05163v2#S4.T1.st2)
- [S32] [4.4 Ablations · 正文段落 83](https://arxiv.org/html/2611.05163v2#S4.T3)
- [S33] [5 Conclusion · 正文段落 88](https://arxiv.org/html/2611.05163v2#S5.p1.1)
- [S34] [Appendix A Limitations and Future Work · 正文段落 90](https://arxiv.org/html/2611.05163v2#A1.p1.1)
- [S35] [Appendix A Limitations and Future Work · 正文段落 91](https://arxiv.org/html/2611.05163v2#A1.p2.1)
- [S36] [B.1 Policy Training Details · 正文段落 92](https://arxiv.org/html/2611.05163v2#A2.SS1.p1.1)
- [S37] [B.2.8 Training Setup · 正文段落 105](https://arxiv.org/html/2611.05163v2#A2.T4)
- [S38] [B.2.8 Training Setup · 正文段落 106](https://arxiv.org/html/2611.05163v2#A2.T4.4.1)
- [S39] [B.2.8 Training Setup · 正文段落 107](https://arxiv.org/html/2611.05163v2#A2.SS2.SSS8.p1.1)
- [S40] [B.2.8 Training Setup · 正文段落 108](https://arxiv.org/html/2611.05163v2#A2.SS2.SSS8.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/RoboTryOn Synthesizing Dexterous Robot Demonstrations from Human Videos via Virt.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keeps the person and swaps the garment, RoboTryOn keeps the demonstrated motion and swaps the human for the robot. Specifically, RoboTryOn converts a human video into a video of the target robot specified by a reference image, while preserving the original task, objects, and background. To maintain visual consistency, we translate selected keyframes autoregressively and use them to guide video synthesis with motion conditioned on the human hand skeleton. Additionally, we use an inverse dynamics model (IDM) that incorporates depth features to infer action labels from synthesized videos for policy learning. Our experiments across multiple humanoid embodiments show that policies trained with our synthetic data improve the average success rate on novel tasks, including challenging bimanual manipulation, from 2% to 60%, without any real robot demonstration of those tasks. Moreover, training with our synthetic data matches the performance of policies trained solely on teleoperated demonstrations at approximately a third of the collection cost, demonstrating the cost efficiency of our approach.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05163v2
- Authors: Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin
- Published: 2026-11-03T16:35:42Z
- Age days: 2

</details>
