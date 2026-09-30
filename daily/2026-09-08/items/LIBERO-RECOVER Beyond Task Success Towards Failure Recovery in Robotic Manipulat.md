---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.05178"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 43
created: 2026-09-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models

> [!summary] 先说人话（基于摘要）
> LIBERO-Recover 专门测试机器人出错后能否继续完成任务。它从模型实际执行失败中构造场景，将恢复难度从重试动作扩展到修复环境状态。

## 这篇到底在做什么

- **卡在哪里**：从固定初始状态获得高成功率，不能说明机器人能处理抓取失败、碰撞或物体意外移动；现有评测基本没有单独测量恢复能力。
- **关键解法**：基于 LIBERO 构建 1,000 多个场景，覆盖动作重试、动作调整、物体状态恢复和环境恢复四级任务，并评估空间、物体结构、交互及拓扑推理。
- **拿什么证明**：摘要报告 1,000 多个恢复场景，并称现有 LIBERO 最优方法接近 100% 成功率；未给出模型在新基准上的恢复成绩。

## 值不值得读

- **和你的研究有什么关系**：为 VLA 和 WAM 研究者提供部署相关的恢复测试，可检验策略是否只会沿正常流程执行。
- **先别急着信**：需核查失败场景的分布、恢复判定和测试结果；“实际执行失败”不能据此理解为来自真实物理机器人。
- **判断**：值得读基准构造与恢复协议；当前摘要足以支持评测动机，尚不足以判断模型恢复能力差距。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/LIBERO-RECOVER Beyond Task Success Towards Failure Recovery in Robotic Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.05178v1 Announce Type: new Abstract: Vision-Language-Action (VLA) or World Action (WAM) models have recently demonstrated remarkable performance in robotic manipulation. On LIBERO, SOTA method have achieved nearly 100\% success rates, seemingly suggesting that the models are ready for deployment in real world. However, near perfect performance on existing benchmarks can be misleading: success under ideal conditions does not imply real world robustness. Existing benchmarks primarily evaluate task completion from predefined initial states, while real world interactions inevitably involve failures such as failed grasps, collisions, and unintended object movements. A robot must therefore not only execute tasks successfully, but also recognize and recover from failures to continue the task. Yet this capability remains largely unmeasured, revealing a critical gap between benchmark performance and real world reliability. To address this gap, we introduce LIBERO-Recover Benchmark, a large scale benchmark for failure recovery in robotic manipulation. Built upon LIBERO, we collect real execution failures from SOTA embodied models and construct 1,000+ scenarios across four recovery levels: (1) Action Retry, (2) Action Adaptation, (3) Object State Recovery, and (4) Environmental Recovery. We evaluate four core capabilities: spatial understanding, object structure reasoning, interaction understanding, and topological reasoning. As the first large-scale benchmark for embodied failure recovery, LIBERO-Recover shifts evaluation from \emph{Can the robot succeed?''} to \emph{Can the robot recover after failure?''}, promoting robust and generalizable embodied agents. The project will be avaible in \textcolor{blue}{https://liulin815.github.io/LIBERO-Recovery/}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.05178
- Authors: Lin Liu, Zhicheng Bao, Lu Zhang, Ziying Song, Wu Yang, Shuai Tao, Wulong Liu, Huchuan Lu
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
