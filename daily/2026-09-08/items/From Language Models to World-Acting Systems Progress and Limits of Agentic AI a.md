---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04894"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-09-08
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# From Language Models to World-Acting Systems: Progress and Limits of Agentic AI across Digital, Social, Virtual, and Physical Environments

> [!summary] 先说人话（基于摘要）
> 这篇综述讨论语言模型接入工具和机器人后，究竟有多少可靠自主行动证据。它用授权范围、持续状态和环境耦合拆解系统，并提出有证据支持的委托原则。

## 问题

关于 Agent 进展的叙述常混淆模型能力、系统集成、持续运行和安全授权，接口能力扩张容易被当成可靠自治的证明。

## 创新点或方法

综合截至 2026 年 8 月 31 日的研究和官方技术规范，区分模型、外围执行系统与环境，从授权、时间持续性和环境耦合组织证据，并提出 justified delegation 分析准则。

## 证据

综述判断：行动接口扩张的证据比可靠完成、恢复、授权和独立核验更充分；机器人及自动实验室体现有限条件下的可行性。摘要未给出可核查的实验数字。


## 局限

作者明确将 justified delegation 定位为分析与规范性启发式，并非已验证规律或认证评分；需核查文献选择是否支撑总体判断。

- **判断**：值得读分析框架与证据边界，用于设计评测和审视自治主张，不宜当作新算法论文阅读。

## 研究关联

适合 Agent、世界模型和具身评测研究者校准论文主张，明确系统可靠性需要哪些超出模型分数的证据。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/From Language Models to World-Acting Systems Progress and Limits of Agentic AI a.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04894v1 Announce Type: new Abstract: Large language models become consequential agents when surrounding systems let outputs change external state. Models now call tools, operate interfaces, delegate work, retain state, inhabit generated worlds, and control robots or laboratory equipment. Such advances are often narrated as one march toward autonomy, conflating model competence, system integration, persistence, and safe authority. This critical review synthesizes primary research and official technical specifications available by 31 August 2026. We organize the evidence along delegated authority, temporal persistence, and environmental coupling, while separating model, harness, and environment. Within the evidence examined, action-interface expansion is documented more convincingly than robust completion, recovery, authorization, or independent verification. Model Context Protocol and Agent2Agent improve interoperability but do not establish trustworthy delegation; multi-agent organization adds specialization alongside cost and correlated failure. Persistent simulations and world models support training and planning but do not themselves demonstrate agency; robotics and self-driving laboratories establish bounded feasibility rather than unattended open-world reliability. We propose justified delegation as an analytical and normative heuristic, not an observed law or certified score: expand action scope only where evidence supports provenance, bounded authority, failure detection, safe recovery, and calibrated human control. This framing yields a research agenda for coupled model-harness evaluation, capability-based permissions, durable state, cross-agent accountability, and staged physical validation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04894
- Authors: Linsen Zhu, Mengqing Cai
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
