---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11152"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-09-13
concepts: ["智能体 Agent"]
---

# terms.txt: A Consent and Compensation Protocol for Agentic Web Access

> [!summary] 先说人话（基于摘要）
> terms.txt让网站按路径和访问目的声明机器访问条款，再通过身份、授权和付款协商把条款接到实际请求处理中。它解决的是Agent访问网页时如何明确许可与补偿。

## 问题

摘要认为，AI抓取削弱了网站开放内容换取回流的机制，而robots.txt无法表达身份、目的、条款和价格，也缺乏可靠执行能力；已有替代方案又多绑定专有CDN功能。

## 创新点或方法

用terms.txt声明细粒度条款，在源站结合Web Bot Auth签名、签名访问意图、委托令牌、HTTP 402协商和签名收据完成交换，并区分技术可强制、可审计与需合同处理的部分。

## 证据

无依赖实现运行在单个vCPU上，每请求增加0.20至0.65毫秒。摘要关于抓取生态的背景判断未提供可核查的具体统计数值。


## 局限

需核查访问目的声明和后续使用行为分别能被强制到什么程度；请求处理开销不能证明实际采用率或条款遵守效果。

- **判断**：做网页Agent基础设施时值得读协议细节，具身智能研究者可略读。

## 研究关联

对网页Agent开发者，这是访问权限、委托和付费交互的协议设计参考；对机器人学习、VLA或世界模型没有直接研究贡献。

- **概念**：智能体 Agent
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/terms.txt A Consent and Compensation Protocol for Agentic Web Access.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.11152v1 Announce Type: cross Abstract: The open web ran on an unwritten bargain: sites admitted crawlers, and search engines sent visitors back. Public measurements show that bargain breaking under AI crawlers and agents. Automated clients now make up most requests, training dominates Cloudflare-classified crawling, and the largest AI platforms fetch thousands of pages for each visitor they return. The web's common control, robots.txt, cannot express identity, purpose, terms, or price, can be circumvented, and newer alternatives are largely proprietary CDN features. We specify terms.txt, a robots.txt-style file for per-path, per-purpose machine-access terms, plus an origin-enforced exchange using Web Bot Auth signatures, signed intent, delegation tokens, HTTP 402 negotiation, and signed receipts. We define what the exchange can enforce, audit, and leave to contract. A dependency-free implementation adds 0.20 to 0.65 ms per request on one vCPU.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11152
- Authors: Rajarshi Chowdhury
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
