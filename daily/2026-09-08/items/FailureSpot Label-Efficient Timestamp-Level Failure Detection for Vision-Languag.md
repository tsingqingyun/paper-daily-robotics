---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04277"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 32
created: 2026-09-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# FailureSpot: Label-Efficient Timestamp-Level Failure Detection for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> FailureSpot 希望更准确地找到 VLA 从哪一刻开始出错，同时减少逐时刻人工标注。它先从动作异常构造弱标签，再主动挑选不确定轨迹补标。

## 这篇到底在做什么

- **卡在哪里**：视觉检测往往在错误动作之后才报警；用整条失败轨迹监督内部表征检测器，又会把失败前的正常行为误标成异常。
- **关键解法**：利用未标注动作块中的前后不一致、冻结或闲置、激烈随机运动生成弱监督，再通过主动学习选择最不确定轨迹进行时间戳标注和微调。
- **拿什么证明**：多个 VLA 策略上的实验报告时间戳级与轨迹级故障检测均改善；摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：可为 VLA 监控、恢复触发和 Agent 执行核验提供更精细的故障信号。
- **先别急着信**：需核查标注节省量、误报率和检测提前量；动作形态异常并不必然意味着任务失败。
- **判断**：值得读弱监督构造与检测时序实验，是否实用取决于提前量和误报之间的取舍。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/FailureSpot Label-Efficient Timestamp-Level Failure Detection for Vision-Languag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04277v1 Announce Type: new Abstract: Vision-language-action (VLA) policies have shown strong potential for general-purpose robotic manipulation, but they can still fail unpredictably during long-horizon execution, making reliable failure detection essential for safe deployment. Existing methods either rely on visual models that typically detect failures only after erroneous actions have occurred, or use lightweight proactive detectors trained on VLA internal representations. However, these proactive methods are often supervised with trajectory-level labels, causing normal pre-failure behavior in unsuccessful trajectories to be incorrectly labeled as failure. This supervision mismatch introduces label noise and limits both trajectory-level detection accuracy and precise timestamp-level failure localization. In this work, we study fine-grained timestamp-level VLA failure detection while addressing the cost of dense annotation. We propose a data-efficient framework that first leverages unlabeled VLA action chunks to construct action-derived weak supervision signals, capturing abnormal patterns such as inconsistent consecutive chunks, frozen or idle actions, and aggressive random motions. We then use active learning to select only the most uncertain trajectories for timestamp-level annotation and fine-tune the detector with these informative labels. Experiments across multiple VLA policies show that our method improves both timestamp-level and trajectory-level failure detection performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04277
- Authors: Jie Ma, Zongxi Liu, Yi Zhu
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
