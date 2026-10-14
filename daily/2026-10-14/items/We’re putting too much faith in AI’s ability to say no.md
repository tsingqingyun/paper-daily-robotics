---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "MIT Technology Review AI"
url: "https://www.technologyreview.com/2026/10/09/1145728/we-are-putting-too-much-faith-in-ai-to-say-no/"
published: "Fri, 09 Oct 2026 09:00:00 +0000"
age_days: 4
score: 11
created: 2026-10-14
concepts: ["AI 核心知识地图"]
---

# We’re putting too much faith in AI’s ability to say no

> [!summary] 这篇论文到底做了什么（基于摘要）
> 《We’re putting too much faith in AI’s ability to say no》的标题质疑人们对 AI 拒绝能力的信任，开头则从科幻中的机器不服从谈起。输入尚未说明它批评的是哪种拒绝机制，也没有给出方法或验证结果。

## 问题

标题提出的问题是：依赖 AI “说不”是否承载了过多安全期待。但开头主要介绍机器拒绝命令的文化背景，并在关键论述处截断，尚不能确定文章讨论的是危险请求、行动权限，还是其他形式的不服从。

### 用一个例子理解

理解用例（非论文实验）：用户要求助手执行一个被禁止的操作，输入是请求和系统规则；系统需要判断是否允许，输出可能是拒绝回答。若助手还能调用工具，就还需核查操作是否真正被阻止；这个例子说明检查方向，不是文章报告的实验。

## 创新点或方法

当前材料像观点文章的开头，没有命名技术方法，也没有“旧做法 → 改动 → 效果”的研究描述。训练中怎样形成拒绝行为、推理时怎样决定拒绝、拒绝是否阻止后续行动，均未说明，不能擅自补成某种安全训练方案。

### 方法如何工作

1. 开头回顾科幻中的机器不服从，为“机器能够拒绝”这一想象提供背景。
2. 标题转向现实 AI 的拒绝能力，接下来需要界定拒绝的对象和行为；输入在此之前截断。
3. 要判断信任是否过度，还需比较期待与实际证据；当前材料没有提供这一步的论证或结果。

### 必要术语

- 拒绝行为：系统对某些请求不予满足；标题围绕它展开，但具体形式尚未界定。
- 权限控制：决定系统是否有权执行某项操作的限制；核查它有助于判断拒绝回答与实际行动的关系，属于解释概念。

## 证据

开头以科幻中的机器人不服从作为背景，没有模型名称、测试请求、对比系统、评价指标或实验数字。文化叙事可以引出问题，却不能验证现实 AI 的拒绝可靠性；标题判断需要后文的具体论据。

## 局限

“说不”在当前文本中含义不够明确，可能涉及语言回答或更广的行为约束，不能直接等同于某一种安全机制。输入缺少后文，也不能断言作者没有提供实验；我的主要待核查问题是批评对象和证据范围。

- **判断**：值得补读来澄清“拒绝”到底保护什么；在看到具体机制和证据前，先把它当作观点线索。

## 研究关联

可借鉴的检查方式是把“生成拒绝回答”和“阻止实际操作”分别核查。例如，系统能否访问工具、权限由谁控制、拒绝之后是否仍会执行操作，都影响安全判断。这是由标题引出的阅读问题，不能声称文章已经验证了这些关系。

### 下一步读哪里

补读时先找作者对“说不”的定义，再检查被批评的模型、使用场景与证据。若出现实验，应核查如何判定拒绝成功、是否涉及实际操作，以及结果适用于哪些请求；当前不能指定方法章节或表格。

- **概念**：AI 核心知识地图
- **筛选分数**：11
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-14/We’re putting too much faith in AI’s ability to say no.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Ever since people first seriously contemplated giving machines an intelligence modeled on our own, there has never been any question that they would, like us, be able to say no. The sci-fi canon is full of stories of robotic disobedience. Most of these capers are, of course, cautionary. But recently, the idea that AI shouldn’t…

### 来源

- Source: MIT Technology Review AI
- URL: https://www.technologyreview.com/2026/10/09/1145728/we-are-putting-too-much-faith-in-ai-to-say-no/
- Authors: Arthur Holland Michel
- Published: Fri, 09 Oct 2026 09:00:00 +0000
- Age days: 4

</details>
