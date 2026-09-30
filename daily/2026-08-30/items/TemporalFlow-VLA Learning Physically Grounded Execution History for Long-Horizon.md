---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26821v1"
published: "2026-08-27T09:00:56Z"
age_days: 2
score: 32
created: 2026-08-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation

> [!summary] 先说人话（基于摘要）
> TemporalFlow-VLA不直接堆历史帧，而是在训练时用机器人几何构造表面时间流，监督两个时间查询，把有物理含义的执行历史压缩给动作专家。部署时不需要几何计算。

## 问题

多阶段操控中，当前画面相似但历史不同可能要求完全不同的动作；简单追加历史帧不能稳定表示刚发生的物理变化，还会增加编码延迟。

## 创新点或方法

训练输入包括历史图像，以及仅用于监督的机器人状态、几何和标定相机；机器人表面时间流监督两个 execution-aligned temporal queries，后者条件化动作预测。部署只使用学得的时间表示，并用异步特征缓存避免重复历史编码。

## 证据

LIBERO 平均成功率 97.63±0.26%，LIBERO Long 为 96.60±0.87%；12 个 RoboTwin 任务 Clean/Randomized 分别为 85.5%/84.2%。历史干预显示模型同时依赖内容与顺序，缓存后服务端采样延迟与单帧相当。


## 局限

时间监督依赖训练期机器人几何与相机标定；需核查这些资产的获取成本，以及跨本体或标定误差下的迁移。

- **判断**：长时程操控研究者应精读，尤其值得看历史干预与延迟核算，而不只看高成功率。

## 研究关联

对长时程 VLA，这是在不增加部署几何管线的情况下，把物理执行史注入策略的清晰方案；也提供了检验模型是否真正使用历史的干预思路。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/TemporalFlow-VLA Learning Physically Grounded Execution History for Long-Horizon.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models leverage pretrained vision-language representations for robot control, yet simply adding historical frames does not reliably capture recent physical change. This is especially problematic in multi-stage manipulation, where visually similar states may require different actions depending on prior execution. To address this challenge, we present TemporalFlow-VLA, which learns compact execution history through physically grounded temporal supervision. Using recorded robot states, robot geometry, and calibrated cameras, we construct robot-surface temporal flow as a training-only target and supervise two execution-aligned temporal queries that provide structured history to the action expert. The geometric supervision path is not evaluated at deployment. TemporalFlow-VLA achieves 97.63 +/- 0.26% average success on LIBERO, including 96.60 +/- 0.87% on LIBERO Long, and 85.5%/84.2% Clean/Randomized success across 12 RoboTwin tasks. It shows its clearest advantage over prior methods on longer-horizon, multi-stage manipulation. Controlled history interventions show that action prediction depends on both historical content and temporal order. With asynchronous feature caching, temporal conditioning maintains single-frame-level server-side sampling latency without additional historical-encoding overhead. Overall, TemporalFlow-VLA provides a compact, physically grounded interface for exploiting ordered execution history without explicit motion estimation or geometric processing at deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26821v1
- Authors: Jiarui Yang, Yehao Lu, Yuning Su, Yu Zhong, Yufeng Xie, Yazhou Zhang, Haiyu Lan, Kaixiang Lu, Peiwen Lin, Chuang Wang, Junwei Liang, Enyu Li
- Published: 2026-08-27T09:00:56Z
- Age days: 2

</details>
