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
url: "https://arxiv.org/abs/2610.40349v1"
published: "2026-10-29T16:06:36Z"
age_days: 2
score: 40
created: 2026-11-01
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> TouchBridge 把人手示范转换成机器人训练数据，核心 Tac-Retarget 不只对齐指尖姿势，还利用触觉保住接触区域及多个接触点的相对关系。这样无需为每件物体建模型或做仿真修正，也能迁移部分接触密集任务。

## 问题

人手和机器人手的尺寸、关节不同，照搬指尖位置可能让手指离开支撑区域，或破坏双手接触关系。依靠物体网格、位姿和仿真补救又增加逐物体建模成本，使快速采集的人类示范难以直接用于训练。[S3](https://arxiv.org/html/2610.40349v1#S1.p2.1) [S4](https://arxiv.org/html/2610.40349v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）：人戴传感手套旋开小罐盖；输入视频、指尖运动和接触分布，转换器求出机器人手姿态并保留对向接触关系，合成机器人示范；输出用于训练旋盖策略的数据，而非直接复制人的关节角。

## 创新点或方法

本文把“匹配手的姿态”改成同时匹配姿态、触觉接触斑块和活跃接触间的空间关系。硬件先对应布置人机腕部相机与指尖传感器；离线转换时去除视频中的人手并补画背景，再渲染机器人手，结合相机坐标中的动作构造训练序列。之后微调预训练 VLA；部署运行训练后的机器人策略，无需在线重做人体重定向。[S6](https://arxiv.org/html/2610.40349v1#S1.p5.1) [S7](https://arxiv.org/html/2610.40349v1#S1.p6.1) [S18](https://arxiv.org/html/2610.40349v1#S3.F3) [S19](https://arxiv.org/html/2610.40349v1#S3.SS1.p1.1) [S20](https://arxiv.org/html/2610.40349v1#S3.SS1.SSS1.p1.1) [S21](https://arxiv.org/html/2610.40349v1#S3.SS2.SSS4.p2.2) [S22](https://arxiv.org/html/2610.40349v1#S3.F4) [S23](https://arxiv.org/html/2610.40349v1#S3.SS3.SSS1.p1.1) 所给节选未完整列出策略观察张量，不能据此断言触觉是否直接输入 VLA。

### 方法如何工作

1. 同步采集相机、手部运动和指尖触觉，并转到统一相机坐标，给跨手型转换建立对应关系。
2. 优化机器人手姿态，兼顾指尖位置、接触区域及活跃接触关系，减少姿势正确却接触失效的情况。
3. 擦除人手并渲染机器人手，配合转换动作形成机器人域示范，缩小训练观察与部署外观的差距。
4. 用转换示范微调预训练策略，再在真机评估任务成功，检查接触保留是否转成实际能力。

### 必要术语

- 重定向：把人的动作转换为不同结构机器人能执行的动作；本文增加触觉约束。
- 接触斑块：指尖上实际受接触的一片区域；用于对齐接触位置与分布。
- 接触激活图：把正在接触的部位连成关系图；用于保留同手或双手接触间的空间关系。

## 证据

Moz1 双臂配 Wuji Hands，在翻书、拧灯泡、涂酱和抓蛋卷四项真机任务测试；每任务用 60 条示范微调 GR00T N1.7，评估 20 次。[S30](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS1.p1.1) [S31](https://arxiv.org/html/2610.40349v1#S4.F6) [S32](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS2.p1.1) [S33](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS4.p1.1) [S34](https://arxiv.org/html/2610.40349v1#S4.SS2.p1.1) [S35](https://arxiv.org/html/2610.40349v1#S4.T2) [S36](https://arxiv.org/html/2610.40349v1#S4.SS3.p1.1) 人类转换数据平均成功率 72.5%，等量遥操作数据为 77.5%；同训练条件下比 DexPilot、UniDex 高 25.0、42.5 个百分点。[S37](https://arxiv.org/html/2610.40349v1#S4.SS3.p2.1) [S41](https://arxiv.org/html/2610.40349v1#S4.SS4.SSS2.p1.1) 每条成功示范采集耗时 11.7 对 81.7 秒，约快 7 倍，计入失败和重置。[S31](https://arxiv.org/html/2610.40349v1#S4.F6) [S38](https://arxiv.org/html/2610.40349v1#S4.SS3.p3.1) 支持这组硬件和任务上的数据替代能力，尚非大规模跨手型验证。

## 局限

作者明确说示范规模仍小，更大更多样的数据有待研究。[S45](https://arxiv.org/html/2610.40349v1#S5.p1.1) 七倍是采集速度，不能当成含标定、视频合成和训练的全流程加速；免仿真指数据转换，论文仍用仿真评估接触保持。[S39](https://arxiv.org/html/2610.40349v1#S4.SS4.p1.1) 我会进一步核查传感器噪声及不同手型下的硬件适配成本。

- **判断**：值得深读接触目标与硬件标定；它较具体地展示了触觉如何改善示范转换，而规模化收益仍需扩大验证。

## 研究关联

启示是跨手型迁移应保留“交互中什么必须不变”。接触区域和接触点关系往往比绝对指尖坐标更接近任务要求，尤其适合姿势相似却总在接触时失败的情形。

### 下一步读哪里

先核查 [S18](https://arxiv.org/html/2610.40349v1#S3.F3) [S21](https://arxiv.org/html/2610.40349v1#S3.SS2.SSS4.p2.2) 接触斑块与图约束如何计算，再看 [S23](https://arxiv.org/html/2610.40349v1#S3.SS3.SSS1.p1.1) 遮挡合成是否破坏物体外观。结合 [S41](https://arxiv.org/html/2610.40349v1#S4.SS4.SSS2.p1.1) [S43](https://arxiv.org/html/2610.40349v1#S4.SS5.p1.1) 检查触觉消融和预训练依赖，并补查部署输入、标定误差与转换耗时。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.40349v1
- 获取时间：2026-11-01T02:25:04.439883+00:00
- [S1] [TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation · 正文段落 1](https://arxiv.org/html/2610.40349v1#abstract1.1)
- [S2] [I INTRODUCTION · 正文段落 2](https://arxiv.org/html/2610.40349v1#S1.p1.1)
- [S3] [I INTRODUCTION · 正文段落 3](https://arxiv.org/html/2610.40349v1#S1.p2.1)
- [S4] [I INTRODUCTION · 正文段落 4](https://arxiv.org/html/2610.40349v1#S1.p3.1)
- [S5] [I INTRODUCTION · 正文段落 5](https://arxiv.org/html/2610.40349v1#S1.p4.1)
- [S6] [I INTRODUCTION · 正文段落 6](https://arxiv.org/html/2610.40349v1#S1.p5.1)
- [S7] [I INTRODUCTION · 正文段落 7](https://arxiv.org/html/2610.40349v1#S1.p6.1)
- [S8] [I INTRODUCTION · 正文段落 8](https://arxiv.org/html/2610.40349v1#S1.p7.1)
- [S9] [I INTRODUCTION · 正文段落 10](https://arxiv.org/html/2610.40349v1#S1.I1.i1)
- [S10] [I INTRODUCTION · 正文段落 11](https://arxiv.org/html/2610.40349v1#S1.I1.i2)
- [S11] [I INTRODUCTION · 正文段落 12](https://arxiv.org/html/2610.40349v1#S1.I1.i3)
- [S12] [II-A Learning from Human Demonstrations · 正文段落 13](https://arxiv.org/html/2610.40349v1#S2.SS1.p1.1)
- [S13] [II-A Learning from Human Demonstrations · 正文段落 14](https://arxiv.org/html/2610.40349v1#S2.T1)
- [S14] [II-A Learning from Human Demonstrations · 正文段落 15](https://arxiv.org/html/2610.40349v1#S2.T1.9)
- [S15] [II-B Dexterous Retargeting · 正文段落 16](https://arxiv.org/html/2610.40349v1#S2.SS2.p1.1)
- [S16] [II-B Dexterous Retargeting · 正文段落 17](https://arxiv.org/html/2610.40349v1#S2.SS2.p2.1)
- [S17] [II-B Dexterous Retargeting · 正文段落 18](https://arxiv.org/html/2610.40349v1#S2.F2)
- [S18] [III Method · 正文段落 19](https://arxiv.org/html/2610.40349v1#S3.F3)
- [S19] [III-A Human-Robot Vision and Tactile System · 正文段落 20](https://arxiv.org/html/2610.40349v1#S3.SS1.p1.1)
- [S20] [III-A1 Human Demonstration Interface · 正文段落 21](https://arxiv.org/html/2610.40349v1#S3.SS1.SSS1.p1.1)
- [S21] [III-B4 Contact Graph · 正文段落 38](https://arxiv.org/html/2610.40349v1#S3.SS2.SSS4.p2.2)
- [S22] [III-C Human-to-Robot Data Transformation Pipeline · 正文段落 41](https://arxiv.org/html/2610.40349v1#S3.F4)
- [S23] [III-C1 Robot-Domain Observation Synthesis · 正文段落 42](https://arxiv.org/html/2610.40349v1#S3.SS3.SSS1.p1.1)
- [S24] [III-C2 Camera-anchored Action Construction · 正文段落 47](https://arxiv.org/html/2610.40349v1#S3.F5)
- [S25] [IV Experiments · 正文段落 48](https://arxiv.org/html/2610.40349v1#S4.p1.1)
- [S26] [IV Experiments · 正文段落 49](https://arxiv.org/html/2610.40349v1#S4.I1.i1)
- [S27] [IV Experiments · 正文段落 50](https://arxiv.org/html/2610.40349v1#S4.I1.i2)
- [S28] [IV Experiments · 正文段落 51](https://arxiv.org/html/2610.40349v1#S4.I1.i3)
- [S29] [IV Experiments · 正文段落 52](https://arxiv.org/html/2610.40349v1#S4.I1.i4)
- [S30] [IV-A1 Robot Platform and Policy Execution · 正文段落 53](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS1.p1.1)
- [S31] [IV-A1 Robot Platform and Policy Execution · 正文段落 54](https://arxiv.org/html/2610.40349v1#S4.F6)
- [S32] [IV-A2 Task Descriptions · 正文段落 55](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS2.p1.1)
- [S33] [IV-A4 Evaluation Protocol · 正文段落 62](https://arxiv.org/html/2610.40349v1#S4.SS1.SSS4.p1.1)
- [S34] [IV-B Evaluation of Human-Derived Robot Demonstrations · 正文段落 63](https://arxiv.org/html/2610.40349v1#S4.SS2.p1.1)
- [S35] [IV-B2 Action Replay · 正文段落 69](https://arxiv.org/html/2610.40349v1#S4.T2)
- [S36] [IV-C Policy Learning from Human-Derived vs. Robot Demonstrations · 正文段落 71](https://arxiv.org/html/2610.40349v1#S4.SS3.p1.1)
- [S37] [IV-C Policy Learning from Human-Derived vs. Robot Demonstrations · 正文段落 72](https://arxiv.org/html/2610.40349v1#S4.SS3.p2.1)
- [S38] [IV-C Policy Learning from Human-Derived vs. Robot Demonstrations · 正文段落 73](https://arxiv.org/html/2610.40349v1#S4.SS3.p3.1)
- [S39] [IV-D Evaluation of Tac-Retarget · 正文段落 74](https://arxiv.org/html/2610.40349v1#S4.SS4.p1.1)
- [S40] [IV-D2 Downstream Policy Performance · 正文段落 78](https://arxiv.org/html/2610.40349v1#S4.F9)
- [S41] [IV-D2 Downstream Policy Performance · 正文段落 79](https://arxiv.org/html/2610.40349v1#S4.SS4.SSS2.p1.1)
- [S42] [IV-D2 Downstream Policy Performance · 正文段落 80](https://arxiv.org/html/2610.40349v1#S4.SS4.SSS2.p2.1)
- [S43] [IV-E Effect of Policy Pretraining · 正文段落 81](https://arxiv.org/html/2610.40349v1#S4.SS5.p1.1)
- [S44] [IV-E Effect of Policy Pretraining · 正文段落 82](https://arxiv.org/html/2610.40349v1#S4.F10)
- [S45] [V Conclusion · 正文段落 83](https://arxiv.org/html/2610.40349v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/TouchBridge Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions. We present TouchBridge, a hardware--software co-designed framework for human-to-robot data transformation. A wearable human demonstration interface and a corresponding robot interface establish cross-embodiment correspondence in visual and fingertip tactile sensing. We introduce Tac-Retarget, a tactile-conditioned retargeting method that uses measured contact to align fingertip contact patches and preserve their spatial relations within and across hands. Unlike object-aware or simulation-based transfer pipelines, Tac-Retarget requires no object mesh, object-pose estimate, or physics simulation for retargeting, enabling direct and scalable conversion of human demonstrations into robot-domain training data. Combined with visual synthesis and camera-anchored action conversion, TouchBridge produces robot-domain demonstrations for fine-tuning a pretrained vision-language-action (VLA) model. Across four real-world contact-rich tasks, policies fine-tuned solely on TouchBridge-converted human demonstrations achieve a 72.5% average success rate, compared with 77.5% using an equal number of teleoperated robot demonstrations, while human demonstration collection is 7.0x faster. Under the same policy and training setup, Tac-Retarget outperforms DexPilot and UniDex by 25.0 and 42.5 percentage points, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40349v1
- Authors: Haozhe Zhang, Gu Zhang, Zirui Zou, Yuzheng Chen, Jinlong Wu, Zixuan Hu, Jianke Zhang, Yucheng Hu, Zhecheng Yuan, Huazhe Xu
- Published: 2026-10-29T16:06:36Z
- Age days: 2

</details>
