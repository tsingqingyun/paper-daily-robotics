---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20562v1"
published: "2026-06-18T17:59:51Z"
age_days: 1
score: 32
created: 2026-06-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# MemoryWAM: Efficient World Action Modeling with Persistent Memory

> [!summary] 一句话结论（基于摘要）
> Across long-horizon, memory-dependent manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong vision-language-action (VLA) and WAM baselines while maintaining favorable computational efficiency.

## 关键点

- **问题**：However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of recent observations and therefore struggle in non-Markovian environments, whereas methods that preserve long histories incur time and space costs that grow substantially with sequence l…
- **创新点 / 方法**：To address this challenge, we introduce MemoryWAM, a world action model with efficient persistent memory.
- **证据**：Across long-horizon, memory-dependent manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong vision-language-action (VLA) and WAM baselines while maintaining favorable computational efficiency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/MemoryWAM Efficient World Action Modeling with Persistent Memory.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robust robotic manipulation in the real world requires not only an understanding of the
current observation, but also memory and dynamics modeling. World action models (WAMs)
possess these capabilities by jointly modeling visual foresight and actions conditioned
on both current and historical observations, making them a promising paradigm for
robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with
efficient inference typically condition only on a bounded window of recent observations
and therefore struggle in non-Markovian environments, whereas methods that preserve long
histories incur time and space costs that grow substantially with sequence length. To
address this challenge, we introduce MemoryWAM, a world action model with efficient
persistent memory. MemoryWAM uses a hybrid memory design that combines recent frames,
event-boundary anchor frames, and compact gist tokens that summarize long-range history.
A tailored attention mechanism enables retrieval of both detailed short-term context and
compressed long-term context, supporting memory-dependent decision-making with reduced
inference latency and GPU memory usage. Across long-horizon, memory-dependent
manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong
vision-language-action (VLA) and WAM baselines while maintaining favorable computational
efficiency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20562v1
- Authors: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
- Published: 2026-06-18T17:59:51Z
- Age days: 1

</details>
