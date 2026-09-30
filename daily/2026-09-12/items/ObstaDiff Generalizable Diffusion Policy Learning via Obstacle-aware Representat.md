---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10918v1"
published: "2026-09-10T00:06:39Z"
age_days: 2
score: 29
created: 2026-09-12
concepts: ["机器人学习"]
---

# ObstaDiff: Generalizable Diffusion Policy Learning via Obstacle-aware Representations

> [!summary] 先说人话（基于摘要）
> ObstaDiff让模仿学习策略明确区分目标、障碍和背景，从而在杂乱环境中生成更少碰撞的接近轨迹。

## 问题

操作策略常在干净背景假设下学习，缺少显式障碍处理机制，进入存在非结构化障碍的场景后难以泛化。

## 创新点或方法

轻量视觉编码器提取目标—障碍—背景结构化表示，供分解式扩散策略中的对齐策略使用，生成通向目标中心瓶颈位姿的末端轨迹。

## 证据

真实温室实验每种方法61次，共366次执行；ObstaDiff平均任务成功率75.41%，平均障碍碰撞率8.20%，优于所比较的代表性模仿学习基线。


## 局限

需核查障碍类型、任务划分与瓶颈位姿定义；现有证据集中于温室场景，且仍有碰撞。

- **判断**：值得读表示设计与真实失败案例，实机证据具体，但泛化范围需结合实验细节判断。

## 研究关联

对机器人学习研究者，提供了通过视觉表示显式引入避障信息的实机案例，尤其适用于杂乱农业操作。

- **概念**：机器人学习
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/ObstaDiff Generalizable Diffusion Policy Learning via Obstacle-aware Representat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation learning has achieved impressive results in robotic manipulation, yet most existing approaches assume clean backgrounds and lack explicit mechanisms for obstacle-aware motion generation. Extending such policies to cluttered, real-world scenes with unstructured obstacles remains a key generalization challenge. We present ObstaDiff, a decomposed diffusion-policy framework with a lightweight obstacle-aware visual encoder. ObstaDiff extracts a structured target-obstacle-background representation, enabling the downstream alignment policy to generate end-effector trajectories toward a target-centered bottleneck pose while reasoning about surrounding obstacles. We evaluate ObstaDiff on 61 real-robot greenhouse trials per method (366 executions in total). ObstaDiff achieves 75.41% average task success and 8.20% average obstacle collision rate, outperforming representative imitation-learning baselines and improving generalization in cluttered agricultural scenes.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10918v1
- Authors: Jiawen Wang, Kevin Yao, Khalid Jawed
- Published: 2026-09-10T00:06:39Z
- Age days: 2

</details>
