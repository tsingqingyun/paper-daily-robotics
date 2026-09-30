---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03889"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-09-05
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> FWBC-VLA 用无传感器残余力矩估计器 HSR-Force 给 VLA 补上接触感知，再由补偿生成器把任务动作与全身纠偏动作合并。目标是在不加力/力矩传感器的情况下完成轮腿机器人的接触丰富型移动操作。

## 这篇到底在做什么

- **卡在哪里**：VLA 能生成语义层动作，却不了解动作造成的物理接触；传统 WBC 虽能稳定机体，却分不清任务接触力和外部扰动。直接加装力传感器又有硬件与集成成本。
- **关键解法**：HSR-Force 从残余力矩估计接触强度及时间变化，将接触 token 注入 VLA 动作专家；同时把本体状态、由雅可比量推得的机体坐标系力和接触状态输入补偿生成器，输出纠偏动作，与操作动作融合后交给 WBC。预训练 VLA 在超过5,000回合的 WL&Arm 数据集上全参数微调。
- **拿什么证明**：摘要报告在白板擦拭和带闭门器的开门任务上进行了真实机器人实验并验证有效性，但未给成功率、力控误差或对照数字。

## 值不值得读

- **和你的研究有什么关系**：它直接连接 VLA 的语义动作和低层接触控制，对具身系统从自由空间抓取走向擦拭、推门等持续接触任务具有实际价值。
- **先别急着信**：摘要不足以判断无传感器力估计的精度、对外扰与任务力的区分能力，以及全参数微调和补偿模块各自贡献。
- **判断**：做接触型 VLA 或轮腿移动操作者值得读方法实现；证据数字不足，结论强度需等全文实验确认。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/FWBC-VLA Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03889v1 Announce Type: new Abstract: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize the robot, it cannot distinguish task-relevant interaction forces from forces induced by external disturbances during manipulation. Although force/torque sensors provide direct measurements of physical interactions, retrofitting them entails additional hardware costs and substantial integration effort, particularly for platforms not designed with sensor integration in mind. To address this problem, we propose FWBC-VLA, a force-aware framework that bridges task-level VLA action generation and low-level whole-body compensation control for wheeled-legged robots. First, we introduce HSR-Force, a sensorless residual-torque estimator for inferring contact strength and its temporal variation. These contact estimates are then encoded as tokens and injected into the VLA action expert during action decoding, enabling the policy to perceive contact onset, sustained loading, and release. For loco-manipulation tasks, all parameters of the pretrained VLA backbone are fine-tuned on our WL\&Arm Dataset, which comprises more than 5,000 episodes. Moreover, the robot's proprioceptive state, the Jacobian-derived body-frame force estimate, and the estimated contact state are jointly fed into a compensation generator to produce corrective actions. The manipulation-centric actions are subsequently combined with the corrective actions and passed to the WBC policy for execution. Real-world experiments on whiteboard wiping and door opening with a door closer demonstrate the effectiveness of our FWBC-VLA in contact-rich loco-manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03889
- Authors: Yutian Zhang, Siyuan Ma, Liwen Yang, Yang Li, Ce Hao, Haozhen Chi, Dong We, Qiaojun Yu, Dibo Hou
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
