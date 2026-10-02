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
url: "https://arxiv.org/abs/2609.38371"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-02
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# TALK-Dem: Benchmarking Embodied Task Planning under Dementia-Associated Communication Patterns

> [!summary] 这篇论文到底做了什么（基于摘要）
> TALK-Dem 检查机器人规划器面对指代不清、叫错物品或话题漂移时，还能否理解任务。配套方法 CARE 检索过去已经解决的相关任务，为当前指令提供解释和规划上下文。

## 问题

任务是把用户语言转成机器人任务计划。常见规划器默认指令清楚、完整且围绕任务，但认知障碍相关沟通可能不满足这些条件；直接按字面规划容易选错对象或误解意图，可能影响实际执行安全。

### 用一个例子理解

理解用例（非论文实验）：用户指着水杯说“把那个碗拿来”；系统检索过去类似称呼混淆的已解决任务，用作解释当前请求的上下文，再生成取物计划。历史记录并不能保证此时“碗”就是杯子，仍需核查场景或澄清。

## 创新点或方法

旧做法主要依赖当前指令和普通提示；CARE 在生成计划前检索相关的已解决任务，让模型参考已有解释经验。它试图补足当前表达缺失或混乱的上下文。摘要描述的是检索辅助规划，没有说明是否另行训练检索器或微调模型，也没交代何时应澄清而非直接执行。

### 方法如何工作

1. 用不同沟通模式和强度呈现任务指令，检验规划器对表达变化的敏感程度。
2. CARE 为当前指令检索相关已解决任务，获得可能有用的解释和规划参照。
3. 把检索经验加入上下文后生成计划，以减少仅凭当前含混文字作判断的错误。
4. 比较普通提示与检索辅助后的任务成功率；计划如何执行和评分，摘要只说明到此。

### 必要术语

- 指代不精确：用“那个”等表达却无法明确定位对象；是基准中的一类沟通模式。
- 物品替代：表达中以其他物品称呼替代目标物品；具体构造规则需查正文。
- CARE：从已解决任务中找相关经验，为当前任务补充解释上下文的方法。
- 开放权重模型：可以获得模型权重的模型；本文选用这类模型研究本地部署所需的沟通鲁棒性。

## 证据

摘要报告 4,800 条指令，包含五类沟通模式、三个强度等级，在六个开放权重 LLM 上测试。相较理想指令，性能最多下降 22.3 个百分点；CARE 相对普通提示的平均任务成功率提高 18.1 个百分点，并总体优于标准提示基线。摘要未给绝对成功率、逐模型结果及任务成功的判定方式，也未说明是否进行了真机执行。

## 局限

输入没有说明指令是否来自真实患者、如何构造，也不能据此推断临床适用性。物理风险是研究动机，摘要没有提供事故或安全指标；成功率提高不等于已证明安全改善。还需核查检索库与测试任务是否有重叠。

- **判断**：值得先读数据构造和评测协议，再读 CARE；只有确认沟通模式真实且检索没有泄漏答案，增益才容易解释。

## 研究关联

可借鉴的是将语言表达变化纳入任务能力评测：同一意图换一种不完整表达，可能比换模型更影响结果。经验检索适合检验重复任务能否帮助消歧，但检索到的历史案例仍需与当前场景一致。

### 下一步读哪里

先检查五类模式和强度如何标注、目标意图如何确定，再看 CARE 的检索依据、经验来源，以及遇到无法消歧的输入是否允许询问用户。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/TALK-Dem Benchmarking Embodied Task Planning under Dementia-Associated Communica.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.38371v1 Announce Type: new Abstract: Existing LLM-driven robot task planners rely on a taken-for-granted assumption of an ideal user whose instructions are clear, complete, and task-focused. However, when interacting with real-world users, especially those experiencing cognitive impairments, such as people living with dementia (PLWD), the planners often make mistakes and even pose physical safety risks. We proposed TALK-Dem (Talking Attributes and Linguistic Knowledge in Dementia), the first benchmark for evaluating LLM-driven robot task planning under dementia-associated verbal communication. TALK-Dem contains 4,800 instructions and covers five typical communication patterns, including Referential Imprecision, Object Substitution, Empty Speech, Topic Drift, and Intrusion, at three intensity levels. Experiments across six open-weight LLMs reveal a substantial robustness gap. Across communication patterns, open-weight models exhibited performance drops of up to 22.3 percentage points compared to ideal instructions. This revealed a critical gap and even danger for real-world applications, especially in assistive robotics, where locally deployable models are necessary due to privacy concerns and connectivity constraints. To mitigate this issue, we proposed the Context-Aware Retrieval from Experience (CARE) method, which retrieves relevant previously resolved tasks to provide task-specific interpretation and planning context. CARE generally outperformed standard prompting baselines across the six open-weight models, improving average task success by 18.1 percentage points over the vanilla prompt. These results highlighted the importance of both evaluating communication robustness and developing effective adaptation strategies for locally deployable assistive robots. The TALK-Dem dataset is publicly available at https://anonymous.4open.science/r/TALK-Dem-A6B3/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38371
- Authors: Guangxin Zhao, Yiran Hu, Yuan Cao, Chenxi Jiang, Jianfei Yang, Yegang Du, Yasuyuki Taki, Yoshifumi Kitamura, Lin Gu, Zhi Zheng
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
