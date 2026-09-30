---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25562v1"
published: "2026-09-22T01:51:09Z"
age_days: 1
score: 33
created: 2026-09-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models

> [!summary] 先说人话（基于摘要）
> IndustrialVLA-Bench 用统一且可追溯的记录比较开放 VLA 与 WAM，发现基础任务分数接近时，鲁棒性和指令改写表现仍可能相差很大。

## 问题

两类策略服务相同操作任务，却常采用不同评测协议，导致能力、语言敏感性、鲁棒性和部署代价难以公平比较。

## 创新点或方法

分别用 LIBERO、LIBERO-Plus、LIBERO-Para 衡量基础能力、非语言鲁棒性和指令敏感性，并记录执行开销。固定检查点与推理配置进行三个不同随机种子的完整评估，同时按协议忠实程度划分证据等级。

## 证据

六个系统的基础 LIBERO 均分跨度为 1.58 分，鲁棒性和改写汇总分跨度为 14.62 与 31.08 分。仅比较三个严格遵循协议的系统，跨度仍为 1.36、14.62 和 23.10 分；另记录延迟、峰值内存与运行模式。

## 局限

六个系统中只有三个支持严格比较；这些差距也不能推导出 VLA 或 WAM 某一范式普遍更优。

- **判断**：值得精读评测记录和证据分级，尤其适合做模型选型或复现实验时作为比较规范参考。

## 研究关联

对 VLA、WAM 和基准研究者，实际价值是把模型选择从单一成功率扩展到稳定性、语言适应和运行代价，并明确哪些结果允许严格比较。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/IndustrialVLA-Bench A Traceable Multi-Axis Evaluation of Open Robot Policy Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Open robot policies increasingly follow two paradigms: vision-language-action models (VLAs) directly map observations and instructions to actions, whereas world-action models (WAMs) incorporate learned video or world dynamics into policy learning or action generation. Although both target the same manipulation tasks and represent alternative design choices, they are commonly reported under different evaluation protocols, leaving their capability, robustness, language sensitivity, and deployment-cost trade-offs unclear. We present IndustrialVLA-Bench, an evidence-aware evaluation of six released VLA and WAM systems under a unified reporting schema. It separately evaluates clean capability on LIBERO, non-language robustness on LIBERO-Plus, instruction sensitivity on LIBERO-Para, and observed execution cost. Reported task scores aggregate three complete evaluations with distinct random seeds under a fixed checkpoint and inference configuration. Across all six systems, clean LIBERO averages differ by only 1.58 points, whereas robustness and paraphrase summaries span 14.62 and 31.08 points. Restricting every comparison to the three protocol-faithful systems preserves the effect (1.36, 14.62 and 23.10 points), so the diagnostic separation reported here does not depend on the weaker evidence tiers. We additionally report observed inference latency, peak memory, runtime mode, and an evidence status for every system. Protocol-faithful, near-reproduction, and pending-verification entries remain visibly separated; only protocol-faithful entries support strict comparisons. Rather than claiming universal superiority of either paradigm, IndustrialVLA-Bench provides traceable evidence for comparing released robot policies on shared practical criteria. Code and evaluation records are available at https://github.com/xiaoqi-7/IndustrialVLA-Bench.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25562v1
- Authors: Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, Xiaoyang Li, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Fei Wang, Shan You, Taotao Cai
- Published: 2026-09-22T01:51:09Z
- Age days: 1

</details>
