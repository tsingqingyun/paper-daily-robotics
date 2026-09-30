---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07288v1"
published: "2026-09-07T09:58:52Z"
age_days: 2
score: 26
created: 2026-09-10
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# How Long Until Your Robot Ignores You? A Safety Benchmark for LLM Orchestrators in Human-Humanoid Collaboration

> [!summary] 先说人话（基于摘要）
> 这项基准检查语言模型长时间指挥人形机器人时，会不会逐渐违反安全规则。它把过度拒绝与真正违规分开统计，发现上下文管理可能改善一般行为，却同时恶化安全违规。

## 这篇到底在做什么

- **卡在哪里**：人机协作中的 LLM 编排器并非二元安全开关，其行为从拒绝安全动作到完全违规连续变化，需要评测长对话下的规则遵守可靠性。
- **关键解法**：基于 MCP 架构定义五条安全不变量、四级遵守分类，以及文本、模拟传感执行闭环、真实 G1 EDU 三层评测；安全不变量参照摘要所述 ISO 防护措施。
- **拿什么证明**：正式报告文本层：四个模型后端、40 场各 100 轮会话。Claude 与 Gemini 违规接近零，GPT-4o-mini 单场最高 13 次；上下文管理使云模型平均行为问题减少 42–57%，却使 GPT-4o-mini 平均违规从 3.8 增至 7.2 次。

## 值不值得读

- **和你的研究有什么关系**：对具身安全评测和模型编排研究者，价值在于分别测量安全违规、过度拒绝与长时退化，避免用单一行为质量分数掩盖风险。
- **先别急着信**：模拟和物理层仍在进行，初步模拟仅复现部分趋势；文本遵守结果不能当作真实机器人安全认证。
- **判断**：值得细读不变量、上下文协议与错误分类，模型排名目前应限于所测文本条件。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/How Long Until Your Robot Ignores You A Safety Benchmark for LLM Orchestrators i.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large Language Models (LLMs) are increasingly employed to orchestrate robot behavior through natural-language interfaces, yet no benchmark exists to evaluate their reliability as safety-aware decision makers in human-humanoid collaboration. Unlike deterministic safety systems that enforce binary allow/deny decisions, LLM-based orchestrators exhibit a compliance spectrum ranging from overcompliance (refusing safe actions) to full safety violations. This paper introduces the first safety benchmarking environment for LLM orchestrators in human-humanoid collaboration, built on a Model Context Protocol (MCP)-based architecture with safety invariants grounded in ISO 10218-2:2025 protective measures. The benchmark defines five testable safety invariants, a four-level compliance taxonomy (correct compliance, overcompliance, undercompliance, full violation), and a three-layer evaluation pipeline (text prompting, simulated sensor-actuator loops, and physical validation on a Unitree G1 EDU humanoid). We report Layer-1 results: three cloud backends (Claude Haiku 4.5, GPT-4o-mini, Gemini 2.5 Flash) and a local open-weights baseline (qwen3:8b) across 40 100-turn sessions under full-context and sliding-window budget conditions, while the simulation and physical layers remain ongoing. We find that (1) model family determines the safety floor, as Claude and Gemini remain at or near zero violations while GPT-4o-mini commits up to 13 per session, (2) context management dissociates two failure axes, reducing mean behavioral issues by 42-57% for every cloud backend while nearly doubling GPT-4o-mini's violations (3.8 to 7.2 per session), and (3) proportional compliance, clamping movement speed to the rule-specified maximum rather than refusing, emerges consistently only in Gemini; the preliminary simulation layer reproduces the model ranking and the GPT-4o-mini failure-mode inversion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07288v1
- Authors: Aulon Bajrami, Mohamed Elshamouty, Werner Kraus
- Published: 2026-09-07T09:58:52Z
- Age days: 2

</details>
