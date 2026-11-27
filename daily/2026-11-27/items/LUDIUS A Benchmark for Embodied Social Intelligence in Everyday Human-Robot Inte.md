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
url: "https://arxiv.org/abs/2611.34328v1"
published: "2026-11-25T13:09:34Z"
age_days: 1
score: 27
created: 2026-11-27
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions

> [!summary] 这篇论文到底做了什么（基于摘要）
> LUDIUS 把家庭里的社会判断变成模拟机器人要说什么、做什么的测试。它让模型根据画面、住户反应和交互历史行动，从而检查模型能否记住谁知道什么，并兼顾不同人的要求和家规。

## 问题

家庭机器人光认出眼前发生了什么还不够。同一句请求该怎么处理，可能取决于某位住户先前听到了什么、其他人有什么安排，以及家里允许怎么做。评测要把这些差别变成可以从机器人言行中判断的结果。

### 用一个例子理解

理解用例（非论文实验）。住户请机器人把音乐调响，另一位住户先前说过正在开会。输入是当前请求、机器人视角和检索到的早前约定。模型结合两人的处境，输出一句解释，再建议戴耳机或询问是否愿意稍后调响。

## 创新点或方法

作者把社会认知相关技能编成连续的模拟家庭事件，用统一评测程序给模型提供机器人视角、住户反应及检索到的交互历史，再把模型的工具调用转成机器人说的话与执行的动作。作者用生成的社交数据微调了一个较小模型，也评估了前沿模型。摘要未交代逐项评分规则与历史检索细节。

### 方法如何工作

1. 把社会技能写成具体家庭情境，明确事件中有哪些人、约束和待判断的问题。
2. 模拟一连串交互，留下后续决策可能需要的事件历史。
3. 将当前视角、住户反应和相关历史交给模型，让它选择要说的话或要做的事。
4. 将工具调用变成可观察言行，再按情境要求检查哪些判断容易出错。

### 必要术语

- 视角推断：根据各人接触过的信息判断他们知道什么；用于检验机器人能否照顾住户之间的知识差异。
- 交互历史检索：从过往事件中找当前决策可能用得到的记录；负责把先前的约定和反应交给模型。
- 工具调用：模型用结构化指令请求说话或行动；评测程序将其转换为模拟机器人的行为。

## 证据

据摘要，LUDIUS 有 6 个版本，每个覆盖一周模拟事件。其中 3 个分别在不同家庭覆盖全部 15 项技能，另 3 个分别侧重多人、安全和情境规范。在统一评测程序下，模型通常在推断住户先前看到或听到什么、调和冲突利益，以及同时遵守安全要求与家规时表现更差。摘要未提供模型名单、分数或分技能差值，也未说明小模型微调前后的变化。已知结果刻画的是模拟家庭中的难点。

## 局限

模拟环境中的低分可能与社会推理有关，也可能是相关往事没有被检索出来，或模型选对了意图却发出了不合适的工具调用。要区分这些原因，需要核查论文是否有分环节对照。真机家庭交互还涉及这里未验证的感知和执行条件。

- **判断**：值得读到场景构造和判分细则，看测试怎样把住户的知识、利益和家规转成可区分的机器人行为。

## 研究关联

设计交互评测时，可以把抽象能力落到具体判断上。比如让两段事件的当前画面一样，只改变某人此前是否听见通知，再看机器人会不会相应改变说法。这类设计能检查历史信息有没有真正进入行动决策。

### 下一步读哪里

找一项涉及「谁听到了什么」的任务，核查历史怎样写入事件、怎样交给模型，以及评分如何接纳多种合理应答。然后看多人或安全任务是否能区分判断错误、记忆错误与工具执行错误。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/LUDIUS A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Inte.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Social intelligence in a robot requires interpreting a situation from the perspectives of the people involved and using that understanding to decide when and how to act. We introduce LUDIUS, a benchmark for evaluating how vision-language models exercise this judgment through a robot's verbal responses and actions, organized around 15 social intelligence skills drawn from social psychology, sociology, and cognitive science. LUDIUS comprises six editions, each a collection of episodes spanning one simulated week. Three editions each cover all 15 skills in a different household. The other three focus on interactions involving multiple people, safety, and context-specific norms, respectively. We evaluate frontier models and a smaller model finetuned on social-interaction data we generated, using a common evaluation harness. The harness supplies each model with the robot's camera views and residents' reactions, retrieves relevant interaction history, and converts the model's tool calls into robot verbal responses and actions. Models tend to perform worse when they must reason about what a resident saw or heard earlier, reconcile competing interests, or fulfill a request within safety constraints and household rules. Beyond the home setting, LUDIUS's design pipeline offers a way to construct social intelligence benchmarks by translating social intelligence skills into context-specific judgments and observable robot behavior.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34328v1
- Authors: Chaewon Kim, Sangheon Lee, Seyeon Choi, Kangwook Lee, Yea Seul Kim
- Published: 2026-11-25T13:09:34Z
- Age days: 1

</details>
