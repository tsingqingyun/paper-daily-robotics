---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.19891v1"
published: "2026-08-20T10:58:45Z"
age_days: 2
score: 37
created: 2026-08-22
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# EXIMO: VLM Guided Exploration of VLA Policies

> [!summary] 一句话结论（基于摘要）
> In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

## 关键点

- **问题**：While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem.
- **创新点 / 方法**：In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies.
- **证据**：In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/EXIMO VLM Guided Exploration of VLA Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours of expensive human labour and the alternative, reinforcement learning (RL), can be notoriously sample-inefficient especially for long-horizon tasks. In addition, RL with VLAs imposes several challenges due to the model's size and architectural design. In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies. EXIMO operates in three stages: explore, imitate, and optimize. During the explore phase, EXIMO equips the VLA with a vision language model (VLM) that acts as a planner. The VLM thinks and breaks down challenging long-horizon problems into shorter ones for the VLA. The VLM, together with the VLA, is used to collect an orchestrated dataset on new tasks. During the imitate phase, the VLA is finetuned with the orchestrated data. Finally, during the optimize stage, we use residual off-policy RL to further finetune the policy. In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.19891v1
- Authors: Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch, Markus Wulfmeier, Abbas Abdolmaleki, Martin Riedmiller
- Published: 2026-08-20T10:58:45Z
- Age days: 2

</details>
