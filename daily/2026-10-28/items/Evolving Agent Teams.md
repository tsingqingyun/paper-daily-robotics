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
url: "https://arxiv.org/abs/2610.36848v1"
published: "2026-10-27T08:46:21Z"
age_days: 0
score: 29
created: 2026-10-28
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Evolving Agent Teams

> [!summary] 这篇论文到底做了什么（基于摘要）
> Evolving Agent Teams（EAT）处理的是编码代理反复修改、却始终突破不了专家代码的问题。它让监督者诊断卡点、重新组织代理团队，并用持久文件保存经验，避免每轮搜索都从头摸索。

## 问题

具体任务是优化 GPU 内核等开放式工程问题：答案可以正确运行，却离更快的实现很远。摘要发现，现有编码代理面对 FlashInfer 这类专家编写的内核容易停在局部最优；继续沿同一路径修改，不一定能发现另一种实现。

### 用一个例子理解

理解用例（非论文实验）：输入一个已正确运行但速度不佳的注意力内核；团队尝试优化后停滞，监督者读取历史并重分任务；新团队据此探索其他实现，输出经正确性和速度检查的候选代码。

## 创新点或方法

旧做法是在既有搜索方向上持续改代码；EAT 增加一个能诊断停滞并重组团队的监督者。学习文档、演化历史和各团队产物留在文件系统中，为重组提供依据。巧处是同时保留经验、改变搜索组织，而不只是增加尝试次数。摘要描述的是解题时的迭代流程，没有说明是否训练模型、监督者如何判定停滞，以及如何具体调整团队。

### 方法如何工作

1. 代理团队生成并测试候选实现，得到可供比较的工程结果。
2. 监督者诊断当前局部最优，决定是否需要改变团队组织；具体触发规则摘要未说明。
3. 把经验与产物保存在文件系统，使新团队能够接续已有探索。
4. 重组后的团队继续搜索并接受评测，以检验新方向是否真正改善结果。

### 必要术语

- 局部最优：当前尝试附近难以找到更好方案；本文用团队重组尝试跳出这一状态。
- 持久文件系统：跨轮次保留材料的存储；在本文中承接经验和代码产物。
- 同 token 预算：限制模型使用的文本计算额度；用于比较不同搜索组织方式的效率。

## 证据

摘要称，同 token 预算下 EAT 持续优于强编码代理基线，但未列名称和差值。扩大预算后，从零生成的 CUDA 内核相对生产版 FlashInfer MLA paged decode 平均加速 1.2 倍，在 FlashInfer-Bench 的 47 个生产负载中赢得 36 个，其余 11 个为基线的 0.86—0.99 倍。另报 KDA prefill 在 MI350X 上较 vLLM 为 3.01 倍、B200 上较 FlashKDA 为 3.44 倍；这些是不同平台和对照，不能合并排名。RoboDojo 留出种子得分为 62.1，对照最佳榜单条目为 55.3，摘要未说明是否涉及真机。

## 局限

扩大预算后的最佳成绩不能单独证明团队重组的收益；还需核查同预算消融，分清监督者、记忆和额外搜索各自的作用。摘要也未交代正确性检查、运行时间和多次独立搜索的波动。

- **判断**：值得细读搜索控制与消融实验：关键是找出它何时、凭什么改变方向，才能判断能否复用。

## 研究关联

可以借鉴的是把“失败后学到了什么”变成下一轮可读取的材料，并允许改变任务分工。对于验证结果明确、但实现路径很多的工程搜索，这比单纯延长同一条推理链更值得试验。

### 下一步读哪里

先核查停滞诊断与团队重组规则，再看移除持久记忆的对照；同时检查 token 预算是否包含监督开销，以及 47 个负载的逐项结果。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/Evolving Agent Teams.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system that comprises a learning document, an evolution history, and per-team artifacts, grounding restructuring with accumulated experience. Under a matched token budget, Evolving Agent Teams consistently outperforms strong coding-agent baselines. With an extended token budget, Evolving Agent Teams generates a CUDA kernel that reaches 1.2x mean speedup over the production FlashInfer MLA paged decode kernel from scratch and wins on 36 of 47 production workloads from FlashInfer-Bench (0.86-0.99x on the remaining 11). It also demonstrates superior performance on tasks such as KDA prefill on AMD MI350X (3.01x over vLLM) and NVIDIA B200 (3.44x over FlashKDA), MoE expert-offload serving on Apple silicon (30.3 tokens/s decode for Qwen3.8-Flash-Next in MLX 4-bit on a 48 GB M4 Pro), and RoboDojo robot manipulation (62.1 on held-out seeds vs. 55.3 for the best leaderboard entry). Code is available at https://github.com/caoshiyi/EAT.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36848v1
- Authors: Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica
- Published: 2026-10-27T08:46:21Z
- Age days: 0

</details>
