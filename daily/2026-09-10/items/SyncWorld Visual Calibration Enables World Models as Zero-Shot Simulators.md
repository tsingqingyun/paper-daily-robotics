---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09155v1"
published: "2026-09-08T17:59:47Z"
age_days: 1
score: 26
created: 2026-09-10
concepts: ["世界模型"]
---

# SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

> [!summary] 先说人话（基于摘要）
> 同一个动作数值，在不同相机和机器人配置下会产生不同画面。SyncWorld 用一段配对的动作与视频进行视觉校准，让世界模型在上下文中学会当前配置下“动作会怎样改变画面”。

## 问题

策略在世界模型中试跑需要精确的低层动作控制，但环境、视角、位置和形态变化会改变动作的视觉效果，造成混合训练监督冲突与部署泛化脆弱。

## 创新点或方法

动作条件世界模型接收覆盖可控自由度的帧—动作校准片段，建立配置特定的 Action–Visual Mapping；训练时使用校准上下文，没有显式校准时则利用交互历史。

## 证据

摘要报告能够在未见设置中准确模拟动作结果，并通过模拟 rollout 实现无需训练的测试时策略改善。摘要未给出可核查的结果数字。


## 局限

零样本仍可依赖目标设置的校准交互；需核查校准长度、自由度覆盖要求，以及未见设置到底变化了什么。

- **判断**：值得重点读方法和泛化实验，关键判断是视觉校准能在多大变化范围内替代重新训练。

## 研究关联

对世界模型研究者，提供了通过上下文适配动作语义的方向，可用于研究跨设置仿真与策略在线试演。

- **概念**：世界模型
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/SyncWorld Visual Calibration Enables World Models as Zero-Shot Simulators.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09155v1
- Authors: Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
- Published: 2026-09-08T17:59:47Z
- Age days: 1

</details>
