---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24042v1"
published: "2026-08-25T04:04:49Z"
age_days: 2
score: 42
created: 2026-08-27
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> HSR 不按整任务或表面视觉相似度检索示范，而是先把目标任务分解成可靠的技能序列，再结合子任务语言检索和行为特征重排，为小样本 VLA 适配挑数据。

## 这篇到底在做什么

- **卡在哪里**：新任务示范有限时，VLA微调容易退化；整任务匹配很少见，而视觉、状态动作或任务级语言检索会忽略长时程任务中可复用的局部技能。
- **关键解法**：先生成候选技能序列，以语义合理性和历史数据中的技能可靠性选计划；随后用子任务语言召回、行为特征重排筛示范，最后通过通用技能预训练与任务微调两阶段适配策略。
- **拿什么证明**：在LIBERO和若干真实机器人任务上，相对最强基线的平均成功率分别提升10.3和21.3个百分点。

## 值不值得读

- **和你的研究有什么关系**：它为机器人数据复用提供了比整轨迹检索更细的单位，适合长时程任务、小样本适配和技能库式Agent。
- **先别急着信**：摘要没有说明技能分解来源、额外示范数量及检索开销；若分解器依赖强先验，数据效率结论需重新衡量。
- **判断**：值得读到实现细节和检索消融，特别适合做数据治理与小样本VLA的人。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While Vision-Language-Action (VLA) models pretrained on large-scale robot datasets provide a strong foundation for robot manipulation, their performance can degrade when adapted to new tasks with limited task-specific demonstrations. Retrieval offers a practical way to reuse existing demonstrations for data-efficient adaptation, but existing methods often rely on visual similarity, state-action representations, or task-level language matching. These approaches may overlook the hierarchical structure of long-horizon manipulation tasks, where complete task matches are rare but reusable skills are often abundant. To address this challenge, we propose Hierarchical Skill Retrieval (HSR), a retrieval framework for data-efficient VLA adaptation. Specifically, HSR first decomposes a target task into candidate skill sequences. It evaluates each plan based on both semantic plausibility and skill reliability estimated from the prior dataset. The selected decomposition is then used for hybrid retrieval. This combines subtask-level language retrieval with behavior-feature reranking to identify demonstrations that are both semantically relevant and compatible with the target task. Finally, we adapt the policy through a two-stage pretraining and finetuning pipeline, which separates general skill acquisition from task-specific adaptation. Experiments on the LIBERO benchmark and several real-world robot manipulation tasks show that HSR improves the average success rate by 10.3% and 21.3% over the strongest baseline, respectively. These results demonstrate the effectiveness of structured skill-level retrieval for data-efficient VLA adaptation. Videos and code are available at https://hoar012.github.io/HSR-Project.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24042v1
- Authors: Haoran Hao, Shahram Najam Syed, Jeff Schneider, Jeffrey Ichnowski
- Published: 2026-08-25T04:04:49Z
- Age days: 2

</details>
