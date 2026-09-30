---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07933v1"
published: "2026-09-07T19:46:56Z"
age_days: 2
score: 25
created: 2026-09-10
concepts: ["智能体 Agent", "机器人学习"]
---

# SPOT: Spatial Perception-Oriented Long-Horizon Humanoid Teleoperation

> [!summary] 先说人话（基于摘要）
> SPOT 改善的是遥操作员“看清周围”的能力：提供宽视野立体画面和稳定显示，让人转头观察时不会顺带驱动机器人。

## 这篇到底在做什么

- **卡在哪里**：长时行走操作需要持续掌握物体位置、环境和机器人姿态；窄视野、移动中的画面晃动，以及头部视角与机器人动作耦合会破坏空间感知。
- **关键解法**：将机器人双目鱼眼图像稳定后呈现在操作员周围的虚拟半球上，结合宽视野立体显示和解耦自由观察；自然转头只改变浏览位置，不发出机器人头部或躯干运动命令。
- **拿什么证明**：在掉落恢复、周边拾取、大工作区双臂操作、精细对齐和动态交互任务上评测，报告效率、精度和恢复速度提升。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习团队，这是改善长时人形示范采集的上游工具；对智能体研究的价值主要是更完整、稳定的人类操作数据。
- **先别急着信**：需核查用户实验设计、各组件收益和长时操作负担；摘要没有展示采集数据对下游策略的提升。
- **判断**：做遥操作采集值得读硬件与人机实验，实际价值在操作界面，学习收益仍需单独检验。

## 研究关联

- **概念**：[[智能体 Agent]] [[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/SPOT Spatial Perception-Oriented Long-Horizon Humanoid Teleoperation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

High-quality demonstration data is becoming a central bottleneck for training general-purpose humanoid robots. While recent humanoid teleoperation systems have made substantial progress in retargeting human motion to robot motion, long-horizon loco-manipulation requires another capability: operators must maintain task-relevant spatial awareness over time, e.g., object locations, surrounding environments, the robot's pose. We call the extent of this awareness the operator's perceptual horizon. However, existing methods often shorten this: narrow views miss peripheral events, robot-mounted cameras become unstable during locomotion, and coupled head-view control makes looking around interfere with robot motion. We present SPOT, a Spatial Perception-Oriented VR Teleoperation system for collecting long-horizon humanoid demonstration data by providing extended perceptual horizon. SPOT combines a robot-mounted binocular fisheye camera, a wide-field stereoscopic display, viewpoint-decoupled free-looking, and visual stabilization to provide a robot-centric view that is wide, stable, and actively inspectable. Unlike conventional egocentric interfaces, SPOT decouples visual exploration from robot actuation: the egocentric stereo observation is rendered on a virtual hemisphere around the operator, so natural head rotations change where the operator looks within the wide-field view rather than commanding the robot head, camera, or torso. We evaluate SPOT on perception-critical humanoid data-collection tasks spanning drop recovery, peripheral retrieval, large-workspace bimanual manipulation, fine alignment, and dynamic interaction. SPOT improves efficiency, accuracy, and recovery speed, demonstrating its effectiveness for user-friendly and scalable long-horizon humanoid data collection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07933v1
- Authors: Lixing Fang, Ziyan Xiong, Sunli Chen, Zhiyang Dou, Chuang Gan
- Published: 2026-09-07T19:46:56Z
- Age days: 2

</details>
