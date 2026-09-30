---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07611v1"
published: "2026-09-07T15:19:13Z"
age_days: 2
score: 24
created: 2026-09-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era

> [!summary] 先说人话（基于摘要）
> AgentIdeaBench 让模型主动查资料后提出科学假设，再与固定材料条件比较。结果显示主动探索主要改善可行性和具体性，并没有提高评审测得的原创性。

## 这篇到底在做什么

- **卡在哪里**：静态精选论文输入偏离 AI 科学家的检索—推理工作流，且随着模型进步，评测区分力下降，难以衡量主动探索的价值。
- **关键解法**：设置匹配的静态观察与主动探索条件，用检索既有文献的多维评审检查假设；另以 Scientific World Modeling 在生成时通过结构化思想实验修订草稿。
- **拿什么证明**：评测 33 个 LLM，覆盖五个学科、40 个细分领域。主动条件下性能扩展速度约为静态的两倍，强模型获益更多；可行性、清晰性和具体性改善，测得原创性不变。思想实验循环主要帮助中等能力模型。

## 值不值得读

- **和你的研究有什么关系**：对科研智能体评测有直接价值，可区分检索带来的事实支撑与原创贡献；其 Scientific World Modeling 是假设推演，与机器人动力学世界模型的关联较弱。
- **先别急着信**：需核查扩展速度的横轴和拟合方式，以及文献检索覆盖与评审者对原创性的识别能力。
- **判断**：做科研智能体值得细读配对协议和评分机制，具身或物理世界模型研究者可低优先级浏览。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/AgentIdeaBench Benchmarking Scientific Ideation in the Agent Era.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scientific ideation is the capacity to formulate novel and testable hypotheses from scientific evidence, and autonomous AI scientists depend on it. Existing evaluations largely assess it by asking models to generate ideas from a static, curated set of reference papers. That passive setup departs from the retrieval-and-reasoning workflow of modern AI scientists, and it becomes less discriminative as models improve. We introduce AgentIdeaBench, a multidisciplinary benchmark that evaluates scientific ideation under two matched settings, static observation and active exploration. We report matched Static-Active evaluations for 33 LLMs across 40 densely scored subfields spanning five disciplines, using a multidimensional, literature-verified scoring framework whose critics assess originality against retrieved prior art. Active exploration reveals considerably more capability headroom, and that headroom is unevenly distributed across models. Performance scales about twice as fast as under static observation, and the exploration gain is capability-gated, favoring the strongest models over the weakest. The gain reflects better grounding, improving feasibility, clarity, and specificity while leaving measured originality unchanged under our critics. We further explore Scientific World Modeling, a generation-time loop that refines a draft hypothesis through structured thought experiments. It benefits mid-capability models, and its impact diminishes among frontier models that appear to have internalized such reasoning patterns already. AgentIdeaBench gives future work on scientific ideation a measurement basis suited to the agent era.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07611v1
- Authors: Yunxiang Mo, Tianshi Zheng, Yisen Gao, Rui Wang, Newt Nguyen Kim Hue Nam, Kelvin Kiu Wai Tam, Jiaxin Bai, Yangqiu Song, Ginny Wong, Simon See
- Published: 2026-09-07T15:19:13Z
- Age days: 2

</details>
