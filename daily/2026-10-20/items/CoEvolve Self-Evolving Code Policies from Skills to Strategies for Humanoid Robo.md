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
url: "https://arxiv.org/abs/2610.23288"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots

> [!summary] 这篇论文到底做了什么（基于摘要）
> CoEvolve 让机器人团队用可执行代码组织已有动作技能，执行不符合物理要求时，就依据验证结果修改协调方式。它调整的是“谁在什么时候怎样配合”，底层运动技能保持固定。

## 问题

任务是让两台人形机器人共同搬运一个自由支撑的刚性载荷，穿过狭窄走廊。难点在于两台机器人受同一物体约束，一方的位置或接触偏差会影响另一方；任务分解和分工正确，也不保证实际动作能配合。摘要指出，现有多机器人系统重视分解、分配和重新规划，对执行偏离预期后如何修改可运行的协调行为支持有限。

### 用一个例子理解

理解用例（非论文实验）：输入是两台机器人抬板材过拐角的目标与当前观测；系统安排一台先转向、另一台保持支撑，调用已有技能执行；若验证拒绝这次转移，就调整角色或步幅，输出下一版协调代码。

## 创新点或方法

旧做法主要修改任务安排；CoEvolve 把配合方式写成调用固定技能的代码，使修改能落实到动作顺序、临时角色和有界执行参数。多模态基础模型生成协调策略，物理验证逐次检查执行转移；被拒绝的行为触发结构化修改，并从已接受的检查点继续，验证通过的经验则供后续决策使用。这样有望把物理失败变成下一次协调的具体约束。摘要描述的是执行期间的修订循环，未说明另有怎样的离线训练，也未说明检查点如何恢复。

### 方法如何工作

1. 根据任务和观测，把搬运目标转成技能调用、语义目标、临时角色及有界参数，使团队安排可以执行。
2. 执行一次转移并做物理验证，得到接受或拒绝结果，为后续修改提供依据。
3. 遇到拒绝时，从已接受检查点进行结构化协调修订，尝试纠正配合方式。
4. 保留通过验证的经验，指导后续决策；经验的表示和检索细节摘要未说明。

### 必要术语

- 运动原语：可调用的基础动作；本文用它们搭建团队协调代码。
- 物理验证：检查执行转移是否满足要求；本文据此决定接受还是修订。
- 检查点：已被接受的执行进度记录；本文把它作为失败后修改的起点。

## 证据

摘要报告：在两台仿真 Unitree G1 搬运载荷的场景中，三个多模态骨干系列共进行 15 次基础任务运行，完成 8 次，每个骨干均有端到端成功。另在两个走廊布局及同骨干、跨骨干经验初始化后实现了经过验证的放置。摘要未提供对照方法、各条件运行次数或消融结果，因此证据支持这条协调接口具有可行性，尚不足以确定验证、修订和经验保留各自贡献多少。

## 局限

作者明确暴露了运动精度和接触稳定性仍有限。全部所述任务都在仿真中；我会进一步核查检查点恢复是否依赖仿真状态回滚，因为真实搬运中的滑落和失稳未必可以撤销。

- **判断**：值得读到验证规则与失败修订实例：它最有启发的部分，是如何把一次物理执行失败转成下一段可运行的协调代码。

## 研究关联

当单机技能已经可用、失败主要来自协同时序和参数时，可以先尝试修改技能之间的组织方式。这里值得借鉴的是让修改依据明确的执行检查结果发生，从而减少整套动作策略重新训练的需要。

### 下一步读哪里

优先核查：验证接受的具体条件是什么，检查点保存哪些状态，代码允许修改哪些参数，以及有无去掉验证或经验保留的对照实验。还应检查额外布局的运行次数和失败类型。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/CoEvolve Self-Evolving Code Policies from Skills to Strategies for Humanoid Robo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.23288v1 Announce Type: new Abstract: Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize task decomposition, allocation, and replanning, while providing limited support for adapting executable coordination when physical execution deviates from the intended behavior. We present CoEvolve, a framework that represents team coordination as executable code over fixed robot motor skills. CoEvolve introduces Verifier Guided Coordination Evolution, where a multimodal foundation model instantiates coordination strategies through motion primitives, semantic objectives, temporary robot roles, and bounded execution parameters. Physical verification evaluates each executed transition, rejected behaviors trigger structured coordination revision from an accepted checkpoint, and verified experience is retained to guide subsequent decisions. We evaluate CoEvolve with two simulated Unitree G1 humanoids transporting a freely supported rigid payload through constrained corridors. Across 15 base task runs with three multimodal backbone families, CoEvolve completes 8 tasks, with every backbone achieving end to end success. Additional evaluations yield verified placement on two additional corridor layouts and after both same-backbone and cross-backbone experience initialization, while exposing persistent limitations in motion precision and contact stability. These results support executable coordination as a practical interface for adapting long horizon multi robot collaboration under shared physical constraints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.23288
- Authors: Zicheng Liu, Haochen Wu, Jiawei He, Suyun Zhao, Huan Yang, Cheng Chi, Hao Tang
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
