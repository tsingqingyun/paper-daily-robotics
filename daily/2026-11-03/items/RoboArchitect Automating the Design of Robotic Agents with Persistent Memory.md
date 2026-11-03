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
url: "https://arxiv.org/abs/2610.42141v1"
published: "2026-10-30T17:58:48Z"
age_days: 3
score: 29
created: 2026-11-03
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboArchitect 不改机器人策略的权重，而让编码模型看执行失败、修改外围控制代码，再反复试验。代码决定何时调用策略、使用视觉工具或直接控制机械臂，还能保存后续可用的经验。

## 问题

具体任务是让已有机器人策略适应新场景和新任务。冻结策略放进合适的控制程序后能做得更好，但这种程序通常靠人手写，换机器人或基准又要重做。瓶颈因此不只在策略本身，也在何时调用它、失败后怎样干预，以及如何复用经验。

### 用一个例子理解

理解用例（非论文实验）：输入是取出柜内物体的指令和现场观测。首次执行从上方接近时受阻，编码模型据轨迹修改程序，加入侧向接近条件并保存有效抓取深度；后续执行由该程序选择动作，输出取物尝试。

## 创新点或方法

旧做法由人设计策略外围的调度与补救逻辑；RoboArchitect 让编码模型观察执行轨迹、诊断失败并迭代改写这些逻辑。优化发生在一组专用回合上，之后在留出场景和任务上测试；全程不更新模型权重。执行时，演化出的程序协调策略、工具与直接动作，并使用持久记忆。摘要未说明代码修改的选择规则、记忆格式和写入时机。

### 方法如何工作

1. 冻结已有策略，在优化回合中执行任务，收集可供诊断的轨迹。
2. 编码模型观察失败并修改外围程序，把问题转化为调用、工具使用或直接控制逻辑。
3. 反复运行修改后的程序，继续修订行为，并让持久记忆携带有效经验；筛选细节未说明。
4. 在留出场景与任务上执行最终程序，以检验改动能否超出优化回合发挥作用。

### 必要术语

- Harness：包在策略外的控制程序；它决定调用策略、工具和直接动作的时机。
- 冻结策略：参数保持不变的机器人模型；本文通过修改其使用方式改善表现。
- 执行轨迹：一次任务中的观测与动作过程；编码模型据此诊断失败。
- 持久记忆：可供后续决策读取的经验记录；本文用它保留如有效抓取深度的信息。

## 证据

摘要报告跨多个基准和策略，未见场景平均成功率从 9.7% 到 43.3%，约 4.5 倍；未见任务从 12.7% 到 40.2%，约 3.2 倍。摘要还称，通用策略配合演化程序后常能超过微调版本，但没有给出对应分项数字。基准名称、样本量、优化成本及仿真与真机比例未提供，结论应限于所测设置。

## 局限

整体提升不能单独证明持久记忆贡献了多少，需要记忆消融。另需核查留出评测时是否继续改代码或写记忆，以及总共用了多少优化回合；这些决定结果代表一次适配后的能力，还是包含持续适配的能力。

- **判断**：值得细读代码演化流程与评测隔离方式，因为它直接检验了“先改控制程序能解决多少失败”这个实用问题。

## 研究关联

它提示一种具体的故障处理思路：策略失败时，先查是否缺少合适的调用条件、脱困动作或可复用参数，再决定是否需要训练权重。遇到机械臂卡住、接近方向受阻这类可由程序识别和修正的错误时，外围代码值得作为独立优化对象。

### 下一步读哪里

我会先看编码模型实际能读取哪些轨迹信息、修改哪些接口，以及候选代码怎样被接受。再核查策略单独运行、手写程序、自动程序与微调版本的比较是否共享工具和执行预算，并检查持久记忆的独立作用。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/RoboArchitect Automating the Design of Robotic Agents with Persistent Memory.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises the harness around the frozen policy. The harness evolves on a set of episodes for its optimization and is evaluated on held-out scenes and tasks. Without updating any model weights, RoboArchitect raises average success from 9.7% to 43.3% on unseen scenes (4.5x) and from 12.7% to 40.2% on unseen tasks (3.2x), across multiple benchmarks and policies. The gains are largest where the benchmark is far from the policy's training data: wrapping a general-purpose policy, the evolved harness yields a specialist that often outperforms even the finetuned version. Intuitive control strategies are automatically designed, such as lifting a jammed arm clear or reaching in horizontally when an obstacle blocks the way from above. The harness also evolves its own persistent memory, carrying learned experience, such as effective grasp depths, into later decisions. These results suggest that substantial headroom in robotic manipulation lies in the agent harness, and its design can be effectively automated and optimized without weight updates.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.42141v1
- Authors: Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
- Published: 2026-10-30T17:58:48Z
- Age days: 3

</details>
