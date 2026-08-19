---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16195v1"
published: "2026-08-17T07:19:09Z"
age_days: 1
score: 30
created: 2026-08-19
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing

> [!summary] 一句话结论（基于摘要）
> Under standard regularity and approximate best-response assumptions, we show that the latent formulation induces an equivalent game over the decoder-reachable action manifold, providing an approximate-Nash interpretation of the resulting self-play dynamics.

## 关键点

- **问题**：Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge, particularly in contact-rich and highly dynamic tasks such as boxing.
- **创新点 / 方法**：To instantiate this theoretical formulation, we propose RoboStriker, a hierarchical framework that decouples high-level reasoning from low-level execution.
- **证据**：Under standard regularity and approximate best-response assumptions, we show that the latent formulation induces an equivalent game over the decoder-reachable action manifold, providing an approximate-Nash interpretation of the resulting self-play dynamics.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/RoboStriker Latent-Space Strategic Games for Autonomous Humanoid Boxing.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning offers a principled framework for strategic interaction, its direct application to unstructured raw motor spaces inevitably leads to joint-level physical collapse, preventing the emergence of any viable combat tactics. To resolve this fundamental conflict between strategic exploration and physical feasibility, we formulate the humanoid combat task as a novel two-player latent-space zero-sum Markov game. Under standard regularity and approximate best-response assumptions, we show that the latent formulation induces an equivalent game over the decoder-reachable action manifold, providing an approximate-Nash interpretation of the resulting self-play dynamics. To instantiate this theoretical formulation, we propose RoboStriker, a hierarchical framework that decouples high-level reasoning from low-level execution. It first distills the tracking expertise of predefined boxing motions into a topologically bounded latent manifold. This structured latent foundation subsequently drives multi-agent co-evolution via Latent-Space Neural Fictitious Self-Play. Extensive experimental results demonstrate that gaming within this structured latent space substantially outperforms direct exploration. By constraining strategic exploration through a pretrained motion decoder, RoboStriker substantially reduces the catastrophic balance failures observed in raw action-space methods and achieves superior tactical performance in both competitive win rates and striking efficiency. Finally, we successfully deploy and validate our learned combat policies on real-world humanoid robots. Our code and video and supplementary materials are available at RoboStriker.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16195v1
- Authors: Kangning Yin, Kaige Liu, Zhe Cao, Wentao Dong, Weishuai Zeng, Tianyi Zhang, Qiang Zhang, Jingbo Wang, Jiangmiao Pang, Yang Li, Ming Zhou, Weinan Zhang
- Published: 2026-08-17T07:19:09Z
- Age days: 1

</details>
