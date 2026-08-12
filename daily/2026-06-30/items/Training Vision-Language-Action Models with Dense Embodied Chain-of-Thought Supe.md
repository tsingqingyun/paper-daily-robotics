---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.30552v1"
published: "2026-06-29T16:48:48Z"
age_days: 0
score: 54
created: 2026-06-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision

> [!summary] 一句话结论（基于摘要）
> Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM).

## 关键点

- **问题**：Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms.
- **创新点 / 方法**：Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms.

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：54
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-30/Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supe.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Cross-embodiment transfer in vision-language-action (VLA) models remains challenging
because low-level state and action spaces differ fundamentally across robot platforms.
We observe that the high-level cognitive process underlying manipulation, including
scene perception, object identification, task planning, and sub-task decomposition, is
largely shared across embodiments. Based on this observation, we present ZR-0, a 2.6
billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT)
supervision to align cross-embodiment representations within the vision-language model
(VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System 2) generates
structured ECoT reasoning during training, while a Diffusion Transformer-based action
expert (System 1) produces continuous action chunks via flow matching. The two
components are coupled through cross-attention, with an attention mask that restricts
the action expert to input prompt features only, enabling ECoT generation to be entirely
skipped at inference without any performance loss. ZR-0 is pre-trained on
ProcCorpus-60M, a large-scale dataset comprising approximately 60 million frames
(approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations
covering 96.8% of all frames. We evaluate ZR-0 on three simulation benchmarks spanning
single-arm (LIBERO), bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop)
embodiments, as well as real-world experiments on the xArm platform, demonstrating
strong performance across all settings. Code and model checkpoints are available at
https://github.com/RUCKBReasoning/ZR-0.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.30552v1
- Authors: Haoyang Li, Guanlin Li, Youhe Feng, Chen Zhao, Zhuoran Wang, Yang Li, Qizhe Wei, Shifeng Bao, Haitao Shen, Yihan Zhao, Tong Yang, Jing Zhang
- Published: 2026-06-29T16:48:48Z
- Age days: 0

</details>
