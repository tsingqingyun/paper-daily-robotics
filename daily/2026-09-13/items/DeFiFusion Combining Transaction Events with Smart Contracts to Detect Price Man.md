---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11008"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 18
created: 2026-09-13
concepts: ["世界模型"]
---

# DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks

> [!summary] 先说人话（基于摘要）
> DeFiFusion同时查看交易行为和智能合约执行语义，识别价格操纵攻击。关键是判断一段交易如何利用合约逻辑，避免仅凭异常波动或静态漏洞报警。

## 这篇到底在做什么

- **卡在哪里**：仅看交易的方法缺乏执行语义，容易将正常市场波动误报；静态合约分析缺少真实交易行为，又可能报告实际不可利用的漏洞。
- **关键解法**：将交易事件编码为时间与经济特征，用LLM提取合约语义，再通过双模态投影融合Transformer结合两种信息；T5式相对位置编码用于捕捉攻击中的循环、多阶段执行结构。
- **拿什么证明**：摘要报告检出225个价格操纵案例中的222个，精确率为96.10%，并称检测性能持续达到最先进水平；未列出具体基线成绩。

## 值不值得读

- **和你的研究有什么关系**：直接价值在智能合约安全检测。虽然research_links标为世界模型，但摘要没有状态转移预测、动作条件模拟或具身规划证据，与世界模型研究的联系很弱。
- **先别急着信**：需核查数据划分、攻击案例来源，以及合约语义提取是否引入测试相关信息，才能判断检测指标的泛化意义。
- **判断**：安全检测研究者可深入，世界模型与机器人日报中低优先级，不应因“双模态”而高估相关性。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：18
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/DeFiFusion Combining Transaction Events with Smart Contracts to Detect Price Man.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.11008v1 Announce Type: cross Abstract: Decentralized Finance (DeFi) has emerged as a rapidly growing blockchain-based financial service, where market transaction dynamics and underlying smart contract logic are intricately intertwined. This autonomous interplay, while eliminating centralized intermediaries, significantly expands the vulnerability surface of DeFi protocols to Price Manipulation Attacks (PMAs), which have already inflicted catastrophic financial losses. Despite their gravity, existing detection paradigms suffer from fundamental limitations. Transaction-centric methods lack awareness of contract execution semantics, making them prone to false positives under legitimate market volatility, while static contract analyses ignore real transaction behaviors and frequently report vulnerabilities that are infeasible to exploit in practice. We present DeFiFusion, a dual-modal PMA detection framework that closes this gap by jointly modeling transaction events and smart contract semantics within a unified pipeline. Our core insight is that PMA maliciousness emerges only from the interaction between transaction behaviors and the contract logic they exploit; neither signal suffices in isolation. Accordingly, we derive price-manipulation-aware event encoding for extracting fine-grained temporal and economic features tailored to manipulation patterns. We further introduce LLM-based contract semantic extraction to supply the execution-logic context that prior behavioral methods lack. To fuse these modalities, we propose a Dual-Modal Projection-Fusion Transformer with T5-style relative positional encoding, capturing the cyclic multi-stage execution structures that distinguish PMAs from benign market activity. Extensive experiments demonstrate that DeFiFusion consistently achieves state-of-the-art detection performance, effectively recalling 222 of the 225 PMA cases while maintaining a precision of 96.10%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11008
- Authors: Rui Cao, Shaojing Fan, Liming Fang, Yuchan Liu, Yingying Jiao, Zhenguang Liu
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
