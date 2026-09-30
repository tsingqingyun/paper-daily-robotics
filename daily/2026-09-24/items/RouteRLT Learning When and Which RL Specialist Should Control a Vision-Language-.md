---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26467v1"
published: "2026-09-22T14:15:28Z"
age_days: 1
score: 37
created: 2026-09-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy

> [!summary] 先说人话（基于摘要）
> RouteRLT 学习让通用 VLA 在精密阶段把控制权交给合适的 RL 专家，并处理切换抖动和动作块衔接。它重点解决的是何时接管、由谁接管。

## 问题

连接器插入和线缆操作的接触阶段需要高精度，而通用 VLA 容易在这些阶段失败。直接用 RL 改造预训练策略，还面临如何保留通用行为、选择专门控制器的问题。

## 创新点或方法

阶段选择器决定当前控制器，稳定器抑制短暂切换，动作边界管理器处理分块动作输出之间的交接。每个 RL 专家针对一个精密阶段训练，路由器负责将其与通用 VLA 组合。

## 证据

评测包括 LIBERO 多物体拾放和真实线缆拾取、端口插入。仿真中的学习路由优于基础 VLA，并达到使用特权阶段边界的路由表现；真实实验在操作者对齐的交接协议下验证了两类专家的自动路由。摘要未给出结果数字。

## 局限

真实实验依赖操作者对齐的交接协议，需核查该协议包含多少人工参与，以及它对自动路由结论的边界。

- **判断**：值得细读路由和动作交接实现，尤其适合已有通用策略、只想补强少数精密阶段的研究。

## 研究关联

对 VLA 与机器人学习研究者，它提供了保留通用策略、局部引入 RL 精度的模块化路径，切换边界处理也直接关系到闭环执行可靠性。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/RouteRLT Learning When and Which RL Specialist Should Control a Vision-Language-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models provide broad manipulation competence, but often struggle during the precision-critical stages that dominate contact-rich industrial tasks such as connector insertion and cable management. A common remedy is to refine a pretrained VLA with reinforcement learning (RL), enabling task-specific improvement beyond behavior cloning. However, how to preserve its generalist behavior while deciding when RL refinement is needed and which specialized policy should act remains an open question. In this work, we present RouteRLT, a routing framework that learns when and which RL specialist, an RL policy trained for a single precision-critical phase, should take control from a generalist VLA. A phase selector identifies the active controller, a stabilizer suppresses transient switches, and an action-boundary manager handles transitions between chunked policy outputs. We evaluate RouteRLT on multi-object pick-and-place tasks in LIBERO, as well as on a real-world cable pickup and port-insertion task with multiple precision-critical stages. In simulation, the learned routing improves over the base VLA and matches routing with privileged phase boundaries, without accessing those boundaries at deployment. The real-robot evaluation validates automatic routing to both the pickup and insertion specialists under an operator-aligned handoff protocol. Altogether, these results show that learned routing applies RL specialist control where precise adaptation is most valuable while preserving generalist VLA behavior, including recovery from failed execution attempts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26467v1
- Authors: Chongyu Zhu, Jaden Hinds, Hyegang Kim, Juan Sebastian Rojas, Ramy Elmallah, Chi-Guhn Lee
- Published: 2026-09-22T14:15:28Z
- Age days: 1

</details>
