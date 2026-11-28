---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.34254v1"
published: "2026-11-25T12:18:29Z"
age_days: 2
score: 27
created: 2026-11-28
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Crucible Bench 让语言模型用专业软件完成化学任务，然后检查它交出的结果。软件顺利跑完也可能得到化学上无效的答案，评分器会按任务规则检查这一点。

## 问题

化学问答能测模型知不知道某条规则，却很难测它会不会在计算时用对规则。比如电子结构计算用了错误的自旋态，也可能正常收敛并给出看似合理的能量。单项任务评测还容易漏掉另一种差异：擅长算能量的模型，未必会根据测量反馈决定下一步测什么。[S4](https://arxiv.org/html/2611.34254v1#S1.p2.1)–[S6](https://arxiv.org/html/2611.34254v1#S1.p4.1)

### 用一个例子理解

理解用例（非论文实验）。给智能体一张普通食盐样品的衍射谱和几个候选晶相。它调用分析软件比对峰位，检查候选能否解释关键峰，再提交相集合。评分器按题目要求核对整个集合，软件正常返回只说明分析跑完。

## 创新点或方法

作者从公开数据筛题，删掉字段缺失、参考答案有歧义或输入已泄露答案的记录，并验证参考解能拿满分 [S15](https://arxiv.org/html/2611.34254v1#S3.SS1.p3.1)[S16](https://arxiv.org/html/2611.34254v1#S3.SS1.p4.1)。这是测评，节选未说明额外的模型训练步骤。评测时，智能体在隔离环境中通过 MCP 调用软件，最后提交能量值、结构判断等产物。确定性评分器按任务核对数值容差、参考答案或运行状态。实验执行题可以通过液体处理仿真检查流程，闭环优化题则按智能体选定的条件返回已有实测值并扣掉一次预算。[S6](https://arxiv.org/html/2611.34254v1#S1.p4.1)[S12](https://arxiv.org/html/2611.34254v1#S3.T2.6)[S18](https://arxiv.org/html/2611.34254v1#S3.SS2.p3.1)[S20](https://arxiv.org/html/2611.34254v1#S3.SS3.p1.1)[S22](https://arxiv.org/html/2611.34254v1#S3.SS3.p4.1)

### 方法如何工作

1. 从公开记录选出证据和参考解可核查的题，把每道题变成有明确交付物的任务。
2. 让模型调用专业工具并读取反馈，使评测覆盖工具选择、结果解释和后续决策。
3. 用任务规则检查产物，必要时查运行记录或输出文件，确认提交有实际执行依据。
4. 比较分任务成绩和禁用工具后的表现，量化工具访问的作用，并看总排名掩盖了哪些能力。

### 必要术语

- DMTA：设计、制造、测试、分析的研究循环；在本文中用来组织独立评分的任务。
- MCP：把外部工具接给模型的协议；智能体通过它获得专业软件的返回结果。
- 闭环优化：根据已测结果决定下一次测什么；本文把预算内实际找到的最好结果与随机搜索比较。

## 证据

评测在 7 个隔离环境中给智能体提供 75 种工具，涵盖 12 个任务族、1,078 道题 [S6](https://arxiv.org/html/2611.34254v1#S1.p4.1)。14 个模型的最高总分是 0.545，总排名第 12 的模型反而在闭环优化上第一 [S1](https://arxiv.org/html/2611.34254v1#abstract1.1)。优化分数以等预算随机搜索的期望最佳值为参照 [S22](https://arxiv.org/html/2611.34254v1#S3.SS3.p4.1)。禁用工具后所有模型得分都明显下降 [S28](https://arxiv.org/html/2611.34254v1#S5.SS2.p1.1)，表明工具访问在这套评测中有贡献。节选未给出各模型的禁用前后分差或不确定性，难以进一步判断增益差异。

## 局限

作者的误差分析显示，逆合成评分会漏给与专利参考不同的有效路线 [S26](https://arxiv.org/html/2611.34254v1#S5.SS1.SSS0.Px2.p1.1)。各题独立评分，湿实验由仿真或既有测量代理 [S8](https://arxiv.org/html/2611.34254v1#S1.F2)[S18](https://arxiv.org/html/2611.34254v1#S3.SS2.p3.1)。若想用排行榜衡量真实科研能力，还要核查换用可接受多解的评分后排名是否稳定，以及模型遇到记录之外的反馈时会怎样决策。

- **判断**：值得读到评分规则和误差案例，因为它们决定了一次扣分究竟意味着科学判断出错，还是答案与参考不同。

## 研究关联

设计工具型智能体评测时，可以分别记录软件是否运行成功、输出是否通过领域检查、最终提交是否遵守这些检查。这样才能区分工具选错、参数设错，以及工具已经指出问题但模型仍提交错误结果。

### 下一步读哪里

先读表 2 的节选 [S11](https://arxiv.org/html/2611.34254v1#S3.T2)[S12](https://arxiv.org/html/2611.34254v1#S3.T2.6)，看每个任务交什么、怎样得分。再读 [S22](https://arxiv.org/html/2611.34254v1#S3.SS3.p4.1)[S26](https://arxiv.org/html/2611.34254v1#S5.SS1.SSS0.Px2.p1.1)[S28](https://arxiv.org/html/2611.34254v1#S5.SS2.p1.1)，核查不同评分尺度怎样汇总，以及哪些任务的工具增益最大。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34254v1
- 获取时间：2026-11-28T03:58:17.214909+00:00
- [S1] [Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments · 正文段落 1](https://arxiv.org/html/2611.34254v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.34254v1#S1.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34254v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34254v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34254v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.34254v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.34254v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.34254v1#S1.F2)
- [S9] [2.1 LLMs for Chemistry · 正文段落 9](https://arxiv.org/html/2611.34254v1#S2.SS1.p1.1)
- [S10] [2.2 Chemistry Agents · 正文段落 11](https://arxiv.org/html/2611.34254v1#S2.SS2.p1.1)
- [S11] [3 Crucible Bench · 正文段落 19](https://arxiv.org/html/2611.34254v1#S3.T2)
- [S12] [3 Crucible Bench · 正文段落 20](https://arxiv.org/html/2611.34254v1#S3.T2.6)
- [S13] [3.1 Covering the Research Workflow · 正文段落 21](https://arxiv.org/html/2611.34254v1#S3.SS1.p1.1)
- [S14] [3.1 Covering the Research Workflow · 正文段落 22](https://arxiv.org/html/2611.34254v1#S3.SS1.p2.1)
- [S15] [3.1 Covering the Research Workflow · 正文段落 23](https://arxiv.org/html/2611.34254v1#S3.SS1.p3.1)
- [S16] [3.1 Covering the Research Workflow · 正文段落 24](https://arxiv.org/html/2611.34254v1#S3.SS1.p4.1)
- [S17] [3.2 Real Software in the Loop · 正文段落 25](https://arxiv.org/html/2611.34254v1#S3.SS2.p1.1)
- [S18] [3.2 Real Software in the Loop · 正文段落 27](https://arxiv.org/html/2611.34254v1#S3.SS2.p3.1)
- [S19] [3.2 Real Software in the Loop · 正文段落 28](https://arxiv.org/html/2611.34254v1#S3.SS2.p4.1)
- [S20] [3.3 Verifying Artifacts · 正文段落 29](https://arxiv.org/html/2611.34254v1#S3.SS3.p1.1)
- [S21] [3.3 Verifying Artifacts · 正文段落 31](https://arxiv.org/html/2611.34254v1#S3.SS3.p3.1)
- [S22] [3.3 Verifying Artifacts · 正文段落 32](https://arxiv.org/html/2611.34254v1#S3.SS3.p4.1)
- [S23] [Synthesis planning and closed-loop optimization are the hardest domains. · 正文段落 41](https://arxiv.org/html/2611.34254v1#S4.SS2.SSS0.Px1.p1.1)
- [S24] [Different models lead at different stages of the workflow. · 正文段落 42](https://arxiv.org/html/2611.34254v1#S4.SS2.SSS0.Px2.p1.1)
- [S25] [The most common error varies by stage. · 正文段落 46](https://arxiv.org/html/2611.34254v1#S5.SS1.SSS0.Px1.p1.1)
- [S26] [Error severity varies across models. · 正文段落 47](https://arxiv.org/html/2611.34254v1#S5.SS1.SSS0.Px2.p1.1)
- [S27] [Agents disregard their own checks. · 正文段落 53](https://arxiv.org/html/2611.34254v1#S5.SS1.SSS0.Px5.p1.1)
- [S28] [5.2 Ablation Study · 正文段落 54](https://arxiv.org/html/2611.34254v1#S5.SS2.p1.1)
- [S29] [6 Conclusion · 正文段落 55](https://arxiv.org/html/2611.34254v1#S6.p1.1)
- [S30] [A.1 Data Sources · 正文段落 58](https://arxiv.org/html/2611.34254v1#A1.SS1.p1.1)
- [S31] [A.1 Data Sources · 正文段落 59](https://arxiv.org/html/2611.34254v1#A1.T5.3)
- [S32] [A.1 Data Sources · 正文段落 60](https://arxiv.org/html/2611.34254v1#A1.T5)
- [S33] [Appendix E Case Studies · 正文段落 81](https://arxiv.org/html/2611.34254v1#A5.F14)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/Crucible Evaluating LLM Agents in Executable Chemistry Research Environments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this gap, we introduce Crucible Bench to evaluate this ability across all four stages of the design-make-test-analyze (DMTA) cycle. The benchmark contains 1,078 tasks in 12 task families curated from 18 published datasets, covering molecular design, synthesis planning, experimental execution, closed-loop optimization, simulation, and analytical characterization. Agents access 75 domain-specific tools through the Model Context Protocol in seven isolated environments. Sandboxed graders verify the resulting synthesis routes, experimental protocols, and other outputs. Laboratory tasks use robotic simulators or previously measured experimental data. We evaluate 14 LLMs as agents and find that the best achieves an overall score of 0.545, with synthesis planning and closed-loop optimization emerging as the hardest domains. Overall performance does not predict optimization performance well: the model ranked twelfth overall achieves the highest score in closed-loop optimization. Error analysis also shows that agents often submit chemically invalid results despite running their tools successfully. Stronger models benefit more from tool access, but reliable use of chemical software remains a challenge that Crucible Bench can track as models improve.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34254v1
- Authors: Yinjun Liu, Xinye Li, Ruisen Peng, Lang Gao, Zixiang Xu, Zirui Song, Xiuying Chen
- Published: 2026-11-25T12:18:29Z
- Age days: 2

</details>
