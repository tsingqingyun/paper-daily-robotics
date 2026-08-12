---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06830v1"
published: "2026-08-07T05:39:27Z"
age_days: 3
score: 25
created: 2026-08-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems

> [!summary] 一句话结论（基于摘要）
> Results show that unsafe information can turn into unsafe actions across all three architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 trigger…

## 关键点

- **问题**：Prior work has focused mainly on individual robots, while communication risks in multi-robot collaboration remain insufficiently understood.
- **创新点 / 方法**：To mitigate risks from trusted information flow, we introduce the Claim Provenance and Verification (CPV) Gate, which verifies communicated claims before downstream reuse and reduces the violation rate from 70.0\% to 36.6\%.
- **证据**：Results show that unsafe information can turn into unsafe actions across all three architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers 88.3\% of task defined unsafe action slots.
- **局限**：Existing multi-robot studies are further limited to preliminary analysis under the Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether these risks persist across other common communication architectures and how attacker access settings shape their propagation.

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/When Coordination Becomes a Threat Communication Attacks in LLM-Controlled Multi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large Language Models (LLMs) are increasingly used as high-level planners in embodied
multi-robot systems, enabling robots to interpret natural language instructions and
coordinate executable actions. Yet, this growing reliance on LLM planners also raises
security concerns. Prior work has focused mainly on individual robots, while
communication risks in multi-robot collaboration remain insufficiently understood.
Existing multi-robot studies are further limited to preliminary analysis under the
Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether
these risks persist across other common communication architectures and how attacker
access settings shape their propagation. To fill this gap, we formulate two
communication attacks corresponding to distinct attacker access settings: the External
Entry Point Attack and the Privileged In-System Attack. We evaluate both attacks across
DMAS, HMAS-1, and HMAS-2 using three LLMs and five embodied multi-robot tasks. Results
show that unsafe information can turn into unsafe actions across all three
architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement
activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers
88.3\% of task defined unsafe action slots. To mitigate risks from trusted information
flow, we introduce the Claim Provenance and Verification (CPV) Gate, which verifies
communicated claims before downstream reuse and reduces the violation rate from 70.0\%
to 36.6\%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06830v1
- Authors: Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai
- Published: 2026-08-07T05:39:27Z
- Age days: 3

</details>
