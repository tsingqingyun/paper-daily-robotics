---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27726v1"
published: "2026-08-27T21:33:38Z"
age_days: 3
score: 31
created: 2026-08-31
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Coordinated Motion Planning for Multi-Arm Systems via Iterative LQ Games

> [!summary] 先说人话（基于摘要）
> 该方法把每条机械臂视为独立博弈参与者，通过反复局部线性化动力学和二次近似代价，利用 Riccati 递推求反馈 Nash 策略，实现多臂协同避碰规划。

## 问题

共享空间中的高自由度多臂规划既要协调又要安全；集中式规划扩展性差，分散式方法又容易缺乏鲁棒性和全局碰撞约束，而博弈方法在关节型多臂系统中的应用仍有限。

## 创新点或方法

输入是多机械臂共享的全局状态、动力学、各自目标和碰撞约束，输出各机械臂的反馈轨迹策略。算法围绕名义轨迹迭代求解局部 LQ 博弈，并把自碰撞和臂间碰撞写成可微惩罚纳入优化。

## 证据

摘要称实验在高维场景生成平滑、安全、高效轨迹并超过传统方法，但未列基准、机械臂数量、成功率或规划时间；摘要未给出可核查的结果数字。


## 局限

最需核查实时性、规模扩展曲线以及可微碰撞惩罚是否能提供硬安全保证；摘要仅声称安全，未给约束违反数据。

- **判断**：博弈规划研究者可读方法，其他人先浏览实验；缺少定量结果使其实际优势尚难判断。

## 研究关联

对多机器人具身系统，这是介于集中式与完全分散式之间的协调规划工具；对学习型世界模型或 VLA 的直接价值有限，但可作为多臂底层规划器或安全参考。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Coordinated Motion Planning for Multi-Arm Systems via Iterative LQ Games.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-agent motion planning for high-degree-of-freedom robotics manipulators in shared workspaces remains a fundamental yet challenging problem. Centralized planners often suffer from poor scalability, while decentralized approaches face robustness and safety concerns. Game-theoretic formulations offer a promising approach for modeling agent interactions, potentially overcoming these limitations. However, their application to articulated multi-arm systems remains limited. This paper presents an iterative Linear Quadratic (LQ) game framework for multi-manipulator motion planning, where each manipulator is modeled as an independent agent optimizing its own objective while interacting with other agents based on shared global states and collision constraints. The method solves a series of local LQ games by linearizing the dynamics and approximating the cost around a nominal trajectory, with Riccati backward recursions yielding feedback Nash strategies. To address the challenges of articulated systems, we incorporate differentiable penalties for self-collision and inter-arm collision into the optimization pipeline, enabling coordinated, collision-aware trajectory generation. Experiments demonstrate that our framework produces smooth, safe, and efficient trajectories in high-dimensional settings, outperforming traditional methods. This highlights the effectiveness of differential game formulations for multi-robot manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27726v1
- Authors: Junyoung Kim, Hanwen Ren, Lei Zhang, Ahmed H. Qureshi
- Published: 2026-08-27T21:33:38Z
- Age days: 3

</details>
