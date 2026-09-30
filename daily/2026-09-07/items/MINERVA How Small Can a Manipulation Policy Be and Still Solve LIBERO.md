---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03715v1"
published: "2026-09-03T11:51:10Z"
age_days: 3
score: 35
created: 2026-09-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?

> [!summary] 先说人话（基于摘要）
> MINERVA 用仅0.54M参数的视觉运动策略在标准LIBERO达到95.1%，说明该基准可能主要考查小容量的任务记忆，而非十亿参数VLA的通用推理。

## 问题

十亿参数VLA主导LIBERO，但基准真正需要多少容量并不清楚；若小模型已接近饱和，用该基准比较大模型可能混淆任务记忆、训练配方与泛化能力。

## 创新点或方法

作者构造紧凑策略族并系统扫描架构、训练和推理配置，测量容量下限；还置换task-ID映射诊断语言条件是否只是任务选择器，并用LIBERO-Plus扰动检验分布外鲁棒性。

## 证据

0.54M模型在四套标准LIBERO、2,000次滚动上平均成功率95.1%，比LeRobot π_0.5低2.4点但参数少7,700倍；约1M参数后饱和，低于0.25M崩溃。L1回归不逊于flow matching且GPU快至3.8倍；LIBERO-90上89任务达94.6%，LIBERO-Plus仅46–56%，光度偏移近零鲁棒。CPU每步重规划耗时5–9毫秒，较SmolVLA快113倍、较π_0.5快1,400倍。task-ID置换使成功率降至接近随机。


## 局限

结论针对LIBERO的任务结构和所用训练配方，不能直接外推到开放词汇、真实机器人或跨任务组合能力；比较口径需全文核查。

- **判断**：强烈建议精读实验与探针设计；这是今天最能改变基准解读方式的一篇。

## 研究关联

它对VLA基准选择和部署都很重要：标准LIBERO高分不能自动证明语言泛化或大模型价值，也提示蒸馏和容量匹配可能比继续扩参更实际。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/MINERVA How Small Can a Manipulation Policy Be and Still Solve LIBERO.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models with billions of parameters now dominate the LIBERO manipulation benchmark, but the model capacity actually required by the benchmark remains unclear. We introduce MINERVA (MINimal Efficient Robotic Vision-Action policy), a family of deliberately compact visuomotor policies designed to measure this task-specific capacity floor. A 0.54M-parameter policy achieves 95.1% average success over 2,000 rollouts on the four standard LIBERO suites, only 2.4 points below the reported LeRobot $π_{0.5}$ result despite using 7,700$\times$ fewer parameters. Performance saturates near 1M parameters and collapses below 0.25M. Across broad architectural, training, and inference sweeps, only action-chunk length and vision capacity consistently exceed a $\pm$1-point training-seed band. Flow matching provides no detectable advantage over direct L1 regression across three seeds, while regression is up to 3.8$\times$ faster on GPU. A task-ID permutation probe shows that standard LIBERO instruction conditioning primarily selects among memorized tasks: changing only the task-ID mapping reduces success to near chance. The same recipe achieves 94.6% success across 89 LIBERO-90 tasks, while LIBERO-Plus perturbations reduce performance to 46--56%, with near-zero robustness to photometric shifts. The 0.54M policy replans every control step in 5--9 ms per chunk on a laptop CPU, 113$\times$ faster than SmolVLA and 1,400$\times$ faster than $π_{0.5}$, without a GPU. These results establish a first empirical estimate of LIBERO's task-specific capacity floor and motivate capacity-aware design and distillation for deployment-efficient robot policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03715v1
- Authors: Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
- Published: 2026-09-03T11:51:10Z
- Age days: 3

</details>
