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
url: "https://arxiv.org/abs/2610.42021v1"
published: "2026-10-30T16:53:26Z"
age_days: 3
score: 36
created: 2026-11-03
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Nexus-VLA 用人类视频帮助机器人学动作，但不要求把人手动作硬变成机器人关节动作。它把“做什么、操作哪里、怎样移动、怎样接触”共同压入一个内部表示，再让这个表示直接参与连续动作生成。

## 问题

人类视频多，机器人示范贵，但两者外观、身体结构和控制空间不同。只对齐任务名称或手部轨迹，会遗漏其他共享信息；先学表示再适配机器人，又让人类知识间接影响动作。推理时显式生成多种语义中间结果还会增加延迟。[S3](https://arxiv.org/html/2610.42021v1#S1.p2.1) [S5](https://arxiv.org/html/2610.42021v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）：训练输入有人把杯子放进柜子的视频，以及不配对的机器人示范；标签分别描述目标、杯与柜的位置、手腕路径和接触。部署输入机器人当前图像及“收好杯子”，模型在内部形成语义表示，输出机器人连续动作，无需先说出四层描述。

## 创新点或方法

本文把分阶段对齐改为人类与机器人数据单阶段混合训练。离线专家为两类示范生成四层标签，共同约束一个 Semantic Latent；动作损失也反过来塑造它，使它既保留共享含义，又能服务控制。人类提供手腕运动监督，机器人额外提供关节监督，无效维度不计损失。推理时直接用潜在表示和视觉语言特征生成动作，不再逐项输出语义标签。[S6](https://arxiv.org/html/2610.42021v1#S1.p4.1) [S15](https://arxiv.org/html/2610.42021v1#S3.SS1.SSS3.p2.1) [S18](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p1.1) [S19](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p3.1) [S20](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p4.1) [S21](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS2.p2.1)

### 方法如何工作

1. 对未配对的人类与机器人示范离线标注意图、位置、运动和接触，建立双方都能使用的监督。
2. 共享视觉语言编码器提取特征，用多项预测目标塑造同一个潜在表示，使不同层次信息相互约束。
3. 把动作分为共享手腕或末端运动与机器人关节控制，只监督各来源真实具有的维度。
4. 联合优化语义与动作目标，部署时由潜在表示直接条件化连续动作生成，省去显式语义生成。

### 必要术语

- 跨身体对齐：找出人和机器人执行任务时共有的含义；本文跨四层建立对应。
- Semantic Latent：承载多层操作信息的内部向量；本文直接用它辅助动作生成。
- 动作掩码：标明哪些动作维度有可靠标签；本文避免把人类缺少的关节控制当成监督。

## 证据

主仿真覆盖 RoboCasa-GR1 的24项人形操作任务，使用24,000条机器人轨迹和21,446段筛选后人类视频；摘要报告成功率80.5%。[S22](https://arxiv.org/html/2610.42021v1#S4.SS1.p1.1) [S23](https://arxiv.org/html/2610.42021v1#S4.SS1.p2.1) 更能解释机制的是消融：相同层级监督下，独立表示改成统一潜在表示，成功率由76.92%升至78.25%；固定该设计再加人类共训，升至80.17%。[S25](https://arxiv.org/html/2610.42021v1#S4.SS3.p1.1) [S26](https://arxiv.org/html/2610.42021v1#S4.SS3.p2.1) 真机标准及四种 OOD 设置平均74.0%，但节选未给试验数。[S30](https://arxiv.org/html/2610.42021v1#S4.SS6.p2.1) 主结果与消融的不同数值应分别理解。

## 局限

作者对自动标签采用重检测、筛选和无效目标掩码，说明监督质量需要专门处理。[S33](https://arxiv.org/html/2610.42021v1#A1.SS1.SSS2.p1.1) [S34](https://arxiv.org/html/2610.42021v1#A1.SS1.SSS2.p3.1) 我的待核查问题是：筛掉的数据是否偏向困难交互，以及收益在不同人类数据量和采样比例下是否稳定。现有消融支持这些部件在该设置中的作用，不能据此断言四层语义是所有跨身体迁移的必要条件。

- **判断**：值得读到动作表示和损失实现：真正关键的是人类数据怎样进入同一个动作学习目标，以及缺失的机器人控制标签怎样被正确屏蔽。

## 研究关联

值得借鉴的是为跨来源数据寻找多层、可共用的监督，再让最终动作目标约束表示。这样既不用假装人手就是机器人关节，也不必把语义预测变成部署时额外执行的一串步骤。

### 下一步读哪里

先看[S18](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p1.1) [S19](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p3.1) [S20](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p4.1) [S21](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS2.p2.1)的共享运动空间、关节空间和有效维度掩码，再核查坐标归一化及人机采样比例。用[S25](https://arxiv.org/html/2610.42021v1#S4.SS3.p1.1) [S26](https://arxiv.org/html/2610.42021v1#S4.SS3.p2.1) [S27](https://arxiv.org/html/2610.42021v1#S4.F3) [S28](https://arxiv.org/html/2610.42021v1#S4.SS3.p3.1)区分监督、表示合并和增加人类数据的各自收益；还应查看离线专家成本及真机试验规模。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.42021v1
- 获取时间：2026-11-03T00:10:22.679396+00:00
- [S1] [Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space · 正文段落 1](https://arxiv.org/html/2610.42021v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.42021v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.42021v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.42021v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.42021v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.42021v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.42021v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.42021v1#S1.p7.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.42021v1#S1.p9.1)
- [S10] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.42021v1#S2.p1.1)
- [S11] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.42021v1#S2.p2.1)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.42021v1#S2.p3.1)
- [S13] [3 Method · 正文段落 16](https://arxiv.org/html/2610.42021v1#S3.p1.1)
- [S14] [3.1.1 Hierarchical Shared Manipulation Semantics · 正文段落 19](https://arxiv.org/html/2610.42021v1#S3.SS1.SSS1.p2.1)
- [S15] [3.1.3 Multi-level Semantic Shaping · 正文段落 28](https://arxiv.org/html/2610.42021v1#S3.SS1.SSS3.p2.1)
- [S16] [3.1.4 Semantics-Enhanced Action Generation · 正文段落 34](https://arxiv.org/html/2610.42021v1#S3.SS1.SSS4.p1.2)
- [S17] [3.2 End-to-End Human-Robot Mixed Training · 正文段落 35](https://arxiv.org/html/2610.42021v1#S3.SS2.p1.1)
- [S18] [3.2.1 Dual-Space Action Representation · 正文段落 36](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p1.1)
- [S19] [3.2.1 Dual-Space Action Representation · 正文段落 41](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p3.1)
- [S20] [3.2.1 Dual-Space Action Representation · 正文段落 42](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS1.p4.1)
- [S21] [3.2.2 Joint Optimization Objective · 正文段落 44](https://arxiv.org/html/2610.42021v1#S3.SS2.SSS2.p2.1)
- [S22] [4.1 Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.42021v1#S4.SS1.p1.1)
- [S23] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.42021v1#S4.SS1.p2.1)
- [S24] [4.1 Experimental Setup · 正文段落 55](https://arxiv.org/html/2610.42021v1#S4.SS1.p3.1)
- [S25] [4.3 Ablation Study and Learning Efficiency · 正文段落 61](https://arxiv.org/html/2610.42021v1#S4.SS3.p1.1)
- [S26] [4.3 Ablation Study and Learning Efficiency · 正文段落 62](https://arxiv.org/html/2610.42021v1#S4.SS3.p2.1)
- [S27] [4.3 Ablation Study and Learning Efficiency · 正文段落 63](https://arxiv.org/html/2610.42021v1#S4.F3)
- [S28] [4.3 Ablation Study and Learning Efficiency · 正文段落 64](https://arxiv.org/html/2610.42021v1#S4.SS3.p3.1)
- [S29] [4.6 Real-World Experiments · 正文段落 71](https://arxiv.org/html/2610.42021v1#S4.SS6.p1.1)
- [S30] [4.6 Real-World Experiments · 正文段落 72](https://arxiv.org/html/2610.42021v1#S4.SS6.p2.1)
- [S31] [4.6 Real-World Experiments · 正文段落 73](https://arxiv.org/html/2610.42021v1#S4.F6)
- [S32] [A.1 Hierarchical Semantic Supervision and Latent Representation Shaping · 正文段落 78](https://arxiv.org/html/2610.42021v1#A1.SS1.p1.1)
- [S33] [A.1.2 Data Quality Control and Low-Quality Sample Filtering · 正文段落 94](https://arxiv.org/html/2610.42021v1#A1.SS1.SSS2.p1.1)
- [S34] [A.1.2 Data Quality Control and Low-Quality Sample Filtering · 正文段落 96](https://arxiv.org/html/2610.42021v1#A1.SS1.SSS2.p3.1)
- [S35] [A.1.3 Semantic projectors and Training Objectives · 正文段落 98](https://arxiv.org/html/2610.42021v1#A1.T5)
- [S36] [A.1.3 Semantic projectors and Training Objectives · 正文段落 108](https://arxiv.org/html/2610.42021v1#A1.SS1.SSS3.p4.2)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/Nexus-VLA Bridging Human and Robot Experiences via a Shared Hierarchical Semanti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale egocentric human videos provide rich and scalable manipulation experience for robot policy learning, yet substantial embodiment gaps in visual appearance, kinematic structure, and action spaces hinder effective knowledge transfer. Existing methods often decouple cross-embodiment knowledge alignment from robot policy learning, making it difficult for human manipulation knowledge to directly and fully contribute to robot action learning. To address this issue, we propose Nexus-VLA, a hybrid policy learning framework that enables cross-embodiment knowledge transfer through end-to-end human-robot joint training, allowing human manipulation experience to directly contribute to robot policy learning. We first introduce a hierarchical cross-embodiment semantic alignment paradigm that progressively establishes shared manipulation semantics from task intent to fine-grained interactions, enabling more complete use of the manipulation knowledge contained in human videos. Building on this hierarchy, we design a shared manipulation latent representation that jointly encodes multi-level shared knowledge into an internal representation directly used for continuous action generation, improving policy learning efficiency while effectively leveraging human knowledge. Across RoboCasa-GR1, OOD settings, and real-world robot experiments, Nexus-VLA achieves an 80.5% task success rate on RoboCasa-GR1 and demonstrates strong advantages in human-data utilization, learning efficiency, and cross-scenario generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.42021v1
- Authors: Biaoliang Guan, Tingyu Yuan, Wen Ye, Ziming Ji, Xu Yang, Yan Huang, Jihua Zhu, Chaoyang Zhao
- Published: 2026-10-30T16:53:26Z
- Age days: 3

</details>
