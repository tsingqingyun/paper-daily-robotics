---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02964"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 23
created: 2026-09-06
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization

> [!summary] 先说人话（基于摘要）
> GEO Defender 防御生成式搜索中的恶意内容优化：Shield Reranker 先压低可疑改写文档，TFSG 再用自然语言经验库指导 LLM 在推理时选择来源，且无需微调目标模型。

## 问题

恶意 GEO 会在保持事实一致的同时重写网页，以迎合搜索引擎的引用偏好并操纵答案。事实核查和困惑度过滤难以发现它，而且攻击所强化的特征也常见于优质正常内容，容易误伤。

## 创新点或方法

输入候选文档与查询，第一阶段在冻结基础重排器上学习偏好式防御残差，在保留相关性判断的同时降权 GEO 文档；第二阶段把防御结果蒸馏成自然语言经验库，在生成阶段约束目标 LLM 使用来源。区别于单点过滤，它对应攻击链同时干预检索排序和生成用证。

## 证据

在两个闭源、三个开源 LLM 和七类 GEO 攻击上，平均攻击成功率由 50.32% 降至 6.20%，保留 94.12% 的正常证据使用，并称答案质量得到保持且可泛化至构造实例之外的未见攻击。


## 局限

需查全文确认攻击成功率、正常证据使用和答案质量的具体定义，并核查对未见攻击的划分是否排除了模板或文档泄漏。

- **判断**：做 RAG、搜索型 Agent 或来源安全者值得精读并复现实验；纯机器人控制研究者可略读，因为关联主要在上游信息可信度。

## 研究关联

它对通用 Agent 的价值是提高检索增强决策所依赖证据的鲁棒性；与具身智能评测只有间接关系，除非机器人智能体依赖开放网络检索或外部文档。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/When Optimization Becomes Manipulation Defending Generative Search against Malic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02964v1 Announce Type: cross Abstract: This paper focuses on defending generative search engines against malicious Generative Engine Optimization (GEO), which rewrites web documents to match engines' citation preferences and thereby manipulates generated answers. Recent GEO methods have advanced from hand-crafted rewriting to automated and agentic optimization, substantially increasing the visibility of target documents in generated answers. However, defending against such manipulation poses two major challenges: attack documents remain factually consistent with their originals, rendering fact verification and perplexity filtering ineffective, and the features they amplify equally characterize high-quality benign content. To address these limitations, we propose GEO Defender, a two-stage defense aligned with the attack chain that requires no fine-tuning of the target LLM. GEO Defender consists of Shield Reranker and Training-Free Shield Generation (TFSG). Specifically, Shield Reranker learns a preference-based defensive residual over a frozen base reranker, demoting GEO-rewritten documents while preserving relevance judgments, and TFSG distills defense outcomes into a natural-language experience library that guides the target LLM's source use at inference. Experiments on two state-of-the-art closed-source LLMs and three open-source LLMs across seven GEO attacks demonstrate that GEO Defender reduces the average attack success rate from 50.32% to 6.20%, retains 94.12% of benign-evidence use, preserves answer quality, and generalizes to unseen attacks from construction instances.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02964
- Authors: Haozhang Li, Yangguang Shao, Xinjie Lin, Zhong Guan, Mi Zhou, Junzheng Shi
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
