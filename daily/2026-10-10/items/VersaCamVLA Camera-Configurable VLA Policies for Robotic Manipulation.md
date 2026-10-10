---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.12451v1"
published: "2026-10-08T17:58:47Z"
age_days: 1
score: 33
created: 2026-10-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> VersaCamVLA 想让机器人换相机位置、增减相机后仍能操作。关键是先把数量可变、带位姿的图像压成固定大小的场景 tokens，再把它们作为补充信息交给基础 VLA。

## 问题

任务是根据图像和语言执行操作，但训练时固定的相机数量与位置容易变成策略的隐含依赖。部署时改变这些条件，视觉输入的组织方式就变了；摘要指出既有 VLA 对此脆弱。真正瓶颈是让动作策略使用场景信息，而不被某套相机配置绑住。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进托盘”和两路带位姿图像；编码器将它们汇成固定大小的场景信息，VLA 据此输出操作动作。若移走一路相机，接口大小仍保持一致，但任务能否完成还取决于剩余视角是否提供必要信息。

## 创新点或方法

旧做法让策略直接适应固定视角组合；本文在相机输入与动作学习之间加入统一接口。训练场景表示时，用多种信号预测目标视角，并通过 WAPS 利用腕部相机运动获得位姿变化，让不同视角集合学会表达同一场景。部署时，轻量空间编码器把场景 tokens 注入预训练 VLA，不需要显式三维传感或生成新视角图像。具体预测信号、损失以及基础 VLA 是否冻结，摘要未说明。

### 方法如何工作

1. 接收数量可变的 RGB 图像及对应相机位姿，为跨视角关联提供空间依据。
2. 训练时通过多信号目标视角预测学习场景表示，并用 WAPS 增加位姿多样性，减少对固定视角的依赖。
3. 把视图集合映射为固定大小的场景 tokens，使下游动作模型获得稳定的输入接口。
4. 部署时由轻量空间编码器注入这些 tokens，作为基础 VLA 的补充视觉条件来生成动作；具体注入方式摘要只说明到此。

### 必要术语

- 场景 tokens：一组压缩的场景信息向量；本文用它承接数量可变的相机输入。
- 相机位姿：相机在哪里、朝向哪里；帮助模型关联不同视角。
- WAPS：利用腕部相机运动进行位姿采样；本文用它增加训练视角变化。

## 证据

摘要报告在 RoboTwin、LIBERO 和真机平台测试，与既有 VLA 方法及直接多视角基线相比表现更好，且覆盖相机数量变化和未见相机位姿。未提供基线名称、指标定义、成功率、变化幅度和重复次数，因此能支持的是这些测试条件下的定性优势，不能判断任意相机布置都有效。

## 局限

这里不需要三维传感，但输入仍是带位姿的 RGB 视图，不能理解成无需相机标定。我的待核查问题是位姿误差、所有视角都遮挡目标以及相机大幅移位时会怎样；提供的摘要没有界定这些边界。仿真与真机结果也需分别查看。

- **判断**：值得读到场景表示的训练目标和相机变化实验，因为关键在于接口是否真正消除了配置依赖。

## 研究关联

可借鉴的是把可变传感器输入先变成稳定接口，让下游策略少承担输入配置变化。如果能取得相机位姿，并有足够视角变化用于训练，这种分工值得尝试。

### 下一步读哪里

先核查目标视角预测用了哪些信号、WAPS 如何选择样本，以及场景 tokens 如何进入 VLA；再看相机数量、未见位姿和标定误差是否分别测试，并确认比较方法获得了相同的视觉信息。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/VersaCamVLA Camera-Configurable VLA Policies for Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-Augmented Pose Sampling (WAPS), which leverages natural wrist-camera motion for free pose diversity. At deployment, a lightweight spatial encoder injects these compact scene tokens into a pretrained base VLA as a supplementary visual condition, requiring no explicit 3D sensing or novel-view rendering. Experiments on RoboTwin, LIBERO, and a real-robot platform demonstrate that VersaCamVLA consistently outperforms prior VLA methods and direct multi-view baselines, maintaining robust performance across varying camera counts and unseen camera poses.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12451v1
- Authors: Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang
- Published: 2026-10-08T17:58:47Z
- Age days: 1

</details>
