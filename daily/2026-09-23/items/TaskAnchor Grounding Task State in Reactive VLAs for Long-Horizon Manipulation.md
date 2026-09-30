---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23580v1"
published: "2026-09-20T11:57:10Z"
age_days: 2
score: 32
created: 2026-09-23
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# TaskAnchor: Grounding Task State in Reactive VLAs for Long-Horizon Manipulation

> [!summary] 先说人话（基于摘要）
> TaskAnchor给反应式VLA补上“任务已经做到哪一步”的线索。它用历史修正当前视觉表示，再用一个表示执行阶段的标量减少长程任务中的动作混淆。

## 问题

长程操作中，相似当前画面可能因过去经历或任务阶段不同而需要不同动作；只看当前输入的反应式策略会发生任务状态混淆。

## 创新点或方法

轻量适配器结合历史条件视觉细化和里程碑监督的任务阶段坐标，分别经原生视觉与语言接口注入预训练VLA，不增加显式规划器，也不修改动作生成机制。

## 证据

RMBench平均成功率约为已发表π₀.₅和X-VLA基线的4.9–5.5倍；RoboMemArena与真实机器人也有一致提升。π₀.₅每个动作块增加2.08毫秒延迟。

## 局限

倍数提升没有对应绝对成功率，需核查基线是否很低；还需确认里程碑监督的成本，以及标量阶段如何表达分支或回退。

- **判断**：值得精读并考虑复现，重点核对绝对成功率和任务阶段监督要求。

## 研究关联

为长程VLA提供较小的结构改造，也方便研究者把历史理解不足与动作生成不足分开分析。

- **概念**：智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/TaskAnchor Grounding Task State in Reactive VLAs for Long-Horizon Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reactive vision--language--action (VLA) models struggle with long-horizon manipulation when visually similar observations can correspond to different actions depending on the task stage or interaction history. We refer to this ambiguity as task-state aliasing and introduce TaskAnchor, a lightweight adapter that grounds pretrained VLAs in execution history. TaskAnchor combines history-conditioned visual refinement with a milestone-supervised task-state coordinate, a scalar representing the semantic stage of execution. These signals are injected through the native visual and language interfaces, respectively, without introducing an explicit planner or modifying the action-generation mechanism. On RMBench, TaskAnchor achieves approximately 4.9--5.5$\times$ the average success rates of the published $π_{0.5}$ and X-VLA baselines, with consistent gains on RoboMemArena and real robots. The added latency is only 2.08\,ms per action chunk for $π_{0.5}$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23580v1
- Authors: Hengyan Liu, Wenlve Zhou, Bo Yue, Yongyi Su, Ruixiang Wang, Zhanqi Zhang, Dekun Lu, Wei Gao, Xiaofen Xing, Kui Jia
- Published: 2026-09-20T11:57:10Z
- Age days: 2

</details>
