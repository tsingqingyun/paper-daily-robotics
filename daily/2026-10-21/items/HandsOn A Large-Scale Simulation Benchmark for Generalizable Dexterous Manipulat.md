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
url: "https://arxiv.org/abs/2610.26765v1"
published: "2026-10-19T17:22:48Z"
age_days: 1
score: 35
created: 2026-10-21
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> HandsOn 提供可以组合机械臂、灵巧手、物体和任务的仿真平台，检验策略能否可靠完成多样操作及迁移任务。它还把失败拆到接触、动作协调和保持已完成目标等阶段，帮助解释机器人究竟卡在哪里。

## 问题

通用操作要求同一类能力跨机器人形态、物体和任务要求工作。单个任务成功难以说明换资产、换关系或串联技能后仍可靠；最终成功率也看不出是没碰到物体、手臂与手指失配，还是后续动作破坏了先前成果。HandsOn 用共享任务与阶段诊断处理这些评测需求。

### 用一个例子理解

理解用例（非论文实验）：输入桌面观测和“打开盒盖，再把软物体放进去”；策略先建立开盖接触、执行开盖，再抓取放入。评测除最终完成外，还检查开盖成果是否在后续过程中保持，以及失败是否来自抓取或顺序；这里的具体任务为自拟。

## 创新点或方法

平台支持组合不同机械臂、灵巧手与随机场景。训练和执行测试使用 Core-50 及演示数据；Transfer-16 则在没有目标任务训练演示的条件下，测试资产与关系迁移、技能组合及可变形物体操作。评测涵盖扩散策略、VLA、WAM 与提示驱动的 VLM 方法。推理时各方法执行任务，再统计成功与阶段失败；模型各自训练配方、跨形态输入输出如何统一，摘要未说明。

### 方法如何工作

1. 组合机械臂、灵巧手、资产和随机场景，生成具有不同操作要求的测试环境。
2. 用演示支持 Core-50 的学习，再执行统一任务，得到多任务策略的完成率。
3. 在缺少目标任务训练演示的 Transfer-16 上执行，检查已有能力能否支持迁移与技能组合。
4. 分析接触、协调、保持目标及任务排序等阶段，把最终失败定位为更具体的执行瓶颈。

### 必要术语

- 跨形态：机器人身体或执行器配置发生变化；本文平台支持多种机械臂与灵巧手。
- 技能组合：把已有操作接成更长任务；本文用它检验串联后是否仍可靠。
- 阶段诊断：按执行过程定位失败；本文借此区分接触、协调、保持与排序问题。

## 证据

摘要给出五种机械臂、六种灵巧手、约 200 个资产、18,000 条人工演示及 66 个经人工核验的任务。最佳已训练多任务策略在 Core-50 达到 29.1%。未经基准微调的 GPT-6 使用 move_eef 控制手掌和手指，在合计 660 次试验中，Core-50 成功率为 5.2%，Transfer-16 为 1.9%。这些是仿真基准结果；真机仅提供定性执行展示。摘要未给任务分项、置信区间及各训练策略成绩。

## 局限

定性真机展示说明存在迁移实例，不能替代系统性的真机成功率。GPT-6 的结果同时受提示、工具接口和控制方式影响，不能单独归因于推理能力。Transfer-16 没有目标任务演示，也不意味着所有组件或物体都从未见过；具体划分需要核查。

- **判断**：值得细读任务划分和阶段诊断，因为它既提供难度参照，也能把低成功率变成可追查的执行问题。

## 研究关联

值得借鉴的是把“任务完成”继续拆成建立接触、协调动作、保持成果和正确排序。若策略经常完成前半段却最终失败，这种诊断能帮助判断应改接触控制、动作耦合还是任务调度，而不是笼统归因于模型不够大。

### 下一步读哪里

先核查 Core-50 与 Transfer-16 的训练重叠、成功判据及随机化范围；再看阶段标签如何判定、不同方法是否获得相当信息和控制能力，以及真机展示覆盖哪些形态与任务。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/HandsOn A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The benchmark pairs 18,000 curated human demonstrations with 66 human-verified tasks: Core-50 supports demonstration-based learning and execution tests, while Transfer-16 evaluates asset and relation transfer, skill composition, and deformable manipulation without target-task training demonstrations. Qualitative real-robot rollouts illustrate sim-to-real transfer. Across diffusion, vision-language-action, world-action, and prompted VLM-based methods, the best trained multi-task policy achieves 29.1% Core-50 success. Without benchmark finetuning, GPT-6 using move_eef for palm-and-finger control achieves 5.2% on Core-50 and 1.9% on Transfer-16 over 660 trials. Trained-policy stage diagnostics expose failures in contact establishment, action coordination, and maintaining achieved goals, with additional sequencing errors in composed tasks. HandsOn provides a shared basis for investigating manipulation generalization and the limits of reliable physical interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26765v1
- Authors: Tianwei Luo, Yiming He, Hongjin Wu, Ting Pan, Debin Ren, Haorui Guo, Junlin Yang, Yuxin Zuo, Zhehao Kou, Kaisen Yang, Zhuoqun Lai, Yi Ding, Jiale Yu, Yuchen Zhang, Zijie Qiu, Haozhan Li, Ning Ding
- Published: 2026-10-19T17:22:48Z
- Age days: 1

</details>
