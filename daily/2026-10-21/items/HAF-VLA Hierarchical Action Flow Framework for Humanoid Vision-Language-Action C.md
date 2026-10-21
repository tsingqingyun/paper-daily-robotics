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
url: "https://arxiv.org/abs/2610.26584v1"
published: "2026-10-19T15:33:34Z"
age_days: 1
score: 42
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> HAF-VLA 不再一次生成全部人形机器人动作，而是先生成移动和头部动作，再加入腰部，最后生成全身操作。后续阶段读取前面阶段的动作表示并允许小幅修正，让双臂操作建立在较一致的身体移动方案上。

## 问题

人形机器人接近目标时，底座位置、腰部姿态和手臂可达性互相影响。若一次无结构地生成所有动作，移动误差可能迫使上身剧烈补偿；固定底座或轮式机器人上学到的动作生成方式未必适用[S4](https://arxiv.org/html/2610.26584v1#S1.p1.1) [S5](https://arxiv.org/html/2610.26584v1#S1.p2.1)。任务是保持移动、注视与双臂操作协调的长流程控制。

### 用一个例子理解

理解用例（非论文实验）：输入“把箱子放到远处桌上”和第一视角画面；先生成接近方向及头部动作，再加入腰部姿态，最后结合前面的表示生成双臂搬放动作并修正站位；执行一段后重新观察。

## 创新点或方法

本文复用π₀.₅编码器和动作专家，用阶段嵌入区分三次生成。各阶段在同一全身动作空间里逐步扩大活动维度，后面能修改前面维度，而非把三个身体片段简单拼起来[S39](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.1) [S40](https://arxiv.org/html/2610.26584v1#A2.E8) [S41](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.2) [S42](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.1) [S43](https://arxiv.org/html/2610.26584v1#A2.E9) [S44](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.2) [S45](https://arxiv.org/html/2610.26584v1#A2.E10) [S46](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.3) [S47](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p3.1)。训练按阶段做流匹配，前阶段缓存来自真实示范；推理缓存来自模型预测，每阶段独立从噪声开始去噪，再执行最终阶段动作的前40步后重规划[S18](https://arxiv.org/html/2610.26584v1#S3.SS4.p3.1) [S19](https://arxiv.org/html/2610.26584v1#S3.SS4.p4.1)。这样用有顺序的条件传递约束身体协调。

### 方法如何工作

1. 从图像和语言获得共享条件，使各阶段面对同一任务与场景。
2. 先生成移动和头部动作并保存表示，为后续姿态与操作提供身体位置依据。
3. 在读取前阶段缓存后加入腰部，再生成全身动作，同时允许修正早期维度以保持协调。
4. 执行最终动作段的一部分后重新观察，更新身体与目标关系，再重复三阶段生成。

### 必要术语

- 流匹配：学习把噪声逐渐变成示范动作的方向；承担各阶段动作生成。
- KV缓存：可供后续注意力读取的中间表示；本文传递前阶段动作信息。
- 累计动作掩码：后阶段包含前阶段已启用的身体维度；使后续可以细化早期动作。

## 证据

在天工2.0与3.0上，每任务采集120条示范，主测试六任务、各设置10次真机运行[S21](https://arxiv.org/html/2610.26584v1#S4.SS1.p1.1) [S24](https://arxiv.org/html/2610.26584v1#S4.SS1.p3.1)。对比ACT、π₀.₅、GR00T N1.7和Cosmos Policy，平均归一化阶段得分由最强基线π₀.₅的53.3%升至68.3%[S29](https://arxiv.org/html/2610.26584v1#S4.T1.4)。搬箱消融中完整方法86.7%，训练部署均去缓存为50.0%，改成手臂优先为60.0%[S32](https://arxiv.org/html/2610.26584v1#S4.T2.4)。支持该设置下顺序与缓存有用；这些分数不是完整成功率。

## 局限

作者明确承认多阶段增加去噪预算，并仍受基础模型先验限制[S38](https://arxiv.org/html/2610.26584v1#S5.p1.1)。训练用真实动作缓存、推理用预测缓存存在输入差异，陌生任务下误差会不会逐级传播仍需核查。部署时突然去掉缓存导致不安全[S33](https://arxiv.org/html/2610.26584v1#S4.SS3.p4.1)，说明条件一致性重要，不能单凭这一结果解释全部收益来源。

- **判断**：值得细读累计动作掩码与缓存实现；真实硬件和受控消融提供了理由，但还不足以证明这种阶段顺序适合所有全身任务。

## 研究关联

可借鉴的是按身体依赖组织生成：先确定支撑后续操作的移动与姿态，再生成精细操作，同时留出回修空间。若误差常表现为手臂替错误站位补偿，这比单纯增加去噪步数更有针对性。

### 下一步读哪里

重点读[S39](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.1) [S40](https://arxiv.org/html/2610.26584v1#A2.E8) [S41](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.2) [S42](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.1) [S43](https://arxiv.org/html/2610.26584v1#A2.E9) [S44](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.2) [S45](https://arxiv.org/html/2610.26584v1#A2.E10) [S46](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.3) [S47](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p3.1)确认阶段是累计细化，再看[S32](https://arxiv.org/html/2610.26584v1#S4.T2.4) [S33](https://arxiv.org/html/2610.26584v1#S4.SS3.p4.1) [S34](https://arxiv.org/html/2610.26584v1#S4.SS3.p5.1)区分顺序、缓存和回修的作用。下一步核查低层步行控制接口、阶段得分细则、误差范围，以及真实缓存与预测缓存的训练推理差异。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.26584v1
- 获取时间：2026-10-21T00:33:54.220982+00:00
- [S1] [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control · 正文段落 1](https://arxiv.org/html/2610.26584v1#abstract1.1)
- [S2] [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control · 正文段落 2](https://arxiv.org/html/2610.26584v1#p2.1.1)
- [S3] [HAF-VLA: Hierarchical Action Flow Framework for Humanoid Vision-Language-Action Control · 正文段落 3](https://arxiv.org/html/2610.26584v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.26584v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.26584v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.26584v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.26584v1#S1.p5.1)
- [S8] [2 Related Work · 正文段落 9](https://arxiv.org/html/2610.26584v1#S2.p1.1)
- [S9] [2 Related Work · 正文段落 10](https://arxiv.org/html/2610.26584v1#S2.p2.1)
- [S10] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.26584v1#S2.p3.1)
- [S11] [3 HAF-VLA · 正文段落 12](https://arxiv.org/html/2610.26584v1#S3.p1.1)
- [S12] [3.3 Cross-Stage KV-Cache Conditioning · 正文段落 27](https://arxiv.org/html/2610.26584v1#S3.SS3.p2.2)
- [S13] [3.4 Training and Receding-Horizon Inference · 正文段落 32](https://arxiv.org/html/2610.26584v1#S3.SS4.p1.1)
- [S14] [3.4 Training and Receding-Horizon Inference · 正文段落 33](https://arxiv.org/html/2610.26584v1#S3.SS4.p2.1)
- [S15] [3.4 Training and Receding-Horizon Inference · 正文段落 34](https://arxiv.org/html/2610.26584v1#S3.E8)
- [S16] [3.4 Training and Receding-Horizon Inference · 正文段落 35](https://arxiv.org/html/2610.26584v1#S3.SS4.p2.2)
- [S17] [3.4 Training and Receding-Horizon Inference · 正文段落 36](https://arxiv.org/html/2610.26584v1#S3.E9)
- [S18] [3.4 Training and Receding-Horizon Inference · 正文段落 37](https://arxiv.org/html/2610.26584v1#S3.SS4.p3.1)
- [S19] [3.4 Training and Receding-Horizon Inference · 正文段落 38](https://arxiv.org/html/2610.26584v1#S3.SS4.p4.1)
- [S20] [4 Experiments · 正文段落 39](https://arxiv.org/html/2610.26584v1#S4.p1.1)
- [S21] [4.1 Experiment Setup · 正文段落 40](https://arxiv.org/html/2610.26584v1#S4.SS1.p1.1)
- [S22] [4.1 Experiment Setup · 正文段落 41](https://arxiv.org/html/2610.26584v1#S4.F3)
- [S23] [4.1 Experiment Setup · 正文段落 42](https://arxiv.org/html/2610.26584v1#S4.SS1.p2.1)
- [S24] [4.1 Experiment Setup · 正文段落 43](https://arxiv.org/html/2610.26584v1#S4.SS1.p3.1)
- [S25] [4.1 Experiment Setup · 正文段落 44](https://arxiv.org/html/2610.26584v1#S4.F4)
- [S26] [4.1 Experiment Setup · 正文段落 45](https://arxiv.org/html/2610.26584v1#S4.SS1.p4.1)
- [S27] [4.2 Q1: Does HAF-VLA enable long-horizon humanoid loco–manipulation beyond existing SOTA methods? · 正文段落 46](https://arxiv.org/html/2610.26584v1#S4.SS2.p1.1)
- [S28] [4.2 Q1: Does HAF-VLA enable long-horizon humanoid loco–manipulation beyond existing SOTA methods? · 正文段落 47](https://arxiv.org/html/2610.26584v1#S4.T1)
- [S29] [4.2 Q1: Does HAF-VLA enable long-horizon humanoid loco–manipulation beyond existing SOTA methods? · 正文段落 48](https://arxiv.org/html/2610.26584v1#S4.T1.4)
- [S30] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 49](https://arxiv.org/html/2610.26584v1#S4.SS3.p1.1)
- [S31] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 50](https://arxiv.org/html/2610.26584v1#S4.T2)
- [S32] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 51](https://arxiv.org/html/2610.26584v1#S4.T2.4)
- [S33] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 54](https://arxiv.org/html/2610.26584v1#S4.SS3.p4.1)
- [S34] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 55](https://arxiv.org/html/2610.26584v1#S4.SS3.p5.1)
- [S35] [4.3 Q2: Which design choices contribute to the performance of HAF-VLA? · 正文段落 56](https://arxiv.org/html/2610.26584v1#S4.F5)
- [S36] [4.4 Q3: Does HAF-VLA generalize to unseen distribution shifts? · 正文段落 58](https://arxiv.org/html/2610.26584v1#S4.F6)
- [S37] [4.4 Q3: Does HAF-VLA generalize to unseen distribution shifts? · 正文段落 59](https://arxiv.org/html/2610.26584v1#S4.SS4.p2.1)
- [S38] [5 Limitations and Conclusion · 正文段落 62](https://arxiv.org/html/2610.26584v1#S5.p1.1)
- [S39] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 107](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.1)
- [S40] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 108](https://arxiv.org/html/2610.26584v1#A2.E8)
- [S41] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 109](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p1.2)
- [S42] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 110](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.1)
- [S43] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 111](https://arxiv.org/html/2610.26584v1#A2.E9)
- [S44] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 112](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.2)
- [S45] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 113](https://arxiv.org/html/2610.26584v1#A2.E10)
- [S46] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 114](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p2.3)
- [S47] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 115](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px1.p3.1)
- [S48] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 117](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px3.p1.1)
- [S49] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 118](https://arxiv.org/html/2610.26584v1#A2.E11)
- [S50] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 119](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px3.p1.2)
- [S51] [S2.3 Implementation Details of Q2 Ablation Variants · 正文段落 121](https://arxiv.org/html/2610.26584v1#A2.SS3.SSS0.Px3.p1.3)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/HAF-VLA Hierarchical Action Flow Framework for Humanoid Vision-Language-Action C.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet adapting generalist vision-language-action (VLA) policies to real-world humanoid loco-manipulation remains challenging. Unlike fixed-base or wheeled manipulators, humanoids must coordinate locomotion, posture, gaze, and dual-arm manipulation over a high-dimensional whole-body action space, where inaccurate base or waist motions can easily induce unstable and aggressive upper-body compensation. We propose HAF-VLA, a hierarchical action-flow framework for humanoid VLA control. Built upon a pretrained flow-matching VLA, HAF-VLA inherits the vision-language prefix encoder and action expert weights, and adapts them to humanoid whole-body loco-manipulation with learnable stage embeddings and cross-stage KV-cache conditioning. Instead of generating the full action chunk in a single pass, HAF-VLA progressively denoises a shared whole-body action space: first locomotion and head commands, then waist refinement, and finally full-body manipulation. To preserve structural dependencies across stages, we introduce a cross-stage KV cache conditioning mechanism, enabling subsequent action generation stages to refine and augment their outputs based on the action representations from preceding stages. Experimental results across six real-world tasks demonstrate that our framework significantly enhances the performance of existing models in humanoid loco-manipulation tasks, demonstrating an effective pathway for adapting strong mobile-manipulation VLAs to humanoid whole-body loco-manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26584v1
- Authors: Langzhe Gu, Chengkai Hou, Meng Li, Xinhua Wang, Xinyuan Lv, Shuanghao Bai, Guangrun Li, Jingyang He, Ziluo Ding, Zhiyuan Xu, Ning Ding, Kuan Cheng, Jian Tang, Shanghang Zhang, Zhengping Che
- Published: 2026-10-19T15:33:34Z
- Age days: 1

</details>
