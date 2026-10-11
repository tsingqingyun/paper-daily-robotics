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
url: "https://arxiv.org/abs/2610.12417v1"
published: "2026-10-08T17:52:03Z"
age_days: 2
score: 28
created: 2026-10-11
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# WOVEN: Weaving Visual World Modeling into Multimodal LLMs

> [!summary] 这篇论文到底做了什么（基于摘要）
> WOVEN 让多模态模型练习判断画面经过某种变化后会怎样，再检查这项能力能否帮助其他任务。它最值得关注的发现是：选训练数据时，教会哪种推理操作可能比展示哪类场景或动作更关键。

## 问题

任务是理解视觉状态如何随动作和时间变化，涉及空间、物理、具身和时序推理。作者怀疑这些失败有共同根源：模型不善于推断视觉状态转换。已有基准分别测量不同能力，却难以控制场景、动作和推理操作，因此难以判断模型到底缺什么、该用什么数据补。

### 用一个例子理解

理解用例（非论文实验）：输入桌上杯子的位置和“向右推”的动作描述，模型判断杯子的新位置；再换成移动玩具车，检查它是否仍能完成同一种位移推理。

## 创新点或方法

旧做法按不同能力分别评测；WOVEN 把视觉转换样本按场景、动作和推理类型组织，便于控制变量。样本来自经过视频预训练的生成模型所产生的片段。训练时让不同规模的多模态模型学习这些转换任务，再到外部基准检验迁移；推理时的输入格式、是否需要中间预测以及训练损失，摘要未说明。它的巧处是把“画面内容相似”与“需要的推理操作相似”分开检验。

### 方法如何工作

1. 从生成片段取得视觉变化样本，并标记场景、动作和推理类型，使不同因素能够分别比较。
2. 评测多种模型与人类，判断哪些转换任务存在稳定差距，为训练选择提供依据。
3. 用受控子集训练模型，再测外部任务，区分学会原题与获得可迁移能力。
4. 比较不同选样原则，并在留出基准检验规律；具体训练目标和推理流程，摘要只说明到此。

### 必要术语

- 视觉转换推理：判断画面状态怎样变化；是本文要训练和测量的共同能力。
- 监督：告诉模型哪些输出才正确的训练信息；本文按推理操作组织这种信息。
- 留出基准：形成方法选择时未使用的测试任务；用于检查选样规律是否能预测后续效果。

## 证据

摘要报告 36,076 个样本，覆盖 20 类场景、5 类动作、8 类推理；评测 38 个前沿模型，最强模型仍明显落后于人类。约 2,000 条规模的训练子集，合计让 26 个外部基准中的 22 个改善，最高增加 27.3 个百分点；替换任务自身 30%–50% 的训练数据可获得相近准确率。摘要还称选数据规律在留出基准上得到前瞻验证，但未提供逐项成绩、人类分数、具体训练模型和误差范围；最高增幅不能理解为平均收益。

## 局限

生成片段的逼真程度不等于物理正确性，我会核查错误片段如何筛除。跨基准改善支持训练能力可迁移，但不能单凭摘要认定所有空间或物理错误都来自同一个机制，也不能推出机器人真机控制收益。

- **判断**：值得读到数据组织和控制实验：真正可复用的是如何挑训练样本，以及作者怎样排除场景内容相似带来的解释。

## 研究关联

可以借鉴的是按“训练样本要求模型完成什么操作”选数据，而不只按领域标签选数据。当目标任务训练数据不足时，这提供了一个值得测试的补充数据原则；是否适用仍应由目标任务的独立测试决定。

### 下一步读哪里

先核查八类推理操作的定义、生成片段的质量控制和监督格式，再看等量数据对比如何隔离场景、动作与推理类型，以及 22 个改善基准的具体收益分布。

- **概念**：多模态基础模型 世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/WOVEN Weaving Visual World Modeling into Multimodal LLMs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a training source and benchmark for visual transition reasoning that organizes transition supervision by scene, action, and reasoning type, using diverse, realistic rollouts from video-pretrained generative models: 36,076 examples across 20 scene types, 5 action types, and 8 reasoning types. We first evaluate 38 frontier MLLMs (e.g., GPT-5.4 and Qwen3-VL-235B-A22B) and find a substantial and systematic deficit: even the strongest models fall far below humans, and the failures recur across model families and persist with scale. We then train MLLMs at multiple scales on WOVEN and find that they learn a shared capability that transfers broadly: training subsets of only about 2,000 items each collectively improve 22 of 26 external benchmarks by up to 27.3 percentage points, and WOVEN data can replace 30-50% of a task's own training data with comparable accuracy. Controlled comparisons further yield a training recipe for visual world modeling, validated prospectively on held-out benchmarks: select supervision by the reasoning operation it teaches rather than by the actions, scenes, or domains it shows, and prefer larger changes to the visual state for robustness. Our work establishes visual transition reasoning as a reusable foundation for systematic visual world-model training in MLLMs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12417v1
- Authors: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li
- Published: 2026-10-08T17:52:03Z
- Age days: 2

</details>
