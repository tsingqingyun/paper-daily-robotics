---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15065v1"
published: "2026-07-16T14:37:43Z"
age_days: 1
score: 32
created: 2026-07-18
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# DriftWorld: Fast World Modeling through Drifting

> [!summary] 一句话结论（基于摘要）
> By producing rollouts that are both accurate and fast, DriftWorld achieves state-of-the-art decision-making performance with far less inference time than diffusion-based world model baselines.

## 关键点

- **问题**：This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time.
- **创新点 / 方法**：We introduce DriftWorld, an action-conditioned world model based on drifting generative models.
- **证据**：By producing rollouts that are both accurate and fast, DriftWorld achieves state-of-the-art decision-making performance with far less inference time than diffusion-based world model baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/DriftWorld Fast World Modeling through Drifting.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Predictive world models enable robots to plan by imagining the outcomes of their
actions, but their value for control hinges on generating many rollouts quickly. This
creates a bottleneck for diffusion-based world models: multistep sampling makes each
rollout expensive, limiting large-scale action search at inference time. We introduce
DriftWorld, an action-conditioned world model based on drifting generative models.
Rather than denoising iteratively at inference, DriftWorld learns an action-conditioned
drift during training, allowing it to generate future frames from the current
observation and a candidate action sequence in a single forward pass at 30+ fps, which
is 17x faster on average than diffusion based baselines. We evaluate DriftWorld on
standard vision-based robotic manipulation benchmarks, including Bridge-V2, RT-1,
Language Table, Push-T, and Robomimic. By producing rollouts that are both accurate and
fast, DriftWorld achieves state-of-the-art decision-making performance with far less
inference time than diffusion-based world model baselines. Beyond online control,
DriftWorld can also serve as an offline simulator for ranking real-world robot policies,
with rollout-based scores correlating with ground truth at up to 0.99. These results
show that drifting models are a strong fit for robot world modeling, where fast, high-
quality imagination directly supports planning and policy evaluation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15065v1
- Authors: Susie Lu, Haonan Chen, Weirui Ye, Yilun Du
- Published: 2026-07-16T14:37:43Z
- Age days: 1

</details>
