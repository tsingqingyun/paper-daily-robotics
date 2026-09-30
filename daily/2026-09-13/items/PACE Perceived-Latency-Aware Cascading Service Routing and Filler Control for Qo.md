---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10372"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-09-13
concepts: ["AI 核心知识地图"]
---

# PACE: Perceived-Latency-Aware Cascading Service Routing and Filler Control for QoE-Efficient Retrieval-Augmented Dialogue Serving

> [!summary] 先说人话（基于摘要）
> PACE同时决定对话回答从哪里来、等待时说什么，以降低用户感觉到的响应延迟。它把服务路由、填充话语和缓存更新放在同一个控制问题中。

## 问题

检索增强对话在质量和成本约束下还需控制感知首响时间；已有级联路由、缓存或检索方法未联合处理答案来源与等待窗口内容，也难以同时应对缓存陈旧和填充话语冲突。

## 创新点或方法

以PTFR为体验目标，组合负载自适应级联路由、路径与填充联合控制，以及感知内容波动的缓存准入，并以门控规则约束相对基线的退化风险。系统部署在人形机器人销售服务上。

## 证据

在75,000条CarQA请求上，c16条件下级联P95 PTFR为0.29秒，纯LLM为0.53秒；自适应控制器P95为0.41秒，高负载同质量下优于RAG 2.4倍。填充控制器减少94%调用且零冲突，陈旧回答比例从86%降至0%。


## 局限

需核查PTFR如何计量、填充内容如何计入首响，以及零冲突和零陈旧回答的测试范围；感知延迟改善不等于完整答案更早完成。

- **判断**：做机器人对话服务值得读控制策略和测量定义，纯机器人学习研究者可低优先级处理。

## 研究关联

对AI系统与机器人对话服务工程有直接价值，说明交互体验需要联合优化服务路径和等待行为；对VLA运动控制或世界模型训练价值有限。

- **概念**：AI 核心知识地图
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/PACE Perceived-Latency-Aware Cascading Service Routing and Filler Control for Qo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.10372v2 Announce Type: replace-cross Abstract: We present the PACE, a framework for retrieval-augmented dialogue serving that formalizes Perceived Time-to-First-Response (PTFR) as a QoE objective and minimizes it under quality/cost constraints. Unlike prior work on cascaded routing, semantic caching, or adaptive retrieval, PACE jointly controls which answer source composes the response and what fills the waiting window. Deployed on a humanoid-robot sales service, it combines three mechanisms: a load-adaptive cascading router, a joint path-filler controller, and volatility-aware cache admission. On 75k CarQA requests, the cascade halves pure-LLM PTFR at P95 (0.29 vs 0.53s at c16). The adaptive controller reaches 0.41s P95, outperforming RAG by 2.4 times at high load with equal quality. The filler controller cuts calls by 94% with zero conflict. Volatility-aware admission reduces stale answers from 86% to 0%. A gating rule ensures the controller never worse than the baseline, with exposure bounded by one hold period. This is the first quantification of filler-answer conflict risk in deployed services.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10372
- Authors: Lin Huang, Yujuan Tan, Weisheng Li, Lixiang Zeng, Kun Yang, Yongzong Wang, Suihan Xiao
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
