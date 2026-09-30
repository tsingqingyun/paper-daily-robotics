---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03681v1"
published: "2026-09-03T11:17:57Z"
age_days: 3
score: 41
created: 2026-09-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> WISE 不让世界模型在所有状态上无差别“脑补”，而是在交互关键状态启动有限长度、多视角想象，再用候选未来的相对结果监督 VLA。

## 问题

VLA 后训练依赖昂贵示范或不稳定的真实探索；世界模型虽能提供想象数据，但不同执行阶段的想象价值不一，长滚动还会累积预测误差，产生不可信监督。

## 创新点或方法

输入是真实交互上下文与策略候选动作；WISE选择需要想象的状态，执行有界多视角滚动，以进度和完成信号比较候选未来，并据此细化动作。关键差异是同时调度“何时想象”和限制“想多远”，而非全程完整滚动。

## 证据

在 π_0 和 π_0.5、多个操作任务上均获得一致提升；相较全量想象约减少80% GPU计算时间。真实环境评测显示在多种分布偏移下鲁棒性和泛化显著提升，但摘要未给成功率数字。


## 局限

最需核查的是关键状态、可靠视界及进度/完成信号如何定义，以及80%计算节省是否在同等训练预算和效果下比较。

- **判断**：值得精读方法和实验设置；它抓住了“想象调度”这一比单纯提高预测精度更贴近策略学习的关键问题。

## 研究关联

它直接给出世界模型辅助 VLA 后训练的效率方案：研究者可把算力集中在决策敏感阶段，并减少长预测误差污染策略。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/WISE World-model-guided Imagination Scheduling for Efficient Post-training of Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Post-training VLA policies typically rely on supervised fine-tuning with costly expert demonstrations or reinforcement learning with expensive and potentially unstable real-world exploration. World models offer a promising alternative by evaluating candidate behaviors through imagined futures, yet effective post-training requires more than accurate prediction: imagination must be scheduled where it is useful, bounded within reliable horizons, and translated into trustworthy policy supervision. In robotic manipulation, the value of imagination varies substantially across execution stages, while extended rollouts can accumulate prediction errors and introduce unreliable learning signals. We introduce WISE (World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models), a unified framework that coordinates when and how world-model imagination is used during policy refinement. WISE selectively invokes imagination at interaction-relevant states, performs bounded multi-view rollouts, evaluates candidate futures using progress and completion signals, and uses their relative outcomes to refine actions generated from real interaction contexts. Extensive experiments with both $π_0$ and $π_{0.5}$ demonstrate consistent improvements across diverse manipulation tasks while reducing GPU computation time by approximately 80% compared with full imagination. Real-world evaluations further show substantial gains in robustness and generalization under diverse real-world distribution shifts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03681v1
- Authors: Chenhao Zhang, Hanyu Zhao, Hang Cheng, Tengfei Pan, Long Zeng
- Published: 2026-09-03T11:17:57Z
- Age days: 3

</details>
