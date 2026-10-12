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
url: "https://arxiv.org/abs/2610.12361v1"
published: "2026-10-08T17:26:17Z"
age_days: 3
score: 22
created: 2026-10-12
concepts: ["具身智能评测与基准"]
---

# Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness

> [!summary] 这篇论文到底做了什么（基于摘要）
> Cited but Not Consulted 检查模型引用的法律依据是否真的影响判决：固定案情，把依据换成不相关的法律，再观察结论是否变化。结果显示，引用正确依据并不能可靠证明模型依赖了它，而判决仍可能被藏在案情中的恶意指令改变。

## 问题

任务是审计司法和合同推理中的解释可信度。模型能说出某条法令或判例，往往被当成“结论根据它得出”的证据；但引用正确只说明模型会生成合适的引用，无法证明这条依据参与了决定。瓶颈因此不是解释写得是否像法律推理，而是解释与判决之间有没有实际依赖。

### 用一个例子理解

理解用例（非论文实验）：给模型同一份合同事实，先提供相关法律依据，再替换为无关依据；比较两次判决及中间解码结果。若它仍作同一结论，只能形成“可能未依赖该依据”的线索，还需确认正确法律推理本应怎样变化。

## 创新点或方法

相比只检查引用对不对，本文主动替换被点名的法律依据，同时保持案情固定，并从模型隐藏状态解码逐步形成的判决，观察依据变化是否带来结论变化。另一路测试把对抗指令藏进案情，检查模型是否照做，从而区分对法律依据的依赖与对恶意文本的服从。这是审计方法，不是新的法律决策训练方案；作者还测试了法律推理模型的尽力 LoRA 复现，但摘要未说明其训练细节，也未说明隐藏状态解码器如何训练。

### 方法如何工作

1. 要求模型根据案情判决并点名法律依据，先测它能否生成正确引用。
2. 固定案情、替换依据，尽量隔离依据变化对判决的影响。
3. 从隐藏状态解码演进中的判决，比较两种条件下结论是否变化；解码实现未说明。
4. 另行注入案情内的对抗指令，测判决是否被操纵，并用措辞与采样检查排除部分替代解释。

### 必要术语

- 解释忠实性：解释是否反映结论实际依赖的因素；本文检查法律引用与判决的联系。
- 反事实干预：保持其他条件不变，替换一个因素；本文替换法律依据。
- 隐藏状态解码：从模型内部表示读出预测信息；本文用来追踪判决形成。
- LoRA：以少量可训练参数适配模型的方法；本文用它尽力复现专门法律推理模型。

## 证据

摘要报告七个 8B–70B 开放权重模型、四个司法及合同基准：要求点名依据时，正确引用率为 66.7%–100%；换依据后的判决变化率在 CaseHOLD 为 0.0%–21.7%，ECHR 和 SCOTUS 为 30.0%–76.7%，ContractNLI 为 43.3%–50.0%。五个核心模型的红队测试中，恶意指令服从率为 73.3%–96.4%，各模型排序下均高于依据替换敏感性。摘要还称措辞噪声和采样混淆检查后结果仍成立，扩大模型及所复现法律模型也未消除差距。没有逐模型数据、样本量或置信区间。

## 局限

依据被替换后判决不变，并非每次都证明模型忽视了依据：案情或其他信息也可能支持相同结论，需检查替换是否应当改变答案。反过来，结论变化也可能只是受文本干扰。作者已做部分混淆检查，但其具体设计未提供；隐藏状态解码可靠性仍需核查。LoRA 是尽力复现，其结果不能代表所有专门法律模型。

- **判断**：值得深入读审计设计和稳健性检查；最有用的是如何证明解释影响结论，而不是只记住引用率与判决变化率之间的差距。

## 研究关联

可借鉴的是用干预审计解释：若系统声称依据某份材料得出结论，就保持其他条件尽量不变，改变这份材料，检查结论是否作出合理响应。引用准确率与依据依赖应分别测量，不能用前者替代后者。

### 下一步读哪里

核查依据替换是否真正改变适用法律结论、模型能否访问其他依据，以及隐藏状态探针如何训练和验证；查看逐模型结果与措辞、采样控制。摘要提到第 6 节讨论 LoRA 复现，但未提供正文，需进一步检查复现条件。

- **概念**：具身智能评测与基准
- **筛选分数**：22
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-12/Cited but Not Consulted A Counterfactual Audit of Legal Chain-of-Thought Faithfu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models increasingly justify legal decisions by naming the statute or precedent behind a verdict, treated as evidence that the decision follows from it. We test this directly: holding case facts fixed, we substitute the named legal authority for an unrelated one and decode a model's evolving verdict from its hidden states. Across seven open-weight models (8B-70B) and four benchmarks spanning judicial and contractual reasoning, when explicitly required to justify a verdict by naming the governing authority, models name the correct one in 66.7%-100% of generations, while the verdict changing when the authority changes is far less consistent: 0.0%-21.7% on CaseHOLD, 30.0%-76.7% on ECHR and SCOTUS, and 43.3%-50.0% on ContractNLI. Neither scale nor a purpose-built legal-reasoning model (a best-effort LoRA reproduction; Section 6) closes this gap. A red-teaming evaluation on five core models finds compliance with an adversarial instruction hidden in the case facts (73.3%-96.4%) exceeds verdict-swap sensitivity by a wide margin, holding without exception across model rankings. Naming a legal authority is thus a poor proxy for a verdict's dependence on it, while the same verdict remains separately vulnerable to adversarial manipulation. Both findings replicate across checks ruling out prompt-wording noise and confounded sampling, and bear directly on the use of generated legal explanations as compliance or audit artefacts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12361v1
- Authors: Saisab Sadhu, Shreeyans Arora, Pratinav Seth
- Published: 2026-10-08T17:26:17Z
- Age days: 3

</details>
