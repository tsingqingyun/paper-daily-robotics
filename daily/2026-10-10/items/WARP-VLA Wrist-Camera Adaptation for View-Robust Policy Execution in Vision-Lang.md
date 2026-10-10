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
url: "https://arxiv.org/abs/2610.11508v1"
published: "2026-10-08T08:44:26Z"
age_days: 1
score: 35
created: 2026-10-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> WARP-VLA 用多个专家学习不同腕部视角下的特征变换，再由路由器根据图像中的视角线索组合专家。这样，相机安装位置发生变化时，策略仍有机会正确理解物体与机械手的几何关系。

## 问题

具体任务是让操作策略跨不同腕部相机配置执行。训练时的相机姿态很难在部署时精确复现，而腕部相机会随机器人运动，小安装误差也会改变抓取所需的细微几何线索。摘要指出现有 VLA 对相机配置敏感，但没有逐项解释已有适配方法的不足。

### 用一个例子理解

理解用例（非论文实验）：输入是“抓起积木”和一个略微向下倾斜的腕部画面；路由器组合适合该视角的特征变换，策略据此判断积木相对夹爪的位置；输出是接近和抓取动作。

## 创新点或方法

旧策略依赖训练视角下学到的特征；WARP-VLA 加入混合专家，让不同专家学习视角相关的特征变换，路由器再按隐含视角信息组合它们。训练阶段学习这些变换与选择方式；推理阶段根据输入选择组合，不需要额外输入相机外参。摘要没有交代专家插入位置、路由训练目标，以及基础策略是否冻结。

### 方法如何工作

1. 训练时让专家学习不同视角对应的特征变换，使相机变化可以在视觉表示中被处理。
2. 路由器从观测中的隐含线索判断如何组合专家，得到适合当前视角的特征。
3. 策略使用变换后的特征生成操作动作，部署时无需额外输入相机外参。
4. 用腕部视角扰动和真机部署检查适配效果；摘要只说明到此，没有给出具体训练配方。

### 必要术语

- 混合专家（MoE）：组合多个专门处理某类输入的模块；本文专家学习视角相关变换。
- 路由器：决定哪些专家参与以及如何组合；本文依据隐含视角信息工作。
- 相机外参：相机相对参考坐标系的位置与朝向；本文推理不要求额外输入它们。

## 证据

摘要报告，在 LIBERO 腕部视角扰动测试中，pi-0.5 平均成功率由 39.2% 增至 78.3%。真机实验还显示仿真中学到的特征适配可迁移到多种部署设置，但未提供任务数、成功率或扰动范围。强数字证据来自该仿真测试，真机部分只能作定性支持。

## 局限

路由器依赖隐含视角信息，物体遮挡或画面相似时能否正确选择专家，需要核查。还要区分训练覆盖的扰动与全新视角：给定结果不能证明任意安装位置都有效。摘要提到真机迁移，但不足以判断其适用范围。

- **判断**：值得优先读实验设置和专家消融，报告的改善很大，关键是确认视角扰动范围及测试配置是否真正超出训练覆盖。

## 研究关联

这里可借鉴的是把相机变化当成需要处理的观测变换，而不必要求策略显式接收精确相机姿态。对于安装误差难以避免、但视觉中仍有足够几何线索的部署情境，学习特征适配值得尝试。

### 下一步读哪里

核查相机扰动包含哪些平移与旋转、训练和测试配置如何分离，以及单专家、普通视角增强与混合专家的比较。再看真机是否需要重新训练、额外标定或任务数据。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/WARP-VLA Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Lang.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration. The problem becomes more evident in cross-setup deployment, as reproducing the exact camera pose used for training is nearly impossible. Unlike fixed external views, wrist views are more challenging because the camera moves with the robot, causing even small mounting variations to alter fine-grained geometric cues. To address this, we propose WARP-VLA, a camera-view robust VLA for diverse wrist camera configurations. WARP-VLA adopts a Mixture-of-Experts (MoE) architecture where individual experts learn view-specific feature transformations, and a router combines them based on implicit view information. This allows the policy to be deployed without requiring camera extrinsic parameters as additional input. Through experiments on the LIBERO benchmark, WARP-VLA improves the average success rate of pi-0.5 from 39.2% to 78.3% under wrist-view perturbations. The real-robot experiments further show that the feature-level adaptation learned in simulation successfully transfers to diverse deployment settings. To facilitate reproducibility and future research, we release our wrist viewpoint robustness benchmark and a plug-and-play implementation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11508v1
- Authors: Junmyeong Lee, Dongmin Shin, Min-Gyu Park, Wooseok Jeon, Inho Chang, Hae-Gon Jeon
- Published: 2026-10-08T08:44:26Z
- Age days: 1

</details>
