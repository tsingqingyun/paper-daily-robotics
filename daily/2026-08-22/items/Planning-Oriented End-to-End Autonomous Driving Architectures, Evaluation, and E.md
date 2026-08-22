---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20111v1"
published: "2026-08-20T14:41:36Z"
age_days: 1
score: 30
created: 2026-08-22
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms

> [!summary] 一句话结论（基于摘要）
> End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols.

## 关键点

- **问题**：Our analysis highlights that architectural progress is difficult to interpret without benchmark-consistent evaluation, and that displacement-based open-loop metrics alone provide limited evidence for safe and human-aligned driving.
- **创新点 / 方法**：End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Planning-Oriented End-to-End Autonomous Driving Architectures, Evaluation, and E.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols. This survey reviews this transition across behavior cloning, conditional imitation learning, privileged distillation, BEV and vectorized planning, unified perception-prediction-planning architectures, world-model-based planners, and vision-language-action systems. We argue that the key distinction in modern end-to-end driving is not whether intermediate representations are used, but whether they are learned, supervised, and evaluated to support safe, feasible, and route-compliant planning. To organize the literature, we synthesize existing methods along four axes: input representation, planning output, supervision signal, and evaluation protocol. We further examine the benchmark shift from open-loop trajectory matching to closed-loop simulation, non-reactive real-log evaluation, long-tail testing, and human-preference-aware metrics. Our analysis highlights that architectural progress is difficult to interpret without benchmark-consistent evaluation, and that displacement-based open-loop metrics alone provide limited evidence for safe and human-aligned driving. We conclude with open challenges in uncertainty-aware planning, learner-expert mismatch, runtime safety assurance, language-action grounding, world-model validation, and reproducible benchmarking.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20111v1
- Authors: Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li, Yunjian Li, Lishengsa Yue, Zhiyong Cui, Chengzhong Xu, Zhenning Li
- Published: 2026-08-20T14:41:36Z
- Age days: 1

</details>
