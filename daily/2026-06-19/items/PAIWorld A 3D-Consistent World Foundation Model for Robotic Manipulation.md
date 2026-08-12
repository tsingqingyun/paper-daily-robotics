---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18375v1"
published: "2026-06-16T18:23:23Z"
age_days: 2
score: 33
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Built upon a DiT-based world foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on the AgiBot-Challenge2026 leaderboard, while enabling downstrea…

## 关键点

- **问题**：World foundation models (WFMs) are powerful simulators, yet they predominantly operate in a single-view setting and lack the multi-view 3D consistency required for robotic manipulation.
- **创新点 / 方法**：To address this, we present PAIWorld, a framework that augments diffusion-transformer world models via three core components: (1) Geometry-Aware Cross- View Attention blocks that establish an explicit pathway across views, (2) Geometric Rotary Position Embedding that encodes camera ray directions and extrinsic poses i…
- **证据**：Built upon a DiT-based world foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on the AgiBot-Challenge2026 leaderboard, while enabling downstream applications such as model-based planning, world action mo…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World foundation models (WFMs) are powerful simulators, yet they predominantly operate
in a single-view setting and lack the multi-view 3D consistency required for robotic
manipulation. While robotic systems rely on multiple cameras (egocentric, eye-to-hand,
and wrist-mounted) for policy learning, current multi-view world models simply
concatenate view tokens without explicit geometric reasoning. This causes cross-view
object drift, depth inconsistency, and texture misalignment. We trace these failures to
two deficiencies: the absence of an explicit inter-view communication mechanism and the
lack of a 3D geometric prior. We argue that resolving both simultaneously is necessary
and sufficient. To address this, we present PAIWorld, a framework that augments
diffusion-transformer world models via three core components: (1) Geometry-Aware Cross-
View Attention blocks that establish an explicit pathway across views, (2) Geometric
Rotary Position Embedding that encodes camera ray directions and extrinsic poses into
the attention mechanism, and (3) Latent 3D-REPA, which distills 3D-aware features from
frozen 3D foundation models to ensure 3D consistency. Built upon a DiT-based world
foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on
robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on
the AgiBot-Challenge2026 leaderboard, while enabling downstream applications such as
model-based planning, world action models, and multi-view policy post-training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18375v1
- Authors: Yuhang Huang, Xuan Lv, Junyan Xu, Zhiyuan Yu, Jiazhao Zhang, Ruizhen Hu, Wancheng Feng, Shilong Zou, Hewen Xiao, Ziqiao Zhou, Kaiyun Huang, Zhiyu Peng, Juzhan Xu, Hang Zhao, Chenyang Zhu, Renjiao Yi, Yifei Huang, Douhui Wu, Yan Zhang, Kexu Cheng, Chunhe Song, Yunzhi Xue, Xiuhong Zhang, Leitao Guo, Yunji Chen, Bin Wu, Haibin Yu, Kai Xu
- Published: 2026-06-16T18:23:23Z
- Age days: 2

</details>
