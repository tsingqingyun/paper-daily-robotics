---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23531v1"
published: "2026-06-22T16:11:15Z"
age_days: 1
score: 35
created: 2026-06-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation

> [!summary] 一句话结论（基于摘要）
> Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success rate (SR) of 84.85\% in real-world phantom experiments.

## 关键点

- **问题**：Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact.
- **创新点 / 方法**：Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem.
- **证据**：Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success rate (SR) of 84.85\% in real-world phantom experiments.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/BiliVLA Scene-Aware Vision-Language-Action Model with Reinforcement Learning for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic
navigation and stable biliary cannulation within a narrow monocular field characterized
by specular reflections, partial occlusions, and frequent tissue contact. Although
recent robotic systems and vision-based assistance techniques improve operator
ergonomics and provide perceptual cues, their performance degrades under pronounced
anatomical variability and safety-critical visual artifacts, which hinders reliable
autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware
Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as
an instruction-conditioned visuomotor learning problem. Given an endoscopic observation
and a stage-specific language instruction, BiliVLA jointly predicts the target category,
a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
a continuum endoscope. The proposed framework incorporates scene-aware supervision to
enhance semantic target consistency and safety-aware recovery supervision to induce
conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is
a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning
(SFT) with Group Relative Policy Optimization (GRPO), which significantly improves
action reliability and decision consistency during closed-loop navigation. Across three
ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall
success rate (SR) of 84.85\% in real-world phantom experiments. These results indicate
that integrating semantic grounding, scene-aware learning, and reward-guided
optimization improves perception-action alignment and enables robust autonomous
endoscopic navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23531v1
- Authors: Jinsong Lin, Chi kit Ng, Zhiyong Xiong, Zikang Pan, Yihan Hu, Tabassum Tamima, Ziyi Hao, Eddie Cheung, Jiewen Lai, Huxin Gao, Hongliang Ren
- Published: 2026-06-22T16:11:15Z
- Age days: 1

</details>
