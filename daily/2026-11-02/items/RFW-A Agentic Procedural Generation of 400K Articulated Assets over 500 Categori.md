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
url: "https://arxiv.org/abs/2610.40333v1"
published: "2026-10-29T15:58:15Z"
age_days: 3
score: 25
created: 2026-11-02
concepts: ["智能体 Agent", "世界模型"]
---

# RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories

> [!summary] 这篇论文到底做了什么（基于摘要）
> RFW-A 让智能体先写好一类可动对象的生成程序，再反复运行程序批量造资产。它把昂贵的推理和修正集中在可复用规则上，避免每生成一个对象都重新调用模型。

## 问题

机器人仿真需要能正确运动的门、抽屉等资产，人工建模和标注难以扩展。逐资产智能体合成虽然自动化，却对每个新对象重复推理与修正，成本随数量增长。

### 用一个例子理解

理解用例（非论文实验）：输入抽屉柜类别及宽度、抽屉数量等配置，生成器组合柜体、抽屉和运动连接，输出可在仿真中开合的资产；更换配置后再次执行程序，得到另一件变体。

## 创新点或方法

本文从已有可动对象程序出发，将组件及依赖整理成类别生成器；智能体在多种参数配置和运动状态下测试、修正生成器。验证后靠程序执行生成变体，无需额外模型调用。资产生成本身不是策略训练；下游再用资产训练关节估计或操作策略。具体程序表示、检查器和下游训练细节未说明。

### 方法如何工作

1. 从已有程序抽取组件与依赖，保留同类资产共享的构造逻辑。
2. 组织类别生成器，让配置参数决定具体结构与外观变化。
3. 智能体跨配置和运动状态测试并修正，减少批量复制错误的风险。
4. 执行验证后的程序批量生成资产，再用于感知或策略训练；具体有效性检查摘要只说明到此。

### 必要术语

- 可动资产：部件之间能按关节关系运动的数字对象；是本文生成的对象。
- 程序合成：让模型生成构造程序；本文用于编写可复用生成器。
- 摊销成本：把一次编写费用分配到多个产物；解释规模增大后的单件 API 成本。

## 证据

摘要报告超过 400K 资产、超过 500 类；生成器编写平均估算 API 成本 10.62 美元，按 200 个资产摊销约每个 0.05 美元，逐资产合成抽样基线为 1.24 美元。还报告结构与运动有效、跨模拟器执行稳定、关节估计改善及仿真策略零样本迁移真机，但未给对应指标、任务数和成功率。

## 局限

每资产成本取决于生成数量，API 费用也不能代表验证、运行和人工的总成本。我会核查参数变化是否带来足够结构多样性；摘要中的真机迁移还使用了检索与程序编辑，不能把效果全部归因于资产数量。

- **判断**：值得细读生成器表示和验证流程，判断它能否复用到目标类别；规模与成本数字本身不足以证明资产覆盖了真实变化。

## 研究关联

可借鉴的核心是把智能体产物从一次性实例变成可执行规则。当同类对象共享构造逻辑、又需要大量变体时，先验证生成器可能比反复生成单件更划算。

### 下一步读哪里

核查组件依赖怎样表达、采样检查如何覆盖极端配置、跨模拟器采用哪些通过标准，以及下游实验是否控制资产数量和多样性。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：25
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/RFW-A Agentic Procedural Generation of 400K Articulated Assets over 500 Categori.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

High-quality articulated assets are essential for embodied perception, simulation, and manipulation, yet constructing them at scale remains difficult. Manual annotation and procedural modeling require substantial human effort. Recent agentic systems automate asset construction through program synthesis, but repeat costly reasoning and refinement for every new asset. Our key observation is that assets within a category can share construction logic despite variations in structure and appearance. Agentic synthesis and procedural generation are therefore complementary: agents can construct reusable programs, while procedural execution reuses the resulting logic across many samples. We therefore present RFW-A, which combines the two in a new articulated-asset generation paradigm. Starting from existing articulated programs, RFW-A organizes reusable components and their dependencies into category-level generators. Agents test and refine these generators across sampled configurations and motion states. Once constructed and validated, the generators produce diverse assets through procedural execution with no further model calls or token charges. The estimated API cost of generator authoring averages $10.62, amortizing to $0.05 per asset over 200 assets, versus $1.24 for the sampled per-asset agentic synthesis baseline. Using RFW-A, we built RFW-A-400K, containing over 400K sim-ready articulated assets across more than 500 categories. Experiments show high structural and kinematic validity and stable execution across physics simulators. Beyond asset validity, training with RFW-A-400K improves part-level articulation estimation on seen and unseen categories, while policies trained in simulation with retrieved and program-edited assets transfer zero-shot to real articulated objects.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40333v1
- Authors: Yuanbo Lyu, Changjian Pan, Saining Zhang, Yi Yang, Peishuo Li, Zhiheng Li, Jialu Liu, Junhao Chen, Jiawei Weng, Yupeng Gao, Weiqing Xiao, Wenyi Li, Jiarui Guo, Rui Zhang, Jingrun Du, Weiyi Lin, Zenan Meng, Hu Wei, Lin Qu, Zongzheng Zhang, Hao Zhao, Chaojian Li
- Published: 2026-10-29T15:58:15Z
- Age days: 3

</details>
