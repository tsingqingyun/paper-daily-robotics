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
url: "https://arxiv.org/abs/2610.02089"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-03
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution

> [!summary] 这篇论文到底做了什么（基于摘要）
> HumanoidToolBench 把“选对工具”和“用工具完成任务”放进同一个人形机器人评测里，并覆盖需要移动执行的情况。它发现，选对工具与完成任务之间仍有明显差距。

## 问题

工具让机器人能完成裸手难以做到的工作，但成功既需要判断工具是否合适，也需要操作工具、必要时移动身体。摘要指出，现有基准没有在人形机器人上联合评估这些能力；分开测会难以判断系统究竟卡在选择还是执行。

### 用一个例子理解

理解用例（非论文实验）：输入“取下高处挂着的物件”和几种候选工具；机器人先选择能触及目标的工具，再抓取、移动到合适位置并操作，最终输出完成或失败结果。分别记录选择与执行，才能区分判断错误和动作失败。

## 创新点或方法

本文主要改变评测设计，而非给出一个新控制策略：用覆盖不同场景、执行层级和工具集合模式的任务，把选择与实际执行放在同一链条上检查。配套 ToolBook 提供仿真和真实 Unitree G1 的示范数据。训练方面，摘要未说明各策略如何使用这些示范；推理评测时检查选工具及完成任务的表现，另对 GR00T N1.7 测试陌生工具和无关指令。

### 方法如何工作

1. 用任务场景、执行层级和工具集合模式组织测试，得到同时涉及选择与操作的任务范围。
2. 收集仿真和真机示范形成 ToolBook，为研究这些任务提供数据；具体训练用法未说明。
3. 运行策略并分别检查工具选择与任务完成，定位两者之间的能力差距。
4. 对 GR00T N1.7 改变工具熟悉度和指令相关性，检查选择迁移及指令依赖；探针具体流程未说明。

### 必要术语

- 工具选择：判断哪个工具适合任务；本文将其与实际完成任务分开检查。
- 移动执行：使用工具时还需改变机器人位置；本文把这种需求纳入评测。
- 示范数据：记录任务执行过程的数据；ToolBook 提供仿真与真机示范。
- 探针测试：针对某个行为改变测试条件；本文用它检查陌生工具和无关指令下的表现。

## 证据

摘要给出 18 个任务、3 类场景、3 个执行层级、2 种工具集合模式，以及 3.1k 条示范；评估了 7 个仿真策略和 3 个真机策略。结果称选择与完成任务之间存在明显差距；GR00T N1.7 在未见工具上选择准确率下降，且收到无关指令后仍继续执行。没有具体成功率、差距大小或策略排名，因此无法量化结论，也不能推广到所有人形策略。

## 局限

摘要未明确列出作者局限。我会核查任务覆盖了哪些工具功能，以及选择和执行是否采用可比较的判定标准。仿真与真机各评估了不同数量的策略，不能默认两边排名一致；GR00T 的探针结果也不足以说明所有模型都会忽略无关指令。

- **判断**：值得读到任务定义、分项评分和探针设计：它的实用性取决于能否把工具使用失败准确归因。

## 研究关联

值得借鉴的是把评测拆到能定位故障的位置。整体失败可能来自选错工具，也可能来自选对后不会用；无关指令测试还检查策略是否依赖当前指令，而不是沿熟悉任务继续动作。这比单一完成率更能指导后续改进。

### 下一步读哪里

先核查三种执行层级、两种工具集合模式的定义及任务评分；再看策略的训练数据与预算是否可比，并检查陌生工具如何划分、无关指令测试如何判断继续执行。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/HumanoidToolBench Benchmarking Humanoid Tool Use from Selection to Mobile Execut.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.02089v1 Announce Type: new Abstract: As robotic hardware and learning methods advance, humanoids need tools to perform tasks beyond their inherent physical limits. Successful tool use requires selecting a suitable tool and coordinating manipulation and, when needed, locomotion to complete the task. Existing benchmarks do not jointly evaluate these capabilities on a humanoid. We introduce HumanoidToolBench, an 18-task benchmark spanning three scenarios, three execution levels, and two tool-set modes, together with ToolBook, a dataset of 3.1k demonstrations collected in simulation and on a real Unitree G1. Evaluation of seven policies in simulation and three on the real robot reveals substantial gaps between selecting a suitable tool and completing the task. Focused GR00T N1.7 probes show reduced selection accuracy on unseen tools and continued task execution under unrelated instructions. Code and data are available at https://snu-pi.github.io/HumanoidToolBench/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02089
- Authors: Kyochul Jang, Seohyeon Park, Ohchul Kwon, Sangjun Park, Junhyeok Choi, Seungyeop Yi, Chaeyun Kim, Sangkyu Lee, Idan Szpektor, Avi Caciularu, Jongmin Park, Youngjae Yu
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
