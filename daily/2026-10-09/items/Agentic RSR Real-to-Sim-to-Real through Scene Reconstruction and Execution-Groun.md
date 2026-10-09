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
url: "https://arxiv.org/abs/2610.10479v1"
published: "2026-10-07T17:37:20Z"
age_days: 1
score: 33
created: 2026-10-09
concepts: ["智能体 Agent", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> Agentic RSR 把重建工作台、在仿真里写策略、再到真机执行连成一个由同一任务驱动的流程。它不仅追求场景看起来像，还检查任务交互，并让策略逐步改用真机能够获得的视觉信息。

## 问题

任务是从真实工作空间建立仿真，在其中开发操作策略，再迁回真实机器人。瓶颈有两个：重建必须保留任务所需交互，策略也不能一直依赖仿真独有的物体精确位姿。摘要指出重建与策略开发常被分开处理，容易让场景可视上相似，却无法支撑实际执行。

### 用一个例子理解

理解用例（非论文实验）：输入工作台视频、“把积木放入盒子”及机器人模型；代理建立场景并测试抓放，编码代理先用物体位姿调通策略，再改用视觉；真机观察当前状态、通过安全检查后执行，并根据反馈决定重试。

## 创新点或方法

本文以同一操作任务贯穿流程。重建代理接收视频、任务描述和已知机器人模型，恢复尺度、利用视觉反馈修正场景，并在 MuJoCo 中检查交互。编码代理先借助物体位姿开发策略，再转向视觉观察与随机化仿真。这里是策略开发过程，摘要未说明必须进行神经网络训练。执行时策略一次调用可包含多次观察和动作，代理依据反馈继续、重试或修改；共享任务接口将策略与经验带到真机。

### 方法如何工作

1. 从视频、任务和机器人模型恢复有尺度的场景，为机器人动作提供可用空间。
2. 利用视觉反馈修正场景并检查任务交互，确认仿真能支持目标操作。
3. 先用物体位姿开发策略，再转向视觉与随机化仿真，逐步适应真实观察条件。
4. 通过共享接口在真机执行，结合新观察、安全检查和执行反馈决定继续、重试或修订。

### 必要术语

- Real-to-Sim-to-Real：由真实环境建仿真，再把策略带回真实环境；本文的完整流程。
- 特权物体位姿：仿真能直接提供的精确位置与朝向；本文开发策略时先使用它。
- 随机化仿真：改变模拟条件以测试或适应差异；本文用于策略开发后期。
- 执行反馈：动作后的观测或结果；本文据此决定后续处理。

## 证据

摘要报告两种机器人、18 个重建场景：相对参考深度估计的四视角平均 Depth MAE 为 0.1057 米，Lab ΔE₇₆ 为 11.04，灰度 SSIM 为 0.6990。真机汇总成功率达到仿真成功率的 80%，这是比例关系，不是绝对成功率 80%。没有任务明细、试验次数、对照方法或仿真绝对成功率，无法判断成功覆盖范围。

## 局限

深度参照是参考估计，不应直接视为精确几何真值；颜色和结构相似度也不能证明摩擦、接触等物理交互正确。真机保留一定比例的仿真表现支持迁移可行，但代理修正、观察变化和随机化各贡献多少，仍需对照实验确认。

- **判断**：值得读策略从位姿转向视觉的过程与仿真真机配对结果，因为它们决定这套流程能否实际复用。

## 研究关联

值得借鉴的是以任务交互检验重建，而不是仅用视觉相似度验收场景；同时在仿真阶段就逐步撤掉真机拿不到的信息。这样能更早暴露场景物理错误与策略观察依赖，减少直到上真机才发现无法执行的情况。

### 下一步读哪里

核查尺度恢复和交互检查的标准、视觉策略如何获得物体信息，以及随机化范围；重点查仿真与真机绝对成功率、任务配对方式、重试预算和安全检查的执行条件。

- **概念**：智能体 Agent 世界模型 Sim2Real 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/Agentic RSR Real-to-Sim-to-Real through Scene Reconstruction and Execution-Groun.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an agent recovers metric scale, iteratively refines the scene using visual feedback, and checks task-relevant interactions in MuJoCo. A coding agent then develops an executable policy, progressing from privileged object poses to visual observations and randomized simulation. The policy can interleave multiple observations and actions within one invocation, while the agent uses execution feedback to continue, retry, or revise its approach. A shared task-level interface carries the policy and accumulated experience to the real robot, where fresh observations and safety checks guide execution. Across 18 reconstructed scenes involving two robots, the mean four-view Depth MAE against reference depth estimates is 0.1057 m, the mean Lab $ΔE_{76}$ is 11.04, and the mean grayscale SSIM is 0.6990. In real-robot experiments, the aggregate task success rate reaches 80% of the simulation task success rate, indicating substantial retention of simulated performance on hardware. Code and reconstructed scene data will be made publicly available.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10479v1
- Authors: Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren, Bowen Yang, Weisheng Xu, Qiwei Wu, Hui Cheng, Renjing Xu
- Published: 2026-10-07T17:37:20Z
- Age days: 1

</details>
