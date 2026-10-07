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
url: "https://arxiv.org/abs/2610.07558v1"
published: "2026-10-06T00:44:06Z"
age_days: 1
score: 39
created: 2026-10-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PG-VP 把传感器发现的热源或辐射风险画成相机画面里的虚拟障碍，让冻结的导航 VLA 用已有避障能力绕行。巧处是新增传感器只需接到风险判断，导航模型无需重新学习每种物理量。

## 问题

RGB 看不到辐射和温度危险，机器人却可能按正常路线靠近它们。直接增加模型输入模态，需要编码器、配对数据和重训练，还可能改变无危险时的导航行为 [S3](https://arxiv.org/html/2610.07558v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“走到走廊尽头”、RGB 和右侧热源测量；风险模块判右侧危险，在图像右边逐渐画出虚拟墙；冻结策略预测向左绕行的路径点，危险解除后恢复原图。

## 创新点或方法

旧做法让 VLA 学懂新传感器；本文先在模型外判断危险侧，再把该侧变成逐帧伸展、消退的虚拟弯墙，利用可见障碍对应的绕行动作 [S12](https://arxiv.org/html/2610.07558v1#S3.p1.1) [S18](https://arxiv.org/html/2610.07558v1#S3.SS3.p1.1) [S19](https://arxiv.org/html/2610.07558v1#S3.SS3.p2.1)。无危险时原图直接通过。导航权重不变，但“无需训练”只适用于导航策略：辐射风险与方向模型用物理仿真生成数据训练，并用辅助损失约束预测与计数观测相容 [S15](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p2.1) [S16](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p3.1) [S17](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p4.1)；温度模型细节未提供。

### 方法如何工作

1. 额外传感器测热或辐射，补上 RGB 无法观察的物理量。
2. 独立风险模型输出危险侧或正常状态，把不同传感器转成共同方向接口。
3. 在危险侧逐帧绘制伸展和消退的虚拟墙，给视觉策略一个明确的避让区域。
4. 冻结策略从修改后的图像生成动作；风险消失时输入恢复原图，停止提示。

### 必要术语

- 视觉提示：直接改变模型看到的图像；本文用虚拟障碍影响动作。
- 正确引导比例：轨迹按预期方向改变的场景比例；不等于安全达标率。
- CPS：每秒探测到的计数；本文扣除背景后衡量沿途辐射。
- 最差 10% 平均：平均轨迹中最不利的一段测量；比单个极值更少受瞬时噪声影响。

## 证据

OmniNav 在 R2R-CE、RxR-CE 未见环境中，正确引导比例为 84.9%、83.2%，导航成功率下降 6.8、7.9 个百分点（摘要）。该测试假设危险存在，主要检验虚拟墙是否能改变路线，未测试完整传感链 [S21](https://arxiv.org/html/2610.07558v1#S4.SS1.p1.1) [S22](https://arxiv.org/html/2610.07558v1#S4.SS1.p2.1)。真机四场景使用实际热源和辐射源，均完成导航 [S24](https://arxiv.org/html/2610.07558v1#S4.SS2.p1.1) [S25](https://arxiv.org/html/2610.07558v1#S4.SS2.p2.1)；最差 10% 轨迹指标改善汇总为热 63.45%、辐射 32.59% [S35](https://arxiv.org/html/2610.07558v1#S4.SS2.p4.1)。热指标是离热源距离，辐射指标是净计数率，不能统一解释为伤害风险下降。

## 局限

作者的场景 D 因遮挡未及时触发提示，辐射峰值仍然出现 [S36](https://arxiv.org/html/2610.07558v1#S4.SS2.p5.1)；作者也要求进一步做工业场景验证 [S38](https://arxiv.org/html/2610.07558v1#S5.p2.1)。我的待核查问题是多危险冲突、误报和狭窄通道如何处理。这里证明的是有限场景中的绕行与暴露指标改善，尚不能视为安全保证。

- **判断**：值得深入读风险触发和动态绘制机制：这是成本明确的接口改造，但成功率损失与触发延迟决定了它能用到哪里。

## 研究关联

值得借鉴的是把新增信息转换成策略已经会响应的输入形式，而不是每次扩充模型。不过前提是这类视觉提示确实触发所需行为，且危险能及时、正确地定位。

### 下一步读哪里

沿 [S14](https://arxiv.org/html/2610.07558v1#S3.SS2.p1.1) [S15](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p2.1) [S16](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p3.1) [S17](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p4.1) 核查风险阈值、方向误差和传感延迟；沿 [S21](https://arxiv.org/html/2610.07558v1#S4.SS1.p1.1) [S22](https://arxiv.org/html/2610.07558v1#S4.SS1.p2.1) 区分提示实验与完整系统实验。再看 [S29](https://arxiv.org/html/2610.07558v1#S4.T2.2) [S36](https://arxiv.org/html/2610.07558v1#S4.SS2.p5.1) 的逐场景指标，检查汇总改善比例如何计算，以及迟触发时剩余暴露有多大。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.07558v1
- 获取时间：2026-10-07T02:13:52.873845+00:00
- [S1] [Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation · 正文段落 1](https://arxiv.org/html/2610.07558v1#abstract1.1)
- [S2] [I INTRODUCTION · 正文段落 2](https://arxiv.org/html/2610.07558v1#S1.p1.1)
- [S3] [I INTRODUCTION · 正文段落 3](https://arxiv.org/html/2610.07558v1#S1.p2.1)
- [S4] [I INTRODUCTION · 正文段落 4](https://arxiv.org/html/2610.07558v1#S1.p3.1)
- [S5] [I INTRODUCTION · 正文段落 6](https://arxiv.org/html/2610.07558v1#S1.I1.i2)
- [S6] [I INTRODUCTION · 正文段落 7](https://arxiv.org/html/2610.07558v1#S1.I1.i3)
- [S7] [I INTRODUCTION · 正文段落 8](https://arxiv.org/html/2610.07558v1#S1.p3.2)
- [S8] [II-A VLA-based Robot Navigation · 正文段落 9](https://arxiv.org/html/2610.07558v1#S2.SS1.p1.1)
- [S9] [II-B Extending Perception Beyond RGB · 正文段落 10](https://arxiv.org/html/2610.07558v1#S2.SS2.p1.1)
- [S10] [II-B Extending Perception Beyond RGB · 正文段落 11](https://arxiv.org/html/2610.07558v1#S2.SS2.p2.1)
- [S11] [III Methodology · 正文段落 13](https://arxiv.org/html/2610.07558v1#S3.F1)
- [S12] [III Methodology · 正文段落 14](https://arxiv.org/html/2610.07558v1#S3.p1.1)
- [S13] [III-A Integrated Robotic Multimodal Perception System · 正文段落 16](https://arxiv.org/html/2610.07558v1#S3.SS1.p2.1)
- [S14] [III-B Physics-Guided Risk Assessment · 正文段落 18](https://arxiv.org/html/2610.07558v1#S3.SS2.p1.1)
- [S15] [III-B2 Radiation · 正文段落 22](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p2.1)
- [S16] [III-B2 Radiation · 正文段落 23](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p3.1)
- [S17] [III-B2 Radiation · 正文段落 29](https://arxiv.org/html/2610.07558v1#S3.SS2.SSS2.p4.1)
- [S18] [III-C Dynamic Visual Prompting · 正文段落 30](https://arxiv.org/html/2610.07558v1#S3.SS3.p1.1)
- [S19] [III-C Dynamic Visual Prompting · 正文段落 31](https://arxiv.org/html/2610.07558v1#S3.SS3.p2.1)
- [S20] [III-C Dynamic Visual Prompting · 正文段落 37](https://arxiv.org/html/2610.07558v1#S3.SS3.p7.1)
- [S21] [IV-A Trajectory Steering on VLN Benchmarks · 正文段落 39](https://arxiv.org/html/2610.07558v1#S4.SS1.p1.1)
- [S22] [IV-A Trajectory Steering on VLN Benchmarks · 正文段落 40](https://arxiv.org/html/2610.07558v1#S4.SS1.p2.1)
- [S23] [IV-A Trajectory Steering on VLN Benchmarks · 正文段落 44](https://arxiv.org/html/2610.07558v1#S4.F4)
- [S24] [IV-B Experimental Validation · 正文段落 53](https://arxiv.org/html/2610.07558v1#S4.SS2.p1.1)
- [S25] [IV-B Experimental Validation · 正文段落 54](https://arxiv.org/html/2610.07558v1#S4.SS2.p2.1)
- [S26] [IV-B Experimental Validation · 正文段落 55](https://arxiv.org/html/2610.07558v1#S4.F6)
- [S27] [IV-B Experimental Validation · 正文段落 56](https://arxiv.org/html/2610.07558v1#S4.SS2.p3.1)
- [S28] [IV-B Experimental Validation · 正文段落 57](https://arxiv.org/html/2610.07558v1#S4.T2)
- [S29] [IV-B Experimental Validation · 正文段落 58](https://arxiv.org/html/2610.07558v1#S4.T2.2)
- [S30] [IV-B Experimental Validation · 正文段落 59](https://arxiv.org/html/2610.07558v1#S4.F7.sf1)
- [S31] [IV-B Experimental Validation · 正文段落 60](https://arxiv.org/html/2610.07558v1#S4.F7.sf2)
- [S32] [IV-B Experimental Validation · 正文段落 61](https://arxiv.org/html/2610.07558v1#S4.F7.sf3)
- [S33] [IV-B Experimental Validation · 正文段落 62](https://arxiv.org/html/2610.07558v1#S4.F7.sf4)
- [S34] [IV-B Experimental Validation · 正文段落 63](https://arxiv.org/html/2610.07558v1#S4.F7)
- [S35] [IV-B Experimental Validation · 正文段落 64](https://arxiv.org/html/2610.07558v1#S4.SS2.p4.1)
- [S36] [IV-B Experimental Validation · 正文段落 65](https://arxiv.org/html/2610.07558v1#S4.SS2.p5.1)
- [S37] [V Conclusions · 正文段落 66](https://arxiv.org/html/2610.07558v1#S5.p1.1)
- [S38] [V Conclusions · 正文段落 67](https://arxiv.org/html/2610.07558v1#S5.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/Seeing the Invisible Physics-Guided Visual Prompting for Temperature- and Radiat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have become a major paradigm for Vision-and-Language Navigation (VLN). However, in safety-critical facilities, invisible risks such as radiation or temperature spikes cannot be detected by an RGB camera, and handling each risk is expensive, requiring a new encoder, new data, and model retraining. We propose Physics-Guided Visual Prompting (PG-VP), a plug-and-play multimodal perception module that instead reuses what a frozen VLA model already does well: avoiding visible obstacles. Given a proximal radiation or thermal source, PG-VP performs a physics-guided risk assessment to determine the avoidance direction and overlays a corresponding virtual obstacle that moves across consecutive frames (Dynamic Visual Prompting). The navigation policy then naturally detours around this invisible hazard. The identical virtual obstacle is used regardless of hazard type, so the visual prompting pattern remains fixed as sensors are added. When no hazard is detected, nothing is rendered, and the policy behaves exactly as it would without PG-VP. We evaluate PG-VP on OmniNav using the val-unseen splits of R2R-CE and RxR-CE, where it guides the policy toward intended low-risk actions in 84.9% and 83.2% of cases, at a cost of 6.8 and 7.9 percentage points in navigation success rate. We further test it with distinct scenarios on a real robot in the presence of actual thermal and radiation sources, all without any retraining. The real test shows that PG-VP effectively avoids these invisible hazards, improving worst-10% average trajectory safety by 63.45% and 32.59% against thermal and radiation sources, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07558v1
- Authors: Hojoon Son, Fan Zhang
- Published: 2026-10-06T00:44:06Z
- Age days: 1

</details>
