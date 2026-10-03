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
url: "https://arxiv.org/abs/2610.00524"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 36
created: 2026-10-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs

> [!summary] 这篇论文到底做了什么（基于摘要）
> CRAFT 要解决的是：场景看起来熟悉，VLA 就照旧做，忽略指令要求的新技能组合。它固定画面、换指令，再借用已示范技能的表示提供监督，让策略学习在同一场景下按不同要求行动。

## 问题

每个单独技能都学过，组合起来却可能失败。本文关注其中一种原因：微调数据里的画面与指令相互绑定，策略把画面当成任务提示。固定画面、换成未示范组合能打破这种关联，但没有对应动作标签；直接搬用其他示范动作也不行，因为同一技能在不同位置和状态下需要不同动作。

### 用一个例子理解

理解用例（非论文实验）：同一画面里有杯子和抽屉，输入指令从“开抽屉后拿杯子”改为“拿杯子后开抽屉”；训练时不复制别处拿杯子的轨迹，而借用拿杯子技能的表示约束当前样本，目标输出是符合新顺序、适应当前物体位置的动作。

## 创新点或方法

旧监督直接要求预测示范动作；CRAFT 为固定观察、改变指令的反事实样本，转移来自已示范所需技能的表示监督。巧处是借用“执行哪种技能”的可复用信息，而不是照搬另一场景里的动作。这个改动用于训练，推理时目标仍是根据当前观察和指令执行组合；技能表示如何提取、对齐哪些状态、是否增加推理模块，摘要未说明。

### 方法如何工作

1. 固定示范观察并改写指令，得到要求未示范组合的样本，使视觉无法唯一决定任务。
2. 找到已示范的所需技能执行，为没有动作标签的样本寻找可用监督来源。
3. 通过可复用技能表示转移监督，避免直接动作标签因场景差异而不适用。
4. 用这些反事实样本训练策略，再测试新旧组合；具体表示结构和损失函数，摘要只说明到此。

### 必要术语

- 组合泛化：把学过的技能按未示范方式组合；这是本文测试的能力。
- 视觉捷径：凭画面猜任务而忽略指令；本文针对这一失败模式训练。
- 反事实配对：保留观察、改变任务要求的样本；本文用它打破画面与任务的固定关联。
- 技能表示：可跨同一技能的不同执行复用的内部表达；本文借它传递监督，具体形式未说明。

## 证据

摘要报告在 3 个 VLA 模型、2 个仿真基准上提高了未示范组合的成功率，同时保持已示范组合的高成功率，并在真实机器人上改善组合泛化。没有提供具体成功率、基线名称、任务数量或真机实验规模，因此支持的是所测设置中的改善，不能量化收益或认定视觉捷径是全部失败的原因。

## 局限

摘要没有明确列出作者局限。我会核查技能表示是否混入场景信息，以及收益能否用对齐消融来归因。视觉捷径是作者关注的一种失败模式；真实机器人改善不意味着任意顺序、任意长度的技能组合都能成功。

- **判断**：值得细读技能表示和监督转移机制：这决定了 CRAFT 是否真正填补反事实样本缺少动作标签的空白。

## 研究关联

值得借鉴的是监督层级的选择：当新任务没有动作标签，但组成技能已有示范时，可以尝试迁移技能信息，避免复制对当前场景不适用的动作。同一画面配不同指令，也能用于检查模型是否真的使用语言。

### 下一步读哪里

重点核查如何确定反事实样本当前需要的技能、技能表示来自哪里、采用什么对齐目标；再看未示范组合的划分、视觉捷径的诊断对照，以及已示范任务是否出现性能损失。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Same Scene, Different Task Skill Alignment for Compositional Generalization in V.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.00524v1 Announce Type: new Abstract: Vision-language-action (VLA) models often struggle to generalize to skill combinations absent from their fine-tuning demonstrations, even when every constituent skill has been demonstrated. We focus on a vision shortcut as one failure mode: during fine-tuning, visual observations can serve as a proxy for the instruction, so a policy may execute a demonstrated combination associated with similar observations rather than the instructed combination. This motivates training with counterfactual pairs formed by holding a demonstration observation fixed while changing the instruction to specify an undemonstrated combination. These pairs, however, lack corresponding demonstrated action targets. Crucially, the currently required skill has already been demonstrated, but actions from those executions cannot serve as direct targets because the same skill can require different actions across observations. We propose CRAFT, which transfers supervision from demonstrated executions of the required skill to counterfactual pairs using skill representations that can be reused across executions of the same skill. Across three VLA models and two simulation benchmarks, CRAFT improves success on undemonstrated combinations while maintaining high success on demonstrated ones; it also improves compositional generalization on a real robot. Project website: https://taegeunyang.github.io/craft/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.00524
- Authors: Taegeun Yang, Youngju Na, Yoonki Cho, Sung-Eui Yoon
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
