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
url: "https://arxiv.org/abs/2611.05163v1"
published: "2026-11-03T16:35:42Z"
age_days: 1
score: 38
created: 2026-11-05
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboTryOn 先把人类操作视频转换成机器人执行同一动作的视频，再从生成视频估计动作标签来训练策略。它把外观转换和动作估计分开，避免直接把人手姿态硬映射成灵巧手机器人的关节命令。

## 问题

任务是用人类视频教灵巧机器人新操作。直接遮掉人手或叠加机器人渲染，仍存在视觉差异；人手重建再重定向，还受手型、运动学和重建精度限制，姿态相似也不代表抓握力度合适。

### 用一个例子理解

理解用例（非论文实验）：输入人在固定头部视角下把海绵放进盒子的视频和机器人参考图；转换关键帧、补全运动，再估计手腕与关节动作；用这些观测—动作对训练策略，部署时机器人根据自己的相机画面完成放置。

## 创新点或方法

本文先用目标机器人参考图逐个转换关键帧，并参考前一机器人关键帧保持一致；再用人手骨架运动引导中间视频合成。含深度特征的 IDM 从机器人视频估计关节动作，重建手腕位置再作修正。生成器和 IDM 用机器人录像训练，无需成对人类—机器人示范；合成数据随后单独或混合遥操作数据训练 VLA。部署只运行策略读取真实画面、输出动作，不在线生成替身视频。[S7](https://arxiv.org/html/2611.05163v1#S1.p4.1) [S14](https://arxiv.org/html/2611.05163v1#S3.F1) [S15](https://arxiv.org/html/2611.05163v1#S3.SS5.p1.1) [S16](https://arxiv.org/html/2611.05163v1#S3.SS5.p2.1) [S17](https://arxiv.org/html/2611.05163v1#S3.E6) [S18](https://arxiv.org/html/2611.05163v1#S3.SS5.p2.2) [S34](https://arxiv.org/html/2611.05163v1#A1.p1.1) [S35](https://arxiv.org/html/2611.05163v1#A1.p2.1)

### 方法如何工作

1. 提取人类视频中的遮罩和手部骨架，建立生成模型训练与转换时共享的条件。
2. 顺序生成机器人关键帧，以前帧作参考，约束外观和场景一致性。
3. 用骨架运动连接关键帧，得到可供动作估计的机器人视频。
4. 用深度 IDM 和手腕重建生成伪标签，再训练策略，使合成视频变成可执行的监督数据。

### 必要术语

- 动作重定向：把人体姿态映射到机器人运动；本文避免仅靠这一步产生全部动作标签。
- 逆动力学模型 IDM：根据观测推测动作；本文用于给合成机器人视频补标签。
- 伪标签：模型估计而非真实执行记录的监督信号；其精度决定合成示范能教会什么。

## 证据

两台真机 OpenArm、RB-Y1 各测11任务，每任务28次；七个新任务各有50个人类视频、没有该任务机器人示范 [S26](https://arxiv.org/html/2611.05163v1#S4.SS1.p1.1) [S27](https://arxiv.org/html/2611.05163v1#S4.SS1.p2.1) [S28](https://arxiv.org/html/2611.05163v1#S4.SS1.p3.1) [S29](https://arxiv.org/html/2611.05163v1#S4.T1)。作者报告跨两机域外平均成功率从2.1%至60.0%，双臂任务45.9% [S8](https://arxiv.org/html/2611.05163v1#S1.p5.1)。EgoMimic、Masquerade 共享策略、遥操作数据和人类视频，以比较转换方式 [S27](https://arxiv.org/html/2611.05163v1#S4.SS1.p2.1)；但节选没给主表数值行，不能补出各基线成绩。约三分之一采集成本的比较见 [S8](https://arxiv.org/html/2611.05163v1#S1.p5.1)，具体成本构成尚需核查。

## 局限

作者明确：新增机型仍需数小时遥操作录像；伪标签不含力，精度不足以可靠标注紧插入；移动相机超出训练分布，且不能修复机器人够不到或手型做不到的动作。合成也把采集时间换成计算量 [S34](https://arxiv.org/html/2611.05163v1#A1.p1.1)。因此“新任务无机器人示范”不等于全流程零机器人数据。

- **判断**：值得细读动作标注与失败边界：真机结果支持它降低新任务示范门槛，但生成得像机器人并不保证动作标签足够精确。

## 研究关联

人类视频不必直接提供准确机器人动作，可以先转成目标机器人观测，再用学过机器人运动的模型补标签。值得尝试的条件是已有该机型基础录像，而新任务遥操作昂贵、又不依赖精细力控。

### 下一步读哪里

先读 [S34](https://arxiv.org/html/2611.05163v1#A1.p1.1) [S35](https://arxiv.org/html/2611.05163v1#A1.p2.1) 判断目标任务是否满足视角、可达性和精度条件；再核查深度 IDM 与手腕修正的消融，以及 [S29](https://arxiv.org/html/2611.05163v1#S4.T1) 完整主表中纯合成、混合数据各自成绩。成本比较需同时查看生成算力。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.05163v1
- 获取时间：2026-11-05T00:11:41.445663+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.05163v1#p1.1)
- [S2] [Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On · 正文段落 2](https://arxiv.org/html/2611.05163v1#abstract1.1)
- [S3] [Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On · 正文段落 3](https://arxiv.org/html/2611.05163v1#p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.05163v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.05163v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.05163v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.05163v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.05163v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2611.05163v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.05163v1#S1.I1.i3)
- [S11] [2 Related Work · 正文段落 13](https://arxiv.org/html/2611.05163v1#S2.p1.1)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2611.05163v1#S2.p2.1)
- [S13] [2 Related Work · 正文段落 15](https://arxiv.org/html/2611.05163v1#S2.p3.1)
- [S14] [3 Method · 正文段落 16](https://arxiv.org/html/2611.05163v1#S3.F1)
- [S15] [3.5 Policy Training · 正文段落 37](https://arxiv.org/html/2611.05163v1#S3.SS5.p1.1)
- [S16] [3.5 Policy Training · 正文段落 38](https://arxiv.org/html/2611.05163v1#S3.SS5.p2.1)
- [S17] [3.5 Policy Training · 正文段落 39](https://arxiv.org/html/2611.05163v1#S3.E6)
- [S18] [3.5 Policy Training · 正文段落 40](https://arxiv.org/html/2611.05163v1#S3.SS5.p2.2)
- [S19] [4 Experiments · 正文段落 41](https://arxiv.org/html/2611.05163v1#S4.p1.1)
- [S20] [4 Experiments · 正文段落 42](https://arxiv.org/html/2611.05163v1#S4.I1.i1)
- [S21] [4 Experiments · 正文段落 43](https://arxiv.org/html/2611.05163v1#S4.I1.i2)
- [S22] [4 Experiments · 正文段落 44](https://arxiv.org/html/2611.05163v1#S4.I1.i3)
- [S23] [4.1 Experimental Setup · 正文段落 45](https://arxiv.org/html/2611.05163v1#S4.F2.2)
- [S24] [4.1 Experimental Setup · 正文段落 46](https://arxiv.org/html/2611.05163v1#S4.F2.3)
- [S25] [4.1 Experimental Setup · 正文段落 47](https://arxiv.org/html/2611.05163v1#S4.F2)
- [S26] [4.1 Experimental Setup · 正文段落 48](https://arxiv.org/html/2611.05163v1#S4.SS1.p1.1)
- [S27] [4.1 Experimental Setup · 正文段落 49](https://arxiv.org/html/2611.05163v1#S4.SS1.p2.1)
- [S28] [4.1 Experimental Setup · 正文段落 50](https://arxiv.org/html/2611.05163v1#S4.SS1.p3.1)
- [S29] [4.1 Experimental Setup · 正文段落 51](https://arxiv.org/html/2611.05163v1#S4.T1)
- [S30] [4.1 Experimental Setup · 正文段落 52](https://arxiv.org/html/2611.05163v1#S4.T1.st1)
- [S31] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2611.05163v1#S4.T1.st2)
- [S32] [4.4 Ablations · 正文段落 83](https://arxiv.org/html/2611.05163v1#S4.T3)
- [S33] [5 Conclusion · 正文段落 88](https://arxiv.org/html/2611.05163v1#S5.p1.1)
- [S34] [Appendix A Limitations and Future Work · 正文段落 90](https://arxiv.org/html/2611.05163v1#A1.p1.1)
- [S35] [Appendix A Limitations and Future Work · 正文段落 91](https://arxiv.org/html/2611.05163v1#A1.p2.1)
- [S36] [B.1 Policy Training Details · 正文段落 92](https://arxiv.org/html/2611.05163v1#A2.SS1.p1.1)
- [S37] [B.2.8 Training Setup · 正文段落 105](https://arxiv.org/html/2611.05163v1#A2.T4)
- [S38] [B.2.8 Training Setup · 正文段落 106](https://arxiv.org/html/2611.05163v1#A2.T4.4.1)
- [S39] [B.2.8 Training Setup · 正文段落 107](https://arxiv.org/html/2611.05163v1#A2.SS2.SSS8.p1.1)
- [S40] [B.2.8 Training Setup · 正文段落 108](https://arxiv.org/html/2611.05163v1#A2.SS2.SSS8.p2.1)
- [S41] [C.1 Real-World Environment · 正文段落 121](https://arxiv.org/html/2611.05163v1#A3.F7.3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/RoboTryOn Synthesizing Dexterous Robot Demonstrations from Human Videos via Virt.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keeps the person and swaps the garment, RoboTryOn keeps the demonstrated motion and swaps the human for the robot. Specifically, RoboTryOn converts a human video into a video of the target robot specified by a reference image, while preserving the original task, objects, and background. To maintain visual consistency, we translate selected keyframes autoregressively and use them to guide video synthesis with motion conditioned on the human hand skeleton. Additionally, we use an inverse dynamics model (IDM) that incorporates depth features to infer action labels from synthesized videos for policy learning. Our experiments across multiple humanoid embodiments show that policies trained with our synthetic data improve the average success rate on novel tasks, including challenging bimanual manipulation, from 2% to 60%, without any real robot demonstration of those tasks. Moreover, training with our synthetic data matches the performance of policies trained solely on teleoperated demonstrations at approximately a third of the collection cost, demonstrating the cost efficiency of our approach.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05163v1
- Authors: Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin
- Published: 2026-11-03T16:35:42Z
- Age days: 1

</details>
