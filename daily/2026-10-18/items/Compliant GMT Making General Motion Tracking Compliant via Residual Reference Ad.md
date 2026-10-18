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
url: "https://arxiv.org/abs/2610.22119v1"
published: "2026-10-15T15:59:04Z"
age_days: 2
score: 29
created: 2026-10-18
concepts: ["世界模型", "具身智能评测与基准"]
---

# Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> C-GMT 让人形机器人继续跟踪多种动作，同时在被拉推时适当退让。关键是先修改机器人要追踪的参考动作，再让擅长保持平衡的跟踪器执行，而不是让它硬顶原目标。

## 问题

通用动作跟踪器能模仿大量动作，但偏离参考位置时会用力纠正，接触中可能产生危险作用力。已有柔顺方法往往只支持单个动作、有限下肢命令或上半身退让；一次训练同时学跟踪、平衡和接触响应也难调 [S2](https://arxiv.org/html/2610.22119v1#S1.p1.1) [S3](https://arxiv.org/html/2610.22119v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：机器人伸手擦桌时手被挡住 → 适配器从关节运动历史感知偏离，并结合刚度命令调整参考 → 跟踪器执行退让后的姿态，而非持续追赶原手位。

## 创新点或方法

本文把“受力后该去哪里”和“怎样稳定到那里”分开。先给 SONIC 加载荷扰动并微调解码器，使其能执行受力下的参考；再用已知外力、弹簧规律和逆运动学生成教师参考，蒸馏给残差适配器。部署时适配器读取本体感觉历史与刚度命令，无需外力传感输入便修正参考 [S9](https://arxiv.org/html/2610.22119v1#S3.F2) [S10](https://arxiv.org/html/2610.22119v1#S3.p1.1) [S11](https://arxiv.org/html/2610.22119v1#S3.SS1.p1.1) [S12](https://arxiv.org/html/2610.22119v1#S3.SS1.p2.1)。并非原版 SONIC 完全不动；适配器训练时才固定增强后的跟踪器。

### 方法如何工作

1. 对预训练跟踪器加入持续载荷训练，得到能稳定执行修改参考的底层。
2. 教师依据外力和刚度计算退让，再用逆运动学生成协调姿态，并筛除会跌倒的组合。
3. 适配器模仿教师，从本体感觉历史学习修正；逐渐用自身轨迹训练以接触自己的预测误差。
4. 部署时修正参考并交给固定跟踪器执行；无外力时训练目标鼓励残差归零。

### 必要术语

- 柔顺：受力时按期望程度让位；本文通过改变参考实现。
- 刚度：同样位移需要多大力；命令越大，期望退让越小。
- 残差适配：在已有参考上增加修正；保留跟踪器的大部分能力。
- 特权教师：训练时能看到真实外力的教师；部署学生只能使用可获得的感觉信息。

## 证据

在128段留出动作的跟踪测试中，双手拉力不超过60 N时，增强跟踪器成功率为0.867，原 SONIC 为0.820；无载荷时全局位置误差反而增加4.8厘米 [S16](https://arxiv.org/html/2610.22119v1#S3.T1.2.1) [S17](https://arxiv.org/html/2610.22119v1#S3.SS1.p7.1)。这检验的是底层抗载能力。柔顺性另在仿真站立中以外力/位移衡量，与站立专用 SoftMimic 接近，但节选没有具体误差 [S23](https://arxiv.org/html/2610.22119v1#S4.F3) [S24](https://arxiv.org/html/2610.22119v1#S4.SS1.p1.1) [S25](https://arxiv.org/html/2610.22119v1#S4.SS1.p2.1)。G1 真机有接触遥操作展示；走近并抬箱的 VLA 对照每条件50次，报告受扰时更好，却未提供成功率表值，也未在该段明确评测环境 [S26](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p1.1) [S27](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p2.1) [S28](https://arxiv.org/html/2610.22119v1#S4.T3) [S29](https://arxiv.org/html/2610.22119v1#S4.F8) [S30](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p3.1)。

## 局限

作者把身体任意部位接触和按情境自动选择刚度列为后续工作 [S31](https://arxiv.org/html/2610.22119v1#S5.p1.1)。因此不能把手部受力结果外推到全身任意碰撞；柔顺指标和成功率也不等于安全认证。我的待核查问题是快速冲击、估力延迟及超出训练刚度范围时的表现。

- **判断**：值得细读教师可行性筛选与适配器训练：分工很实用，但要连同底层微调成本和接触范围一起理解。

## 研究关联

当已有控制器善于跟踪而不善于接触，可以先改它追逐的目标，让退让成为一个可执行的新目标。前提是修改后的参考经过可行性检查，底层也确实承受得住负载。

### 下一步读哪里

沿 [S11](https://arxiv.org/html/2610.22119v1#S3.SS1.p1.1) [S18](https://arxiv.org/html/2610.22119v1#S3.SS2.p3.1) [S19](https://arxiv.org/html/2610.22119v1#S3.SS4.p1.1) [S20](https://arxiv.org/html/2610.22119v1#S3.SS4.p2.1) 核查残差到底改哪些量、教师怎样排除不稳定参考；再检查同一增强跟踪器有无适配器的对照，以分清抗扰训练与柔顺响应的贡献。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22119v1
- 获取时间：2026-10-18T03:39:25.533520+00:00
- [S1] [Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation · 正文段落 1](https://arxiv.org/html/2610.22119v1#abstract1.1)
- [S2] [I INTRODUCTION · 正文段落 2](https://arxiv.org/html/2610.22119v1#S1.p1.1)
- [S3] [I INTRODUCTION · 正文段落 3](https://arxiv.org/html/2610.22119v1#S1.p2.1)
- [S4] [I INTRODUCTION · 正文段落 4](https://arxiv.org/html/2610.22119v1#S1.p3.1)
- [S5] [I INTRODUCTION · 正文段落 6](https://arxiv.org/html/2610.22119v1#S1.p5.1)
- [S6] [II-A General Motion Tracking · 正文段落 7](https://arxiv.org/html/2610.22119v1#S2.SS1.p1.1)
- [S7] [II-B Learned Compliant Humanoid Control · 正文段落 8](https://arxiv.org/html/2610.22119v1#S2.SS2.p1.1)
- [S8] [II-C Residual Models for Humanoid Robotics · 正文段落 9](https://arxiv.org/html/2610.22119v1#S2.SS3.p1.1)
- [S9] [III METHODS · 正文段落 10](https://arxiv.org/html/2610.22119v1#S3.F2)
- [S10] [III METHODS · 正文段落 11](https://arxiv.org/html/2610.22119v1#S3.p1.1)
- [S11] [III-A Force-Robust General Motion Tracker · 正文段落 12](https://arxiv.org/html/2610.22119v1#S3.SS1.p1.1)
- [S12] [III-A Force-Robust General Motion Tracker · 正文段落 13](https://arxiv.org/html/2610.22119v1#S3.SS1.p2.1)
- [S13] [III-A Force-Robust General Motion Tracker · 正文段落 14](https://arxiv.org/html/2610.22119v1#S3.SS1.p3.1)
- [S14] [III-A Force-Robust General Motion Tracker · 正文段落 15](https://arxiv.org/html/2610.22119v1#S3.SS1.p4.1)
- [S15] [III-A Force-Robust General Motion Tracker · 正文段落 17](https://arxiv.org/html/2610.22119v1#S3.SS1.p6.1)
- [S16] [III-A Force-Robust General Motion Tracker · 正文段落 19](https://arxiv.org/html/2610.22119v1#S3.T1.2.1)
- [S17] [III-A Force-Robust General Motion Tracker · 正文段落 20](https://arxiv.org/html/2610.22119v1#S3.SS1.p7.1)
- [S18] [III-B Compliant Teacher and Feasibility Tuning · 正文段落 24](https://arxiv.org/html/2610.22119v1#S3.SS2.p3.1)
- [S19] [III-D Residual Adapter Training · 正文段落 31](https://arxiv.org/html/2610.22119v1#S3.SS4.p1.1)
- [S20] [III-D Residual Adapter Training · 正文段落 32](https://arxiv.org/html/2610.22119v1#S3.SS4.p2.1)
- [S21] [III-E Experimental Setup · 正文段落 43](https://arxiv.org/html/2610.22119v1#S3.SS5.p1.1)
- [S22] [III-E Experimental Setup · 正文段落 44](https://arxiv.org/html/2610.22119v1#S3.SS5.p2.1)
- [S23] [IV-A C-GMT accurately tracks compliance levels · 正文段落 45](https://arxiv.org/html/2610.22119v1#S4.F3)
- [S24] [IV-A C-GMT accurately tracks compliance levels · 正文段落 46](https://arxiv.org/html/2610.22119v1#S4.SS1.p1.1)
- [S25] [IV-A C-GMT accurately tracks compliance levels · 正文段落 47](https://arxiv.org/html/2610.22119v1#S4.SS1.p2.1)
- [S26] [IV-D2 Compliance provides robustness during high-level controller execution · 正文段落 61](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p1.1)
- [S27] [IV-D2 Compliance provides robustness during high-level controller execution · 正文段落 62](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p2.1)
- [S28] [IV-D2 Compliance provides robustness during high-level controller execution · 正文段落 63](https://arxiv.org/html/2610.22119v1#S4.T3)
- [S29] [IV-D2 Compliance provides robustness during high-level controller execution · 正文段落 65](https://arxiv.org/html/2610.22119v1#S4.F8)
- [S30] [IV-D2 Compliance provides robustness during high-level controller execution · 正文段落 66](https://arxiv.org/html/2610.22119v1#S4.SS4.SSS2.p3.1)
- [S31] [V CONCLUSION · 正文段落 67](https://arxiv.org/html/2610.22119v1#S5.p1.1)
- [S32] [A-A Force-Robust Tracker Training · 正文段落 69](https://arxiv.org/html/2610.22119v1#A1.SS1.p1.1)
- [S33] [A-A Force-Robust Tracker Training · 正文段落 70](https://arxiv.org/html/2610.22119v1#A1.SS1.p2.1)
- [S34] [A-A Force-Robust Tracker Training · 正文段落 71](https://arxiv.org/html/2610.22119v1#A1.SS1.p3.1)
- [S35] [A-D Residual Adapter Training · 正文段落 84](https://arxiv.org/html/2610.22119v1#A1.SS4.p1.1)
- [S36] [A-D Residual Adapter Training · 正文段落 85](https://arxiv.org/html/2610.22119v1#A1.SS4.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/Compliant GMT Making General Motion Tracking Compliant via Residual Reference Ad.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking. As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained to be stiff, leading to unexpected and unsafe behaviors under disturbance. Prior work in compliant humanoid control trades off compliance and generality. There exist examples of full-body compliant responses, but these are heavily curated to single-reference policies. On the other hand, general motion trackers (GMT) are trained to rigidly imitate massive motion capture datasets. Our key insight is to leverage the generality of pretrained GMTs for motion tracking while introducing compliance from a residual adapter that conditions on a history of proprioception. This enables our approach, C-GMT, to achieve both general motion tracking and whole-body compliant responses. Compared to state-of-the-art general motion trackers and single-motion compliant policies, C-GMT demonstrates competitive performance in both motion tracking accuracy and compliance adherence. We further demonstrate improved safety, robustness, and error tolerance in simulation and real-world G1 experiments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22119v1
- Authors: Venki Parsuram, Michelle Wang, Jin-Hyuk Hong, Pulkit Agrawal
- Published: 2026-10-15T15:59:04Z
- Age days: 2

</details>
