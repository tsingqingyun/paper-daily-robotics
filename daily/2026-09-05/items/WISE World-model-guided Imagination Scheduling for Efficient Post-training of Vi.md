---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03681"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 41
created: 2026-09-05
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> WISE 的关键不是让世界模型无限想象，而是决定何时值得想、最多想多远，以及如何把候选未来转成 VLA 的可靠监督。它通过选择关键状态、有限多视角 rollout 和相对结果比较来做高效后训练。

## 这篇到底在做什么

- **卡在哪里**：专家示范昂贵，真实环境强化学习又成本高且不稳定；直接使用世界模型长程推演还会累积误差。真正瓶颈是不同执行阶段的想象价值不同，未经调度的想象既浪费算力又可能制造错误学习信号。
- **关键解法**：WISE 从真实交互上下文产生动作，在交互相关状态才调用世界模型，执行有界的多视角 rollout，以进度和完成信号评价候选未来，再依据相对优劣细化动作。与全程、长跨度想象相比，它显式控制调用时机和可信时域。
- **拿什么证明**：在 π0 与 π0.5、多种操作任务上均获一致提升；相比全量想象，GPU 计算时间约减少80%。真实环境测试显示面对多种分布偏移时鲁棒性和泛化明显提升，但摘要未给成功率数字。

## 值不值得读

- **和你的研究有什么关系**：对用世界模型后训练 VLA 的研究者，WISE 提供了比“提高视频预测精度”更直接的切入点：把有限模型容量和算力集中到决策敏感阶段。
- **先别急着信**：需要全文核查关键状态、可靠时域、进度与完成信号如何定义，以及80%节省是在何种统一设置下测得。
- **判断**：值得精读，尤其适合正在做 VLA 后训练或想象式规划的人；核心价值在调度机制，而非单纯扩大世界模型。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/WISE World-model-guided Imagination Scheduling for Efficient Post-training of Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03681v1 Announce Type: new Abstract: Post-training VLA policies typically rely on supervised fine-tuning with costly expert demonstrations or reinforcement learning with expensive and potentially unstable real-world exploration. World models offer a promising alternative by evaluating candidate behaviors through imagined futures, yet effective post-training requires more than accurate prediction: imagination must be scheduled where it is useful, bounded within reliable horizons, and translated into trustworthy policy supervision. In robotic manipulation, the value of imagination varies substantially across execution stages, while extended rollouts can accumulate prediction errors and introduce unreliable learning signals. We introduce WISE (World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models), a unified framework that coordinates when and how world-model imagination is used during policy refinement. WISE selectively invokes imagination at interaction-relevant states, performs bounded multi-view rollouts, evaluates candidate futures using progress and completion signals, and uses their relative outcomes to refine actions generated from real interaction contexts. Extensive experiments with both $\pi_0$ and $\pi_{0.5}$ demonstrate consistent improvements across diverse manipulation tasks while reducing GPU computation time by approximately 80% compared with full imagination. Real-world evaluations further show substantial gains in robustness and generalization under diverse real-world distribution shifts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03681
- Authors: Chenhao Zhang, Hanyu Zhao, Hang Cheng, Tengfei Pan, Long Zeng
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
