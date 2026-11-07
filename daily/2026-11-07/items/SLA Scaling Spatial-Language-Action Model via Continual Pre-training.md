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
url: "https://arxiv.org/abs/2611.08373v1"
published: "2026-11-05T17:52:16Z"
age_days: 1
score: 35
created: 2026-11-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> SLA 在继续训练 π0.5 时，让内部视觉特征同时向冻结的三维感知教师学习，再把这种监督保留到下游适配。部署时移除教师和辅助模块，策略仍按原来的方式生成动作。

## 问题

机器人不仅要认出物体，还要判断空间关系并精确移动。直接加入深度或点云会遇到噪声、缺失和相机配置差异；只在单项任务微调时补空间监督，又限制了跨数据积累。本文要让空间学习进入更广泛的机器人继续预训练。[S5](https://arxiv.org/html/2611.08373v1#S1.p2.1) [S6](https://arxiv.org/html/2611.08373v1#S1.p3.1) [S7](https://arxiv.org/html/2611.08373v1#S1.p4.1) [S8](https://arxiv.org/html/2611.08373v1#S1.p5.1)

### 用一个例子理解

理解用例（非论文实验）：输入桌面画面和“拿起后面的瓶子”；训练时教师提供空间特征，督促策略区分前后关系。部署只输入原策略所需图像、指令和状态，输出接近并抓取瓶子的动作块，无需现场运行三维教师。

## 创新点或方法

旧做法在部署增加几何输入，或仅在下游补空间能力；SLA 用教师特征作为训练目标。教师结合 RGB 和可用的深度、标定信息生成空间表示；门控按当前特征聚合多个 VLA 层，与教师对齐，同时学习动作。随机丢弃状态输入以减少轨迹外推捷径。继续预训练和下游训练都保留对齐，推理不需新增深度、标定或教师。[S8](https://arxiv.org/html/2611.08373v1#S1.p5.1) [S16](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p1.1) [S17](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p4.1) [S18](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p4.2) [S19](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p5.1)

### 方法如何工作

1. 统一多机器人数据的末端动作与坐标约定，为跨数据空间学习建立共同基础。[S8](https://arxiv.org/html/2611.08373v1#S1.p5.1)
2. 冻结教师，从图像及可用几何标注提取空间特征，并重采样到策略视觉 token 的位置。[S16](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p1.1)
3. 用门控聚合策略多层特征，联合优化空间对齐与动作预测，让几何监督进入行动表示。[S8](https://arxiv.org/html/2611.08373v1#S1.p5.1) [S17](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p4.1)
4. 继续预训练后在下游保留该监督；推理移除辅助模块，沿用原策略结构输出动作。[S19](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p5.1)

### 必要术语

- 继续预训练：从已有策略出发，用广泛数据进一步学习；本文在此阶段加入空间监督。
- 空间对齐：让策略特征接近教师的三维相关特征；本文无需让策略直接输出三维重建。
- 特征依赖门控：根据当前输入决定各层特征的组合；本文用它适应不同数据域。
- 状态丢弃：训练时随机隐藏机器人状态；本文借此鼓励利用图像，减少仅凭状态推演动作。

## 证据

LIBERO-Plus 的 10,030 次评估成功率为 87.4%；RoboTwin Clean2Random 为 72.3%；RoboCasa-Panda 每任务用 50 条下游示范达到 68.4%。真机 RoboDojo-Real 三种机器人上，SLA 为 33.9%，π0.5 为 12.8%；八种自建部署条件平均为 83.8%，高出 π0.5 24.0 个百分点。[S9](https://arxiv.org/html/2611.08373v1#S1.p6.1) 后者按对象计成功，不能当作整回合成功率。[S26](https://arxiv.org/html/2611.08373v1#S4.SS1.p6.1) 结果支持多种场景的有效性，单个机制贡献还需消融。

## 局限

我的待核查问题是继续预训练的数据增量与空间对齐各贡献多少。[S9](https://arxiv.org/html/2611.08373v1#S1.p6.1) 报告双阶段对齐优于单阶段，但节选没有完整数值。数据统一也很关键：不同机器人坐标、动作和旋转处理错误可能影响迁移。真机跨平台仍经过联合适配，不能解释为无需示范的跨机器人零样本控制。

- **判断**：值得读到数据统一、门控和双阶段消融；它提供了一条不增加部署结构、却能利用异构几何监督的具体路线。

## 研究关联

可借鉴的是把训练时可获得、部署时不方便获得的信息转成表示监督。数据集几何标注不齐全时，也不必一律丢弃：教师可以利用已有标注，策略则学习部署时实际可用的视觉输入。

### 下一步读哪里

先看 [S16](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p1.1) 教师特征如何对齐到视觉 token，再核查门控权重、对齐损失和状态丢弃概率。重点检查等数据、等训练预算的 π0.5 对照；[S28](https://arxiv.org/html/2611.08373v1#S4.T9) 的旋转约定和 [S26](https://arxiv.org/html/2611.08373v1#S4.SS1.p6.1) 的对象级评估也是复现前必须确认的条件。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：35
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.08373v1
- 获取时间：2026-11-07T03:39:47.778850+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.08373v1#p1.1)
- [S2] [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training · 正文段落 2](https://arxiv.org/html/2611.08373v1#abstract1.1)
- [S3] [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training · 正文段落 3](https://arxiv.org/html/2611.08373v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.08373v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.08373v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.08373v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.08373v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.08373v1#S1.p5.1)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.08373v1#S1.p6.1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2611.08373v1#S1.I1.i2)
- [S11] [1 Introduction · 正文段落 13](https://arxiv.org/html/2611.08373v1#S1.I1.i3)
- [S12] [2.1 VLA Foundation Models · 正文段落 14](https://arxiv.org/html/2611.08373v1#S2.SS1.p1.1)
- [S13] [2.2 3D VLA Models · 正文段落 15](https://arxiv.org/html/2611.08373v1#S2.SS2.p1.1)
- [S14] [2.3 Continual Pre-training · 正文段落 16](https://arxiv.org/html/2611.08373v1#S2.SS3.p1.1)
- [S15] [3 Methodology · 正文段落 17](https://arxiv.org/html/2611.08373v1#S3.p1.1)
- [S16] [3.2.1 Model Architecture · 正文段落 27](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p1.1)
- [S17] [3.2.1 Model Architecture · 正文段落 36](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p4.1)
- [S18] [3.2.1 Model Architecture · 正文段落 38](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p4.2)
- [S19] [3.2.1 Model Architecture · 正文段落 39](https://arxiv.org/html/2611.08373v1#S3.SS2.SSS1.p5.1)
- [S20] [3.3.1 Data Sources · 正文段落 49](https://arxiv.org/html/2611.08373v1#S3.SS3.SSS1.p1.1)
- [S21] [4.1 Experimental Setup · 正文段落 70](https://arxiv.org/html/2611.08373v1#S4.SS1.p1.1)
- [S22] [4.1 Experimental Setup · 正文段落 71](https://arxiv.org/html/2611.08373v1#S4.SS1.p2.1)
- [S23] [4.1 Experimental Setup · 正文段落 72](https://arxiv.org/html/2611.08373v1#S4.SS1.p3.1)
- [S24] [4.1 Experimental Setup · 正文段落 73](https://arxiv.org/html/2611.08373v1#S4.SS1.p4.1)
- [S25] [4.1 Experimental Setup · 正文段落 74](https://arxiv.org/html/2611.08373v1#S4.SS1.p5.1)
- [S26] [4.1 Experimental Setup · 正文段落 75](https://arxiv.org/html/2611.08373v1#S4.SS1.p6.1)
- [S27] [4.3 Comparisons with State-of-The-Art Methods · 正文段落 79](https://arxiv.org/html/2611.08373v1#S4.SS3.p1.1)
- [S28] [4.4.4 Rotation Representation · 正文段落 104](https://arxiv.org/html/2611.08373v1#S4.T9)
- [S29] [4.5 Comparisons on Real-world Deployment · 正文段落 110](https://arxiv.org/html/2611.08373v1#S4.F5)
- [S30] [4.5 Comparisons on Real-world Deployment · 正文段落 111](https://arxiv.org/html/2611.08373v1#S4.F6)
- [S31] [4.5.1 Real-world Tasks · 正文段落 112](https://arxiv.org/html/2611.08373v1#S4.SS5.SSS1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/SLA Scaling Spatial-Language-Action Model via Continual Pre-training.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it during downstream post-training. Initialized from a pretrained pi05 policy, SLA jointly optimizes action prediction and alignment between intermediate visual embeddings and spatial representations from a frozen 3D perception model. We curate and unify heterogeneous robot datasets to support spatial learning across diverse embodiments, tasks, and scenes. To accommodate this diversity, we introduce feature-dependent gates that adaptively aggregate visual embeddings from multiple VLA layers for spatial supervision. The teacher further exploits partially available depth and camera calibration alongside RGB observations, enabling effective use of heterogeneous geometric annotations. Probabilistic state dropout encourages reliance on visual cues and mitigates overfitting to demonstration trajectories. All auxiliary components are used only during training, allowing direct reuse of pretrained VLA weights and preserving the original inference architecture.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08373v1
- Authors: Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li
- Published: 2026-11-05T17:52:16Z
- Age days: 1

</details>
