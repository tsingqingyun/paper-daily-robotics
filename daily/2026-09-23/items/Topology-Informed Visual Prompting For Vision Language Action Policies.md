---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23944v1"
published: "2026-09-20T23:39:39Z"
age_days: 2
score: 38
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Topology-Informed Visual Prompting For Vision Language Action Policies

> [!summary] 先说人话（基于摘要）
> 这项拓扑视觉提示方法帮助VLA分清“看起来相似、却必须走不同路线”的状态。它先用仿真几何构造正确路线的示范，再把预测的末端路点画到实时图像上引导动作。

## 问题

复杂障碍和部分可观测性会让相似图像或机器人构型对应不同动作；完整几何规划器能区分这些状态，但部署时通常没有完整环境信息。

## 创新点或方法

以Gauss-Linking-Integral表示拓扑签名，用仿真特权几何生成到达示范签名后继续执行的轨迹；微调VLM从相机观测预测签名和末端路点，渲染为视觉提示供VLA使用。

## 证据

在3项仿真双臂任务及真实搬箱任务上，优于仅用正常示范微调的VLA和可能丢失拓扑信息的VLM提示基线；硬件任务成功率比最强基线高40%，摘要未明确是否为百分点。

## 局限

依赖环境的仿真近似与特权几何生成训练数据，需核查近似误差和视觉签名预测错误的影响。

- **判断**：做障碍约束操作值得读方法，重点审查拓扑签名是否比普通路点提示提供独立收益。

## 研究关联

对VLA与机器人规划，价值是把几何规划中的路径结构知识转换为策略可读取的视觉提示。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Topology-Informed Visual Prompting For Vision Language Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies can struggle with manipulation tasks with complex obstacle geometries due to partial observability. These complex geometries can lead to similar visual observations or robot configurations requiring qualitatively different actions, a distinction that can be quantified using topological signatures. While motion planners with full knowledge of environment geometries and object states can reason about these signatures in planning, this information is often not known at deployment. To address this issue, we present a topology-guided visual-prompting framework that uses simulation-based planning to augment a nominal demonstration dataset and provides vision-based guidance at deployment. Our method uses a Gauss-Linking-Integral topological signature representation to capture important topological properties of the environment. Using privileged geometry information from a simulation approximation of our environment, we augment a VLA fine-tuning dataset with trajectories that move the system to a demonstrated signature and, from the new configuration, resume task execution. A vision-language model (VLM) is fine-tuned on the same dataset to both predict signatures from live camera observations and predict end-effector waypoints, which are rendered as visual prompts on the observations to guide the VLA. Across three simulated bimanual tasks and a real-world box pickup task, our method outperforms a VLA fine-tuned only on nominal demonstrations and a VLM-prompting baseline that can remove topology-relevant information from observations. On hardware, it exceeds the strongest baseline by 40% in task success. Project website: https://topology-vla.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23944v1
- Authors: Haoyang Wu, Abhinav Kumar, Dmitry Berenson
- Published: 2026-09-20T23:39:39Z
- Age days: 2

</details>
