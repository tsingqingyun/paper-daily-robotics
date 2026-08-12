---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06799v1"
published: "2026-08-07T04:44:16Z"
age_days: 3
score: 27
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Is Forward Prediction Enough? Physical State Grounding for JEPA World Models

> [!summary] 一句话结论（基于摘要）
> Experiments demonstrate that our PSG-JEPA consistently outperforms state-of-the-art latent world-model baselines at all three levels.

## 关键点

- **问题**：Learning structured and control-relevant latent representations remains a key challenge for world models.
- **创新点 / 方法**：We propose PSG-JEPA, a physically grounded JEPA world model that shapes its latent space with two complementary grounding objectives beyond forward prediction: grounding individual latents in robot proprioceptive state, and grounding latent pairs in multi-horizon joint-angle changes.
- **证据**：Experiments demonstrate that our PSG-JEPA consistently outperforms state-of-the-art latent world-model baselines at all three levels.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/Is Forward Prediction Enough Physical State Grounding for JEPA World Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning structured and control-relevant latent representations remains a key challenge
for world models. Recent JEPA-based world models learn action-conditioned predictive
latent dynamics from observation sequences. However, their forward-prediction objectives
do not explicitly enforce reliable identifiability of robot-centric physical state from
individual latents or state changes from latent pairs, which can limit downstream
planning and policy performance. We propose PSG-JEPA, a physically grounded JEPA world
model that shapes its latent space with two complementary grounding objectives beyond
forward prediction: grounding individual latents in robot proprioceptive state, and
grounding latent pairs in multi-horizon joint-angle changes. Both objectives are applied
only during training, leaving the inference architecture and computational cost
unchanged. To comprehensively evaluate PSG-JEPA, we conduct experiments at three levels:
(1) latent identifiability via probing, (2) goal-conditioned planning on frozen latents,
and (3) policy learning in simulation and on a real robot. Experiments demonstrate that
our PSG-JEPA consistently outperforms state-of-the-art latent world-model baselines at
all three levels.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06799v1
- Authors: Haodong Yan, Jiaguan Zhu, Mingyuan Jia, Ruiqing Yin, Junjie He, Zhide Zhong, Junfeng Li, Jinxuan Lu, Hengtao Li, Tianran Zhang, Jiayi Chen, Wenxuan Song, Wen Chen, Yuxiang Gao, Haoang Li
- Published: 2026-08-07T04:44:16Z
- Age days: 3

</details>
