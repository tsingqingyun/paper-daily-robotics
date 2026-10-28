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
url: "https://arxiv.org/abs/2610.36789v1"
published: "2026-10-27T07:53:51Z"
age_days: 0
score: 29
created: 2026-10-28
concepts: ["具身智能评测与基准"]
---

# A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Torch-Hand 想让机器手既有接近人手的关节活动能力，又能稳定用力、方便控制。它用全连杆传动和螺杆连杆驱动，把电机运动与关节运动建立直接对应，并减少一个关节动作对其他关节的意外牵动。

## 问题

任务是在紧凑的五指手里兼顾灵活姿态、机械可靠性、承载与控制。摘要指出，已有设计在这些要求间持续取舍：关节丰富并不自动意味着容易控制或足够有力，但没有逐项说明腱驱动或混合驱动的具体失败案例。

### 用一个例子理解

理解用例（非论文实验）：输入“捏起一枚小积木”的目标；控制器安排拇指与食指接触姿态，再驱动对应关节靠拢；输出稳定捏持姿态。这个例子说明独立寻址和主动协调的用途，不代表论文验证了该任务。

## 创新点或方法

相对于腱驱动或混合传动路线，Torch-Hand 采用全连杆架构，将所有执行器装进手掌，并按类似串联机器人的方式安排运动关系。手有 21 个自由度：拇指 5 个，其余四指各 4 个。拇指根部支持多轴运动，以改变对掌姿态和接触朝向。设计先从机械上减少功能自由度间的串扰，再由控制主动协调多关节动作。这是硬件与运动控制设计；摘要没有说明学习训练，也未给出运行时控制器细节。

### 方法如何工作

1. 用拇指和四指的关节配置提供多种接触姿态，为抓握不同形状物体留下运动空间。
2. 通过掌内执行器与连杆传动把电机动作传到关节，建立便于控制的运动对应。
3. 机械上减少非预期关节联动，使指定动作更少扰动其他关节。
4. 主动协调可独立控制的自由度，组成多关节操作；具体规划和控制算法摘要只说明到此。

### 必要术语

- 自由度：可独立变化的运动方向；本文用它描述手的运动能力。
- CMC 关节：拇指根部的腕掌关节；本文利用其多轴运动扩大对掌姿态。
- 机械解耦：减少一个运动对其他运动的意外影响；为主动协调提供更可控的基础。

## 证据

摘要列出可达工作空间、指尖协调轨迹、拇指对掌、33 类抓握分类覆盖、抓握力、载荷和任务操作等评估项目。除自由度配置外，没有提供力、载荷、成功率或对照数据。“评估 33 类抓握覆盖”也不等于已成功完成全部 33 类。输入支持理解设计及验证方向，尚不足以量化其相对优势。

## 局限

这项工作描述的是实体手硬件，但摘要没有交代各项实验的工况、重复次数和具体结果。我的待核查问题是：紧凑掌内布局如何影响重量、散热和维修，以及较大抓握力能否同时用于细小、易损物体的精细操作。

- **判断**：值得读机械结构和实测部分；是否适合采用，取决于力、精度、耐久性与体积之间的实际取舍。

## 研究关联

值得借鉴的是先通过机械设计让关节响应更独立，再按任务需要主动组合动作。如果控制困难源于传动串扰，单纯换更复杂的控制算法可能绕了远路；改善电机到关节的对应关系也能直接降低控制负担。

### 下一步读哪里

优先检查 21 个自由度与执行器如何对应、螺杆连杆的运动映射，以及负载下的串扰测量；再核查抓握分类覆盖的判定标准和实际任务成功率。

- **概念**：具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/A fully articulated humanoid dexterous hand with human-level joint structure ena.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous manipulation in unstructured environments. Here we present Torch-Hand, a fully articulated humanoid dexterous hand that replicates the joint structure and motion hierarchy of the human hand with 21 degrees of freedom (DOF), comprising a highly articulated five-DOF thumb and four DOF in each of the remaining fingers. The differentiated thumb integrates multi-axis CMC motion to provide broad opposition and flexible contact orientation relative to the four fingers. Unlike tendon-driven or hybrid actuation approaches, Torch-Hand adopts an entirely linkage-based transmission architecture. By integrating screw-linkage actuation, the hand achieves high grasping force and substantial payload capacity while maintaining a compact anthropomorphic form. Its actuation architecture is optimized for control tractability, with all actuators integrated within the palm and arranged in a serial-robot-like configuration that establishes a direct correspondence between motor motion and joint kinematics. This architecture mechanically decouples functional DOF to reduce unintended inter-joint motion propagation, while allowing independently addressable DOF to be actively coordinated into coupled multi-joint motion patterns during complex manipulation. Comprehensive experiments assess reachable workspace, coordinated fingertip trajectories, thumb opposition, 33-grasp taxonomy coverage, grasping force, payload capacity and task-level manipulation. These results establish Torch-Hand as a robust hardware foundation for dexterous embodied manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36789v1
- Authors: Jihao Li, Jianguo Wang, Haotian Guo, Yanzhe Wang, Guodong Lu, Huixu Dong
- Published: 2026-10-27T07:53:51Z
- Age days: 0

</details>
