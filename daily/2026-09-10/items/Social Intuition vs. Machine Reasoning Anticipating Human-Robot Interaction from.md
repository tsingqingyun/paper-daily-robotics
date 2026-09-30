---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07394v1"
published: "2026-09-07T12:06:48Z"
age_days: 2
score: 24
created: 2026-09-10
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Social Intuition vs. Machine Reasoning: Anticipating Human-Robot Interaction from multiple modalities

> [!summary] 先说人话（基于摘要）
> 这项研究测试机器人能否提前看出一个人要来互动。人类从完整视频中获得的帮助明显超过当前 VLM，而更大的模型也未必预测得更好。

## 问题

服务机器人需要从自身视角判断人的互动意图，这依赖姿态及场景等多种线索；研究比较轻量姿态模型、VLM 与人类能利用多少信息。

## 创新点或方法

在固定测试轨迹上比较仅姿态输入与带目标框的完整第一视角视频，并评测不同大小和输入条件的 VLM。

## 证据

HUI360 试点子集包含 100 条轨迹，其中 25 正例、75 负例。仅姿态条件下人类 F1 高于轻量模型约 0.08，完整视频条件下高于 VLM 约 0.2；最佳结果不随模型规模一致变化。


## 局限

只有 100 条固定试点轨迹；此外，人类领先不能单独证明推理能力是必要条件，摘要的这一解释需要更强证据。

- **判断**：值得读输入协议与错误案例，但将其作为小规模诊断证据更合适，不宜据此建立稳定模型排名。

## 研究关联

对多模态与具身评测研究者，可用于检验社会意图理解是否超出一般视觉描述能力，也提醒选型时直接测任务而非依赖参数规模。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/Social Intuition vs. Machine Reasoning Anticipating Human-Robot Interaction from.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Anticipating whether a person will interact from one's own perspective is a highly intuitive task for humans, that relies on a combination of cues. We investigate how humans perform at predicting a person's intention to interact from a service robot's point of view, using pose-only or full video input, then benchmark different lightweight pose-based models and state-of-the-art vision-language models. We conducted our benchmark on the HUI360 dataset on a fixed pilot subset of 100 test tracks (25 positive, 75 negative). We found that with pose-only input, human annotators outperform lightweight trained pose models but not by large margins (+0.08 in F1-Score). But when given full egocentric video with a target bounding box, human annotators perform substantially better and largely outperform the Vision-Language Models (+0.2 in F1-Score). We also compared VLMs of different size and under different input conditions, and found that the best results do not correlate with model size. Our result confirms that predicting interactions is a challenging task for social robots and that reasoning-capable models are necessary but their actual reasoning capabilities alone do not suffice to match the social intuition of humans.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07394v1
- Authors: Raphael Lorenzo-Louis, Bertrand Luvison, Serena Ivaldi
- Published: 2026-09-07T12:06:48Z
- Age days: 2

</details>
