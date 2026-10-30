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
url: "https://arxiv.org/abs/2610.36848"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-10-30
concepts: ["多模态基础模型", "智能体 Agent"]
---

# Evolving Agent Teams

> [!summary] 这篇论文到底做了什么（基于摘要）
> Evolving Agent Teams（EAT）针对代码智能体反复修改却优化不动的问题，让主管诊断卡点、重新组织团队，并用持久文件保留历次经验。关键是让搜索方式随失败原因变化，而不只是继续生成更多代码。

## 问题

任务是继续优化专家写好的 GPU 内核等开放式工程问题。这类代码已有很强的起点，摘要发现现有编码智能体会停在局部最优：能找到附近的改进，却难以跳出当前实现路线。真正瓶颈是搜索停滞，单纯延长运行未必能改变探索方向。

### 用一个例子理解

理解用例（非论文实验）：输入一个通过正确性测试、但延迟偏高的归约内核；团队多轮修改仍无进展，主管结合历史记录重新安排探索；输出新的候选实现及其测试记录，供下一轮优化继续使用。

## 创新点或方法

旧做法沿既定编码流程反复尝试；EAT 加入中央主管，在发现局部最优后诊断原因并重组团队。学习文档、演化历史和各团队产物组成持久文件系统，让新团队继承已试路线与经验。摘要没有说明是否训练模型权重；明确描述的是任务执行期间的团队调整与记忆机制，不能把它理解成已验证的模型训练算法。

### 方法如何工作

1. 团队修改候选实现并接受任务反馈，得到当前性能及尝试记录，为判断是否停滞提供依据。
2. 主管诊断当前局部最优并重组团队，使下一轮搜索有机会改变方向；具体诊断规则摘要未说明。
3. 新团队读取学习文档、演化历史和已有产物，继承经验后继续尝试，减少重复探索。
4. 把后续结果留在持久文件中，供再次诊断和重组使用；更新细则摘要只说明到此。

### 必要术语

- 局部最优：附近的修改难再改善结果；本文用它描述编码搜索的停滞。
- 持久文件系统：跨轮次保留的共享文件；本文用来承接团队更替前后的经验。
- token 预算：模型可消耗的文本计算额度；本文用它约束方法比较的资源条件。

## 证据

摘要称相同 token 预算下胜过强编码智能体基线，但未给基线名称和差距。扩大预算后，生成的 CUDA 内核相对 FlashInfer MLA paged decode 平均加速 1.2 倍，在 FlashInfer-Bench 的 47 个生产负载中赢 36 个，其余为基线速度的 0.86–0.99 倍。KDA prefill 在 MI350X、B200 上分别达到 vLLM 的 3.01 倍、FlashKDA 的 3.44 倍。RoboDojo 留出种子得分为 62.1，对比最佳榜单条目 55.3。以上均来自摘要；跨任务成绩支持适用范围较广，但不能单独证明每个组件的作用。

## 局限

摘要未给明确局限。我会核查主管怎样判定局部最优，以及重组、持久记忆和额外计算分别贡献多少。扩展预算成绩不能直接当作同预算优势的大小；RoboDojo 的环境与评分含义也未说明，不能据此推出真机操控能力。

- **判断**：值得读到主管决策规则和同预算消融，因为可迁移的核心是怎样识别停滞并改变搜索，而不只是最终内核有多快。

## 研究关联

值得借鉴的是把“卡住了”当成调整组织方式的信号。对于能自动测试、需要多轮试错的任务，可以保留失败路线及其原因，再决定下一轮由什么团队继续，避免反复支付同一种探索成本。

### 下一步读哪里

先核查局部最优的判定、团队如何重组、文件怎样更新和被读取；再看同 token 预算是否包含主管开销，以及内核正确性、计时条件和各组件消融。输入没有提供正文节选。

- **概念**：多模态基础模型 智能体 Agent
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Evolving Agent Teams.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.36848v1 Announce Type: new Abstract: The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system that comprises a learning document, an evolution history, and per-team artifacts, grounding restructuring with accumulated experience. Under a matched token budget, Evolving Agent Teams consistently outperforms strong coding-agent baselines. With an extended token budget, Evolving Agent Teams generates a CUDA kernel that reaches 1.2x mean speedup over the production FlashInfer MLA paged decode kernel from scratch and wins on 36 of 47 production workloads from FlashInfer-Bench (0.86-0.99x on the remaining 11). It also demonstrates superior performance on tasks such as KDA prefill on AMD MI350X (3.01x over vLLM) and NVIDIA B200 (3.44x over FlashKDA), MoE expert-offload serving on Apple silicon (30.3 tokens/s decode for Qwen3.8-Flash-Next in MLX 4-bit on a 48 GB M4 Pro), and RoboDojo robot manipulation (62.1 on held-out seeds vs. 55.3 for the best leaderboard entry). Code is available at https://github.com/caoshiyi/EAT.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36848
- Authors: Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
