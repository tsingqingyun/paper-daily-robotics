---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26545v1"
published: "2026-08-27T02:36:21Z"
age_days: 2
score: 26
created: 2026-08-30
concepts: ["机器人学习", "具身智能评测与基准"]
---

# Memory Anchors for Continual Robot Learning

> [!summary] 先说人话（基于摘要）
> Memory Anchors发现持续学习中并非所有旧数据同等重要：当新旧任务观测表征重叠、但所需动作冲突时，那一小撮旧经验最能阻止灾难性遗忘。

## 这篇到底在做什么

- **卡在哪里**：随机回放旧数据会浪费有限缓冲区，却不知道哪些经验真正保护旧技能。高风险区域是相似物体或观测在新任务中要求不同动作，表征坍缩会导致旧动作知识被覆盖。
- **关键解法**：在新旧任务表征接近但动作冲突的区域识别 Memory Anchors，并在回放采样中富集这些旧经验。区别于从全部历史均匀或随机回放，它按表征冲突定位关键保护样本。
- **拿什么证明**：仅排除 10% Memory Anchors，就使 LIBERO 套件上的灾难性遗忘增加超过 4.5 倍；富集锚点可使高冲突任务遗忘下降 63%，并在真机上成功持续学习两个任务序列。

## 值不值得读

- **和你的研究有什么关系**：对机器人持续学习者，这是可直接改善回放效率的数据选择原则，也给出了分析任务冲突发生在何处的表征诊断工具。
- **先别急着信**：需核查锚点识别是否依赖保存全部旧数据、任务标签或动作可比性，以及在长任务序列中的计算和存储扩展性。
- **判断**：值得精读定义和采样算法；结果具体、机制直观，是今天较扎实的机器人学习工作。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Memory Anchors for Continual Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot policies deployed in the wild should have the capability to continually learn new tasks without forgetting existing behaviors. A common approach to combat such catastrophic forgetting is to train on new task data with a replay buffer of previously learned task data. Although this buffer is commonly sampled randomly from all prior experiences, we show that a small set of these experiences contributes greatly in anchoring past performance. We call these experiences Memory Anchors. We identify Memory Anchors in regions where representations of new-task observations collapse onto those of old-task observations even though the tasks require conflicting actions, like when a familiar object must be manipulated in a new way. Rehearsing old data in this region plays a key role in preventing destructive overwriting of past task knowledge, serving as this critical Memory Anchor role. Excluding only 10% Memory Anchors before sampling the buffer leads to more than a 4.5x increase in catastrophic forgetting on the LIBERO benchmark suites. Conversely, enriching the replay buffer with Memory Anchors can decrease high-conflict task forgetting by 63% and enables successful continual learning of two task sequences on a real robot. Videos and additional visualizations can be found at https://robot-adaptation.github.io/MemoryAnchors

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26545v1
- Authors: Maximilian Du, Zhanyi Sun, Chen Xu, Paarth Shah, Masha Itkina, Shuran Song
- Published: 2026-08-27T02:36:21Z
- Age days: 2

</details>
