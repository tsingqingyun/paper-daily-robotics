---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27371v1"
published: "2026-08-27T17:08:40Z"
age_days: 2
score: 31
created: 2026-08-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Embodied Scene Rearrangement Planning

> [!summary] 先说人话（基于摘要）
> ESRP把家具重排改造成更接近真实部署的长时程任务：智能体只能看第一视角观测，却要对齐俯视目标布局，并处理物体相互遮挡。

## 问题

以往重排任务常给全局状态，回避了现实中局部可见、遮挡严重的问题；真正难点是把不断变化的局部观测对齐全局目标，并规划多物体、长时程移动。

## 创新点或方法

ESRP-Bench基于 OmniGibson构建场景对任务，输入第一视角观测与目标俯视布局，输出家具操作序列。它定义三级指标，并提供分层任务—运动规划、VLM、模仿学习和强化学习四类基线。

## 证据

基准包含超过 5400 对场景和 8200 个物体。实验结论是现有方法难以高效完成任务；摘要未给出基线成功率或各级指标数字。


## 局限

需全文核查任务可解性、仿真感知假设和三级指标是否会奖励部分但无效的重排；摘要没有定量难度分布。

- **判断**：做具身规划或 benchmark 的人值得精读任务定义；方法研究者先看基线失败模式再决定投入。

## 研究关联

对具身 Agent、世界模型和评测研究者，它补上了局部观测到全局布局对齐的大尺度重排测试，可暴露记忆、空间推理与长时程规划的联合短板。

- **概念**：多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Embodied Scene Rearrangement Planning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This paper introduces Embodied Scene Rearrangement Planning (ESRP), a novel task requiring embodied agents to rearrange furniture in 3D scenes to match a target configuration using only egocentric observations and a top-down target layout. Unlike prior rearrangement tasks, ESRP precludes global state access and introduces mutual object occlusions, reflecting the practical constraints of real-world robotic deployment. These factors make aligning partial egocentric observations with the global target layout particularly challenging for long-horizon planning. To facilitate research, we present ESRP-Bench, a comprehensive benchmark built on OmniGibson featuring over 5,400 scene pairs and 8,200 objects. We define three multi-level metrics to evaluate rearrangement quality and provide four baselines: a hierarchical task-and-motion planning method, a vision-language-model-based method, and two learning-based approaches (IL and RL). Experimental results demonstrate that current methods struggle to complete the task efficiently, highlighting ESRP as a challenging frontier for embodied agents in scene understanding and long-horizon task planning. This work serves as a stepping stone toward deploying intelligent agents in real-world scenarios. Project page: https://pie-lab.cn/ESRP/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27371v1
- Authors: Canzhi Chen, Zan Wang, Siqi Zhu, Qi Wu, Yixuan Li, Wei Liang
- Published: 2026-08-27T17:08:40Z
- Age days: 2

</details>
