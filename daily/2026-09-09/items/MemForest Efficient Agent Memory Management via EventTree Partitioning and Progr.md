---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08273v1"
published: "2026-09-08T05:30:30Z"
age_days: 1
score: 28
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging

> [!summary] 先说人话（基于摘要）
> MemForest把长期记忆按事件分组，再沿树结构逐步合并重复内容。检索时从关键记忆向时间邻域扩展，用较少存储保留大部分任务表现。

## 这篇到底在做什么

- **卡在哪里**：Agent记忆持续增长会增加存储和检索成本；压缩需要减少冗余，同时保留回答和视频理解所需的事件关联。
- **关键解法**：结合全局语义相似性与局部时间连续性划分事件，为每组构建最大生成树EventTree，并优先沿高权重边合并节点。锚点引导传播检索再从关键节点的时间邻域找回相关信息。
- **拿什么证明**：Mem0下，在LoCoMo、LongMemEval、PersonaMem三个基准压缩50%历史记忆，保留97.1%原始性能，检索加速1.89倍；M3-Agent下，在M3-Bench-robot和M3-Bench-web压缩50%，保留99.7%性能，检索加速2.24倍。

## 值不值得读

- **和你的研究有什么关系**：适合需要长期运行的多模态Agent，提供可量化的记忆成本取舍；机器人相关基准带来关联，但摘要未证明闭环控制能力提升。
- **先别急着信**：需核查合并时是否损失少见但关键事件，以及速度统计是否包括建树、压缩与更新成本。
- **判断**：Agent记忆方向值得精读压缩和检索实验，机器人策略方向可作为系统组件参考。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/MemForest Efficient Agent Memory Management via EventTree Partitioning and Progr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Agent memory systems have demonstrated significant potential in long-term dialogue, personalized assistants, and video understanding. However, continuously accumulated memory introduces substantial storage and retrieval costs during inference. To address this issue, we propose \textbf{MemForest}, a general memory compression framework adaptable to various agent memory systems. Specifically, MemForest partitions historical memory into event-centric units by leveraging global semantic similarity and local temporal continuity. For each unit, it constructs a maximum spanning tree, termed an EventTree, and progressively merges redundant memory nodes by selecting high-weight edges, reducing storage overhead. Furthermore, we introduce an anchor-guided propagation retrieval mechanism that retrieves relevant memory nodes from the temporal neighborhoods of key nodes, improving retrieval accuracy. Extensive experiments demonstrate the effectiveness of MemForest. Under the unimodal Mem0 framework, MemForest retains \textbf{97.1%} of the original performance while compressing \textbf{50%} of historical memory across three benchmarks (LoCoMo, LongMemEval, and PersonaMem), achieving a \textbf{1.89x} retrieval speedup. Under the multimodal M3-Agent framework, it preserves \textbf{99.7%} of the original performance with a \textbf{50%} compression ratio across two benchmarks (M3-Bench-robot and M3-Bench-web), achieving a \textbf{2.24x} retrieval speedup. \textcolor{RoyalBlue}{\textit{Our code is available at [https://github.com/Celina-love-sweet/MemForest.}}](https://github.com/Celina-love-sweet/MemForest.}})

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08273v1
- Authors: Junxi Wang, Te Sun, Jiayi Zhu, Chen Zhang, Siyuan Li, Xuyang Liu, Zichen Wen, Xiaobing Tu, Jinkui Ren, Xiantao Zhang, Ziqi Yuan, Linfeng Zhang
- Published: 2026-09-08T05:30:30Z
- Age days: 1

</details>
