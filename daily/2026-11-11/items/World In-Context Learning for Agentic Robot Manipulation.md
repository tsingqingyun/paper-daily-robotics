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
url: "https://arxiv.org/abs/2611.12885v1"
published: "2026-11-09T18:59:45Z"
age_days: 1
score: 39
created: 2026-11-11
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# World In-Context Learning for Agentic Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> WICL 让冻结模型从一次示范出发，在仿真中反复练习，把反馈写进上下文里的 Task Memory，而不更新网络权重。RoboScript 再把这份记忆带到新场景执行，尝试迁移任务步骤和物体角色，而不是记住原场景长相。

## 问题

训练动作策略通常把技能写入权重，适应新分布可能需要重新训练；仅靠另一场景的示范做上下文学习，又缺少当前环境执行后的反馈。本文要补的是这个反馈环节：模型如何在不改权重时，知道示范中的计划执行起来哪里不对。以上均来自摘要。

### 用一个例子理解

理解用例（非论文实验）：输入一次“先开盒再放入积木”的示范；模型在仿真尝试后发现盒盖未充分打开，便把检查开盖状态写进记忆；到新颜色的盒子前，使用同一任务步骤生成操作计划。摘要未说明具体怎样检测开盖。

## 创新点或方法

旧做法是训练权重，或把示范直接交给冻结模型；WICL 增加仿真排练，让模型依据执行反馈修订上下文，再冻结为 Task Memory。新场景部署使用冻结记忆，并声称通过信息隔离确保输入都能在真实机器人取得。这里的“学习”发生在记忆中；推理是带着记忆操作新场景。摘要没有说明记忆格式、反馈内容、反思算法、动作接口及底层控制器来源。

### 方法如何工作

1. 从一次示范建立任务的初始上下文；摘要未说明如何提取步骤与角色。
2. 在仿真世界执行任务并获得反馈，使模型有机会发现示范无法预先覆盖的问题。
3. 把反馈与反思结果写回上下文而非权重，逐步形成 Task Memory；更新规则未说明。
4. 冻结任务记忆并部署到新场景，使用真实机器人可获取的输入执行；跨形态适配细节未说明。

### 必要术语

- 上下文学习：通过输入中的示例与经验改变行为，无须更新参数；本文用其吸收排练反馈。
- Task Memory：排练后保留的任务知识；本文将其冻结后用于新场景。
- 跨形态适配：把经验用于身体结构不同的机器人；本文报告记忆可经适配迁移，但摘要未给具体做法。

## 证据

摘要报告：RoboTwin 2.0 全部 50 项任务，每任务一次示范、无梯度更新，干净与随机化设置平均成功率 83.4%，比最强受训动作策略高超过 20 个百分点。还报告跨视觉分布、反思收益、基础模型扩展和物理双臂迁移，但未给具体对比模型、试验次数、排练成本或真机成功率。这些支持一个值得核查的仿真结果，不能把 83.4% 当成真机表现。

## 局限

摘要没有交代足以判断规模成本的限制。我的待核查问题是：每任务排练多少次、用了什么成功反馈、动作执行依赖哪些已有技能。“一次示范”并不代表只有一次环境交互；信息隔离的具体实现也需要正文证据。真机跨形态迁移仅有定性声明。

- **判断**：值得继续读方法和评测协议；核心主张很明确，但目前摘要不足以判断优势来自记忆学习、工具接口还是不同的交互预算。

## 研究关联

值得借鉴的是把任务经验保存成可迁移的执行知识，而非只依赖参数更新。若能方便地试错、任务又能用步骤和物体角色表达，上下文记忆可能成为适应新任务的另一种成本选择；是否划算还取决于排练和模型调用开销。

### 下一步读哪里

下一步应核查 Task Memory 的实际样例、排练停止条件、失败反馈来源，以及部署是否能修改记忆。比较基线时，需要对齐示范、环境交互、工具与控制接口预算；真机部分应查看迁移需要多少人工改写和独立试验。未提供正文节选，以上都是核查问题。

- **概念**：多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：HTTPError: HTTP Error 404: Not Found

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/World In-Context Learning for Agentic Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at https://github.com/ArcheOne-AI/RoboScript

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.12885v1
- Authors: Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang, Xiang Bai
- Published: 2026-11-09T18:59:45Z
- Age days: 1

</details>
