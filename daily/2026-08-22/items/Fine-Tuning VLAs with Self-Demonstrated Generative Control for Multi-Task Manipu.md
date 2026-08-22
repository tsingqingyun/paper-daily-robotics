---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19490v1"
published: "2026-08-19T23:02:07Z"
age_days: 2
score: 35
created: 2026-08-22
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation

> [!summary] 一句话结论（基于摘要）
> Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data wi…

## 关键点

- **问题**：However, when deployed on new robots, even minor mismatches in hardware configuration relative to pretraining can cause severe performance drops.
- **创新点 / 方法**：In this paper, we propose a self-supervised method that generates online interaction rollouts from the zero-shot VLA as additional training data for finetuning.
- **证据**：Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data with improved sample efficiency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

State-of-the-art vision-language-action (VLA) models such as $π_{0.5}$ exhibit strong semantic understanding, instruction following and task behavior. However, when deployed on new robots, even minor mismatches in hardware configuration relative to pretraining can cause severe performance drops. Finetuning the VLA on in-domain expert data from the new embodiment improves performance on the expert task but leads to a loss in its original instruction following and behavioral priors. In this paper, we propose a self-supervised method that generates online interaction rollouts from the zero-shot VLA as additional training data for finetuning. Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data with improved sample efficiency. We demonstrate the success of our approach across test sets probing generalization on a real ALOHA robot and a new simulation benchmark in RoboTwin. Video results are available at https://self-supervised-control.pages.dev/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19490v1
- Authors: Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem
- Published: 2026-08-19T23:02:07Z
- Age days: 2

</details>
