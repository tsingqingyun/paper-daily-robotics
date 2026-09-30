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
url: "https://arxiv.org/abs/2609.37181v1"
published: "2026-09-29T10:05:10Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> EgoHumanoid-V2 尝试用人的第一视角示范教机器人边走边操作：先把人的动作修正到机器人身体能做到，再处理人手与机器手在画面中的差别。四项真机任务中，这种人类数据训练出的策略，任务得分可与遥操作数据训练的策略相当。

## 问题

人类示范容易采集，却不能直接作为机器人动作标签：身体结构、动力学和相机看到的身体都不同。摘要指出，既有第一视角迁移工作主要在解耦控制下研究场景泛化，对协调全身技能的直接迁移探索较少；难点是提高末端精度时仍保住全身协同。

### 用一个例子理解

理解用例（非论文实验）：输入人走近桌子并双手搬盒子的第一视角示范；系统修正人体动作到机器人参考，再细化可执行性并处理视觉差异；训练后的 VLA 根据当前图像和指令输出协调移动与搬运的动作。

## 创新点或方法

相比把移动和操作解耦处理，本文采用由粗到细的动作对齐：先做运动学参考修正，再做考虑动力学的细化，兼顾末端位姿和身体协调。视觉侧使用机器人手臂渲染及训练时图像增强，减少人机外观差异并提高视角鲁棒性。训练阶段用对齐的人类数据训练 VLA；推理阶段在目标任务上执行，不需要该任务的机器人示范。具体损失、动力学细化算法和底层控制接口未说明。

### 方法如何工作

1. 从人类示范建立机器人动作参考并做运动学修正，减少身体结构差异造成的末端偏差。
2. 用动力学感知细化处理参考动作，使精度改善与全身协调兼容；摘要未说明求解方式。
3. 通过机器人手臂渲染和图像增强处理训练图像，减轻外观及视角差异。
4. 用对齐数据训练 VLA，再在目标任务上直接执行，以检验人类示范能否提供技能监督。

### 必要术语

- 移动操作：机器人一边移动身体一边操作物体；本文关注二者的协调。
- 末端位姿：手或工具的位置与朝向；它是动作对齐需要提高精度的对象。
- 视觉具身差异：人和机器人看到的身体外观不同；本文用渲染与增强缩小这种差异。

## 证据

摘要报告四项真机任务：用对齐人类数据训练的 VLA 实现零样本技能迁移，任务得分与遥操作数据训练的策略相当，采集成本更低。未给任务名称、得分定义、实际数值、数据量和成本核算。因此证据支持这四项任务的人类数据可用性，尚不能量化节省幅度或判断复杂度扩展。

## 局限

作者未在摘要中明确列出剩余局限。我会重点核查：需要哪些人体运动测量、场景几何或标定信息，动力学细化成本多大，以及失败是否集中于接触或平衡。零样本限定为无目标任务机器人示范，不代表完全没有机器人训练数据；这里只报告真机任务，未交代仿真训练环节。

- **判断**：适合评估能否用人类示范降低数据成本；摘要没给出总工时和节省幅度，暂时不能据此断言更便宜。

## 研究关联

如果采机器人示范太贵，可以考虑让人先演示，但要把动作转换和视觉差异当成数据工程的核心。值得优先核查的是：为了把人的示范变成可靠动作标签，究竟还需要多少测量、标定和人工处理。

### 下一步读哪里

下一步核查运动学修正保留哪些协调约束、动力学细化如何验证稳定性、手臂渲染怎样进入训练，以及与遥操作对比是否匹配数据量、任务覆盖和总采集工时。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/EgoHumanoid-V2 Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human demonstrations capture diverse scenes and rich whole-body skills without requiring robot teleoperation. Prior work on egocentric transfer has emphasized scene generalization in loco-manipulation under decoupled control, leaving direct transfer of coordinated whole-body skills less explored. We present EgoHumanoid-V2, the first egocentric human-to-humanoid skill transfer framework for coordinated whole-body loco-manipulation. At its core, coarse-to-fine action alignment combines kinematic reference correction with dynamics-aware refinement. It improves end-effector pose accuracy while preserving whole-body coordination. We also use robot-arm rendering and training-time image augmentation to reduce the visual embodiment gap and improve viewpoint robustness. On four real-world tasks, vision-language-action (VLA) policies trained on aligned human data show zero-shot skill transfer without target-task robot demonstrations. Task scores are comparable to those of policies trained on teleoperation data at a lower collection cost. These results support human data as direct skill supervision.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37181v1
- Authors: Jin Chen, Yiming Jiang, Chongyang Xu, Modi Shi, Shijia Peng, Li Chen, Tianyu Li, Mu Xu, Yilun Chen, Steven Hoi, Hongyang Li
- Published: 2026-09-29T10:05:10Z
- Age days: 0

</details>
