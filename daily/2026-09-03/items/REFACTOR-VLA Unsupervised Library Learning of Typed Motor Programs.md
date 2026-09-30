---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01215v1"
published: "2026-09-01T13:19:05Z"
age_days: 1
score: 33
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs

> [!summary] 先说人话（基于摘要）
> REFACTOR-VLA 用 wake/sleep 机制从动作片段中无监督归纳可复用、带类型的运动程序。睡眠阶段借助潜在世界模型的 Behavioral-Equivalence Kernel 判断行为等价，清醒阶段则让动作解码器消费类型化 lambda term。

## 问题

单体 VLA 只输出原始动作或短块，难以复用行为、解释长程结构；旧技能发现依赖表征相似度或不熟悉机器人动力学的语言模型，无法可靠判断两段动作是否在行为上等价。

## 创新点或方法

sleep 阶段用学习到的世界模型 rollout 计算 BEK 并聚类程序片段；wake 阶段以 Hindley–Milner 风格词汇生成类型化程序，由库条件 rectified-flow 解码器执行。候选抽象还必须通过最小描述长度和回报保持门控。

## 证据

LIBERO 上，将世界模型从188M增至430M反而在4/4套件变差。加入监督式对比 InfoNCE 后，3个种子的 NMI 分别为对象0.462±0.021、空间0.867±0.025、目标0.915±0.013、LIBERO-10 0.754±0.010，四套件较最强已发表基线平均高0.184；12个 provider 的平均成对 NMI 为0.705，95%区间[0.683,0.729]。解码器使用3个获准抽象中的2个，并重写全部256条样例。


## 局限

摘要的强证据主要是聚类 NMI 和演示重写，尚未给出这些抽象对长程任务成功率、迁移或真实机器人控制的直接收益。

- **判断**：值得精读 BEK、门控和评测定义；概念很强、聚类证据扎实，但“技能库改善控制”仍需全文中的行为结果支撑。

## 研究关联

它把世界模型用于定义技能的行为等价性，而非只预测像素；对长程 VLA、技能库和可解释机器人学习都有直接价值，也提示训练目标比单纯扩模型更关键。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/REFACTOR-VLA Unsupervised Library Learning of Typed Motor Programs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's dynamics. We introduce REFACTOR-VLA, a wake/sleep system for learning reusable skills. Its sleep phase clusters motor-program fragments under a Behavioral-Equivalence Kernel (BEK) computed from rollouts of a learned latent world model $M_φ$; its wake phase emits typed lambda terms over a Hindley--Milner-inspired vocabulary, consumed by a library-conditioned rectified-flow action decoder. Abstractions are admitted only if they pass Minimum Description Length and return-preservation gates. On LIBERO we report two findings. First, enlarging the world model from 188M to 430M parameters worsened performance on 4 of 4 suites, so capacity alone does not help. Second, the training objective matters far more: adding an auxiliary supervised contrastive (InfoNCE) loss during world-model warmup substantially improves sleep-phase clustering, giving Normalized Mutual Information at $n=3$ seeds of $0.462 \pm 0.021$ (object), $0.867 \pm 0.025$ (spatial), $0.915 \pm 0.013$ (goal) and $0.754 \pm 0.010$ (LIBERO-10), and beating the strongest published baseline on all 4 suites by a mean $Δ= +0.184$. Across providers ($n=12$) the 95% bootstrap confidence interval for mean pairwise NMI is $[0.683, 0.729]$ (mean $0.705$). The sleep phase also yields the first real-LIBERO task-language library: the decoder uses 2 of 3 admitted abstractions and rewrites all 256 sampled demonstrations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01215v1
- Authors: Riyaaz Shaik, Chandru Venkataraman
- Published: 2026-09-01T13:19:05Z
- Age days: 1

</details>
