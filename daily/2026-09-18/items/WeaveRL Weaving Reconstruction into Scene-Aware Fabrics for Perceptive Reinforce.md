---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.18685v1"
published: "2026-09-16T14:00:37Z"
age_days: 1
score: 28
created: 2026-09-18
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# WeaveRL: Weaving Reconstruction into Scene-Aware Fabrics for Perceptive Reinforcement Learning

> [!summary] 先说人话（基于摘要）
> WeaveRL让机器人强化学习直接使用传感器重建的三维几何来避障，并把这套重建扩展到数千个并行仿真环境。

## 问题

几何复杂的操作难以训练；基于几何fabrics的避碰控制此前依赖静态人工场景表示，主动在线三维感知难以接入大规模并行强化学习。

## 创新点或方法

GPU加速重建在交互过程中把场景表示为表面元，并将该几何输入场景感知fabrics控制器上的学习策略。关键变化是用传感器得到的几何取代手工指定的几何基元。

## 证据

在碰撞密集操作任务中处理了基元基线失败的复杂场景，并保持仿真到真实迁移；未知障碍下无碰撞任务完成率由35%提高到61%。摘要称发布重建系统、训练代码和测试数据。

## 局限

需核查35%到61%对应的任务与基线，以及重建误差如何影响控制；摘要未量化实机迁移结果。

- **判断**：值得精读并行重建与控制器接口，特别适合复杂障碍操作和感知驱动强化学习方向。

## 研究关联

对机器人学习与Sim2Real，直接价值是缩小训练控制器所用几何与部署感知所得几何之间的差异；核心贡献是感知与控制集成。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/WeaveRL Weaving Reconstruction into Scene-Aware Fabrics for Perceptive Reinforce.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reinforcement learning allows robots to acquire complex skills, but producing policies for geometrically complex manipulation remains difficult. A promising approach is to learn on top of collision-avoidant controllers, such as geometric fabrics. However, these approaches have relied on static, hand-specified representations of the scene. Integrating active, online 3D perception into massively parallel RL training has so far been inaccessible. We introduce a GPU-accelerated method that reconstructs the scene as a collection of surfels across thousands of parallel simulation instances during active rollouts. This lets policies operate over sensor-derived, rather than hand-specified, geometry. On a suite of collision-dense manipulation tasks, our surfel fabrics enable policies to tackle geometrically complex scenes where primitive-based baselines fail, while maintaining sim-to-real transfer. Furthermore, policies learned with a scene-aware fabric are more robust to the introduction of novel geometry at test time, improving collision-free task completion under unseen obstacles from 35% to 61%. We release our reconstruction system, training code and test dataset to spur research in this direction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.18685v1
- Authors: Remo Steiner, Vikram Ramasamy, David Tingdahl, Sam Mady, Karl Van Wyk, Nathan Ratliff, David Recasens Lafuente, Soha Pouya, Tuur Stuyck, Alex Millane
- Published: 2026-09-16T14:00:37Z
- Age days: 1

</details>
