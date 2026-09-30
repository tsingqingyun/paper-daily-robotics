---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03889v1"
published: "2026-09-03T14:10:47Z"
age_days: 3
score: 39
created: 2026-09-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> FWBC-VLA 用无力传感器的 HSR-Force 估计接触强度与变化，把接触信息送入 VLA，同时生成全身补偿动作，让轮腿机器人执行擦拭、开门等接触密集任务。

## 问题

VLA能生成语义层动作却不理解动作引起的物理接触；WBC能维持稳定但分不清任务所需接触力与外部扰动，而加装力/力矩传感器又有硬件与集成成本。

## 创新点或方法

系统从残余力矩估计接触状态，将其编码为token注入VLA动作解码；再联合本体状态、由雅可比量推得的机体坐标系力和接触状态生成纠偏动作，与操作动作合并后交给WBC执行。预训练VLA在超过5,000段的WL&Arm数据集上全参数微调。

## 证据

摘要报告在真实轮腿机器人白板擦拭和带闭门器开门任务上验证有效，并给出训练集超过5,000个episode；未给出成功率、力估计误差或相对基线数字。


## 局限

关键待核查点是无传感器力估计在模型误差、碰撞和外扰下能否可靠区分任务接触，以及各模块对最终收益的贡献。

- **判断**：做轮腿移动操作或接触控制者值得精读系统与控制部分；仅关注通用VLA者可先看架构和真实实验。

## 研究关联

它把VLA与接触估计、全身控制连接起来，对研究移动操作和接触丰富具身任务的人具有直接系统设计价值。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/FWBC-VLA Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize the robot, it cannot distinguish task-relevant interaction forces from forces induced by external disturbances during manipulation. Although force/torque sensors provide direct measurements of physical interactions, retrofitting them entails additional hardware costs and substantial integration effort, particularly for platforms not designed with sensor integration in mind. To address this problem, we propose FWBC-VLA, a force-aware framework that bridges task-level VLA action generation and low-level whole-body compensation control for wheeled-legged robots. First, we introduce HSR-Force, a sensorless residual-torque estimator for inferring contact strength and its temporal variation. These contact estimates are then encoded as tokens and injected into the VLA action expert during action decoding, enabling the policy to perceive contact onset, sustained loading, and release. For loco-manipulation tasks, all parameters of the pretrained VLA backbone are fine-tuned on our WL\&Arm Dataset, which comprises more than 5,000 episodes. Moreover, the robot's proprioceptive state, the Jacobian-derived body-frame force estimate, and the estimated contact state are jointly fed into a compensation generator to produce corrective actions. The manipulation-centric actions are subsequently combined with the corrective actions and passed to the WBC policy for execution. Real-world experiments on whiteboard wiping and door opening with a door closer demonstrate the effectiveness of our FWBC-VLA in contact-rich loco-manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03889v1
- Authors: Yutian Zhang, Siyuan Ma, Liwen Yang, Yang Li, Ce Hao, Haozhen Chi, Dong We, Qiaojun Yu, Dibo Hou
- Published: 2026-09-03T14:10:47Z
- Age days: 3

</details>
