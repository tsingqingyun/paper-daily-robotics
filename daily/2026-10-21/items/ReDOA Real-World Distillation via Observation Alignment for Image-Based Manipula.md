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
url: "https://arxiv.org/abs/2610.25691v1"
published: "2026-10-19T02:37:51Z"
age_days: 1
score: 33
created: 2026-10-21
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# ReDOA: Real-World Distillation via Observation Alignment for Image-Based Manipulation Policy Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> ReDOA 先在仿真里教会一个读取状态的教师策略控制机器人，再让它到真机上收集动作与真实图像，训练看图行动的学生策略。Observation Alignment 用来处理采集阶段与部署阶段的观察不匹配，让控制学习和视觉学习能够分开进行。

## 问题

目标是学会从图像控制真实机器人操作。真人示教昂贵，而全部在仿真里学又会受到动力学和传感观察差异影响。瓶颈是如何既减少专家示范，又让策略见到真实部署中的视觉输入；单纯模仿真人或在仿真中完成视觉策略蒸馏，各自都有成本或迁移问题。

### 用一个例子理解

理解用例（非论文实验）：目标是把桌面方块推到标记区；状态教师读取物体位置并在真机执行，采集相机图像与动作；训练后的学生输入图像，输出推动动作。这个用例展示知识传递路线，不代表论文的三个任务包含推方块。

## 创新点或方法

ReDOA 将控制与感知分开：状态教师先在仿真中学控制，再在真实机器人上执行，生成带真实视觉观察的轨迹；图像学生从这些轨迹学习教师的控制行为。Observation Alignment 负责解决数据采集与部署之间的观察不匹配，但摘要没有说明具体对齐哪些量、如何变换或优化。训练时需要状态教师、真机轨迹采集和学生蒸馏；最终部署对象是图像策略。教师在真机执行所需的状态如何获取，也未说明。

### 方法如何工作

1. 在仿真中训练读取状态的教师策略，先获得控制能力，避免同时承担真实图像学习的难度。
2. 让教师在真实机器人上执行，采集动作与真实视觉观察，使学生训练数据接触真实传感条件。
3. 通过 Observation Alignment 处理采集与部署观察的不匹配，为知识转移建立一致的输入条件；具体实现未说明。
4. 用采集轨迹蒸馏图像学生，使其从视觉输入学习控制，并作为最终图像策略部署。

### 必要术语

- 状态策略：读取位置等状态变量的控制策略；本文用它担任教师。
- 策略蒸馏：让学生学习教师的控制行为；本文借此把控制知识传给图像策略。
- 观察对齐：处理两个使用阶段的输入差异；本文针对采集与部署之间的不匹配。
- 非抓取操作：通过推、接触等方式改变物体状态；这是本文真机评测的任务范围。

## 证据

摘要报告三个非抓取式操作任务的真机实验，其中包含双臂操作。对比对象是使用真人示范的模仿学习，以及在仿真中进行的策略蒸馏；结论是联合考虑任务成功与执行效率时，ReDOA 总体表现更好。没有具体成功率、执行耗时、数据预算或综合评价规则，因此不能说它在每个任务、每个指标上都领先，也不能量化节省了多少采集成本。

## 局限

摆脱真人专家示范不等于无需真实采集或额外测量。教师如何跨过动力学差异、如何获得状态，以及失败轨迹如何处理，直接决定这种方法的适用条件。已有证据来自三个非抓取任务，不能据此推断抓取、复杂接触或更广任务也同样有效。

- **判断**：值得细读 Observation Alignment 和真机数据采集条件；这两部分决定它能否成为可复用的数据获取办法，而不只是特定设备上的成功流程。

## 研究关联

这里改变问题拆法的是：控制知识可以在仿真中获得，而视觉对应关系可以在真机执行时补齐。如果状态策略能够可靠地在真机运行，就有机会用它生成真实视觉教学数据，减少让专家逐条演示的需求。

### 下一步读哪里

优先核查教师在真机上需要哪些状态测量、Observation Alignment 对齐的具体对象及部署依赖。实验应看相同数据预算下的成功率与耗时、教师自身的真机表现，以及去掉对齐后的结果；摘要没有这些分项信息。

- **概念**：世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/ReDOA Real-World Distillation via Observation Alignment for Image-Based Manipula.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Data-driven learning for general-purpose robotic manipulation presents a fundamental trade-off between data-collection cost and adaptability to real-world environments. Imitation learning (IL) requires costly human demonstrations, whereas simulation-based learning is vulnerable to sim-to-real gaps in dynamics and sensor observations. We propose ReDOA (Real-World Distillation via Observation Alignment), a framework that decouples control learning from perception learning to learn image-based policies in the real world. A state-based teacher policy trained in simulation is executed on a real robot, and its control knowledge is distilled into an image-based student policy using the collected trajectories. Observation Alignment resolves observation mismatches between data collection and deployment. This framework collects successful, efficiently executed trajectories paired with real-world visual observations, without requiring demonstrations from human experts. In real-robot experiments on three non-prehensile manipulation tasks, including bimanual manipulation, our method achieves better overall performance when jointly considering task success and execution efficiency than both IL based on human demonstrations and policy distillation in simulation. https://isri-aist.github.io/redoa-project-page/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25691v1
- Authors: Kotaro Kajitsuka, Masaki Murooka, Fumio Kanehiro
- Published: 2026-10-19T02:37:51Z
- Age days: 1

</details>
