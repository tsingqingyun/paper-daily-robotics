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
url: "https://arxiv.org/abs/2610.34356"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 41
created: 2026-11-04
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions

> [!summary] 这篇论文到底做了什么（基于摘要）
> RynnVLA-Latent 想让没有机器人控制记录的视频也能用于训练机器人：先用 RynnLAM 从画面变化中提取带三维运动信息的潜在动作，再训练策略预测这些动作，最后适配具体机器人的控制指令。关键是尽量把物体运动与相机运动分开，避免把镜头变化学成操作动作。

## 问题

任务是根据视觉和语言控制机器人操作物体。瓶颈有两个：带动作标签的示范少，不同机器人的控制量又不兼容。人类和仿真视频很多，却没有可直接共用的机器人指令；仅学习画面变化，还可能把外观变化或相机移动误当成需要控制的运动。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子移到盘子旁”的视频，先分离镜头移动与杯子移动，提取潜在动作；策略结合当前画面和指令预测动作段，适配后的机器人执行抓取和搬移。

## 创新点或方法

旧路径依赖各机器人自己的动作标签；本文先把异构视频转成统一的连续潜在动作。RynnLAM 结合残差式未来特征预测、补偿相机运动的三维流监督，以及相机运动解耦，约束表示关注可用于控制的变化。预训练时，策略通过流匹配学习从观察和语言预测一段潜在动作；随后适配骨干和动作专家，学习具体机器人的动作。实际部署仍要输出该机器人的控制量，摘要未说明潜在动作与最终控制之间的完整计算路径。

### 方法如何工作

1. 把人类、机器人和仿真视频中的视觉转变交给 RynnLAM，得到不依赖原生控制量的动作描述。
2. 用未来特征预测和三维运动监督约束描述，并分离相机运动，使表示更贴近操作变化。
3. 用这些描述监督策略预测潜在动作段，让大量视频参与策略预训练。
4. 用机器人动作适配骨干和动作专家，获得可执行控制；具体适配损失与部署路径摘要只说明到此。

### 必要术语

- 潜在动作：用学习到的连续数值表示一次运动；本文用它统一不同视频的监督。
- 三维流：场景点在三维空间中的位移；本文借此约束动作表示关注真实运动。
- 流匹配：学习把简单分布逐步变成目标分布的生成方法；本文用它预测潜在动作段。

## 证据

摘要报告使用 30.1K 小时视频，生成 745.52M 个潜在动作描述符。4B 策略在 LIBERO、LIBERO-Plus、VLABench 五条赛道和 RoboTwin 2.0 上分别达到 98.8%、84.7%、51.9% 和 88.6%；其中 LIBERO-Plus 未作基准专门适配。六项真机任务覆盖灵巧手与移动夹爪平台，在所比较方法中成功率最高，但未给具体数值和基线名称。摘要提到表示消融与数据扩展实验，却未提供细项，因而尚不能分清各机制贡献。

## 局限

视频规模和最终成绩不能单独证明三维监督带来了多少收益。需要核查相机补偿误差、三维流监督来源，以及适配新机器人需要多少动作数据；摘要没有明确列出作者承认的局限。

- **判断**：值得读到表示学习目标和消融实验，因为最关键的问题是它究竟怎样让视频变化成为可迁移的控制线索。

## 研究关联

值得借鉴的是先设计跨数据来源共用的运动监督，再适配控制接口。这为利用无动作标签视频提供了具体路线；前提是抽出的表示确实保留操作相关运动，而非主要记录拍摄方式。

### 下一步读哪里

先核查残差预测的具体目标、三维流如何获得、相机运动如何估计；再看固定数据量的表示消融，以及跨机器人适配的数据需求。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/RynnVLA-Latent Scaling Robotic Manipulation Foundation Models with 3D-Grounded L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.34356v2 Announce Type: replace Abstract: Scaling vision-language-action (VLA) models is constrained by scarce action-labeled demonstrations and incompatible control spaces across robot embodiments. We present RynnVLA-Latent, a framework that turns heterogeneous interaction videos into scalable supervision for robot policy pretraining. At its core, RynnLAM learns continuous, 3D-grounded latent actions from visual transitions without requiring native robot controls. By combining residual future-feature prediction, camera-compensated 3D-flow supervision, and camera-motion decoupling, RynnLAM encourages representations that capture control-relevant motion rather than appearance changes alone. We apply RynnLAM to 30.1K hours of human, robot, and simulation videos, producing 745.52M latent-action descriptors. RynnVLA-Latent then learns to predict latent-action chunks from visual observations and language through flow matching, before adapting its pretrained backbone and action expert to embodiment-specific robot actions. The resulting 4B policy achieves 98.8% success on LIBERO, 84.7% on LIBERO-Plus without benchmark-specific adaptation, 51.9% average success across five VLABench tracks, and 88.6% average success on the RoboTwin 2.0 bimanual benchmark. It also achieves the highest observed success rates among the compared methods on six real-world manipulation tasks across dexterous-hand and mobile-gripper platforms. Together with representation ablations and data-scaling results, these findings demonstrate the potential of latent-action supervision for scaling robot policy learning beyond native action-labeled data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.34356
- Authors: Haoyu Zhao, Xingyue Zhao, Zhian Su, Bohan Hou, Yinzhou Tang, Fengyi Wang, Kehan Li, Yuming Jiang, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Siteng Huang, Xin Li, Zhongyu Li
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
