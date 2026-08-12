---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2604.28192v3"
published: "2026-04-30T17:59:52Z"
age_days: 
score: 41
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning

> [!summary] 一句话结论（基于摘要）
> Experiments show that LaST-R1 achieves a near-perfect 99.9% average success rate on the LIBERO benchmark with only one-shot supervised warm-up, significantly improving convergence speed and performance over prior state-of-the-art (SOTA) methods.

## 关键点

- **问题**：While recent studies on latent-reasoning Vision-Language-Action (VLA) models have demonstrated the capability to capture fine- grained physical dynamics, they remain predominantly confined to static imitation learning, severely limiting their adaptability and generalization.
- **创新点 / 方法**：In this paper, we present LaST-R1, a novel reinforcement learning (RL) post-training framework designed to effectively harness "latent reasoning-before-acting" policies.
- **证据**：Experiments show that LaST-R1 achieves a near-perfect 99.9% average success rate on the LIBERO benchmark with only one-shot supervised warm-up, significantly improving convergence speed and performance over prior state-of-the-art (SOTA) methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/LaST-R1 Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic foundation models require reasoning over complex visual scenes to execute
adaptive actions in dynamic environments. While recent studies on latent-reasoning
Vision-Language-Action (VLA) models have demonstrated the capability to capture fine-
grained physical dynamics, they remain predominantly confined to static imitation
learning, severely limiting their adaptability and generalization. In this paper, we
present LaST-R1, a novel reinforcement learning (RL) post-training framework designed to
effectively harness "latent reasoning-before-acting" policies. Specifically, we propose
Latent-to-Action Policy Optimization (LAPO), a core RL algorithm that jointly optimizes
the latent reasoning process and the action generation. By explicitly embedding latent
Chain-of-Thought (CoT) reasoning directly within the RL optimization loop, LAPO
stimulates profound physical world modeling, which in turn drives robust execution in
interactive environments. Furthermore, an adaptive latent CoT mechanism is introduced,
allowing the policy to dynamically modulate its reasoning horizon based on diverse
environment states. Experiments show that LaST-R1 achieves a near-perfect 99.9% average
success rate on the LIBERO benchmark with only one-shot supervised warm-up,
significantly improving convergence speed and performance over prior state-of-the-art
(SOTA) methods. In real-world deployments, LaST-R1 yields up to a 22.5% average
improvement over SOTA supervised fine-tuning approach across four complex tasks,
including both single-arm and dual-arm settings. Finally, LaST-R1 demonstrates strong
generalization across simulated and real-world environments.

### 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2604.28192v3
- Authors: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Shanghang Zhang, Pheng-Ann Heng
- Published: 2026-04-30T17:59:52Z
- Age days: 

</details>
