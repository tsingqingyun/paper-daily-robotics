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
url: "https://arxiv.org/abs/2611.34675v1"
published: "2026-11-25T16:39:10Z"
age_days: 1
score: 32
created: 2026-11-27
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboEvo² 让机器人控制策略暴露失败，再让能写代码的智能体尝试并验证修法。成功修法一部分留给智能体复用，一部分变成训练数据，让策略下次有机会直接完成操作。

## 问题

VLA 执行动作高效，但碰到陌生设置常需要更多人类示范。推理智能体可以借助已有知识和控制接口试出方案，每回合都重新推理和修补又很贵。难点在于把少数回合里找到的修法积累下来，并让底层策略逐轮学会其中可复用的动作。

### 用一个例子理解

理解用例（非论文实验）：输入一个抽屉初始状态和打开指令，策略第一次抓住把手却沿错误方向拉动。编码智能体尝试一段调整拉动方向的程序，验证成功后保存修法。从同一初始状态出发的失败与成功轨迹进入训练，输出是更新后的策略和一项可再次调用的修正技能。

## 创新点或方法

策略到外层系统的更新从失败回合开始。编码智能体在 Code、Code+ICL 和 Code+Policy 三类路线中搜索，把验证过的解法沉淀为技能、选择策略和经验记忆。外层系统到策略的更新用验证过的轨迹做监督训练，再用 CPD 比较同一初始状态下的成功修正和失败轨迹，训练策略偏向前者。更新后的策略既能独立执行，也可以参与混合执行。剩余失败再进入下一轮搜索。摘要未说明成功验证器、路线触发和配对损失的实现。

### 方法如何工作

1. 让当前策略执行任务，留下失败回合，为编码智能体指出应解决的具体操作。
2. 搜索代码及其他组合路线并验证成功，把能复用的修法存成技能和经验。
3. 用验证轨迹监督训练，并配对同一起点的成功修正和失败记录，让策略学习优先选择成功动作。
4. 部署更新后的策略，记录剩余失败，用它们决定下一轮搜索的方向。

### 必要术语

- Harness：管理代码、技能选择和经验记忆的外层执行系统；RoboEvo² 用它搜索并复用修法。
- 上下文学习（ICL）：通过输入中的示例或经验影响当前模型输出；它是编码智能体搜索解法时可搭配的一条路线。
- 反事实偏好蒸馏（CPD）：比较同一起点下的失败和成功修正；它给策略训练提供偏向哪条轨迹的信号。

## 证据

摘要报告，在 LIBERO-PRO 上，独立策略成功率从 11.0% 到 84.1%，混合执行从 30.4% 到 90.5%，迭代期间未加入额外人类示范。RoboTwin C2R 上据称也有类似提升，智能体开销下降，摘要未提供具体幅度。另报告 Unitree G1-D 上混合成功率为 95.0%，但未给出回合数或独立策略分数。摘要还提到自主习得任务和跨本体迁移，未展开对照。主要数字比较的是系统迭代前后。

## 局限

作者明确把反复推理与修补的开销视为瓶颈。我会核查节省的部署开销能否抵掉搜索、验证和重训成本，以及 CPD 相比只学习成功轨迹的独立贡献。Unitree G1-D 的数字对应混合执行，摘要没有给出策略独立接手的程度。

- **判断**：值得读到成功验证、同起点配对和逐轮成本，尤其要看哪些修法最终能从智能体交给独立策略。

## 研究关联

智能体试出的修法可以同时用作临时补救和训练样本。若能复现起始状态并可靠判断成功，把失败与修正配成一对，有机会让训练集中在改对了哪段动作，减少后续反复调用智能体的开销。

### 下一步读哪里

先查如何恢复同一初始状态、谁判定修法成功，以及 CPD 怎样使用轨迹对。再看每轮独立和混合成功率是否分开统计，并核对仿真和真机上的交互预算及开销。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/RoboEvo$ 2$ Recursive Robot Self-Improvement via Harness-Policy Co-Evolution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings; reasoning agents can discover solutions using broad prior knowledge and robot-control APIs, but repeated deliberation and repair are costly. Inspired by human learning through reasoning and practice, we propose RoboEvo$^2$, a framework for recursive harness-policy co-evolution. In Policy-to-Harness (P2H) evolution, policy failures guide a coding agent to search complementary Code, Code+ICL, and Code+Policy routes, consolidating verified solutions into reusable skills, routing strategies, and experience memory. In Harness-to-Policy (H2P) evolution, verified trajectories provide supervised training, while Counterfactual Preference Distillation (CPD) teaches the policy to favor successful corrections over failures from the same starting state. The improved policy provides stronger motor skills for subsequent search, while its remaining failures redirect harness evolution, closing the reciprocal loop. Through recursive co-evolution without additional human demonstrations, RoboEvo$^2$ improves standalone success from 11.0% to 84.1% and hybrid success from 30.4% to 90.5% on LIBERO-PRO, with similar gains and reduced agentic costs on RoboTwin C2R. Further experiments demonstrate autonomous task acquisition, cross-embodiment harness transfer, and 95.0% hybrid success on the Unitree G1-D. Our models and code will be publicly released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34675v1
- Authors: Chenzhi Liu, Jiehong Lin, Wei Huang, Xuzhao Huang, Haoyuan Li, Yang Zhang, Junchao Huang, Chenyeyang Cai, Bo Wang, Kazuhiro Kosuge, Zhongrui Wang, Xiaojuan Qi
- Published: 2026-11-25T16:39:10Z
- Age days: 1

</details>
