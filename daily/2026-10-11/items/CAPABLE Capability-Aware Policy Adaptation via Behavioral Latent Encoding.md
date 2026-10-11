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
url: "https://arxiv.org/abs/2610.11971v1"
published: "2026-10-08T13:46:52Z"
age_days: 2
score: 27
created: 2026-10-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding

> [!summary] 这篇论文到底做了什么（基于摘要）
> CAPABLE 在冻结的 VLA 旁边增加一个纠偏策略：先观察各关节收到命令后实际动了多少，再据此给原动作加上有限修正。它不需要先告诉系统哪个关节坏了，而是从身体响应中推断当前还能怎么动。

## 问题

VLA 学会的动作默认训练时的身体能力；关节故障改变命令执行效果后，同样的输出可能到不了目标。摘要指出既有恢复方法常依赖任务专门重训、故障标签、显式诊断或额外身体信息。真正瓶颈是让策略从可观测运动历史识别能力变化，并把这个变化转化为动作补偿。

### 用一个例子理解

理解用例（非论文实验）：机器人收到把杯子移到右侧的指令，一处关节转动小于命令值；CAPABLE 根据历史和运动学更新能力表示，残差策略调整后续手臂动作，输出修正后的命令。是否最终搬到杯子仍取决于剩余能力。

## 创新点或方法

旧做法先诊断故障或重训任务策略；CAPABLE 保留 VLA，用命令与响应历史估计实际能力，再训练残差策略修正手臂动作。共享时间编码器逐关节处理历史，Jacobian 把关节运动联系到末端效果，跨关节注意力表达关节之间的关系，自监督物理预测帮助学到有物理含义的表示。训练包含能力表示学习和残差强化学习；推理在线更新表示并叠加有界修正。摘要未说明奖励、历史长度和训练模块的先后关系。

### 方法如何工作

1. 记录命令与实际关节响应，得到执行偏差的时间历史，为能力推断提供依据。
2. 逐关节编码历史并用 Jacobian 联系末端运动，形成描述动作实际效果的表示。
3. 结合跨关节信息和自监督物理预测，让表示反映多关节共同作用。
4. 残差策略读取能力表示，为冻结 VLA 的动作添加有界修正，输出当前身体条件下的命令。

### 必要术语

- 冻结 VLA：原视觉语言动作策略不更新参数；本文在其输出旁增加适应机制。
- 残差策略：只输出原动作需要增减的部分；用于补偿执行偏差。
- Jacobian：描述关节小幅运动如何影响末端运动；用于给能力表示加入运动学关系。
- 留一执行器测试：故障训练排除一个执行器，再测试该处故障；用于检验跨关节迁移。

## 证据

摘要给出 28 项 LIBERO 任务：在一个未参与故障训练的执行器上，成功率从 24.8% 升至 59.3%，比参数量匹配的全局历史基线高 17.4 个百分点，同时保留健康状态性能。六个关节的逐一留出实验表明迁移不限于单个执行器；另有未见故障类型测试和实体 Franka Panda 恢复演示。上述数字来自摘要；它未给出健康性能、各关节结果或真机成功率，因此量化结论主要落在 LIBERO 测试范围。

## 局限

不需要故障标签，并不意味着不需要关节响应和运动学信息。恢复还受剩余身体能力与修正幅度限制：目标物理上不可达时，纠偏不能保证成功。真机证据不能直接替代系统性的真机统计，具体故障强度、适应速度和不可恢复边界需要核查。

- **判断**：值得深入读能力表示的监督目标和留出实验，它把“身体变化如何进入策略”讲得具体；部署前要确认可观测信息与修正权限。

## 研究关联

可借鉴的是把故障识别从“叫什么故障”改成“命令还能实现多少、会怎样影响末端”。如果补偿真正需要的是动作效果，这种连续能力表示可能比离散故障标签更适合迁移到未见关节变化。

### 下一步读哪里

先查自监督预测什么物理量、Jacobian 如何参与编码，再查留出关节时训练故障覆盖范围；重点看健康状态回退、故障出现后的适应时间及 Franka 真机实验设置。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/CAPABLE Capability-Aware Policy Adaptation via Behavioral Latent Encoding.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that motion contributes to end-effector behavior, online from command-response history and kinematics using a temporal encoder shared across joints, Jacobian grounding, cross-joint attention, and self-supervised physical prediction. The resulting representation conditions a residual policy that adds bounded corrections to the VLA arm action without fault labels or faulty-joint identifiers. Across 28 LIBERO tasks, CAPABLE raises success on an actuator excluded from fault training from 24.8% to 59.3%, outperforming a parameter-matched global-history baseline by 17.4 points while preserving healthy performance. Leave-one-actuator-out experiments across six joints show that this transfer is not specific to one actuator, and additional evaluations characterize transfer to unseen fault families and demonstrate recovery on a physical Franka Panda. https://capable-vla.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11971v1
- Authors: Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan, Jeroen Schafer, Andrew Melnik, Qing Yang, Michael Beetz
- Published: 2026-10-08T13:46:52Z
- Age days: 2

</details>
