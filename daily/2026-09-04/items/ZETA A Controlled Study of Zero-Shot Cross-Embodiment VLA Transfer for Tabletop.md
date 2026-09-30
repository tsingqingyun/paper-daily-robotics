---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02546"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 43
created: 2026-09-04
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation

> [!summary] 先说人话（基于摘要）
> ZETA把VLA跨机器人本体的“零样本”迁移做成受控实验，并明确区分严格零样本与预训练见过目标本体的零样本。结果指向三个实用杠杆：局部末端状态—动作表示、本体多样性和辅助共训。

## 这篇到底在做什么

- **卡在哪里**：既有跨本体研究缺少统一的零样本定义，任务、场景和实验协议变化又常与硬件变化混在一起，难以判断迁移究竟来自何处；目标本体是否在预训练中出现也经常未被区分。
- **关键解法**：基准固定其他条件，覆盖仿真及真实验证中的14种留出目标本体，分别控制状态—动作表示、预训练本体多样性、辅助目标和目标本体暴露。输出是桌面双指夹爪操作的迁移表现，关键差异是隔离本体变化并分开报告两类零样本。
- **拿什么证明**：局部末端执行器表示、源本体多样性和辅助共训分别带来约15、18和7个百分点提升；仅在预训练加入5%的目标本体数据，就使目标本体平均任务进度提升13.4个百分点。

## 值不值得读

- **和你的研究有什么关系**：这是VLA跨硬件泛化研究可直接采用的定义、基准和实验清单，也警示研究者不能把预训练见过硬件称作严格零样本。对通用机器人策略的数据设计和表示选择有明确参考价值。
- **先别急着信**：结论限定在固定式桌面操作和双指夹爪；摘要明确把移动底盘、灵巧手和长时程任务留作未来研究，不能外推到更广泛本体。
- **判断**：做跨本体VLA者应精读实验控制与报告规范；它的主要价值是厘清因果因素和术语，而不只是刷新单一分数。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/ZETA A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02546v1 Announce Type: new Abstract: Zero-shot generalization to unseen embodiments is important for generalizable vision-language-action (VLA) models as robot hardware evolves and task-specific data collection remains costly. However, a systematic understanding of this problem remains limited, in part because the literature lacks a unified zero-shot transfer definition and controlled evaluation settings that isolate embodiment changes from differences in tasks, scenes, or protocols. To address this gap, we first distinguish strict zero-shot transfer, where the target embodiment is absent from all training data, from pretrain-exposed zero-shot transfer, where it appears only during pretraining. We then introduce a controlled benchmark spanning 14 held-out target embodiments across simulation and real-world validation. Within this framework, we conduct a controlled analysis of four factors: state-action representations, pretraining embodiment diversity, auxiliary co-training objectives, and target-embodiment exposure. Experimental results show that local end-effector (EEF) state-action representations, the source embodiment diversity, and auxiliary co-training improve cross-embodiment transfer by around 15, 18, and 7 percentage points, respectively. We further find that adding only 5% target-embodiment data during pretraining improves average target-embodiment progress by 13.4 percentage points, showing that strict and pretrain-exposed zero-shot transfer are distinct and should be reported separately. Together, these findings provide practical guidance for evaluating and improving cross-embodiment VLA transfer in stationary tabletop manipulation with two-finger grippers, while motivating future investigation of broader settings including mobile-base control, dexterous hands, and long-horizon tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02546
- Authors: Mi Yan, Wenhao Zhang, Zhiqi Zhang, Yu Peng, Tangxinyu Wang, Lingfei Zhai, Jiayi Su, Shengliang Deng, Lin Peng, Yaowei Liu, Yuxing Chen, Zhiyuan Wei, Jilong Wang, Jiayi Chen, Jiangran Lyu, Zhizheng Zhang, He Wang
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
