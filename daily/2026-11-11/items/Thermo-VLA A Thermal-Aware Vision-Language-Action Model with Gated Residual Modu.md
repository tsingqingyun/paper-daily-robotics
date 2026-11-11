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
url: "https://arxiv.org/abs/2611.11981v1"
published: "2026-11-09T07:06:20Z"
age_days: 1
score: 40
created: 2026-11-11
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Thermo-VLA 让机器人根据温度选对操作对象，而不是只把热成像当成另一张图片。它用 ThermoRes Encoder 提取冷、热属性，再由语言控制这些信息如何补进 RGB 表示，随后生成连续动作。

## 问题

RGB 看不见温度；直接加入热图，也可能只吸引模型注意最热的地方，而指令实际要求选择冷物体或排除热源。任务因此同时涉及目标判断和稳定操作，热信息融合不当还可能干扰原有抓放能力。[S3](https://arxiv.org/html/2611.11981v1#S1.p1.1) [S4](https://arxiv.org/html/2611.11981v1#S1.p2.1) [S5](https://arxiv.org/html/2611.11981v1#S1.p3.1) [S16](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS2.p1.1)

### 用一个例子理解

理解用例（非论文实验）：两只外观相似的杯子一冷一热，指令要求把冷杯放到托盘。RGB 提供杯子位置和抓取外形，热分支提供冷属性，语言门控补入相关信息，动作模块输出选中冷杯后的抓放动作。

## 创新点或方法

旧做法把热图作为额外视觉输入；本文将热属性作为受控补充。双分支构造互补的冷、热属性表示，语言条件门控决定向 RGB token 注入哪些残差信息，再用融合表示训练流匹配动作策略。[S5](https://arxiv.org/html/2611.11981v1#S1.p3.1) [S9](https://arxiv.org/html/2611.11981v1#S2.F2) 推理时仍需要 RGB、热图、指令和机器人状态，直接生成双臂动作块。节选未给属性图计算公式、门控结构和冻结参数范围，不能据此补全实现。

### 方法如何工作

1. 分别编码 RGB 和热观测，使物体外观与温度信息进入不同处理路径。[S5](https://arxiv.org/html/2611.11981v1#S1.p3.1)
2. 将热观测分成冷、热属性表示，让任务可利用互补温度线索；具体计算式未提供。
3. 根据语言门控热残差并注入 RGB token，使温度信息参与目标选择。[S5](https://arxiv.org/html/2611.11981v1#S1.p3.1) [S9](https://arxiv.org/html/2611.11981v1#S2.F2)
4. 训练时用融合表示学习动作生成；推理时结合机器人状态输出连续双臂动作块。[S9](https://arxiv.org/html/2611.11981v1#S2.F2) [S10](https://arxiv.org/html/2611.11981v1#S3.SS1.p1.1)

### 必要术语

- 残差调制：在原表示上添加修正量；本文用它补入温度属性。
- 门控：控制信息通过的程度；本文由语言条件决定热信息怎样注入。
- 流匹配：学习把噪声逐步变成目标动作序列的生成方法；本文用于连续动作输出。

## 证据

真机为双臂 Unitree G1，六任务共 1,307 条专家示范，每指令测试 20 次。[S15](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS1.p1.1) 摘要报告四项温度任务平均成功率 0.86，比直接加入热图的 π₀.₅ 高 18 个百分点；相对温度咖啡任务仅 0.58。[S13](https://arxiv.org/html/2611.11981v1#S4.T2.4.1) 小目标测试中去掉门控，成功率由 0.85 降至 0.60；热残差置零后，温度任务接近随机二选一，但仍能抓放。[S22](https://arxiv.org/html/2611.11981v1#S4.SS3.p1.1) [S23](https://arxiv.org/html/2611.11981v1#S4.SS3.p2.1) [S24](https://arxiv.org/html/2611.11981v1#S4.T4) [S25](https://arxiv.org/html/2611.11981v1#S4.T4.2) 消融支持残差参与目标选择，不能仅凭注意力图认定其具有人类式推理。

## 局限

作者承认 RGB-only 能力略低于原始 π₀.₅，冷/热分解也不足以分清更细温差。[S17](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS2.p2.1) [S31](https://arxiv.org/html/2611.11981v1#S6.p2.1) 已知物体交换温度后，相关任务成功率降至 0.60。[S21](https://arxiv.org/html/2611.11981v1#S4.SS2.SSS2.p1.1) 我的待核查问题是跨传感器标定与热成像变化的敏感性；模拟鼠任务不能证明真实生物状态识别。

- **判断**：值得读融合机制与消融；它给出了属性如何进入动作策略的可检查解释，但精细温度比较仍是明显短板。

## 研究关联

当新增传感器主要帮助判断“选哪个”，可以尝试让它修正已有视觉表示，而不是全面重写控制输入。本文的残差置零实验尤其有用：它检查了新增信息影响的是目标选择还是基本动作。

### 下一步读哪里

先核查冷、热属性图如何生成及是否保留温度量值，再对照 [S25](https://arxiv.org/html/2611.11981v1#S4.T4.2) 的门控、双分支和残差置零消融。结合 [S21](https://arxiv.org/html/2611.11981v1#S4.SS2.SSS2.p1.1) 看属性重分配与小目标失败；颜色迁移 [S27](https://arxiv.org/html/2611.11981v1#S5.SS2.p1.1) [S28](https://arxiv.org/html/2611.11981v1#S5.SS2.p2.1) [S29](https://arxiv.org/html/2611.11981v1#S5.T5) [S30](https://arxiv.org/html/2611.11981v1#S5.T5.4) 支持进一步尝试，尚不足以证明任意模态都适用。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.11981v1
- 获取时间：2026-11-11T00:09:12.715510+00:00
- [S1] [Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation · 正文段落 1](https://arxiv.org/html/2611.11981v1#abstract1.1)
- [S2] [Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation · 正文段落 2](https://arxiv.org/html/2611.11981v1#:~:text=Fig.%201%3A%20Overview%20of%20the%20Thermo-VLA%20framework%20and%20results.%20Left%3A%20real-world%20RGB%20and%20thermal%20manipulation%20data.%20Centre%3A%20the%20Thermo-VLA%20framework%20for%20multimodal%20en)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2611.11981v1#S1.p1.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2611.11981v1#S1.p2.1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2611.11981v1#S1.p3.1)
- [S6] [I Introduction · 正文段落 6](https://arxiv.org/html/2611.11981v1#S1.p4.1)
- [S7] [I Introduction · 正文段落 8](https://arxiv.org/html/2611.11981v1#S1.I1.i1)
- [S8] [II-A Generalist Robotic Manipulation Methods · 正文段落 11](https://arxiv.org/html/2611.11981v1#S2.SS1.p1.1)
- [S9] [II-C Thermal Perception, Understanding, and Action · 正文段落 14](https://arxiv.org/html/2611.11981v1#S2.F2)
- [S10] [III-A Problem Formulation · 正文段落 15](https://arxiv.org/html/2611.11981v1#S3.SS1.p1.1)
- [S11] [III-B2 Gated Residual Injection · 正文段落 30](https://arxiv.org/html/2611.11981v1#S3.T1)
- [S12] [IV Experiments · 正文段落 33](https://arxiv.org/html/2611.11981v1#S4.T2)
- [S13] [IV Experiments · 正文段落 34](https://arxiv.org/html/2611.11981v1#S4.T2.4.1)
- [S14] [IV-A Comparative Experiments · 正文段落 35](https://arxiv.org/html/2611.11981v1#S4.F3)
- [S15] [IV-A1 Task Description · 正文段落 36](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS1.p1.1)
- [S16] [IV-A2 Comparison Results · 正文段落 37](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS2.p1.1)
- [S17] [IV-A2 Comparison Results · 正文段落 38](https://arxiv.org/html/2611.11981v1#S4.SS1.SSS2.p2.1)
- [S18] [IV-B1 Task Description · 正文段落 39](https://arxiv.org/html/2611.11981v1#S4.SS2.SSS1.p1.1)
- [S19] [IV-B1 Task Description · 正文段落 40](https://arxiv.org/html/2611.11981v1#S4.T3)
- [S20] [IV-B1 Task Description · 正文段落 42](https://arxiv.org/html/2611.11981v1#S4.F4)
- [S21] [IV-B2 Generalization Results · 正文段落 43](https://arxiv.org/html/2611.11981v1#S4.SS2.SSS2.p1.1)
- [S22] [IV-C Ablation Studies · 正文段落 44](https://arxiv.org/html/2611.11981v1#S4.SS3.p1.1)
- [S23] [IV-C Ablation Studies · 正文段落 45](https://arxiv.org/html/2611.11981v1#S4.SS3.p2.1)
- [S24] [IV-C Ablation Studies · 正文段落 46](https://arxiv.org/html/2611.11981v1#S4.T4)
- [S25] [IV-C Ablation Studies · 正文段落 47](https://arxiv.org/html/2611.11981v1#S4.T4.2)
- [S26] [V-A RGBRes Encoder · 正文段落 54](https://arxiv.org/html/2611.11981v1#S5.F5)
- [S27] [V-B Additional Experiments · 正文段落 55](https://arxiv.org/html/2611.11981v1#S5.SS2.p1.1)
- [S28] [V-B Additional Experiments · 正文段落 56](https://arxiv.org/html/2611.11981v1#S5.SS2.p2.1)
- [S29] [V-B Additional Experiments · 正文段落 57](https://arxiv.org/html/2611.11981v1#S5.T5)
- [S30] [V-B Additional Experiments · 正文段落 58](https://arxiv.org/html/2611.11981v1#S5.T5.4)
- [S31] [VI Conclusion · 正文段落 60](https://arxiv.org/html/2611.11981v1#S6.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/Thermo-VLA A Thermal-Aware Vision-Language-Action Model with Gated Residual Modu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal images into cold and hot attribute representations and injects them into the RGB token through language-conditioned residual modulation, enabling temperature-driven target selection and continuous manipulation. We further construct six real-world robotic tasks on a dual-arm Unitree G1 platform, spanning basic grounding to relational reasoning. Experiments show that Thermo-VLA achieves an average success rate of 0.86 across four thermal-dependent tasks, outperforming a pi_0.5 baseline that directly incorporates RGB-thermal observations by 18 percentage points. Under unseen-object and scene variations, Thermo-VLA maintains an average success rate of 0.78, achieving the best generalisation performance among the compared methods. Beyond thermal sensing, we transfer the same residual modulation mechanism to colour attributes and observe consistent improvements in both simulation and real-robot experiments, indicating its potential to generalise beyond thermal attributes. Project website: https://j-x-chen.github.io/Thermo-VLA-web/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.11981v1
- Authors: Jingxuan Chen, Junshi Luo, Chencheng Dong, Xiaojian Nie, Tongge Huang, Qiang Huang
- Published: 2026-11-09T07:06:20Z
- Age days: 1

</details>
