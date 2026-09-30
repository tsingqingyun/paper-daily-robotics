---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02546v1"
published: "2026-09-02T13:00:18Z"
age_days: 0
score: 43
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation

> [!summary] 先说人话（基于摘要）
> ZETA 把零样本跨本体迁移拆成严格零样本与预训练见过目标本体两种情形，并用受控基准隔离本体变化。结果表明，局部末端执行器表征、源本体多样性和辅助共训练都是明确有效的杠杆。

## 问题

任务是在未见机器人本体上零样本执行桌面操作。真正瓶颈是既有研究混杂了任务、场景和协议变化，而且把训练阶段完全未见与预训练见过目标本体统称为零样本，导致结论不可比。

## 创新点或方法

基准覆盖仿真与真实验证中的14种留出目标本体，固定其他条件，分别控制状态—动作表征、预训练本体多样性、辅助目标和目标本体暴露量；关键区别是明确区分 strict 与 pretrain-exposed zero-shot transfer。

## 证据

局部 EEF 状态—动作表征、源本体多样性和辅助共训练分别带来约15、18和7个百分点提升；预训练中加入5%目标本体数据，使平均任务进度提高13.4个百分点。


## 局限

结论目前限定于静态桌面、双指夹爪；摘要也明确指出移动底盘、灵巧手和长程任务尚未覆盖。

- **判断**：值得精读实验设计和变量控制部分；它的主要价值不是新模型，而是把跨本体 VLA 的概念与证据做得可比较。

## 研究关联

它为 VLA 和具身评测研究者提供了更可信的跨本体报告规范，也给出数据配比与动作表征设计的直接经验，能减少把预训练泄漏误当作真正零样本能力的风险。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/ZETA A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Zero-shot generalization to unseen embodiments is important for generalizable vision-language-action (VLA) models as robot hardware evolves and task-specific data collection remains costly. However, a systematic understanding of this problem remains limited, in part because the literature lacks a unified zero-shot transfer definition and controlled evaluation settings that isolate embodiment changes from differences in tasks, scenes, or protocols. To address this gap, we first distinguish strict zero-shot transfer, where the target embodiment is absent from all training data, from pretrain-exposed zero-shot transfer, where it appears only during pretraining. We then introduce a controlled benchmark spanning 14 held-out target embodiments across simulation and real-world validation. Within this framework, we conduct a controlled analysis of four factors: state-action representations, pretraining embodiment diversity, auxiliary co-training objectives, and target-embodiment exposure. Experimental results show that local end-effector (EEF) state-action representations, the source embodiment diversity, and auxiliary co-training improve cross-embodiment transfer by around 15, 18, and 7 percentage points, respectively. We further find that adding only 5% target-embodiment data during pretraining improves average target-embodiment progress by 13.4 percentage points, showing that strict and pretrain-exposed zero-shot transfer are distinct and should be reported separately. Together, these findings provide practical guidance for evaluating and improving cross-embodiment VLA transfer in stationary tabletop manipulation with two-finger grippers, while motivating future investigation of broader settings including mobile-base control, dexterous hands, and long-horizon tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02546v1
- Authors: Mi Yan, Wenhao Zhang, Zhiqi Zhang, Yu Peng, Tangxinyu Wang, Lingfei Zhai, Jiayi Su, Shengliang Deng, Lin Peng, Yaowei Liu, Yuxing Chen, Zhiyuan Wei, Jilong Wang, Jiayi Chen, Jiangran Lyu, Zhizheng Zhang, He Wang
- Published: 2026-09-02T13:00:18Z
- Age days: 0

</details>
