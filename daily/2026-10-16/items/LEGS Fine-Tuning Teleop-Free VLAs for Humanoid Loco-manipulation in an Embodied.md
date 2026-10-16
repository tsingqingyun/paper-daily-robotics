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
url: "https://arxiv.org/abs/2606.01458"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 40
created: 2026-10-16
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World

> [!summary] 这篇论文到底做了什么（基于摘要）
> LEGS 把可模拟动作的机器人和物体，放进从真实场景重建的逼真背景里，自动生成 VLA 示范。关键是把动作与外观分开保存，同一段动作能换场景重新渲染，减少重新遥操作的成本。

## 问题

任务是人形机器人需要全身配合的移动操作。人工遥操作示范采集昂贵复杂，而已有仿真微调策略迁移到此类任务的效果不理想。LEGS 同时针对示范生产成本和仿真画面与部署相机之间的差异。

### 用一个例子理解

理解用例（非论文实验）：输入一段取盒动作、新桌面的手持拍摄和目标物体配置；系统重建背景并重新渲染动作，输出用于微调的图像与动作示范，再训练机器人在该布置中取盒。

## 创新点或方法

旧做法依赖人工示教，或使用纯网格仿真画面；LEGS 用手持拍摄重建 3D Gaussian Splatting 背景，再合成网格表示的机器人、物体和道具。程序化运动基元生成带标签示范，两阶段颜色校准让渲染更贴近部署相机。训练时用这些合成示范微调 VLA；部署时由训练后的策略控制真机，仿真器负责生产数据，摘要未说它参与在线决策。

### 方法如何工作

1. 从手持场景拍摄重建 3DGS 背景，取得接近实际部署环境的外观。
2. 用网格前景承载机器人、物体和道具，结合运动基元生成带标签动作示范。
3. 通过两阶段颜色校准调整渲染，使训练图像更贴近部署相机。
4. 用合成数据微调 VLA 并部署真机；场景改变时复用适用动作重新渲染，减少重复示教。

### 必要术语

- 3D Gaussian Splatting：用许多三维高斯元素表示并渲染场景；本文负责真实感背景。
- 运动基元：可组合的基础运动；本文用于程序化生成示范。
- 重新渲染：保留动作、重新生成对应画面；本文用来适配目标场景外观。

## 证据

摘要报告 Unitree G1 真机上的三项取放任务及 ψ₀、π₀.₅、GR00T N1.6 三种骨干：纯 LEGS 数据训练的策略在每个报告实验中达到或超过遥操作数据训练策略，也优于使用相同运动的纯网格基线。摘要称重新渲染示范的成本比遥操作低逾 15 倍，但未给成本核算。场景和物体都改变时，面向目标重新渲染的 LEGS-AUG 保持任务成功，而遥操作基线完全失败；未提供具体成功率。

## 局限

目标场景重新渲染需要针对目标准备数据，不能解释为直接适应任意未见场景。已给证据集中于三项取放任务；待核查的是运动基元能覆盖多少接触复杂度，以及重建、校准和失败修正是否计入成本。

- **判断**：值得细读数据生成、颜色校准及真机对照，尤其适合判断哪些示范可以靠重新渲染复用；复杂接触能力仍需更多证据。

## 研究关联

可借鉴的是把一条示范拆成可复用的动作和可替换的外观。若任务运动仍适用，改变场景时可能不必重录动作，而是重新生成训练图像；数据复用因此不只靠图像增强。

### 下一步读哪里

优先核查运动基元如何生成有效动作、两阶段校准需要什么数据，以及相同运动的纯网格对照；再检查逐任务试验次数、目标场景适配流程和成本口径。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/LEGS Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.01458v2 Announce Type: replace Abstract: Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have so far transferred poorly to humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) background reconstructed from a handheld scene capture. LEGS uses a procedural motion-primitive generator to synthesize labeled demonstrations at scale without human teleoperation, and a two-stage color calibration that aligns renders to the deployment camera. On a Unitree G1 humanoid robot, across three pick-and-place tasks of increasing whole-body difficulty and three VLA backbones ($\psi_0$, $\pi_{0.5}$, GR00T N1.6), a policy trained purely on LEGS data matches or exceeds one trained on human teleoperation demos on every experiment. It also outperforms a mesh-only baseline trained on the same motions without the calibrated 3DGS frontend. Because motion is recorded independently of appearance, the same demonstrations can be re-rendered for a target scene and objects at over 15x lower cost than teleoperation. When both the objects and the scene change, a policy trained on LEGS-AUG data re-rendered for that target maintains task success, while the teleop baseline fails entirely. Code and videos are available at https://hojjunekim.github.io/legs/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.01458
- Authors: Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
