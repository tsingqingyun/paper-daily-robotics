---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28266v1"
published: "2026-08-28T12:29:23Z"
age_days: 2
score: 27
created: 2026-08-31
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# CoCoBench: A Cooperative Coordination Benchmark for Embodied Multi-Agent Task Planning

> [!summary] 先说人话（基于摘要）
> CoCoBench 不只问多智能体任务是否完成，而是分别测任务分配、顺序约束、互斥和交接四类协调能力，从而揭示总成功率掩盖的具体故障。

## 问题

现有具身基准多聚焦单智能体，或只用整体成功率概括多人行为，无法区分重复劳动、顺序违规、资源争抢和交接不同步等协调失败。

## 创新点或方法

基准包含可执行家务任务，并将实例按四种协调构件组织；除任务成功率外提供构件级得分。评测系统性改变协调模式、观测输入和智能体数量，以诊断能力结构而非只作总排名。

## 证据

CoCoBench 含 897 个经 oracle 验证的实例；评测了 11 个主流 MLLM。结果表明协调能力高度依赖具体构件，整体表现强不代表四类能力均衡；摘要未给各模型具体分数。


## 局限

需核查 oracle 验证、构件划分和评分是否覆盖真实协调的复合情况，以及结果对不同执行器或通信机制是否稳健。

- **判断**：值得所有做具身多智能体评测的人精读基准定义；其价值主要在诊断设计，不在摘要未披露的排行榜。

## 研究关联

对多智能体和具身评测研究者，它提供可定位训练短板的诊断维度，可指导针对交接、互斥或排序的模型与数据设计，而不是继续追逐单一成功率。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/CoCoBench A Cooperative Coordination Benchmark for Embodied Multi-Agent Task Pla.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Agent systems powered by multimodal large language models (MLLMs) have advanced rapidly in recent years, yet existing embodied-agent benchmarks still lack fine-grained diagnostics for multi-agent coordination. Most benchmarks either focus on single-agent task completion or summarize multi-agent behavior with overall task success rates, which can obscure coordination failures such as duplicated work, violations of ordering constraints, resource contention, and desynchronized handoffs. In this paper, we introduce CoCoBench, a construct-level benchmark for evaluating multi-agent embodied coordination in executable household tasks. CoCoBench contains 897 oracle-validated instances organized around four recurring coordination constructs: task allocation, sequential ordering, mutual exclusion, and handoff coordination. In addition to task success rate, CoCoBench provides construct-level scores that measure whether agents coordinate effectively. We evaluate 11 leading MLLMs across different coordination modes, observation inputs, and numbers of agents. The results show that coordination ability is highly construct-specific: strong overall performance does not imply balanced competence across different coordination types. These findings point to new directions for designing targeted model architectures and improving multi-agent coordination ability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28266v1
- Authors: Yang Chen, Ye-Xin Xie, Lirong Che, Danyang Peng, Yuzhe Yang, Peiwen Lin, Xu Cao, Chuang Wang, Lei Yuan, Jian Su, Lan-Zhe Guo
- Published: 2026-08-28T12:29:23Z
- Age days: 2

</details>
