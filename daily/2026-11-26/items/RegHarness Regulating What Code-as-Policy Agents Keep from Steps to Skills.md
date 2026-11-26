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
url: "https://arxiv.org/abs/2611.33739v1"
published: "2026-11-25T04:01:05Z"
age_days: 0
score: 32
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills

> [!summary] 这篇论文到底做了什么（基于摘要）
> RegHarness 给写代码控制机器人的 RATs 加了两道关口。单次试验中，每一步要通过双重审核才能留下。试验结束后，失败日志可用来改技能，但改动需要作者启用才会进入后续运行。

## 问题

Code-as-Policy 智能体会生成程序、执行并修改它，但哪些动作算作本轮已经完成、哪些代码改动会影响后续试验，往往缺少明确规则。前者关系到错误动作会不会成为下一步的起点，后者关系到从一次失败得出的修改会不会改变以后所有运行。两者需要在不同时间点做决定。

### 用一个例子理解

理解用例（非论文实验）：输入是把方块推入托盘的指令。每次试推之前先重置场景，重放已经批准的靠近动作。若验证器和审核器都认可这次试推，系统就把它计入已完成步骤。若多轮日志反复记录相同的滑脱，编码智能体可测试推块技能的修订，获作者启用后才供后续任务使用。

## 创新点或方法

试验内，每次评估候选步骤都从重置场景开始，先重放已提交步骤，再检查新步骤。RATs 自己的验证器与贯穿整项任务的 LLM 审核器都同意，固定规则控制器才提交。试验间，编码智能体根据失败日志修改并测试技能、底层操作与规则，修订默认关闭，由作者显式启用。这两层分别发生在在线执行和离线改代码阶段。摘要未说明审核输入及修订测试细节。

### 方法如何工作

1. 重置场景并重放已批准步骤，为候选动作重建评估起点。
2. 验证器和任务级审核器分别检查候选动作，固定规则在两者都通过时才把它写入本轮执行记录。
3. 跨轮收集失败日志，交给编码智能体形成并测试可复用代码的修订。
4. 作者显式启用通过其选择的改动，使后续运行能调用新版本。

### 必要术语

- Code-as-Policy：把机器人怎么做写成程序，在本文中，RATs 会生成和执行这类程序。
- 重置重放：恢复初始场景后重做已提交步骤，在本文中用来评估下一步。
- 2×2 消融：交叉开关两个组件，在本文中用于估计逐步审批和技能修订各自的贡献。

## 证据

摘要中，配对的 LIBERO-PRO 试验使用同一低成本模型承担各运行角色，RegHarness 成功率为 87.8%（158/180），RATs 为 39.4%。MolmoSpaces 成功率为 72.0%，摘要未给出对应基线。2×2 消融以 RATs 的 71 次成功为参照，只改技能达到 135 次，只加运行审批达到 105 次，RATs 自带的逐步重置重放模式成功 46 次。结果支持在该配置下，两层都能独立增加成功次数，单独改技能的增量更大。

## 局限

作者把代码改动的启用权留给自己。我会核查修技能用过的失败日志与评测任务是否重叠，以及重放和双重审核各增加多少成本。摘要给出的是两个仿真基准上的成绩，真机上能否重建足够接近的中间状态还需验证。

- **判断**：值得先读消融与评测协议，再看审核器读到了什么，因为这两处决定了技能改进和运行审批的收益能否在自己的设置里复现。

## 研究关联

设计实验时，可以分别检验机器人调用的技能本身是否可靠，以及执行器能否及时拦下坏决策。这里两种改动都有收益，而单独启用原生重置重放的结果提醒读者，能回到已确认的状态和能正确评估下一步，需要各自测量。

### 下一步读哪里

核查两个审核角色分别能看到哪些信息、固定规则如何处理分歧，再看消融是否共享试验集合和预算。读技能更新部分时，追踪一次修订用过哪些日志、怎样测试、如何进入评测。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/RegHarness Regulating What Code-as-Policy Agents Keep from Steps to Skills.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Code-as-Policy agents generate, execute, and revise robot programs, but often lack explicit mechanisms to govern what persists across executions: which actions are retained within a trial and which code modifications carry over to subsequent runs. This leaves two critical aspects of agent behavior insufficiently controlled: step-level execution and cross-run adaptation. We present RegHarness, a two-level harness that governs both forms of persistence for the RATs agent team, without relying on a vision-language-action (VLA) policy or demonstrations. Within each trial, run-time governance evaluates each proposed step from a reset scene, replaying the committed steps, while a fixed-rule controller commits the step only when both RATs' verifier and a task-long LLM auditor approve it. Between runs, a coding agent uses logged failures to develop and test revisions to skills, primitives, and rules, which remain disabled by default until explicitly enabled by the authors. Using a single low-cost model across all run-time roles, RegHarness achieves an 87.8% success rate (158/180) on paired LIBERO-PRO trials, compared with 39.4% for RATs, and a 72.0% success rate on MolmoSpaces trials. A $2\times2$ ablation study of RegHarness's two levels shows that its skill refinement alone increases RATs' successful trials from 71 to 135, whereas run-time governance alone achieves 105 and RATs' native stepwise reset-and-replay mode achieves only 46. These findings suggest that, for Code-as-Policy agents operating with low-cost models, task success depends not only on how generated programs are executed, but also on the quality of the reusable skills they invoke and how those skills evolve across runs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33739v1
- Authors: Shengming Liu, Yunyi Gao, Xinyi Wang, Jianyong Sun, Shuai Wang, Yi Deng, Li Chenye, Mingcai Zhou, Sim Kuan Goh
- Published: 2026-11-25T04:01:05Z
- Age days: 0

</details>
