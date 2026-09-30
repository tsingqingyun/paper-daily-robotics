---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03565"
published: "Sat, 05 Sep 2026 00:00:00 -0400"
age_days: 0
score: 25
created: 2026-09-06
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning

> [!summary] 先说人话（基于摘要）
> 该文让 JEPA 不只预测潜变量，还通过逆动力学和状态对齐保留动作及物理状态信息，从而服务视觉目标条件下的机器人规划。核心方法是同时加入 IDM 与 SA。

## 问题

任务是根据视觉目标在潜空间中规划动作；瓶颈在于潜变量预测本身并不保证编码控制所需的物理信息，甚至可能坍缩。仅用逆动力学虽能使转移携带动作信息，但摘要显示仍不如再加入状态对齐稳定。

## 创新点或方法

输入连续观测、动作及对应物理状态，输出可用于目标规划的潜在转移。IDM 约束潜变量能够反推出产生转移的动作，SA 则把相邻表征对齐到相关物理配置和运动；区别于只做潜预测或仅加 IDM，它显式赋予表征物理落点。

## 证据

四项基准中，TwoRoom、PushT 和 OGBench-Cube 成功率分别为 100%、98% 和 87%，Reacher 与 LeWorldModel 相当。消融显示 SA 在四项任务上均优于仅用 IDM；模型的有效转移维度也高于 LeWorldModel，但后者在 OGBench-Cube 的平均 straightening 指标更高。


## 局限

最需核查的是 SA 在训练或部署时具体需要哪些状态信息，以及这种监督在状态难以获得的真实机器人上是否仍可用；摘要没有说明。

- **判断**：值得精读方法、消融与转移子空间分析，因为它不仅报出强成功率，还对“为什么潜表征更适合控制”给出了可验证解释。

## 研究关联

对世界模型和具身智能研究者，价值在于给出一个可直接检验的表征设计：无需重建未来像素，也能借助物理状态监督提升规划。它还提示评测不能只看预测质量，应同时检查闭环成功率和潜在转移结构。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-06/Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planni.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03565v1 Announce Type: cross Abstract: Action-conditioned JEPA world models enable planning toward visually specified goals without reconstructing future pixels, yet latent prediction alone does not explicitly encourage the learned representations to retain information relevant to robotic control. We introduce an end-to-end JEPA world model that augments latent prediction with inverse dynamics (IDM) and state alignment (SA). While inverse dynamics discourages latent collapse and makes latent transitions informative of the actions that produced them, state alignment grounds consecutive representations in their associated physical configuration and motion. Across four benchmark tasks, our model attains the highest success rates on TwoRoom (100%), PushT (98%), and OGBench-Cube (87%), while performing comparably to LeWorldModel on Reacher. Our ablation further shows that adding state alignment consistently improves planning success over IDM alone across all four tasks. Although LeWorldModel, our primary baseline, attains higher average straightening on OGBench-Cube, transition-subspace analysis shows that its transition energy is concentrated in a substantially lower-dimensional subspace. Our state-aligned model exhibits a higher effective transition dimension than LeWorldModel and improves planning over IDM alone, supporting state alignment as an effective complement to inverse dynamics for robotic planning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03565
- Authors: Muyuan Liu (GENISOM AI, Beijing, China), Yue Huang (GENISOM AI, Beijing, China), Zheng Liang (GENISOM AI, Beijing, China), Xiang Gao (GENISOM AI, Beijing, China)
- Published: Sat, 05 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
