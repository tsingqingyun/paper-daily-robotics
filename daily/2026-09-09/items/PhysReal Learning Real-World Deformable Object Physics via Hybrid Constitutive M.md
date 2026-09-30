---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07532v1"
published: "2026-09-07T14:11:57Z"
age_days: 1
score: 32
created: 2026-09-09
concepts: ["智能体 Agent", "世界模型"]
---

# PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling

> [!summary] 先说人话（基于摘要）
> PhysReal从视频反推可变形物体的材料行为，再用物理仿真预测运动。它让解析材料模型负责物理先验，神经残差补足复杂响应，并允许物体不同位置具有不同材料性质。

## 问题

真实可变形物体的动力学具有复杂且空间不均匀的材料响应，稀疏视觉观测下很难辨识；预定义材料公式难以覆盖所有响应。

## 创新点或方法

把空间变化的专家—神经混合本构模型接入可微MPM仿真器与3DGS渲染器。通过局部块表示连续材料场，依次优化全局材料属性、局部参数和神经残差，并结合运动与掩码监督。

## 证据

摘要报告在多种可变形物体交互中，动态重建与未来状态预测优于对照；摘要未给出可核查的结果数字，也未报告具体机器人任务收益。


## 局限

最需核查未来预测是否覆盖新外力或新交互条件，以区分观测运动拟合与材料规律的可迁移辨识。

- **判断**：可变形世界模型方向值得读到模型与预测协议，机器人控制研究者可先关注是否存在实际闭环验证。

## 研究关联

对交互世界模型有直接价值：提供带材料结构的动态表示，可用于研究视觉拟合能否转化为物理预测；下游机器人价值目前仍是潜力描述。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/PhysReal Learning Real-World Deformable Object Physics via Hybrid Constitutive M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning physically plausible dynamics from visual observations is essential for interactive world models and embodied agents. However, modeling real-world deformable objects remains challenging because their dynamics often arise from complex, spatially heterogeneous material responses. To address this challenge, we propose PhysReal, a video-driven framework for learning and simulating the underlying physics of real deformable objects. PhysReal integrates a spatially varying hybrid expert-neural constitutive model with a differentiable MPM simulator and 3DGS renderer. Analytical expert models provide interpretable physical priors, while neural constitutive residuals capture material responses beyond predefined formulations. Spatially distributed patches parameterize the constitutive field, enabling a continuous representation of local material variations. To organize the identification of this model from sparse visual observations, we adopt a progressive curriculum that sequentially optimizes global material properties, spatially varying local parameters, and neural constitutive residuals, together with complementary motion and mask supervision. Extensive experiments on diverse deformable-object interactions demonstrate that PhysReal achieves superior performance in dynamic reconstruction and future-state prediction, while showing strong potential for downstream robotic applications.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07532v1
- Authors: Yinan Deng, Jianqiao Song, Yisi Zhang, Yuhan Wang, Jiahui Wang, Yufeng Yue
- Published: 2026-09-07T14:11:57Z
- Age days: 1

</details>
