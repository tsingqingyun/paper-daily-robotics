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
url: "https://arxiv.org/abs/2609.37348v1"
published: "2026-09-29T12:15:48Z"
age_days: 0
score: 34
created: 2026-09-30
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# DROM: A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> DROM 想用少量示范教会机器人一套可组合的动作：先用可调整的运动模板扩展示范，再训练一个按语言生成不同技能轨迹的扩散模型。遇到长任务，语言模型把请求拆成已有技能，机器人逐项执行。

## 问题

任务是从有限示范学习多种操纵技能，并把它们组合成长期操作。瓶颈包括采集多技能数据昂贵、示范覆盖空间有限，以及有些行为对姿态敏感，难用常规规划或手写控制器描述。单一技能生成能力也不足以直接完成高层语言请求。

### 用一个例子理解

理解用例（非论文实验）：输入“把零件拿起、转到指定朝向，再放入支架”；语言模型输出技能序列，DROM 按各技能语言条件生成相应轨迹，机器人依次执行。例子帮助理解分工，不表示论文测试过这些零件或装配动作。

## 创新点或方法

相较已有 Motion Planning Diffusion，DROM 增加了两类能力：先用动态运动基元扩展示范覆盖，再通过交叉注意力引入语言条件，使一个扩散模型生成不同技能的轨迹。训练阶段学习语言与多技能运动的对应关系；推理阶段由大语言模型拆解请求，再条件生成各技能动作。扩散训练目标、环境观测如何输入及技能衔接反馈，摘要未说明。

### 方法如何工作

1. 从少量专家示范提取并扩展运动，形成覆盖更多空间条件的技能数据，降低额外采集需求。
2. 以扩增数据训练语言条件扩散模型，通过交叉注意力让技能描述影响轨迹生成，统一表示多种动作。
3. 把高层请求交给大语言模型分解，得到可调用的技能序列，弥合任务意图与轨迹生成之间的粒度差异。
4. 逐项生成并执行技能轨迹，组成长任务；摘要只说明到此，未交代在线纠错与衔接算法。

### 必要术语

- 动态运动基元（DMP）：可参数化调整的运动表示；本文用它从少量示范扩增轨迹。
- 扩散策略：通过逐步去噪生成动作或轨迹的模型；本文用一个模型表达多种技能。
- 交叉注意力：让一组信息按相关性读取另一组信息；本文借此让语言条件影响运动生成。

## 证据

摘要报告在 Franka Emika Panda、FANUC CRX25ia 两种真机及 MuJoCo 仿真中测试，并称优于 Motion Planning Diffusion 和行为克隆，具有多技能泛化及语言驱动的长任务组合能力。它明确包含真机证据，但未给示范数量、任务清单、成功率、空间外推距离或各平台分项结果，无法量化数据效率及鲁棒性的范围。

## 局限

摘要未列作者明确局限。我会重点核查：DMP 生成的轨迹如何保证接触和碰撞可行性，姿态敏感动作如何表示，某技能失败后是否重规划？在两种机器人上验证不等于同一策略跨机型零样本迁移；空间泛化也不等于新物体或新技能泛化。

- **判断**：少示范学多技能，值得看数据扩增和技能组合这两部分。论文有两种真机验证，但摘要没给示范数量、成功率或失败恢复办法，暂时无法判断长任务能稳定做到什么程度。

## 研究关联

如果动作形态比较稳定，只是位置、方向需要变化，可以先考虑扩展示范覆盖，再训练多技能策略，减少重新采集的次数。最需要补的检查是扩出的轨迹是否仍然可执行，尤其遇到接触或障碍时，轨迹变得平滑并不代表动作可行。

### 下一步读哪里

下一步核查原始与扩增示范数量、DMP 可调范围及有效性筛选；查看语言条件的粒度、姿态表示、未见位置划分，以及真机长任务是否允许人工干预。

- **概念**：智能体 Agent 世界模型 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/DROM A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning robust manipulation policies for diverse, long-horizon tasks from limited demonstrations remains a fundamental challenge in robotics. We present DROM, a language-guided diffusion framework that enables robots to learn, represent, and compose multiple manipulation skills within a single generative policy. DROM leverages Dynamic Movement Primitives (DMPs) to augment a small set of expert demonstrations into expressive multi-skill datasets, substantially reducing data collection while improving spatial generalization beyond the demonstrated workspace. Building upon Motion Planning Diffusion (MPD), we extend the diffusion architecture to support language-conditioned multi-skill trajectory generation through cross-attention, allowing a single model to generate skill-consistent motions for a diverse set of manipulation primitives, including orientation-sensitive behaviors that are difficult to design using conventional motion planning or hard-coded controllers. For long-horizon manipulation, a large language model decomposes high-level operator requests into executable sequences of skills, enabling natural language interaction and autonomous task execution. We validate DROM on a Franka Emika Panda robot, a FANUC CRX25ia robot, and in MuJoCo simulation across a wide range of manipulation tasks. Experimental results demonstrate that DROM outperforms Motion Planning Diffusion and Behavior Cloning baselines, achieves robust multi-skill generalization, and composes learned skills to reliably execute long-horizon manipulation tasks from natural language instructions using only a limited number of human demonstrations. Datasets, simulation environments, and more at https://github.com/automation-robotics-machines/drom.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37348v1
- Authors: Vincenzo Pomponi, Rocco Felici, Paolo Franceschi, Stefano Baraldo, Oliver Avram, Loris Roveda, Luca Maria Gambardella, Anna Valente
- Published: 2026-09-29T12:15:48Z
- Age days: 0

</details>
