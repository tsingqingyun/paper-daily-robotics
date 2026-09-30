---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19977v1"
published: "2026-08-20T12:50:18Z"
age_days: 3
score: 23
created: 2026-08-23
concepts: ["机器人学习"]
---

# Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space

> [!summary] 一句话结论（基于摘要）
> Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate.

## 问题

Although legged animals are capable of performing explosive motions while traversing confined spaces, replicating this behavior in quadrupedal robots has been a longstanding challenge.

## 创新点或方法

Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate.

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：机器人学习
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-23/Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrai.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Although legged animals are capable of performing explosive motions while traversing confined spaces, replicating this behavior in quadrupedal robots has been a longstanding challenge. Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate. The imitation learning technique is used to train the low-level policy, which mimics the behaviors of real animals and forms a set of diverse skills. The high-level controller, having an awareness of the capability of low-level skills and acquiring the gate information via vision-based detection, determines the suitable maneuvers with collision-free trajectories to traverse it dynamically. Notably, we also verify that this framework can be extended to other highly dynamic tasks. This is one of the first works that perform autonomous and agile aerial gate traversal tasks on ground-walking robots, extending the lifelike agility of legged robots to match that of their biological counterparts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19977v1
- Authors: Zeren Luo, Jiahui Zhang, Yimin Han, Ji Ma, Minghao Lu, Ioannis Havoutis, Peng Lu
- Published: 2026-08-20T12:50:18Z
- Age days: 3

</details>
