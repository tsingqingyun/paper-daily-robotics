---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13435v1"
published: "2026-06-11T14:59:38Z"
age_days: 1
score: 38
created: 2026-06-13
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# GIVE: Grounding Human Gestures in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> In real-world HRI experiments, GIVE substantially outperforms the baseline, improving target object recognition accuracy by 40% and overall task success rate by 80%, while demonstrating strong robustness and generalization to unseen spatial layouts and divers…

## 关键点

- **问题**：However, current Vision-Language- Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking the important role of gestures in Human-Robot Interaction (HRI).
- **创新点 / 方法**：To address this challenge, we propose GIVE (Gesture Intent via Visual-Semantic Enhancement), an effective approach that enhances pre-trained VLA models with human gesture understanding without architectural modifications.
- **证据**：In real-world HRI experiments, GIVE substantially outperforms the baseline, improving target object recognition accuracy by 40% and overall task success rate by 80%, while demonstrating strong robustness and generalization to unseen spatial layouts and diverse participants.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/GIVE Grounding Human Gestures in Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human communication is inherently multimodal, where language is often accompanied by
non-verbal cues such as gestures to convey intentions. However, current Vision-Language-
Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking
the important role of gestures in Human-Robot Interaction (HRI). This often leads to
inaccurate intent grounding and unreliable manipulation when language instructions are
ambiguous or underspecified. To address this challenge, we propose GIVE (Gesture Intent
via Visual-Semantic Enhancement), an effective approach that enhances pre-trained VLA
models with human gesture understanding without architectural modifications.
Specifically, GIVE incorporates gesture information through two complementary pathways:
a visual pathway that overlays hand skeletons and fingertip rays onto robot observations
for explicit object grounding, and a semantic pathway that generates high-level
descriptions of human gestures and task instructions for robust intent grounding. By
jointly leveraging visual and semantic guidance, GIVE enables VLA policies to better
associate gestures with manipulation behaviors and adapt to dynamic interaction intents.
In real-world HRI experiments, GIVE substantially outperforms the baseline, improving
target object recognition accuracy by 40% and overall task success rate by 80%, while
demonstrating strong robustness and generalization to unseen spatial layouts and diverse
participants.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13435v1
- Authors: Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia, Yang Xiao, Jianfei Yang
- Published: 2026-06-11T14:59:38Z
- Age days: 1

</details>
