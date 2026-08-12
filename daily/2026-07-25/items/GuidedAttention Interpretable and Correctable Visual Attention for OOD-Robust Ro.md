---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21049v1"
published: "2026-07-23T08:33:40Z"
age_days: 1
score: 25
created: 2026-07-25
concepts: ["世界模型", "机器人学习"]
---

# GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning

> [!summary] 一句话结论（基于摘要）
> Experiments in simulation and the real world demonstrate that GuidedAttention consistently improves robot manipulation performance, particularly under positional and appearance out-of-distribution (OOD) conditions.

## 关键点

- **问题**：End-to-end visuomotor policies provide little opportunity for humans to understand or correct the policy's visual attention.
- **创新点 / 方法**：We propose GuidedAttention, a visuomotor imitation learning framework that introduces interpretable and correctable visual attention as an explicit intermediate representation.
- **证据**：Experiments in simulation and the real world demonstrate that GuidedAttention consistently improves robot manipulation performance, particularly under positional and appearance out-of-distribution (OOD) conditions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/GuidedAttention Interpretable and Correctable Visual Attention for OOD-Robust Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end visuomotor policies provide little opportunity for humans to understand or
correct the policy's visual attention. We propose GuidedAttention, a visuomotor
imitation learning framework that introduces interpretable and correctable visual
attention as an explicit intermediate representation. Task-relevant attention keypoints
are predicted from camera images and condition a diffusion-based action policy. Users
can inspect and optionally correct selected keypoints once at rollout initialization,
after which the corrected attention is automatically propagated throughout execution by
a tracking module. Experiments in simulation and the real world demonstrate that
GuidedAttention consistently improves robot manipulation performance, particularly under
positional and appearance out-of-distribution (OOD) conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21049v1
- Authors: Masaki Murooka, Ryoichi Nakajo, Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryo Hanai, Yukiyasu Domae
- Published: 2026-07-23T08:33:40Z
- Age days: 1

</details>
