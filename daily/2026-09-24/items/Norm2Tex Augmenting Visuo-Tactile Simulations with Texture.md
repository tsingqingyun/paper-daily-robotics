---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25398v1"
published: "2026-09-21T20:40:59Z"
age_days: 2
score: 31
created: 2026-09-24
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture

> [!summary] 先说人话（基于摘要）
> Norm2Tex 在视觉触觉仿真中补入表面细纹理，让模拟接触图像包含更多与真实材质相关的信息。

## 问题

真实触觉数据采集昂贵，而现有触觉模拟器主要表现整体接触几何，遗漏细纹理，造成仿真与真实触觉数据之间的差异。

## 创新点或方法

插件从法线纹理图获取高频表面细节，在触觉模拟器渲染之前修改目标物体深度图，因此可接入不同模拟器的现有渲染流程。

## 证据

通过材质分类和一个强化学习任务评估 sim-to-real。摘要报告跨域保留材质信息、改善纹理识别，并在真实环境产生随材质变化的控制行为，未给出可核查的结果数字。

## 局限

需核查纹理增强在哪些传感器、材质和接触条件下有效；渲染细节改善不能直接代表接触动力学也更准确。

- **判断**：做视觉触觉仿真值得阅读插件机制和迁移实验，收益大小需由全文量化结果判断。

## 研究关联

对机器人学习和 Sim2Real 研究者，它提供了改善触觉训练数据的局部接口；与世界模型的联系主要在仿真观测质量，而非动作结果预测模型。

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/Norm2Tex Augmenting Visuo-Tactile Simulations with Texture.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale datasets are essential for training generalist robot control policies. Collecting real-world tactile data is costly and time-consuming, motivating the use of tactile simulations. However, current tactile simulators capture only overall contact geometry and miss fine details like texture. This results in a significant domain shift between simulated and real tactile data. To address this gap, we introduce Norm2Tex, a plug-in method that augments simulations of vision-based tactile sensors with high-frequency surface details from normal map textures. By modifying the target object's depth map before a tactile simulator's rendering pipeline, Norm2Tex seamlessly integrates into different tactile simulators. We also evaluate sim-to-real transfer using material classification and a reinforcement learning task. Our results show that Norm2Tex preserves material-dependent tactile information across domains, improving texture recognition and producing material-dependent control behavior in the real world.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25398v1
- Authors: Seongjin Bien, Débora Oliveira Makowski, Roberto Calandra, Florian Walter, Wolfram Burgard
- Published: 2026-09-21T20:40:59Z
- Age days: 2

</details>
