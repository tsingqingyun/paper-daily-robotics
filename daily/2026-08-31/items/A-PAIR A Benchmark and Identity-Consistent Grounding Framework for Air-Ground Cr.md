---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27997v1"
published: "2026-08-28T07:05:43Z"
age_days: 2
score: 27
created: 2026-08-31
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# A-PAIR: A Benchmark and Identity-Consistent Grounding Framework for Air-Ground Cross-View Referring Person Detection

> [!summary] 先说人话（基于摘要）
> A-PAIR 把地面与空中视角中的语言指代检测定义为成对身份一致的目标选择。ICRG 通过因子化指代定位、候选完整性监督和跨视角一致性校准，避免两端各自找到“像是同一人”的错误目标。

## 这篇到底在做什么

- **卡在哪里**：相似行人干扰、航拍外观信息弱以及跨视角身份一致性，使传统指代表达理解和开放词汇定位不足；它们通常不联合保证空地检测结果属于同一物理目标。
- **关键解法**：A-PAIR 提供成对跨视角指代样本；FARA 半自动生成因子化描述和身份一致性监督以降低标注成本。ICRG 联合选择地面与空中候选，并通过候选完整性和跨视角校准约束配对输出。
- **拿什么证明**：基准包含 22,137 个跨视角指代样本。ICRG 在地面、空中和配对检测上均超过强基线，pair F1 从 16.65% 提升至 22.28%。

## 值不值得读

- **和你的研究有什么关系**：对空地协同智能体，这是语言命令进入感知—控制链之前的关键身份对齐基准；它能防止多机器人因目标不一致而产生后续协调错误。
- **先别急着信**：尽管相对提升明确，22.28% 的 pair F1 仍然较低，说明任务远未解决；需核查数据分布和身份泄漏风险。
- **判断**：值得精读数据构造与配对指标；基准意义大于当前模型能力，结果也诚实显示了问题难度。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/A-PAIR A Benchmark and Identity-Consistent Grounding Framework for Air-Ground Cr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Air-ground cross-view referring person detection is a necessary component in the language-to-perception-to-control chain of collective embodied intelligence, grounding a language command into the same physical target before ground and aerial agents can coordinate downstream actions. Existing referring expression comprehension and open-vocabulary grounding methods do not jointly account for cross-view identity consistency, making them insufficient for Air-Ground Cross-View Referring Person Detection (AGCV-RPD), which involves similar pedestrian distractors, weak aerial appearance cues, and cross-view identity consistency. To study this problem, we introduce Air-Ground Paired Identity-Aware Referring (A-PAIR), the first comprehensive AGCV-RPD benchmark, containing 22,137 cross-view referring samples. To construct A-PAIR efficiently, we propose Factorized Annotation and Referential Alignment (FARA), a semi-automatic annotation framework that generates factorized referring descriptions and identity-consistency supervision at reduced cost. We propose Identity-Consistent Referring Grounding (ICRG), a framework that combines factorized referential grounding, candidate-completeness supervision, and cross-view consistency calibration for joint air-ground pair selection. ICRG improves ground, aerial, and pair-level detection over strong baselines, increasing pair F1 from 16.65% to 22.28%. These results show that AGCV-RPD requires paired detection and identity-consistent reasoning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27997v1
- Authors: Zhoupeng Guo, Xinjie Yao, Yunqi Zhu, Zhihe Fan, Siqi Zhao, Jianjun Chen, Yichen Dong, Yan Fan, Pengfei Zhu
- Published: 2026-08-28T07:05:43Z
- Age days: 2

</details>
