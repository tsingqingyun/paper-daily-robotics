---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03715"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-09-05
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?

> [!summary] 先说人话（基于摘要）
> MINERVA 用极小视觉运动策略测 LIBERO 的任务容量下限：54万参数已达95.1%，而任务 ID 置换会让成绩跌至近随机。它指出标准 LIBERO 高分更可能反映任务记忆，而不是强语言泛化。

## 问题

数十亿参数 VLA 主导 LIBERO，但基准实际需要多大容量并不清楚；若简单小模型也能饱和，继续比较大模型分数就无法证明语义理解、泛化或复杂生成机制的价值。

## 创新点或方法

作者构建一组刻意压缩的视觉动作策略，系统扫描容量、架构、训练、推理、动作块长度和视觉容量，并对任务 ID 映射做置换探针；还在 LIBERO-90、LIBERO-Plus及 CPU 延迟上测试。

## 证据

54万参数模型在四套标准 LIBERO、2,000次 rollout 上平均成功率95.1%，只比所报 π0.5 低2.4点但参数少7,700倍；约100万参数后饱和，低于25万时崩溃。Flow matching 相对 L1 回归无可检测优势，回归最快3.8倍。模型在89项 LIBERO-90任务上达94.6%，LIBERO-Plus仅46–56%，对光度变化近零鲁棒；CPU 每块5–9毫秒，较 SmolVLA 快113倍、较 π0.5 快1,400倍。


## 局限

容量下限只针对当前 LIBERO 设置；需核查输入信息、任务 ID 使用方式及训练数据是否与大模型基线完全可比。

- **判断**：今天最值得精读的评测论文之一；无论做 VLA 还是基准，都应认真看任务 ID 探针和公平性设置。

## 研究关联

它直接影响 VLA 基准选择、蒸馏和部署：标准 LIBERO 分数可能不足以证明大模型能力，研究者应把容量、扰动泛化和任务绑定探针纳入报告。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/MINERVA How Small Can a Manipulation Policy Be and Still Solve LIBERO.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03715v1 Announce Type: new Abstract: Vision-language-action (VLA) models with billions of parameters now dominate the LIBERO manipulation benchmark, but the model capacity actually required by the benchmark remains unclear. We introduce MINERVA (MINimal Efficient Robotic Vision-Action policy), a family of deliberately compact visuomotor policies designed to measure this task-specific capacity floor. A 0.54M-parameter policy achieves 95.1% average success over 2,000 rollouts on the four standard LIBERO suites, only 2.4 points below the reported LeRobot $\pi_{0.5}$ result despite using 7,700$\times$ fewer parameters. Performance saturates near 1M parameters and collapses below 0.25M. Across broad architectural, training, and inference sweeps, only action-chunk length and vision capacity consistently exceed a $\pm$1-point training-seed band. Flow matching provides no detectable advantage over direct L1 regression across three seeds, while regression is up to 3.8$\times$ faster on GPU. A task-ID permutation probe shows that standard LIBERO instruction conditioning primarily selects among memorized tasks: changing only the task-ID mapping reduces success to near chance. The same recipe achieves 94.6% success across 89 LIBERO-90 tasks, while LIBERO-Plus perturbations reduce performance to 46--56%, with near-zero robustness to photometric shifts. The 0.54M policy replans every control step in 5--9 ms per chunk on a laptop CPU, 113$\times$ faster than SmolVLA and 1,400$\times$ faster than $\pi_{0.5}$, without a GPU. These results establish a first empirical estimate of LIBERO's task-specific capacity floor and motivate capacity-aware design and distillation for deployment-efficient robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03715
- Authors: Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
